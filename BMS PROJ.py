import mysql.connector
mydb=mysql.connector.connect(host='Localhost',user='root',password='utkarsh@python04',database='BANK_MANAGEMENT')

def OpenAcc():
    n=input("enter the name:")
    acc=input("enter the account no. :")
    db=input("enter the Date of Birth:")
    add=input("enter the Address:")
    cn=input("enter the contact no. :")
    ob=int(input("enter the opening balance:"))
    data1=(n,acc,db,add,cn,ob)
    data2=(n,acc,ob)
    sql1=('insert into account values (%s,%s,%s,%s,%s,%s)')
    sql2=('insert into amount values (%s,%s,%s)')
    x=mydb.cursor()
    x.execute(sql1,data1)
    x.execute(sql2,data2)
    mydb.commit()
    print("data entered successfully")
    main()
def Depoamo():
    amount=input("Enter the amount you want to deposit")
    acc=input("enter the account no. :")
    a='select balance from amount where AccountNo=%s'
    data=(acc,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    t=result[0]+amount
    sql=('update amount set balance where AccountNO=%s')
    d=(t,acc)
    x.execute(sql,d)
    mydb.commit()
    main()

def withdrawamount():
    amount=input("Enter the amount you want to withdraw")
    acc=input("enter the account no. :")
    s='select balance from amount table where AccountNO=%s'
    data=(acc,)
    x=mydb.cursor()
    x.execute(s,data)
    result=x.fetchone()
    t=result[0]-amount
    sql=('update amount set balance where AccountNO=%s')
    d=(t,acc)
    x.execute(sql,d)
    mydb.commit()
    main()

def Balance():
    acc=input("enter your account no. :")
    a='select * from amount where AccountNo=%s'
    data=(acc,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    print("Balance for account:",acc,"is",result[-1])
    main()
    
def Dispdetails():
    acc=input("enter your account no. :")
    a='select * from account where AccountNo=%s'
    data=(acc,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    for i in result:
        print(i)
    main()

def  Closeacc():
     acc=input("enter your account no. :")
     sql1='delete from the account where AccountNo=%s'
     sql2='delete from amount where AccountNo=%s'
     data=(acc,)
     x=mydb.cursor()
     x.execute(sql1,data)
     x.execute(sql2,data)
     mydb.commit
     main()
    
    
def main():
    print('''
              1.OPEN NEW ACCOUNT
              2.DEPOSIT AMOUNT
              3.WITHDRAW AMOUNT
              4.BALANCE ENQUIRY
              5.DISPLAY CUSTOMER DETAILS
              6.CLOSE AN ACCOUNT''')
    choice=input("Enter the task that you want to perform:")
    if(choice=='1'):
        OpenAcc()
    elif(choice=='2'):
        Depoamo()
    elif(choice=='3'):
        withdrawamount()
    elif(choice=='4'):
        Balance()
    elif(choice=='5'):
        Dispdetails()
    elif(choice=='6'):
        Closeacc()
    else:
        print("invalid choice!")
        main()
main()        
        
