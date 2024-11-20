username="surendra"
password="1234"
user_name=input("enter the you username:")
pass_word=input("enter the password:")
s='''
1.credit
2.debit
3.mini statement
4.exit
'''
amount=10000
if user_name==username and pass_word==password:
    print(s)
while True:        
    option=(input("enter the option:"))
    if option==1:
        credit=int(input("enter the amount:"))
        print("amount after credit:", amount+credit)
            
    elif option==2:
        debits=float(input("enter the amount:",amount-debits))
        print("amount after debit:",amount)
    elif option==3:
            print("amount",amount)
    elif option==4:    
        break
else:
        print("incorrect")  
   


