Aim
To write a Python program to calculate an employee’s net salary using the basic salary, HRA, and PF, and classify the employee as Senior Manager, Manager, or Front Level Job based on the net salary.

Algorithm
1.Start the program.

2.Define a function EmpCalc().

3.Input the employee’s Name.

4.Input the employee’s Age.

5.Input the employee’s Salary.

6.Calculate HRA as 35% of the salary:
HRA = (Salary × 35) / 100

7.Calculate PF as 25% of the salary:

8.PF = (Salary × 25) / 100

9.Calculate Net Salary:

10.Net Salary = Salary + HRA + PF

11.Check the Net Salary:

12.If Net Salary is between 30,000 and 1,00,000, display "Senior manager".

13.Else if Net Salary is between 20,000 and 29,999, display "Manager".

14.Otherwise, display "Front level job".

15.Return the employee’s Name, Age, and Net Salary.

16.Display the employee’s Name, Age, and Net Salary.

17.Stop the program.

    
    def EmpCalc():
    Name=input("enter Name:")
    Age=int(input("enter Age:"))
    sal=float(input("enter salary:"))
    HRA=(sal*35)/100
    PF=(sal*25)/100
    Netsal=sal+HRA+PF
    if(Netsal>=30000) and (Netsal<=100000):
        print("Senior manager")
    elif(Netsal>=20000)and(Netesal<=29999):
            print("Manager")

    else:
          print("Front level job")      
    return Name,Age,Netsal
Name,Age,Netsal=EmpCalc()
print("Employee Name:",Name)
print("Employee age:",Age)
print("Net salary:",Netsal)

OUTPUT:enter Name:himani
enter Age:20
enter salary:30000
Senior manager
Employee Name: himani
Employee age: 20
Net salary: 48000.0

            
