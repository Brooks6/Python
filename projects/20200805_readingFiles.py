employee_file = open("employee.txt", 'a')
#employee_file.writelines("\nwendy")
employee_file = open("employee.txt", 'r')
print(employee_file.readlines()[1])
employee_file.close()

