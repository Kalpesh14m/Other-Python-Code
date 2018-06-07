cgpa = float(input("Please enter your CGPA: "))
percentage = float((cgpa - 0.75) * 10)

marks = percentage * 5

print("Your percentage is : ", float(percentage), "%")
print("Your marks is : ", int(marks))
