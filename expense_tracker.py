# Project: Smart Expense Tracker with Catagory Analysis
import csv
import os

File_name="expense.csv"

#LOAD DATA

def load_data():
    expenses= []
    if os.path.exists(File_name):
        with open(File_name, "r") as file:
            reader=csv.reader(file)
            for row in reader:
                if row:
                    expenses.append([row[0],float(row[1]),row[2]])
                    return expenses
                
#save data
def save_data(expenses):
    with open(File_name, "w", newline="") as file:
        writer=csv.writer(file)
        writer.writerows(expenses)

#add expenses
def add_expenses(expenses):
    name=input("enter expense name: ")
    amount=float(input("enter amount: "))
    category=input("enter category: ")
    expenses.append([name, amount, category])

#view expenses
def view_expenses(expenses):
    for i, exp in enumerate(expenses):
        print(f"{i+1}. {exp[0]} | {exp[1]} | {exp[2]}")
        total += exp[1]

#delete expenses
def delete_expenses(expenses):
    view_expenses(expenses)
    try:
        index=int(input("enter number to delete: ")) - 1
        if






