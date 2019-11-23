import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="blademaster90",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql="SELECT \
    cashier.name AS cashier, \
    product.name AS product, \
    category.name AS category,\
    product.price AS price\
    FROM product \
    INNER JOIN cashier ON product.id_cashier=cashier.id\
    INNER JOIN category ON product.id_category=category.id"
     
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print (x)