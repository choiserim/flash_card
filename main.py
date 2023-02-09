from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data_dic = {}

# ---------------------------- LOAD DATA ------------------------------- #
try:
    data = pd.read_csv("data/remain_wore.csv")
except FileNotFoundError:
    orignal_data = pd.read_csv("data/word.csv")
    data_dic = orignal_data.to_dict(orient="records")
else:
    data_dic = data.to_dict(orient="records")

print(data_dic)
print(type(data_dic))
print(len(data_dic))


# ---------------------------- next card button ------------------------------- #
def next_card():

    global current_card, change_korea_card
    current_card = random.choice(data_dic)
    # current_word = current_card["english"]
    # print(type(word))

    # updating canvas text
    canvas.itemconfig(title_text, text="English", fill="black")
    canvas.itemconfig(word_text, text=current_card["English"], fill="black")
    canvas.itemconfig(card_background, image=front_image)

    # 3초 후에 카드 바꾸기
    change_korea_card = window.after(3000, func=change_card)
# def known_click():
#     data_list = []
#
#     for t in data_dic:
#         data_list.append(t["english"])
#
#     word = random.choice(data_list)
#     # print(type(word))
#     canvas.itemconfigure(mean_text, text=word)


# ---------------------------- change card button ------------------------------- #
def change_card():

    # current_word = current_card["korea"]
    # print(type(word))

    # change word
    canvas.itemconfig(title_text, text="korea", fill="white")
    canvas.itemconfig(word_text, text=current_card["Korea"], fill="white")
    canvas.itemconfig(card_background, image=back_image)


def is_know():
    data_dic.remove(current_card)
    print(len(data_dic))
    data = pd.DataFrame(data_dic)
    # index option을 False로 하면 번호가 안생긴다.
    # data.to_csv("data/remain_wore.csv")
    data.to_csv("data/remain_wore.csv", index=False)

    next_card()

# ---------------------------- UI SETUP ------------------------------- #
# made window
window = Tk()
window.title(string="Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# 3초 후에 카드 바꾸기
change_korea_card = window.after(3000, func=change_card)

# import card image
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_image)
canvas.grid(row=0, column=0, columnspan=2)

# expression word text
title_text = canvas.create_text(400, 150, text="Title", fill="black", font=("Courier", 35, "italic"))
word_text = canvas.create_text(400, 263, text="Word", fill="black", font=("Courier", 40, "bold"))

# import button images
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_know)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
