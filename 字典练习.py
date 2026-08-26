books = {"书名": "西游记",
         "作者": "吴承恩",
         "价格": 50}
print(books["书名"])

books["价格"] = 60
books["类型"] = "小说"
for key,value in books.items():
    print(key,":",value)