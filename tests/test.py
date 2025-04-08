import os 
import threading
import random
import time
import queue
import sys

"""Simple Test to test threading between game state and input handling"""

class Game:
    
    def __init__(self):
        self.is_running = False
        self.is_paused = False
        self.turn = 0
        self.time_elapsed = 0
        self.command_queue = queue.Queue()
        self.input_thread = None

    def start(self):
        print("Starting game...")
        self.is_running = True
        self.input_thread = threading.Thread(target=self.input_handler)
        self.input_thread.daemon = True
        
        # Actually start the input thread and the game loop
        self.input_thread.start()
        self.run()
    
    def input_handler(self):
        """Thread function that continuously handles user input"""
        while self.is_running:
            try:
                user_action = input("> ")
                # Put the command in the queue for processing by the main thread
                print(f"Command received: '{user_action}'")
                self.command_queue.put(user_action)
                
            except EOFError:
                # Handle EOF (Ctrl+D on Unix, Ctrl+Z on Windows)
                self.command_queue.put("q")
                break
            except Exception as e:
                print(f"Input error: {e}")
        
    def process_commands(self):
        """Process any commands in the queue without blocking"""
        try:
            # Process all available commands in the queue
            while not self.command_queue.empty():
                user_action = self.command_queue.get_nowait()
                self.handle_command(user_action)
        except queue.Empty:
            # Queue is empty, continue with game loop
            pass
    
    def handle_command(self, user_action):
        """Process a single user command"""
        if user_action == "q":
            print("Quitting the game!")
            self.quit()
            
        elif user_action == "p":
            self.is_paused = not self.is_paused # toggle pause state 
            if self.is_paused:
                print("Game is now PAUSED. Press 'p' to continue.")
            else:
                print("Game is now RESUMED.")
    
    def update(self):
        # Simulate game logic here
        pass
        
    def run(self):
        micro_turn_duration = 1.25  
        pause_message_timer = 0
        
        try:
            # Main Game Loop Here: 
            while self.is_running:
                # Always process commands regardless of pause state
                self.process_commands()
                    
                if not self.is_paused:
                    self.update()
                    self.time_elapsed += micro_turn_duration
                    self.turn += 1
                    
                    print(f"Turn: {self.turn} | Time elapsed: {self.time_elapsed:.1f}s")
                    
                    # allow some time for the game to process and the human to read
                    time.sleep(micro_turn_duration)
                else:
                    # Only show the pause message occasionally to avoid spamming
                    pause_message_timer += 1
                    if pause_message_timer >= 5:  # every ~5 seconds
                        print("Game is paused. Waiting for commands...")
                        pause_message_timer = 0
                    
                    time.sleep(1)
        except KeyboardInterrupt:
            print("\nGame interrupted by user.")
            self.quit()

    def quit(self):
        print("Shutting down the game...")
        self.is_running = False
        # Don't try to join here - it can cause deadlocks
        # since input_thread is waiting for input
        print("Game has been stopped.")
        sys.exit(0)  # Force exit

def main():
    game = Game()
    try:
        game.start()
    except Exception as e:
        print(f"Error in main game loop: {e}")
    
if __name__ == "__main__":
    main()