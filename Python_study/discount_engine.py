product = input("Product name: ")
amount = float(input("请输入消费金额："))
member_level = input("请输入会员等级(普通会员/黄金会员/白金会员):")
is_birthday = input("是否生日月(是/否)")
#根据金额判断折扣率
if amount >= 500:
    base_discount = 0.8
elif amount >= 200:
    base_discount = 0.9
else:
    base_discount = 1.0
#根据会员等级判断折扣率
if member_level == "普通会员":
    member_discount = 1.0
elif member_level == "黄金会员":
    member_discount = 0.95
else:
    member_discount = 0.98
#根据是否生日月判断折扣率
if is_birthday == "是":
    birthday_discount = 0.9
else:
    birthday_discount = 1.0
final_discount = base_discount * member_discount * birthday_discount
if final_discount < 0.6:
    final_discount = 0.6
final_amount = amount * final_discount
print(f"product name: {product}")
print(f"您最终折扣: {final_discount}")
print(f"您最终支付的金额: {final_amount}")
