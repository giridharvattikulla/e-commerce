print("WELCOME To Blink-IT")

x={"akhil":"0000","naveen":"8000" ,"remo":"6000","pawan":"9000","lucky":"7000"}

user=(str(input("Enter The User Name : ")))
password=(str(input("Enter The Password : ")))

fruits={"grapes":150,"apple":120,"orange":100,"mango":200}
vegetables={"carrot":200,"potato":220,"onion":90,"tomato":60}
groceries={"sugar":50,"salt":60,"redchili":60}


if user in x and x[user] == password:
    print("we are providing 3 types of category in our store ")
    print("fruits")
    print("vegetables")
    print("groceries")
    items=(str(input("\nchoose category  : ")))
else:
    print("enter the correct user and password")
        
total = 0

if items == "fruits":
    print("we are providing four types of fruits in our store")
    print("1.grapes = perkg 150")
    print("2.apple = per kg 120")
    print("3.orange = per kg 100")
    print("4.mango = per kg 200\n")


    fitem=(str(input("enter the item : ")))
    fquantity=(int(input("enter how many kgs you want : ")))

    fitem2=(str(input("enter the item : ")))
    fquantity2=(int(input("enter how many kgs you want : ")))

    # packaging

    packging={"wooden-box":60,"plastic-cover":30}
    print("\n we are providing packaging for orders \n select packging type \n a.wooden-box \n b.plastic-cover")
    pitem=(str(input("enter the what type of packging you want : ")))
    
    pprice=packging[pitem] * 1

    cost=fruits[fitem] * fquantity
    cost2=fruits[fitem2] * fquantity2
    total+= cost + cost2 + pprice
    
    # payment mode

    print("\nchoose your payment method")
    print("1 .card ")
    print("2 .upi ")
    print("3 .cash")

    payment = (str(input("enter the Payment option --- ")))

    # cardpayment
    if payment == "card":
        card_number = (int(input("card number : ")))
        cvv = (str(input("enter your cvv : ")))
        print("Total bill =",total)
        p=(str(input("conform your payment yes / no : ")))
        if p == "yes":
            print("payment succesfully completed")
            print("thank you for shopping")
            print("your bill")
            print("cost of" ,fitem , "item :" ,cost)
            print("cost of" ,fitem2 , "item :" ,cost2)
            print("cost of packging : ",pprice)
            print("-----------------------------------")
            print("total bill",total)

        else:
            print("payment is cancelled")

    elif payment == "upi":
        upi_number = (str(input("enter the UPI number : ")))
        otp = (int(input("enter otp 4 digit : ")))
        print("Total bill = ",total)
        p=(str(input("conform your payment yes / no : ")))
        if p =="yes":
            print("payment succesfully completed")
            print("thank you for shopping")
            print("your bill")
            print("cost of" ,fitem , "item :" ,cost)
            print("cost of" ,fitem2 , "item :" ,cost2)
            print("cost of packging : ",pprice)
            print("-----------------------------------")
            print("total bill",total)

        else:
            print("payment is cancelled")

    else:
        print("pay via cash")
        print("thank you for shopping")
        print("your bill")
        print("cost of" ,fitem , "item :" ,cost)
        print("cost of" ,fitem2, "item :" ,cost2)
        print("cost of packging : ",pprice)
        print("-----------------------------------")
        print("total bill",total)

    
   
elif items == "vegetables":
    print("we are providing four types of vegetables in our store ")
    print("1.carrot = 200")
    print("2.potato = 220")
    print("3.onion = 90")
    print("4.tomato = 60\n")

    vitem=(str(input("enter the item : ")))
    vquantity=(int(input("enter how many kgs you want : ")))

    vitem2=(str(input("enter the item : ")))
    vquantity2=(int(input("enter how many kgs you want : ")))

    packging={"wooden-box":60,"plastic-cover":30}
    print("\n we are providing packaging for orders \n select packging type \n a.wooden-box \n b.plastic-cover")
    vpitem=(str(input("enter the what type of packging you want : ")))
    vprice=packging[vpitem] * 1

    vcost=vegetables[vitem] * vquantity
    vcost2=vegetables[vitem2] * vquantity

    total+= vcost + vcost2 + vprice

    print("\nchoose your payment method")
    print("1 .card ")
    print("2 .upi ")
    print("3 .cash")

    payment = (str(input("enter the Payment option --- ")))
    if payment == "card":
        card_number = (int(input("card number : ")))
        cvv = (str(input("enter your cvv : ")))
        print("Total bill = ",total)

        p=(str(input("conform your payment yes / no : ")))
        if p =="yes":
            print("payment succesfully completed")
            print("thank you for shopping")
            print("your bill")
            print("cost of" ,vitem , "item :" ,vcost)
            print("cost of" ,vitem2 , "item :" ,vcost2)
            print("cost of packging : ",vprice)
            print("-----------------------------------")
            print("total bill",total)

        else:
            print("payment is cancelled")

    elif payment == "upi":
        upi_number = (str(input("enter the UPI number : ")))
        otp = (int(input("enter otp 4 digit : ")))
        print("Total bill = ",total)
        p=(str(input("conform your payment yes / no : ")))
        if p =="yes":
            print("payment succesfully completed")
            print("thank you for shopping")
            print("your bill")
            print("cost of" ,vitem , "item :" ,vcost)
            print("cost of" ,vitem2 , "item :" ,vcost2)
            print("cost of packging : ",vprice)
            print("-----------------------------------")
            print("total bill",total)

    else:
        print("pay via cash")
        print("thank you for shopping")
        print("your bill")
        print("cost of" ,vitem , "item :" ,vcost)
        print("cost of" ,vitem2 , "item :" ,vcost2)
        print("cost of packging : ",vprice)
        print("-----------------------------------")
        print("total bill",total)


elif items == "groceries":
    print("we are providing three types of groceries in our store \n 1.sugar = 50 \n 2.salt = 60 \n 3.redchili = 60")

    gitem = str(input("Enter the grocery item: "))
    gquantity = int(input("Enter the quantity you want: "))

    gitem2 = str(input("enter the grocery item:"))
    gquantity2 = int(input("Enter the quantity you want: "))

    gcost = groceries[gitem] * gquantity
    gcost2 = groceries[gitem2] * gquantity2

    packging={"wooden-box":60,"plastic-cover":30}
    print("\nwe are providing packaging for orders \nselect packging types \n a.wooden-box \n b.plastic-cover")
    gpitem=(str(input("enter the packging you want : ")))
    gpprice=packging[gpitem] 

    total += gcost + gcost2 + gpprice

    print("\nChoose your payment method")
    print("1. Card")
    print("2. UPI")
    print("3. Cash")

    payment = str(input("Enter the Payment option: "))
    if payment == "card":
        card_number = str(input("Enter card number: "))
        cvv = str(input("Enter your CVV: "))
        print("Total bill =",total)

        p=(str(input("conform your payment yes / no : ")))
        if p =="yes":
            print("payment succesfully completed")
            print("thank you for shopping")
            print("your bill")
            print("cost of" ,gitem , "item :" ,gcost)
            print("cost of" ,gitem2 , "item :" ,gcost2)
            print("cost of packging : ",gpprice)
            print("-----------------------------------")
            print("total bill",total)

        else:
            print("payment is cancelled")

    elif payment == "upi":
        upi_number = str(input("Enter your UPI ID: "))
        otp = int(input("Enter OTP 4 digits: "))
        print("Total bill =",total)

        p=(str(input("conform your payment yes / no : ")))
        if p =="yes":
            print("payment succesfully completed")
            print("thank you for shopping")
            print("your bill")
            print("cost of" ,gitem , "item :" ,gcost)
            print("cost of" ,gitem2 , "item :" ,gcost2)
            print("cost of packging : ",gpprice)
            print("-----------------------------------")
            print("total bill",total)

        else:
            print("payment is cancelled")

    else:
            print("Pay via cash.")
            print("thank you for shopping")
            print("your bill")
            print("cost of" ,gitem , "item :" ,gcost)
            print("cost of" ,gitem2 , "item :" ,gcost2)
            print("cost of packging : ",gpprice)
            print("-----------------------------------")
            print("total bill",total)

    
else:
        print ("enter correctly")
    
