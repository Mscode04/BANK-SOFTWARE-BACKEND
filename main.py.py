import mysql.connector as x

# MYSQL AND PYTHON CONNECTION
db = x.connect(host="host_name", user="root", passwd="password")
c = db.cursor()

# DATABASE AND TABLES CREATION
c.execute("create database if not exists euro_bank_of_california")
c.execute("use euro_bank_of_california")
c.execute(
    "create table if not exists BANK_MASTER(Account_number int ,Pin_number varchar(8) primary key, Name varchar(50),"
    "City varchar(50),Mobile varchar(15) ,Balance int)")
c.execute(
    "create table if not exists BANK_TRANSACTION(Account_number int ,Amount int,Date_of_transaction date,"
    "Transaction_type varchar(50))")
c.execute(
    "create table if not exists EMPLOYEE(Employee_ID varchar(20) primary key, Employee_Name varchar(30), Age varchar("
    "20), Employee_Salary varchar(20))")
c.execute(
    "create table if not exists EMPLOYEE_ATTENDANCE(Employee_ID int , Employee_Name varchar(30), "
    "Date_of_attendance date, attendance_status varchar(6))")
db.commit()

# BANK OFFICIAL PASS CODE
Bank_id = ["euro@1980"]


# PIN NUMBERS WILL ENROLLED
def AUTO_CALL_PIN():
    data_pin = []
    c.execute("select Pin_number from BANK_MASTER")
    get_data = c.fetchall()
    for rec in get_data:
        rec = list(rec)
        for fec in rec:
            data_pin.append(fec)
    return data_pin


# EMPLOYEE ID WILL ENROLLED
def AUTO_CALL_ID():
    employee_id_list = []
    c.execute("select Employee_ID from EMPLOYEE")
    get_data = c.fetchall()
    for rec in get_data:
        rec = list(rec)
        for fec in rec:
            employee_id_list.append(fec)
    return employee_id_list


# THE MAIN FUNCTION :  MENU FUNCTION
def MENU():
    Wish = input("DO YOU WANT TO OPEN THE BANK SERVER (Y/N) ")
    print("**********   EURO BANK LIMITED CALIFORNIA   **********")
    print()
    Bank_id_entered = input("ENTER THE YOUR BANK ID NUMBER : ")
    print('******************')
    print('------------------')

    if Bank_id_entered in Bank_id:
        while Wish == "Y" or "y":
            print()
            print()
            print("1=CREATE NEW ACCOUNT")
            print()
            print("2=DEPOSIT MONEY")
            print()
            print("3=WITHDRAW MONEY")
            print()
            print("4=DISPLAY ACCOUNT")
            print()
            print("5 DISPLAY ACCOUNT STATEMENT")
            print()
            print("6=ADD NEW EMPLOYEE TO BANK")
            print()
            print("7=EMPLOYEE ATTENDANCE PORTAL")
            print()
            print("8=EXIT FROM SERVER")
            print()
            choice = int(input("ENTER YOUR PREFERENCE: "))
            print('******************')
            print('------------------')
            print()
            if choice == 1:
                CREATE_ACCOUNT()
            elif choice == 2:
                data = AUTO_CALL_PIN()
                DEPOSIT_MONEY(data)
            elif choice == 3:
                data = AUTO_CALL_PIN()
                WITHDRAW(data)
            elif choice == 4:
                DISPLAY_ACCOUNT_DETAILS()
            elif choice == 5:
                DISPLAY_ACCOUNT_STATEMENTS()
            elif choice == 6:
                ADD_NEW_EMPLOYEE()
            elif choice == 7:
                rec = AUTO_CALL_ID()
                EMPLOYEE_ATTENDANCE(rec)
            elif choice == 8:
                print("EXIT FROM EURO BANK LIMITED CALIFORNIA")
                print('******************')
                print('------------------')
                print("**********THANK YOU FOR CHOOSING EURO BANK LIMITED CALIFORNIA**********")
                print()
                break
            else:
                print('-----------')
                print('***********')
                print('WRONG INPUT')
                print('***********')
                print('-----------')
                print()

    else:
        print('-----------')
        print('***********')
        print('INVALID PIN')
        print('***********')
        print('-----------')
        print()


# CREATE AN ACCOUNT
def CREATE_ACCOUNT():
    print("ALL INFORMATION PROMPTED ARE MANDATORY TO BE FILLED")
    print()
    Ano = str(input("ENTER YOUR ACCOUNT NUMBER: "))
    print()
    Name = input("ENTER USER NAME: ")
    print()
    Pin = input("ENTER THE NEW ACCOUNT PIN NUMBER")
    print()
    Pin_02 = input("REENTER PIN NUMBER")
    print()
    if Pin == Pin_02:
        City = str(input("ENTER YOUR CITY NAME: "))
        print()
        Mn = int(input("ENTER YOUR MOBILE NUMBER: "))
        Balance = 0
        c.execute(
            "insert into BANK_MASTER values('" + str(Ano) + "','" + Pin + "','" + Name + "','" + City + "','" +
            str(Mn) + "','" + str(Balance) + "')")
        db.commit()
        db.close()
        print("***** ACCOUNT IS SUCCESSFULLY CREATED!!! *****")
    else:
        while True:
            print("PIN NOT MATCH")
            print()
            Pin = input("ENTER THE NEW ACCOUNT PIN NUMBER")
            print()
            Pin_02 = input("REENTER PIN NUMBER")
            if Pin == Pin_02:
                City = str(input("ENTER YOUR CITY NAME: "))
                print()
                Mn = int(input("ENTER YOUR MOBILE NUMBER: "))
                print()
                Balance = 0
                c.execute("insert into BANK_MASTER values('" + str(
                    Ano) + "','" + Pin + "','" + Name + "','" + City + "','" + str(Mn) + "','" + str(
                    Balance) + "')")
                db.commit()
                db.close()
                print("***** ACCOUNT IS SUCCESSFULLY CREATED!!! *****")
                break
            else:
                pass


# MONEY DEPOSIT
def DEPOSIT_MONEY(data_list=None):
    print(data_list)
    n = int(input(" ENTER HOW MANY DEPOSIT REQUESTS: "))
    print()
    i = 0
    while i < n:
        Pin = input("ENTER THE ACCOUNT PIN NUMBER")
        if Pin in data_list:
            Ano = str(input("ENTER ACCOUNT NUMBER: "))
            print()
            Dp = (input("ENTER AMOUNT TO BE DEPOSITED: "))
            print()
            Dot = str(input("ENTER DATE OF TRANSACTION: YYYY-MM-DD "))
            print()
            Ttype = "MONEY DEPOSIT REQUEST"
            c.execute("insert into BANK_TRANSACTION values('" + Ano + "','" + Dp + "','" + Dot + "','" + Ttype + "')")
            c.execute("update BANK_MASTER set Balance=Balance+ '" + Dp + "' where Pin_number='" + Pin + "'")
            db.commit()
            print("***** MONEY DEPOSIT REQUEST IS SUCCESSFULLY COMPLETED!!! *****")
            print()
        else:
            print("AGAIN YOU ENTER WRONG PIN NUMBER")
            print('******************')
            print('------------------')
            print()
            print(" EXIT AND CONTINUE")
            print()
            print('******************')
            print('------------------')
            break
        i = i + 1


# WITHDRAW MONEY
def WITHDRAW(data_list=None):
    print(data_list)
    n = int(input(" ENTER HOW MANY DEPOSIT REQUESTS: "))
    print()
    i = 0
    while i < n:
        Pin = input("ENTER THE ACCOUNT PIN NUMBER")
        print()
        if Pin in data_list:
            Ano = str(input("ENTER ACCOUNT NUMBER: "))
            print()
            Dp = (input("ENTER AMOUNT TO BE WITHDRAW: "))
            print()
            Dot = str(input("ENTER DATE OF TRANSACTION: YYYY-MM-DD "))
            print()
            Ttype = "MONEY WITHDRAWAL REQUEST"
            c.execute(
                "insert into BANK_TRANSACTION values('" + Ano + "','" + Dp + "','" + Dot + "','" + Ttype + "')")
            c.execute("update BANK_MASTER set Balance=Balance- '" + Dp + "' where Pin_number='" + Pin + "'")
            db.commit()
            print("***** MONEY WITHDRAWAL REQUEST SUCCESSFULLY COMPLETED!!! *****")
            print()
        else:
            print("AGAIN YOU ENTER WRONG PIN NUMBER")
            print('******************')
            print('------------------')
            print()
            print(" EXIT AND CONTINUE")
            print()
            print('******************')
            print('------------------')
            break
        i = i + 1


# DISPLAY ACCOUNT DETAILS
def DISPLAY_ACCOUNT_DETAILS():
    Ano = str(input("ENTER ACCOUNT NUMBER TO SHOW DETAILS:"))
    print()
    c.execute("select * from BANK_MASTER where Account_number='" + Ano + "'")
    result = c.fetchall()
    for rec in result:
        print(rec)
        print()
    print("********** END OF THE DETAILS **********")
    print()
    print('******************')
    print('------------------')


# DISPLAY ACCOUNT STATEMENT
def DISPLAY_ACCOUNT_STATEMENTS():
    Ano = str(input("ENTER ACCOUNT NUMBER TO SHOW DETAILS:"))
    print()
    c.execute("select * from BANK_TRANSACTION where Account_number='" + Ano + "'")
    result = c.fetchall()
    for rec in result:
        print(rec)
        print()
    print("********** END OF THE STATEMENT **********")
    print()
    print('******************')
    print('------------------')


# EMPLOYEE ATTENDANCE REGISTER
def EMPLOYEE_ATTENDANCE(employee_id_list=None):
    print(employee_id_list)
    print("*** WELCOME TO EMPLOYEE ATTENDANCE WINDOW ***")
    EmployeeID = input("ENTER EMPLOYEE ID: ")
    if EmployeeID in employee_id_list:
        Name = input("ENTER NAME: ")
        print()
        Date = str(input("ENTER DATE: "))
        print()
        Status = str(input("ENTER YOUR ATTENDANCE ABSENCE OR PRESENT"))
        c.execute(
            "insert into EMPLOYEE_ATTENDANCE values('" + EmployeeID + "','" + Name + "','" + Date + "','" + Status +
            "')")
        db.commit()
    else:
        print("***** ENTERED ID IS NOT MATCH *****")
        print()
        print('******************')
        print('------------------')
        print()
        print(" EXIT AND CONTINUE")
        print()
        print('******************')
        print('------------------')


# ADD NEW EMPLOYEE
def ADD_NEW_EMPLOYEE():
    print("WELCOME TO EMPLOYEE DETAILS WINDOW")
    n = int(input(" ENTER HOW MANY EMPLOYEES SHOULD BE ADDED: "))
    i = 0
    while i < n:
        EmpID = str(input("ENTER EMPLOYEE ID: "))
        print()
        Name = input("ENTER NAME: ")
        print()
        Age = str(input("ENTER AGE: "))
        print()
        salary = str(input("ENTER SALARY: "))
        c.execute("insert into EMPLOYEE values('" + str(EmpID) + "','" + Name + "','" + str(Age) + "','" + str(
            salary) + "')")
        i = i + 1
    print("***** DATAS ARE STORED *****")
    db.commit()


MENU()
