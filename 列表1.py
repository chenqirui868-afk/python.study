fruits = ["苹果", "香蕉", "橙子"]

# 添加元素
fruits.append("葡萄")
print("添加后：", fruits)

# 访问元素
print("第一个水果：", fruits[0])
print("最后一个水果：", fruits[-1])

# 列表长度
print("总共有", len(fruits), "个水果")

# 删除元素
fruits.remove("香蕉")
print("删除后：", fruits)

# 遍历列表
print("所有水果：")
for fruit in fruits:
    print(" -", fruit)