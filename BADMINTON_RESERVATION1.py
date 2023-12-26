import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="badminton_reservation"
)
cursor = mydb.cursor()

def calculate_cost():
    number_of_hours = int(number_of_hours_spinbox.get())
    number_of_players = int(number_of_players_spinbox.get())

    # price of 15.00 per hour
    price_per_hour = 15.00

    # Calculate the total cost without predefined prices
    total_cost =price_per_hour * number_of_hours

    # Apply a 5% discount if the player plays more than 5 hours
    if number_of_hours > 5:
        discount_percentage = 10
        discount_amount = (total_cost * discount_percentage) / 100
        total_cost -= discount_amount

    cost_label.config(text=f"Total Price: RM{total_cost:.2f}", font=("Cooper Black", 12, "bold"))
    return total_cost


    

def enter_data():
    player_name = player_name_entry.get()
    court_number = court_number_combobox.get()
    number_of_players = int(number_of_players_spinbox.get())
    number_of_hours = int(number_of_hours_spinbox.get())
    total_cost = calculate_cost()

    print("Player Name:", player_name)
    print("Court Number:", court_number)
    print("Number_of_players:", number_of_players)
    print("Number of Hours:", number_of_hours)
    print("Total Cost:", total_cost)
    print("------------------------------------")

    # Inserting data into the "player information" table
    sql = "INSERT INTO player_information (player_name, court_number, number_of_players, number_of_hours, total_cost) VALUES (%s, %s, %s, %s, %s)"
    values = (player_name, court_number, number_of_players, number_of_hours, total_cost)

    try:
        cursor.execute(sql, values)
        mydb.commit()
        print("Data inserted successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        mydb.rollback()

#my window title
window = tk.Tk()
window.title("Badminton Reservation System",)

frame = tk.Frame(window)
frame.pack()

# Player Info Frame
player_info_frame = tk.LabelFrame(frame, text="Player Information", font=("Cooper Black",12),bg="olivedrab3")
player_info_frame.grid(row=0, column=0, padx=20, pady=10)

# Price Information
prices_text = tk.Text(player_info_frame, height=6, width=73)
prices_text.grid(row=0, column=0, columnspan=7, pady=10)

prices_text.insert(tk.END, "Prices per hour:\n")
prices_text.insert(tk.END, "1 hour: RM15.00\n")
prices_text.insert(tk.END, "Above than 5 hour discount 10%\n")
prices_text.configure(state='disabled')

# Player Information
tk.Label(player_info_frame, text="Player Name", font=("Cooper Black", 10)).grid(row=1, column=0)
player_name_entry = tk.Entry(player_info_frame, font=("Jumbo", 10, "bold"))
player_name_entry.grid(row=1, column=1, pady=4)

tk.Label(player_info_frame, text="Court Number", font=("Cooper Black", 10)).grid(row=1, column=2)
court_number_combobox = ttk.Combobox(player_info_frame, values=["C1", "C2", "C3", "C4"], font=("Jumbo", 10, "bold"))
court_number_combobox.grid(row=1, column=3, columnspan=2, pady=4)

tk.Label(player_info_frame, text="Number of hours", font=("Cooper Black", 10)).grid(row=3, column=2, pady=7)
number_of_hours_spinbox = ttk.Spinbox(player_info_frame, from_=1, to=10, font=("Jumbo", 10, "bold"))
number_of_hours_spinbox.grid(row=3, column=3,columnspan=2,pady=4)

tk.Label(player_info_frame, text="Player Number", font=("Cooper Black", 10)).grid(row=3, column=0, pady=8)
number_of_players_spinbox = ttk.Spinbox(player_info_frame, from_=1, to=20, font=("Jumbo", 10, "bold"))
number_of_players_spinbox.grid(row=3, column=1, pady=4)

# Cost Calculation
calculate_button = tk.Button(player_info_frame, text="Calculate", command=calculate_cost, font=("hooge 05_53", 9, "bold",),bg="darkolivegreen4")
calculate_button.grid(row=6, column=1, columnspan=2, pady=2)

cost_label = tk.Label(player_info_frame, text="Total Cost: RM0", font=("hooge 05_53", 9, "bold"))
cost_label.grid(row=7, column=1, columnspan=2, pady=2)

# Button inserts data into my SQL
button = tk.Button(frame, text="Enter data", command=enter_data,font=("hooge 05_53",10), bg="darkolivegreen4")
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()
