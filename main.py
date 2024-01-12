from tkinter import *
from tkinter import messagebox
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------------Function----------------------------------- #
current_card = {}
data_dict = {}
new_dict = {}
try:
    data = pandas.read_csv("data/words_to_lear.csv")
except FileNotFoundError:
    orig_data = pandas.read_csv("data/french_words.csv")
    data_dict = orig_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


def rights():
    global current_card
    data_dict.remove(current_card)
    datas = pandas.DataFrame(data_dict)
    datas.to_csv("data/words_to_learn.csv")
    next_card()


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    try:
        current_card = random.choice(data_dict)
    except IndexError:
        messagebox.showinfo(title="Congratulations!", message="You completed the quiz!")
    else:
        random_french = current_card["French"]
        canvas.itemconfig(card_text, text=f"{random_french}",fill="black")
        canvas.itemconfig(card_title, text="French", fill="black")
        canvas.itemconfig(card_bg, image=bg_white)
        flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_bg, image=bg_green)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=current_card["English"], fill="white")

# ---------------------------------UI----------------------------------------- #


window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, flip_card)


# Card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
bg_white = PhotoImage(file="images/card_front.png")
bg_green = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=bg_white)
card_title = canvas.create_text(400, 150, text=f"French", font=("Ariel", 40, "italic"))
card_text = canvas.create_text(400, 253, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Option
wrong = PhotoImage(file="images/wrong.png", )
wrong_button = Button(image=wrong, highlightcolor=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column=0, row=1)

right = PhotoImage(file="images/right.png")
right_button = Button(image=right, highlightcolor=BACKGROUND_COLOR, command=rights)
right_button.grid(column=1, row=1)
next_card()
window.mainloop()
