from tabulate import tabulate
headers=["Name","Age","Department"]
data=[
    ["raj",25,"HR"]
    ["anjali",34,"finace"]
    ["aman",23,"sells"]
    ["hem",29,"finace"]
]
print(tabulate(data,headers=headers,tablefmt="fancy_grid"))