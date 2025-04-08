
import time
import threading 
import os
import queue
from character import character

class Game:
    def __init__(self):
        self.is_running = False
        self.is_paused = False
        self.turn = 0
        self.time_elapsed = 0
        self.command_queue = queue.Queue()
        self.input_thread = None
        
        warrior_equipment = {"weapon": ["sword"], "armor": ["shield", "helmet"]}
        goblin_equipment = {"weapon": ["dagger"], "armor": ["leather"]}
        
        self.team_a = [
            character("Tim", "Warrior", strength=7 , inventory=warrior_equipment.copy()),
            character("Bob", "Warrior", strength=8, inventory=warrior_equipment.copy())
        ]
        
        self.team_b = [
            character("Goblin A", "Goblin", strength=3, inventory=goblin_equipment.copy()),
            character("Goblin B", "Goblin", strength=3, inventory=goblin_equipment.copy())
        ]

        self.action_queues = {
            "team_a": [],
            "team_b": []
        }
            
    def start_game(self):
        self.display_commands()
        self.is_running = True
        self.input_thread = threading.Thread(target=self.input_handler)
        self.input_thread.daemon = True
        
        # Start the input thread and the game loop
        self.input_thread.start()
        self.run()
        
    
    def print_status(self):
        print("Team A Status:")
        for character in self.team_a:
            print(character.get_status(detailed=True))
            
        print("==========================")
        print("==========================")
        
        
        print("Team B Status:")
        for character in self.team_b:
            print(character.get_status(detailed=True))       
        
    def input_handler(self):
        """Thread function handles user input"""
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
        if user_action == "q":
            print("Quitting the game!")
            self.stop_game()
  
        if user_action == "q":
            self.stop_game()
            return
            
        if user_action == "0":
           pass
        
        if user_action == "1":
            print("attack")
            
        elif user_action == "2":   
            pass
                 
        elif user_action == "3":
            pass
        
        elif user_action == "4":
            pass
        
        elif user_action == "5":
            self.print_status()
             
        elif user_action == "p":
            print("Pausing game...")
            self.is_paused = True
            print("Game paused. Press 'r' to resume.")
        
        elif user_action == "r":
            print("Resuming game...")
            self.is_paused = False
            print("Game resumed.")
        
        elif user_action == "h":
            print("help")
            self.display_commands()
              
        else:
            print("Invalid command. Please try again.")
        
    
    def print_action_queue(self):
        pass

    def is_gameOver(self):
        pass
    
    def display_commands(self):
        print("\n------------ ACTION COMMANDS -------------")
        print("0. interact - Interact with a something")
        print("1. attack <team> <character> <target_team> <target_character> - Basic attack")
        print("2. special <team> <character> <target_team> <target_character> - Special attack with chance to stun")
        print("3. heal <team> <character> <team> <target_character> - Heal a character")
        print("4. move <team> <character> <target_team> - Move to a different location")
        print("5. status - Display the status of all characters")
        print ("6. show team inventory - Display the inventory of a character")
        print("7. map")
        
        print("----- ADMIN COMMANDS ----------------------")
        print("p. pause")
        print("r. resume")
        print("h. help")
        print("q. quit")
        print("-------------------------------------------\n")
        
    def display_map(self):
        pass 
    
    
    def is_gameOver():
        # check if any team has lost all characters
        pass
      
  
    def update(self):
        # get actions from the queue, check if they are valid, 
        
        pass
    
    
    # main game loop
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
            
    def stop_game(self):
        print("Stopping game... See you next time!")
        self.is_running = False
  
def show_colored_title():
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    RESET = "\033[0m"
    
    print(f"""
    {CYAN} _____                       {YELLOW}____                  _   {RESET}
    {CYAN}|  __ \\                     {YELLOW}/ __ \\                | |  {RESET}
    {CYAN}| |__) |_ _ _   _ ___  ___ {YELLOW}| |  | |_   _  ___  ___| |_ {RESET}
    {CYAN}|  ___/ _` | | | / __|/ _ \\{YELLOW}| |  | | | | |/ _ \\/ __| __|{RESET}
    {CYAN}| |  | (_| | |_| \\__ \\  __/{YELLOW}| |__| | |_| |  __/\\__ \\ |_ {RESET}
    {CYAN}|_|   \\__,_|\\__,_|___/\\___/{YELLOW} \\___\\_\\\\__,_|\\___||___/\\__|{RESET}
                                                           
        {MAGENTA}* A CLI Based Real-Time With Pause RPG Adventure *{RESET}
    {GREEN}=========================================================={RESET}
                    {RED}Press ENTER to begin{RESET}
    """)

    
def main():
    show_colored_title()
    start = input(">")
    if start == "":
        print("Starting game...")
        game = Game()
        game.start_game()
    else:
        print("Invalid input. Exiting game.")
        return
    
   
if __name__ == "__main__":
    main()