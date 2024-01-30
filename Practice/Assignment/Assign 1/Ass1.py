
print("Press 1 to add employee")
print("press 2 to exit")

ep = []

while True:
    ch = int(input("enter number to perform action"))
    if ch == 1:
        ep_no = int(input("enter employee number"))
        emp_name = input("enter emp name")
        emp_sal = int(input("enter salary"))
        emp_ad = input("enter adderes")
        emp_mar_str = input("Married or not").lower()
        emp_mar = True if emp_mar_str == 'true' else False
        
        dt = dict(employee_no = ep_no, name = emp_name , salary = emp_sal , address = emp_ad, married = emp_mar )
        
        ep.append(dt)
    elif ch == 2:
        if not ep:
            print("empty") 
            exit()
        else:
            print(ep)
            file = open('assign1.txt','w')
            file.write(str(ep)+'\n')
            file.close()
            exit()
    else:
        print("exit from loop")
        exit()