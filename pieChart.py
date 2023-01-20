import matplotlib.pyplot as plt

expenses = {
    'Rent': 800,
    'Food': 300,
    'Transportation': 150,
    'Entertainment': 100,
    'Other': 50
}

total_expenses = sum(expenses.values())

# Create a list of the expenses and their percentages
expenses_list = [[key, value/total_expenses*100] for key, value in expenses.items()]

# Create the pie chart
plt.pie([i[1] for i in expenses_list], labels=[i[0] for i in expenses_list], autopct='%1.1f%%')
plt.title("Monthly Expenses")
plt.show()
