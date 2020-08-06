import csv
import os

budgetFilePath = os.path.join("Resources/" + "budget_data.csv")

#variables & lists
total = 0
profit = 0
loss = 0
total_amount = 0
month= []
revenue = []
revenue_change = []
avg_change = []

#read csv
with open(budgetFilePath ) as csvFile:
	csvReader = csv.reader(csvFile, delimiter=",")

	csvRow = next(csvReader)

#find the total number of months and total amount
	for row in csvReader:
		month.append(row[0])
		revenue.append(row[1])
		total = int(row[1])
		if total > 0:
			profit += total
		elif total < 0:
			loss += total
	total_amount = profit + loss
	month_total = len(month)

	print("Financial Analysis")
	print("-----------------------------")
	print(f"Total Months: {month_total}")
	print(f"Total: ${total_amount}")


#find the average change
	i = 0
	for i in range(len(revenue)-1):
		revenue_loss = int(revenue[i +1])- int(revenue[i])
		revenue_change.append(revenue_loss)
	Total = sum(revenue_change)
	avg_change = Total / len(revenue_change)
	avg = round(avg_change,2)

	print(f"Average Change : ${avg}")

#find greatest increase in profits
	inc_change = max(revenue_change)
	inc = revenue_change.index(inc_change)
	month_inc = month[inc+1]

	print(f"Greatest Increase in Profits : {month_inc} (${inc_change})")

#find greatest decrease in profits:
	dec_change = min(revenue_change)
	dec = revenue_change.index(dec_change)
	month_dec = month[dec+1]

	print(f"Greatest Decrease in Profits : {month_dec} (${dec_change})")

outputPath = os.path.join("analysis/" + "PyBank.py")
with open(outputPath, 'w+', newline='') as text_file:

	print("Financial Analysis", file=text_file)
	print("-----------------------------", file=text_file)
	print(f"Total Months: {month_total}", file=text_file)
	print(f"Total: ${total_amount}", file=text_file)
	print(f"Average Change : ${avg}", file=text_file)
	print(f"Greatest Increase in Profits : {month_inc} (${inc_change})", file=text_file)
	print(f"Greatest Decrease in Profits : {month_dec} (${dec_change})", file=text_file)
