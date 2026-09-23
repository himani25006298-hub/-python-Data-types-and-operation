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
            
