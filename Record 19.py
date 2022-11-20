import mysql.connector as mycon
mydb=mycon.connect(host='localhost',database='Ritesh',user='root',passwd='monu@2005')
mycursor=mydb.cursor()
mycursor.execute("Select * from empl")
print("Empno","Ename","Job","Mgr","Hiredate","Sal","Comm","Deptno",sep='\t')
for i in mycursor:
    print(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],sep='\t')
