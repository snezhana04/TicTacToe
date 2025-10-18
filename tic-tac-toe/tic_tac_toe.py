# tic_tac_toe.py
import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Крестики-нолики")
        self.window.geometry("400x400")
        self.window.configure(bg="#F5F5F5")
        
        self.current_player = "X"
        self.board = [""] * 9
        self.game_active = True
        self.buttons = []
        
        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(
            self.window, 
            text="Крестики-нолики", 
            font=("Arial", 20),
            pady=15,
            bg="#F5F5F5"
        ).pack()
        
        board_frame = tk.Frame(self.window, bg="#F5F5F5")
        board_frame.pack(pady=20)
        
        for i in range(9):
            button = tk.Button(
                board_frame,
                text="",
                font=("Arial", 20),
                width=4,
                height=2,
                command=lambda idx=i: self.make_move(idx),
                bg="#FFFFFF"
            )
            button.grid(row=i//3, column=i%3, padx=2, pady=2)
            self.buttons.append(button)
    
    def make_move(self, position):
        if not self.game_active:
            return
        
        # ЕСТЬ: проверка ничьи
        if self.check_draw():
            self.handle_draw()
            return
        
        # НЕТ: выполнение хода, проверка победы, смена игрока, рестарт игры
    
    def check_draw(self):
        """Проверяет ничью"""
        return all(cell != "" for cell in self.board)
    
    def handle_draw(self):
        """Обрабатывает ничью"""
        messagebox.showinfo("Ничья!", "Игра закончилась вничью!")
        # НЕТ: рестарт игры
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()