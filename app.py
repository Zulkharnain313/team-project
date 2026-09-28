import tkinter as tk
from tkinter import messagebox
import smtplib
from email.message import EmailMessage


# =========================================================
# EMAIL SETTINGS
# =========================================================

# Put YOUR email address here
SENDER_EMAIL = "your_email@gmail.com"

# Put your Gmail APP PASSWORD here
# Do NOT use your normal Gmail password
SENDER_APP_PASSWORD = "YOUR_APP_PASSWORD"


# =========================================================
# CALCULATE
# =========================================================

def calculate():
    try:
        price = float(price_entry.get())
        discount = float(discount_entry.get())
        gst = float(gst_entry.get())

        if price < 0 or discount < 0 or gst < 0:
            raise ValueError

        discount_amount = price * discount / 100
        discounted_price = price - discount_amount

        gst_amount = discounted_price * gst / 100
        final_price = discounted_price + gst_amount

        discount_result.config(
            text=f"Discount Amount: ₹{discount_amount:.2f}"
        )

        gst_result.config(
            text=f"GST Amount: ₹{gst_amount:.2f}"
        )

        final_result.config(
            text=f"Final Price: ₹{final_price:.2f}"
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numbers."
        )


# =========================================================
# SEND RECEIPT
# =========================================================

def send_receipt():

    try:
        name = name_entry.get().strip()
        customer_email = email_entry.get().strip()

        price = float(price_entry.get())
        discount = float(discount_entry.get())
        gst = float(gst_entry.get())

        if not name:
            messagebox.showerror(
                "Missing Information",
                "Please enter the customer name."
            )
            return

        if not customer_email or "@" not in customer_email:
            messagebox.showerror(
                "Invalid Email",
                "Please enter a valid customer email."
            )
            return

        if price < 0 or discount < 0 or gst < 0:
            raise ValueError

        # Calculate values
        discount_amount = price * discount / 100
        discounted_price = price - discount_amount

        gst_amount = discounted_price * gst / 100
        final_price = discounted_price + gst_amount

        # Create receipt
        receipt = f"""
SMART PRICE CALCULATOR
==============================

Customer Name: {name}

Original Price: ₹{price:.2f}
Discount:       {discount:.2f}%
Discount Amount: ₹{discount_amount:.2f}

Price After Discount: ₹{discounted_price:.2f}

GST:            {gst:.2f}%
GST Amount:     ₹{gst_amount:.2f}

------------------------------
FINAL PRICE:    ₹{final_price:.2f}
------------------------------

Thank you for your purchase!
"""

        # Create email
        message = EmailMessage()

        message["Subject"] = "Your Smart Price Calculator Receipt"
        message["From"] = SENDER_EMAIL
        message["To"] = customer_email

        message.set_content(receipt)

        # Connect to Gmail
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:

            server.login(
                SENDER_EMAIL,
                SENDER_APP_PASSWORD
            )

            server.send_message(messages)

        messagebox.showinfo(
            "Success",
            f"Receipt sent successfully to\n{customer_email}"
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid price, discount and GST values."
        )

    except Exception as error:
        messagebox.showerror(
            "Email Error",
            f"Could not send the receipt.\n\n{error}"
        )


# =========================================================
# CLEAR
# =========================================================

def clear():

    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    discount_entry.delete(0, tk.END)
    gst_entry.delete(0, tk.END)

    discount_result.config(
        text="Discount Amount: ₹0.00"
    )

    gst_result.config(
        text="GST Amount: ₹0.00"
    )

    final_result.config(
        text="Final Price: ₹0.00"
    )


# =========================================================
# MAIN WINDOW
# =========================================================

root = tk.Tk()

root.title("Smart Price Calculator")
root.geometry("550x700")
root.resizable(False, False)


# =========================================================
# TITLE
# =========================================================

title_label = tk.Label(
    root,
    text="SMART PRICE CALCULATOR",
    font=("Arial", 22, "bold")
)

title_label.pack(pady=(25, 5))


subtitle_label = tk.Label(
    root,
    text="Calculate price, discount and GST",
    font=("Arial", 12)
)

subtitle_label.pack(pady=(0, 20))


# =========================================================
# CUSTOMER INFORMATION
# =========================================================

customer_frame = tk.Frame(root)
customer_frame.pack(pady=5)


tk.Label(
    customer_frame,
    text="Customer Name:",
    font=("Arial", 11)
).grid(row=0, column=0, padx=10, pady=8, sticky="w")


name_entry = tk.Entry(
    customer_frame,
    width=28,
    font=("Arial", 11)
)

name_entry.grid(row=0, column=1, padx=10, pady=8)


tk.Label(
    customer_frame,
    text="Customer Email:",
    font=("Arial", 11)
).grid(row=1, column=0, padx=10, pady=8, sticky="w")


email_entry = tk.Entry(
    customer_frame,
    width=28,
    font=("Arial", 11)
)

email_entry.grid(row=1, column=1, padx=10, pady=8)


# =========================================================
# PRICE INFORMATION
# =========================================================

input_frame = tk.Frame(root)
input_frame.pack(pady=10)


tk.Label(
    input_frame,
    text="Original Price (₹):",
    font=("Arial", 11)
).grid(row=0, column=0, padx=10, pady=8, sticky="w")


price_entry = tk.Entry(
    input_frame,
    width=20,
    font=("Arial", 11)
)

price_entry.grid(row=0, column=1, padx=10, pady=8)


tk.Label(
    input_frame,
    text="Discount (%):",
    font=("Arial", 11)
).grid(row=1, column=0, padx=10, pady=8, sticky="w")


discount_entry = tk.Entry(
    input_frame,
    width=20,
    font=("Arial", 11)
)

discount_entry.grid(row=1, column=1, padx=10, pady=8)


tk.Label(
    input_frame,
    text="GST (%):",
    font=("Arial", 11)
).grid(row=2, column=0, padx=10, pady=8, sticky="w")


gst_entry = tk.Entry(
    input_frame,
    width=20,
    font=("Arial", 11)
)

gst_entry.grid(row=2, column=1, padx=10, pady=8)


# =========================================================
# BUTTONS
# =========================================================

button_frame = tk.Frame(root)
button_frame.pack(pady=15)


tk.Button(
    button_frame,
    text="Calculate",
    command=calculate,
    width=13,
    font=("Arial", 11, "bold")
).grid(row=0, column=0, padx=5)


tk.Button(
    button_frame,
    text="Send Receipt",
    command=send_receipt,
    width=13,
    font=("Arial", 11, "bold")
).grid(row=0, column=1, padx=5)


tk.Button(
    button_frame,
    text="Clear",
    command=clear,
    width=13,
    font=("Arial", 11, "bold")
).grid(row=0, column=2, padx=5)


# =========================================================
# RESULTS
# =========================================================

result_frame = tk.Frame(root)
result_frame.pack(pady=15)


discount_result = tk.Label(
    result_frame,
    text="Discount Amount: ₹0.00",
    font=("Arial", 11)
)

discount_result.pack(pady=7)


gst_result = tk.Label(
    result_frame,
    text="GST Amount: ₹0.00",
    font=("Arial", 11)
)

gst_result.pack(pady=7)


final_result = tk.Label(
    result_frame,
    text="Final Price: ₹0.00",
    font=("Arial", 16, "bold")
)

final_result.pack(pady=10)


# =========================================================
# START
# =========================================================

root.mainloop()
# i have added 