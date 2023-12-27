

'''def welcome():
	print("Welcome to your dashboard")

#def gainAccess(Username=None, Password=None):
    Username = input("Enter your username:")
    Password = input("Enter your Password:")
    
    if not len(Username or Password) < 1:
        if True:
            db = open("database.txt", "r")
            d = []
            f = []
            for i in db:
                a,b = i.split(",")
                b = b.strip()
                c = a,b
                d.append(a)
                f.append(b)
                data = dict(zip(d, f))
            try:
                if Username in data:
                    hashed = data[Username].strip('b')
                    hashed = hashed.replace("'", "")
                    hashed = hashed.encode('utf-8')
                    
                    try:
                        if bcrypt.checkpw(Password.encode(), hashed):
                        
                            print("Login success!")
                            print("Hi", Username)
                            welcome()
                        else:
                            print("Wrong password")
                        
                    except:
                        print("Incorrect passwords or username")
                else:
                    print("Username doesn't exist")
            except:
                print("Password or username doesn't exist")
        else:
            print("Error logging into the system")
            
    else:
        print("Please attempt login again")
        gainAccess()
		
		# b = b.strip()
# accessDb()

def register(Username=None, Password1=None, Password2=None):
    Username = input("Enter a username:")
    Password1 = input("Create password:")
    Password2 = input("Confirm Password:")
    db = open("database.txt", "r")
    d = []
    for i in db:
        a,b = i.split(",")
        b = b.strip()
        c = a,b
        d.append(a)
    if not len(Password1)<=8:
        db = open("database.txt", "r")
        if not Username ==None:
            if len(Username) <1:
                print("Please provide a username")
                register()
            elif Username in d:
                print("Username exists")
                register()		
            else:
                if Password1 == Password2:
                    Password1 = Password1.encode('utf-8')
                    Password1 = bcrypt.hashpw(Password1, bcrypt.gensalt())
                                       
                    db = open("database.txt", "a")
                    db.write(Username+", "+str(Password1)+"\n")
                    print("User created successfully!")
                    print("Please login to proceed:")

					
					# print(texts)
                else:
                    print("Passwords do not match")
                    register()
    else:
        print("Password too short")



def home(option=None):
	print("Welcome, please select an option")
	option = input("Login | Signup:")
	if option == "Login":
		gainAccess()
	elif option == "Signup":
		register()
	else:
		print("Please enter a valid parameter, this is case-sensitive")




# register(Username, Password1, Password2)
# gainAccess(Username, Password1)
home()'''


def welcome():
	print("Welcome to your dashboard")

def gainAccess(Username=None, Password=None):
    Username = input("Enter your username:")
    Password = input("Enter your Password:")
    
    if not len(Username or Password) < 1:
        if True:
            db = open("database.txt", "r")
            d = []
            f = []
            for i in db:
                a,b = i.split(",")
                b = b.strip()
                c = a,b
                d.append(a)
                f.append(b)
                data = dict(zip(d, f))
            try:
                if Username in data:
                   # hashed = data[Username].strip('b')
                    #hashed = hashed.replace("'", "")
                    #hashed = hashed.encode('utf-8')
                    
                    try:
                        if Password==data[Username]:
                        
                            print("Login success!")
                            print("Hi", Username)
                            welcome()
                        else:
                            print("Wrong password")
                        
                    except:
                        print("Incorrect passwords or username")
                else:
                    print("Username doesn't exist")
            except:
                print("Password or username doesn't exist")
        else:
            print("Error logging into the system")
            
    else:
        print("Please attempt login again")
        gainAccess()
		
		# b = b.strip()
# accessDb()

def register(Username=None, Password1=None, Password2=None):
    Username = input("Enter a username:")
    Password1 = input("Create password:")
    Password2 = input("Confirm Password:")
    d = []
    f=[]
    for i in db:
        a,b=i.split(",")
        b=b.strip()
        d.append(a)
        f.append
					
					# print(texts)
            else:
                    print("Passwords do not match")
                    register()
    else:
        print("Password too short")



def home(option=None):
	print("Welcome, please select an option")
	option = input("Login | Signup:")
	if option == "Login":
		gainAccess()
	elif option == "Signup":
		register()
	else:
		print("Please enter a valid parameter, this is case-sensitive")




# register(Username, Password1, Password2)
# gainAccess(Username, Password1)
home()





















import math, random

def generateCardno() :

    # Declare a digits variable
    # which stores all digits
    digits = "0123456789"
    Cardno = ""

    for i in range(16) :
        Cardno += digits[math.floor(random.random() * 10)]

    return Cardno

if __name__ == "__main__" :
    
    print("Cardno of 16 digits:", generateCardno())

def newcard():
    n=input("enter the name:")
    db=input("enter the Date of Birth:")
    add=input("enter the Address:")
    cn=input("enter the contact no. :")
    ob=int(input("enter the limit required:"))
    em=input("enter your email: ")
    pas=input
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

def main():
    print("WELCOME TO CARD MANAGEMENT SYSTEM,")
    print("Select from options below")
    print('''
              1.GET A NEW CARD
              2.VIEW CARD DETAILS
              3.REDEEM YOUR LOYALTY POINTS
              4.PAY YOUR BILLS''')
    choice=input("Enter the task that you want to perform:")
    if(choice=='1'):
        OpenAcc()
    elif(choice=='2'):
        Depoamo()
    elif(choice=='3'):
        withdrawamount()
    elif(choice=='4'):
        Balance()

    else:
        print("invalid choice!")
        main()
main()        
