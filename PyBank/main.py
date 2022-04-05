import os
import csv

print("Financial Analysis")
print('----------------------------')

budget_csv = os.path.join = ("PyBank/Resources/budget_data.csv")   
with open(budget_csv, "r", encoding="utf-8") as f:
    bank_csv = csv.reader(f, delimiter=",")
    next(f, None)
  
    months = []
    profit_loss = []
    change = []
   
    for row in bank_csv:
        date = row[0]
        months.append(date)
        profit = int(row[1])
        profit_loss.append(profit)
    total_months = len(months)
    total_amount = sum(profit_loss)
    print(f"Total Months: {str(total_months)}")
    
    for i in range(len(profit_loss)-1):
     change.append(profit_loss[i+1]-profit_loss[i]) 
    total_change = sum(change)
    print(f"Total: ${total_amount}")

average_change = round((total_change/(total_months-1)), 2)
print(f"Average Change: ${average_change}")

max_profit = max(change)
max_loss = min(change)
max_profit_month = change.index(max_profit)
max_loss_month = change.index(max_loss)
profit_month = months[max_profit_month+1]
loss_month = months[max_loss_month+1]
print(f"Greatest Increase in Profits: {profit_month} (${max_profit})")
print(f"Greatest Decrease in Profits: {loss_month} (${max_loss})")


with open("MyFile.txt","w") as file1:
    file1.write("Financial Analysis \n")
    file1.write("---------------------------- \n")
    file1.write(f"Total Months: {str(total_months)} \n")
    file1.write(f"Total: ${total_amount} \n")
    file1.write(f"Greatest Increase in Profits: {profit_month} (${max_profit}) \n")
    file1.write(f"Greatest Decrease in Profits: {loss_month} (${max_loss}) \n")