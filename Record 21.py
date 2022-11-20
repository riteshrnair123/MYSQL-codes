import mysql.connector as sql
mydb=sql.connect(host='localhost',user='root',passwd='monu@2005',database="Ritesh")
mycursor =mydb.cursor()
mycursor.execute("drop table Employee")
mycursor.execute("create table Employee( EmpId Varchar(4), empname varchar(30),designation varchar(40),salary Integer,experience integer)")
mycursor.execute("insert into Employee values('M001','Ahmad zussain','Manager',100000,3)")
mycursor.execute("insert into Employee values('S012','Ravinder','Sales Personnel',5500,1)")
mycursor.execute("insert into Employee values('F013','Janila','Finance Manager',7000,2)")
mycursor.execute("insert into Employee values('S114','Naaz','Security Personnel',3000,2)")
mycursor.execute("insert into Employee values('S215','Radhe Shyam','Supervisor',4000,1)")
mycursor.execute("insert into Employee values('O116','Chander Nath','Operator',2500,2)")
mydb.commit()
def connect():
    import mysql.connector as mycon
    mydb=mycon.connect(host='localhost',database='Ritesh',user='root',passwd='monu@2005')
    mycursor=mydb.cursor()
    mycursor.execute("Select * from Employee")
    for i in mycursor:
        print(i)
def delete():
    import mysql.connector as mycon
    mydb=mycon.connect(host='localhost',database='Ritesh',user='root',passwd='monu@2005')
    mycursor=mydb.cursor()
    x=input("Enter the Employee ID to be updated: ")
    a=int(input("Enter the new salary: "))
    st="update employee set salary={} where empID='{}'".format(a,x)
    mycursor.execute(st)
    mycursor.execute("Select * from Employee")
    rows=mycursor.fetchall()
    for i in rows:
        print(i)
    mydb.commit()
while True:
    print("1) Display the table")
    print("2) Update the details of a particular employee")
    ch=int(input("Enter the choice: "))
    if ch==2:
        delete()
    elif ch==1:
        connect()
    ans=input("Do you want to continue(y/n): ")
    if ans=='n':
        break
