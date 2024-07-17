def service():
    op=int(input("Enter your choice between 1 to 3: "))
    if op==1:
        new_customer()
    elif op==2:
        ex_customer()
    elif op==3:
        exit()
    else:
        print("invalid option plz enter again!")
        service()
def new_customer():
    print(" Enter the below information about new customer ")
    acc=int(input("enter your account no: "))
    pin_no=pin_number()
    name=input("enter customer name: ")
    amount= float(input("Enter the amount::"))
    add=input("enter your address: ")
    ph_no=phone_no()
    acc_type=input("enter type of account: ")
    customer[acc]={'name':name,'amt':amount,'address':add,'phone no':ph_no,'account type':acc_type,'pin_no':pin_no}
    again()
def pin_number():
    n=input("enter pin no :")
    if len(n) == 4:
        return n
    elif len(n)>4:
        print("pin should not be more than four")
        return pin_number()
    else:
        print("Pin should be a four-digit number.")
        return pin_number()
def phone_no():
    ph_no=input("enter your phone no :")
    if len(ph_no) == 10:
        return(ph_no)
    else:
        print("Phone number should be 10 digits.")
        return(ph_no)
def again():
    ch=input("do you want to contiune(yes / no):").lower()
    if ch=="yes":
        new_customer()
    else: 
        main()
def ex_customer():
    global customer
    a=int(input("enter the account no you want to check:"))
    if a in customer:
        print("record found")
        print(customer[a]['name'])
        chance = 3
        while chance >=1:
            pin = input("Enter the pin:::")  
            if pin == customer[a]['pin_no']:
                sub_service(a)
            else:
                print(f"Incorrect pin:{chance-1}")
                if chance==1:
                    main()
            chance+=1
    else:
        again()
def sub_service(a):
    print("1.check balance\n2.deposit\n3.withdrawl\n4.exit")
    op=int(input("enter your choice:"))
    if op==1:
        print("Available balace==>",customer[a]['amt']) 
    elif op==2:
        c=int(input("enter amount you want to deposit ::"))
        customer[a]['amt']+=c
    elif op==3:
        withdrawl(a)
    elif op==4:
        print("*"*50, "\n CUSTOMER DETAILS\n","*"*50)
        print(f"ACCOUNT NO : {a}")
        for k,v in customer[a].items():
            print(f"{k} : {v}")
    elif op==5:
        main()
    else:
        print("invalid option")
        sub_service(a)
    ch=input("do you want to continue (yes/no): ").lower()
    if ch=="yes":
        sub_service(a)
    else:
        main()
def withdrawl(a):
        b=int(input("enter amount you want to withdraw :"))
        customer[a]['amt']-=b
        if customer[a]['amt']<b:
            print(f"available amount{customer[a]['amt']} is less than withdrwal amount")
            withdrawl(a)
        else:
            sub_service(a)
def main():
    print("*" * 50 ,"\n        BANK MANAGEMENT SYSTEM        \n","*"*50)
    print("please choose any one option")
    print("  1. New_customer \n  2. Existing_customer \n  3. Exit")
    service() 

customer={}
main()
