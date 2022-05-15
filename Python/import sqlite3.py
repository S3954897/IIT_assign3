import mysql.connector

mydb = mysql.connector.connect(
    host="bqbjw0okdcewzqeo5swt-mysql.services.clever-cloud.com",
    user="uwvzaqz89axgep1k",
    passwd="efTB17fQfWVImVWxZPFI",
    database="bqbjw0okdcewzqeo5swt"
)

mycursor = mydb.cursor()
mycursor.execute("DROP TABLE IF EXISTS users")
mycursor.execute("CREATE TABLE users (f_name VARCHAR(255), l_name VARCHAR(255), dob VARCHAR(255), address VARCHAR(255), phone VARCHAR(255), email VARCHAR(255), password VARCHAR(255))")

sql = "INSERT INTO users (f_name, l_name, dob, address, phone, email, password) VALUES (%s,%s,%s,%s,%s,%s,%s)"
val = ("Grant", "Nicholas", "", "", "", "grant.nicholas@mail.com", "Yolo2009")

mydb.commit()

for x in mycursor:
    print(x)
