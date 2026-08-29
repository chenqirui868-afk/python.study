clients = {
    '客户A': {'股票': 100000, '基金': 50000, '债券': 30000},
    '客户B': {'股票': 150000, '基金': 80000, '债券': 40000},
    '客户C': {'股票': 80000, '基金': 40000, '债券': 25000}
}
print(clients['客户B']['基金'])
total = sum(clients['客户C'].values())
print(total)
highest_client = None
highest_bond = 0
for client, investments in clients.items():
    if investments['债券'] > highest_bond:
        highest_bond = investments['债券']
        highest_client = client
print(f"{highest_client}的债券投资最多:{highest_bond}")
