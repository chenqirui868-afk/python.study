employees = {'张三':[8000,8500,8200],
             '李四':[9000,9200,9500],
             '王五':[7500,7800,8000]}
person = '张三'
avg_salary = sum(employees['张三'])/len(employees['张三'])
print(f'{'张三'}{avg_salary}')
highest_salary = max(employees.values())
print(highest_salary)
for person in employees:
    avg = sum(employees[person])/len(employees[person])
print(f'{person}的平均月薪是:{avg}')