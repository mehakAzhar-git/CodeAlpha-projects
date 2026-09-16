import tkinter as tk
from tkinter import scrolledtext


def get_response(user_message):

    message = user_message.lower().strip()

    if message == "hello" or message == "hi":
        return "Hi! How can I help you?"

    elif message == "how are you":
        return "I'm fine, thanks!"

    elif message == "what is your name":
        return "My name is Basic Chatbot."

    elif message == "help":
        return "You can say hello, ask how I am, or say bye."

    elif message == "bye" or message == "goodbye":
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand that."


def send_message():

    user_message = entry.get().strip()

    if user_message == "":
        return

    chat_box.config(state=tk.NORMAL)

    chat_box.insert(
        tk.END,
        "You: " + user_message + "\n"
    )

    response = get_response(user_message)

    chat_box.insert(
        tk.END,
        "Bot: " + response + "\n\n"
    )

    chat_box.config(state=tk.DISABLED)
    chat_box.see(tk.END)

    entry.delete(0, tk.END)


def clear_chat():

    chat_box.config(state=tk.NORMAL)
    chat_box.delete("1.0", tk.END)
    chat_box.config(state=tk.DISABLED)


# Main window
root = tk.Tk()

root.title("Basic Chatbot")
root.geometry("650x600")
root.resizable(False, False)


# Title
title = tk.Label(
    root,
    text="BASIC CHATBOT",
    font=("Arial", 26, "bold")
)

title.pack(pady=20)


# Chat area
chat_box = scrolledtext.ScrolledText(
    root,
    width=65,
    height=20,
    font=("Arial", 12),
    wrap=tk.WORD
)

chat_box.pack(padx=20, pady=10)

chat_box.config(state=tk.DISABLED)


# Input
input_frame = tk.Frame(root)
input_frame.pack(pady=10)


entry = tk.Entry(
    input_frame,
    width=45,
    font=("Arial", 13)
)

entry.pack(side=tk.LEFT, padx=5)


send_button = tk.Button(
    input_frame,
    text="SEND",
    font=("Arial", 11, "bold"),
    command=send_message,
    width=10
)

send_button.pack(side=tk.LEFT)


# Clear button
clear_button = tk.Button(
    root,
    text="CLEAR CHAT",
    font=("Arial", 11, "bold"),
    command=clear_chat,
    width=15
)

clear_button.pack(pady=10)


# Welcome message
chat_box.config(state=tk.NORMAL)

chat_box.insert(
    tk.END,
    "Bot: Hello! I am your basic chatbot.\n"
)

chat_box.insert(
    tk.END,
    "Bot: You can say hello, ask how are you, or say bye.\n\n"
)

chat_box.config(state=tk.DISABLED)


root.mainloop()



