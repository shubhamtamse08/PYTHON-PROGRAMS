class emp:
    profit=1000000
    tax=10
    company="cognizate"
    def __init__(self,name,sal,age,per):
        self.name=name
        self.sal=sal
        self.age=age
        self.per=per
        self.tax_amount=0
        self.share_amount=0

    def cal_tax(self):
        return (emp.tax/100)*self.sal

    def cal_share(self):
        return (self.per / 100)*emp.profit


    def display(self):
        print("1",self.name)
        print("2",emp.company)
        print("3",self.age)
        print("4",self.cal_tax())
        print("5",self.cal_share())


a1=emp("sachin",50000,40,5)
a2=emp("rahul",30000,38,2)
a1.display()
print("----------")
a2.display()