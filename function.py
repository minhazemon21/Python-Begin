def total_expanse(exp):
    total = 0
    for item in exp:
        total = total + item
    return total
emon_expense_list = [50000, 59000, 90000]
keya_expense_list = [10000, 75000, 100000]

emon_total = total_expanse(emon_expense_list)
keya_total = total_expanse(keya_expense_list)

print("Emon's Total Expense", emon_total)
print("Keya's Total Expense", keya_total)

#
def sum(a,b):
    total = a+b
    return total
emon = int(input())
keya = int(input())
e = sum(emon,keya)
print(e)