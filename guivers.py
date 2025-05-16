import tkinter as tk
from tkinter import messagebox
import random

# Game state
gateKey = False
lantern = False
questComplete = False
questFailed = False
questIncomplete = False
hermitMet = False
gateBeen = False
cabinBeen = False
forestBeen = False
cave_fail = False

a, b = random.sample(range(1, 101), 2)

riddles = [
    "What has to be broken before you can use it?",
    "I speak without a mouth and hear without ears. What am I?",
    "I’m tall when I’m young, and I’m short when I’m old. What am I?",
    "What can you break, even if you never pick it up or touch it?",
    "What is always in front of you but can’t be seen?"
]
answers = ["egg", "echo", "candle", "promise", "future"]

class GameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Textventure")
        self.text_frame = tk.Frame(root)
        self.text_frame.pack(padx=10, pady=10)

        self.text = tk.Text(self.text_frame, height=20, width=60, wrap=tk.WORD, state='disabled')
        self.text.pack()

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.show_main_menu()

    def clear_screen(self):
        self.text.configure(state='normal')
        self.text.delete("1.0", tk.END)
        for widget in self.button_frame.winfo_children():
            widget.destroy()

    def write(self, message):
        self.text.configure(state='normal')
        self.text.insert(tk.END, message + '\n')
        self.text.see(tk.END)
        self.text.configure(state='disabled')

    def show_main_menu(self):
        self.clear_screen()
        self.write("Welcome to Textventure\n")
        self.write("Main Menu")
        self.create_button("Play", self.cabin)
        self.create_button("Settings", self.settings_menu)
        self.create_button("Exit", self.root.quit)

    def create_button(self, text, command):
        btn = tk.Button(self.button_frame, text=text, width=30, command=command)
        btn.pack(pady=5)

    def settings_menu(self):
        self.clear_screen()
        self.write("Settings Menu (Decorative Only)")
        self.create_button("Sound", lambda: self.popup("No sound options available"))
        self.create_button("Graphics", lambda: self.popup("No graphic settings here either"))
        self.create_button("Back", self.show_main_menu)

    def popup(self, message):
        messagebox.showinfo("Info", message)

    def cabin(self):
        global forestBeen
        self.clear_screen()
        if forestBeen:
            self.write("You enter the dimly lit room.")
            self.write("You can see a window in front of you.")
            self.write("You can see a table to the left of you.")
            self.write("What do you want to do?")
            self.create_button("Go back outside", self.forest)
            self.create_button("Look out the window", lambda: self.write("It's still dark outside."))
            self.create_button("Inspect the table", self.inspect_table)
        else:
            self.write("You have awoken inside of a dimly lit room.")
            self.write("You see a door to your left, a window to your right, and a table in front.")
            self.create_button("Open the door", self.forest)
            self.create_button("Look out the window", lambda: self.write("You can't see much as it's dark out."))
            self.create_button("Inspect the table", self.inspect_table)

    def inspect_table(self):
        global gateKey
        if gateKey:
            self.write("The table is empty.")
        else:
            self.write("You inspect the table and find a mysterious key.")
            gateKey = True

    def forest(self):
        global forestBeen
        forestBeen = True
        self.clear_screen()
        self.write("You are in a dense forest.")
        self.create_button("Talk to the Hermit", self.hermit)
        self.create_button("Travel deeper into the forest", self.locked_gate)
        self.create_button("Go back to the cabin", self.cabin)

    def hermit(self):
        global hermitMet, lantern
        hermitMet = True
        self.clear_screen()
        self.write("The Hermit greets you and hands you a lantern.")
        self.write("He offers you a quest")
        self.write("Do you accept?")
        self.create_button("Accept the quest", self.hermit_quest)
        self.create_button("Decline the quest", self.forest)
        lantern = True

    def hermit_quest(self):
        global questComplete
        global questFailed
        self.clear_screen()
        self.write("The Hermit gives you a crumpled piece of paper")
        self.write("You uncrumple the paper to find mysterious runes etched into it")
        self.write("You read the paper")
        self.create_button(f"What is {a} + {b}", lambda: self.check_answer(a + b))

    def locked_gate(self):
        self.clear_screen()
        global gateKey
        if gateKey:
            self.write("You use the mysterious key to unlock the gate.")
            self.create_button("Enter the cave", self.cave)
            self.create_button("Return to forest", self.forest)
        else:
            self.write("The gate is locked. You need a key.")
            self.create_button("Back to forest", self.forest)

    def cave(self):
        global lantern
        self.clear_screen()
        self.write("You arrive at a dark cave.")
        if lantern:
            self.write("With your lantern, you feel confident to enter.")
            self.create_button("Enter the cave", self.cave_deeper)
        else:
            self.write("It's too dark to proceed. You need a light source.")
            self.create_button("Return to forest", self.forest)

    def cave_deeper(self):
        global cave_fail
        self.clear_screen()
        self.write("You venture deeper. The lantern flickers...")
        if random.random() < 0.5:
            self.write("The lantern survives the wind.")
            self.create_button("Continue to puzzle room", self.puzzle_room)
        else:
            cave_fail = True
            self.write("The lantern goes out! You flee the cave.")
            self.create_button("Return to forest", self.forest)

    def puzzle_room(self):
        self.clear_screen()
        self.write("You arrive at a glowing ancient door.")
        self.create_button(f"What is {a} + {b}?", lambda: self.check_answer(a + b))

    def check_answer(self, correct):
        def inner():
            try:
                ans = int(entry.get())
                if ans == correct:
                    self.write("You answer correctly and hand back the paper")
                else:
                    self.write("You answer incorrectly")
                    self.write("The paper emits a black smog and engulfs you")
                    self.write("You have failed the Hermit's Quest")
                    self.root.quit()
            except:
                self.write("This doesn't look quite right")
                self.write("You must answer using runic symbols... Hint: numbers")

        self.clear_screen()
        self.write("Answer the Hermit's question:")
        entry = tk.Entry(self.button_frame)
        entry.pack()
        self.create_button("Submit", inner)

    def end_game(self):
        self.clear_screen()
        self.write("Game Over! Adventurer's Ending.")
        self.create_button("Quit", self.root.quit)

if __name__ == "__main__":
    root = tk.Tk()
    game = GameGUI(root)
    root.mainloop()
