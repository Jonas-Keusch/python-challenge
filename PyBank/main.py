import pandas as pd

file_path = 'budget_data.csv'
df = pd.read_csv(file_path)

df.columns = ['Date', 'Profit/Losses']

total_months = df.shape[0]

net_total = df['Profit/Losses'].sum()

df['Change'] = df['Profit/Losses'].diff()
average_change = df['Change'].mean()

greatest_increase = df.loc[df['Change'].idxmax()]
greatest_decrease = df.loc[df['Change'].idxmin()]

greatest_increase_date = greatest_increase['Date']
greatest_increase_amount = greatest_increase['Change']
greatest_decrease_date = greatest_decrease['Date']
greatest_decrease_amount = greatest_decrease['Change']

print("Financial Analysis")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total:,.2f}")
print(f"Average Change: ${average_change:,.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount:,.2f})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount:,.2f})")

with open('financial_analysis.txt', 'w') as file:
    file.write("Financial Analysis\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total:,.2f}\n")
    file.write(f"Average Change: ${average_change:,.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount:,.2f})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount:,.2f})\n")

print("Analysis has been written to financial_analysis.txt")