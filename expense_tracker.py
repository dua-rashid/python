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
    category=input("enter category (Food/ Transport/ Bills/ Shopping/ Education): ")
    expenses.append([name, amount, category])
    print("Expenses added!")

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
        if 0<=index < len(expenses):
            removed=expenses.pop(index)
            print("deleted:" , removed[0])
        else:
            print("invalid number!")
    except:
        print("invalid input!")

#Category Analysis
def category_analysis(expenses):
    data={}
    for exp in expenses:
        cat =exp[2]
        amt =exp[1]
        data[cat] =data.get(cat, 0) + amt

    print("category analysis")
    for k, v in data.items():
        print(k, ":", v)

    if data:
        max_cat = max(data, key=data.get)
        print("most spending category:" , max_cat)

#budget check
def budget_check(expenses):
    try:
        budget=float(input("enter your budget"))
        total=sum(exp[1] for exp in expenses)
        print("total spending:", total)
        if total > budget:
            print("you exceed your budget!")
        else:
            print("you are within your budget.")
    except:
        print("invalid input!")  

#smaert insight
def insights (expenses):
    if not expenses:
        print("no data available!")
        return
    highest=max(expenses, key=lambda x: x[1])
    print("highest expense:", highest[0], "-", highest[1])
          
    



      
    






