class employee:
    def __init__(self,employee_id,name,basic_salary):
        self.employee_id=employee_id
        self.name=name
        self.basic_salary=basic_salary
    def calaculate_salary(self):
        hra=0.2*self.basic_salary
        da=0.1*self.basic_salary
        total_salary=self.basic_salary+hra+da
        return total_salary
himanshu=employee(101,"Himanshu",50000)
print(himanshu.calaculate_salary()) 