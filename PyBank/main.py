import csv
import os

budget_file = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'Resources', 'budget_data.csv')
with open(budget_file, newline='', encoding='utf-8') as f:
    all_months = list(csv.reader(f))[1:]

total_months = len(all_months)

total = 0
count = -1
month_to_month_changes = {}
for x in all_months:
    count += 1
    month = x[0]
    month_total = int(x[1])
    total += month_total
    if count == 0:
        continue
    previous_month_total = int(all_months[count - 1][1])
    if month_total > previous_month_total:
        if month_total < 0 and previous_month_total < 0:
            month_to_month_changes[month] = abs(
                previous_month_total) - abs(month_total)
        elif month_total > 0 and previous_month_total < 0:
            month_to_month_changes[month] = month_total + \
                abs(previous_month_total)
        else:
            month_to_month_changes[month] = month_total - previous_month_total
    else:
        if previous_month_total < 0 and month_total < 0:
            month_to_month_changes[month] = (
                abs(month_total) - abs(previous_month_total)) * -1
        elif previous_month_total > 0 and month_total < 0:
            month_to_month_changes[month] = (
                previous_month_total + abs(month_total)) * -1
        else:
            month_to_month_changes[month] = (
                previous_month_total - month_total) * -1

avg_change = round(sum(month_to_month_changes.values()) /
                   (total_months - 1), 2)

max_val = {'month': None, 'value': 0}
min_val = {'month': None, 'value': 0}
for x, y in month_to_month_changes.items():
    if y > max_val['value']:
        max_val['month'] = x
        max_val['value'] = y
    if y < min_val['value']:
        min_val['month'] = x
        min_val['value'] = y


output = []

output.append("Financial Analysis")
output.append('-'*25)
output.append("Total Months: " + str(total_months))
output.append("Total: $ " + str(total))
output.append("Average Change: " + str(avg_change))
output.append("Greatest Increase In Profits: " +
              max_val['month'] + " ($" + str(max_val['value']) + ")")
output.append("Greatest Decrease In Profits: " +
              min_val['month'] + " ($" + str(min_val['value']) + ")")

output_file = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'analysis', 'output.txt')
with open(output_file, 'w') as f:
    for x in output:
        print(x, "\n")
        f.write(x + "\n")
