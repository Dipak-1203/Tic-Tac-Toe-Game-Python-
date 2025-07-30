import tkinter as tk
from tkinter import messagebox




def check_winner():
    global winner
    for combination in [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]:
        if buttons[combination[0]]['text'] == buttons[combination[1]]['text'] == buttons[combination[2]]['text'] != "":
            buttons[combination[0]].config(bg='green')
            buttons[combination[1]].config(bg='green')
            buttons[combination[2]].config(bg='green')
            messagebox.showinfo("Game Over", f"{buttons[combination[0]]['text']} wins!")
            winner = True
            return
            
def button_click(index):
    if buttons[index]['text'] == "" and not winner:
        buttons[index]['text'] = current_player
        check_winner()
        toggle_player()
        
        
def toggle_player():
    global current_player
    current_player = 'O' if current_player == 'X' else 'X'
    label.config(text=f"Current Player: {current_player}")        
    
    
root = tk.Tk()
root.title("O / X Game")

buttons = [tk.Button(root, text="", font=('calibri', 40, 'bold'), width=5, height=2,command=lambda i=i: button_click(i)) for i in range(9)]
for i, button in enumerate(buttons):
    button.grid(row=i//3, column=i%3)
    
current_player = 'X'
winner = False   
label = tk.Label(root, text=f"Current Player: {current_player}'s turn ", font=('calibri', 20, 'bold'))
label.grid(row=3, column=0, columnspan=3)
 

root.mainloop()
