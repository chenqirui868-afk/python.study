print("hello world")
name=input("请输入你的名字：")
print("你好,"+ name +"！")
age = 20
height = 1.75
is_student = True
print("年龄:", age)
print("身高:", height)
print("是学生吗:", is_student)
score = int(input("\n请输入你的分数 (0-100) : "))
if score >= 90:
    print("优秀！")
elif score >= 80:
    print("很好！")
elif score >= 70:
    print("及格！")
else:
    print("不及格,继续努力! ")
print("\n---乘法表(5 的乘法) --- ")
for i in range(1,11):
    result = 5 * i
    print(f"5 x {i} = {result}")
print("\n--- 猜数字游戏 ---")
secret = 7
guess = 0
while guess != secret:
    guess = int(input("猜一个数字 （1-10）："))
    if guess > secret:
        print("太大了，再试试！")
    elif guess < secret:
        print("太小了，再试试！")
    else:
        print("恭喜你,猜对了！")
