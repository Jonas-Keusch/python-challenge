import pandas as pd

file_path = 'budget_data.csv'
df = pd.read_csv(file_path)

df.columns = ['Date', 'Profit/Losses']

total_months = df.shape[0]

net_total = df['Profit/Losses'].sum()

df['Change'] = df['Profit/Losses'].diff()
average_change = df['Change'].mean()

greatest_inc = df.loc[df['Change'].idxmax()]
greatest_dec = df.loc[df['Change'].idxmin()]

greatest_inc_date = greatest_inc['Date']
greatest_inc_amnt = greatest_inc['Change']
greatest_dec_date = greatest_dec['Date']
greatest_dec_amnt = greatest_dec['Change']

print("Financial Analysis")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total:,.2f}")
print(f"Average Change: ${average_change:,.2f}")
print(f"Greatest Increase in Profits: {greatest_inc_date} (${greatest_inc_amnt:,.2f})")
print(f"Greatest Decrease in Profits: {greatest_dec_date} (${greatest_dec_amnt:,.2f})")

with open('financial_analysis.txt', 'w') as file:
    file.write("Financial Analysis\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total:,.2f}\n")
    file.write(f"Average Change: ${average_change:,.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_inc_date} (${greatest_inc_amnt:,.2f})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_dec_date} (${greatest_dec_amnt:,.2f})\n")

print("Analysis has been written to financial_analysis.txt")