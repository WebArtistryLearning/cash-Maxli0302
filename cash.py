change = input ()
change = int(change)
number = change // 25
left = change % 25
number = number + left // 10
left = left % 10
number = number + left // 5
left = left % 5
number = number + left
print(number)