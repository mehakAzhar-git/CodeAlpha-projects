import tkinter as tk
from tkinter import messagebox

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "GOOGL": 160,
    "AMZN": 190
}

portfolio = {}


# Add stock
def add_stock():
    stock = stock_var.get().strip().upper()

    if stock == "":
        messagebox.showwarning("Warning", "Please select a stock.")
        return

    try:
        quantity = int(quantity_entry.get())

        if quantity <= 0:
            messagebox.showwarning(
                "Warning",
                "Quantity must be greater than 0."
            )
            return

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid quantity."
        )
        return

    portfolio[stock] = portfolio.get(stock, 0) + quantity

    update_portfolio()

    quantity_entry.delete(0, tk.END)


# Update portfolio display
def update_portfolio():
    portfolio_list.delete(0, tk.END)

    total = 0

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity
        total += value

        portfolio_list.insert(
            tk.END,
            f"{stock}   |   {quantity} shares   |   ${value}"
        )

    total_label.config(
        text=f"Total Investment: ${total}"
    )


# Save portfolio
def save_portfolio():
    total = 0

    with open("portfolio_result.txt", "w") as file:

        file.write("STOCK PORTFOLIO TRACKER\n")
        file.write("=======================\n\n")

        for stock, quantity in portfolio.items():

            price = stock_prices[stock]
            value = price * quantity
            total += value

            file.write(
                f"{stock}: {quantity} shares x ${price} = ${value}\n"
            )

        file.write("\n")
        file.write(f"Total Investment: ${total}\n")

    messagebox.showinfo(
        "Saved",
        "Portfolio saved successfully!\n\n"
        "File: portfolio_result.txt"
    )


# Clear portfolio
def clear_portfolio():
    portfolio.clear()
    update_portfolio()


# Main window
root = tk.Tk()

root.title("Stock Portfolio Tracker")
root.geometry("700x750")
root.resizable(False, False)


# Title
title_label = tk.Label(
    root,
    text="STOCK PORTFOLIO TRACKER",
    font=("Arial", 26, "bold")
)

title_label.pack(pady=20)


# Available stocks
stocks_label = tk.Label(
    root,
    text="Available Stocks & Prices",
    font=("Arial", 16, "bold")
)

stocks_label.pack()


prices_text = "   ".join(
    [f"{stock}: ${price}" for stock, price in stock_prices.items()]
)

prices_label = tk.Label(
    root,
    text=prices_text,
    font=("Arial", 12)
)

prices_label.pack(pady=10)


# Stock selection
stock_label = tk.Label(
    root,
    text="Select Stock:",
    font=("Arial", 13)
)

stock_label.pack(pady=(15, 5))


stock_var = tk.StringVar()

stock_menu = tk.OptionMenu(
    root,
    stock_var,
    *stock_prices.keys()
)

stock_menu.config(
    font=("Arial", 12),
    width=15
)

stock_menu.pack()


# Quantity
quantity_label = tk.Label(
    root,
    text="Enter Quantity:",
    font=("Arial", 13)
)

quantity_label.pack(pady=(15, 5))


quantity_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=15,
    justify="center"
)

quantity_entry.pack()


# Add button
add_button = tk.Button(
    root,
    text="ADD STOCK",
    font=("Arial", 12, "bold"),
    command=add_stock,
    width=18
)

add_button.pack(pady=15)


# Portfolio heading
portfolio_label = tk.Label(
    root,
    text="Your Portfolio",
    font=("Arial", 16, "bold")
)

portfolio_label.pack(pady=5)


# Portfolio list
portfolio_list = tk.Listbox(
    root,
    font=("Arial", 12),
    width=55,
    height=8
)

portfolio_list.pack(pady=5)


# Total investment
total_label = tk.Label(
    root,
    text="Total Investment: $0",
    font=("Arial", 18, "bold")
)

total_label.pack(pady=15)


# Buttons
button_frame = tk.Frame(root)
button_frame.pack()


save_button = tk.Button(
    button_frame,
    text="SAVE RESULT",
    font=("Arial", 11, "bold"),
    command=save_portfolio,
    width=15
)

save_button.grid(row=0, column=0, padx=10)


clear_button = tk.Button(
    button_frame,
    text="CLEAR",
    font=("Arial", 11, "bold"),
    command=clear_portfolio,
    width=15
)

clear_button.grid(row=0, column=1, padx=10)


# Start application
root.mainloop()