#import mysql.connector
from database import *



# Connect to the MySQL database
conn = mysql.connector.connect(host='localhost',
                               user='root',
                               password='',
                               port = 3307,
                               database='test')

# Create a cursor object
cursor = conn.cursor()

#cursor.execute('DROP TABLE Announcement')

#cursor.execute('ALTER TABLE announcement DROP COLUMN announcer_name')

#QUERY to create table Block
# cursor.execute('CREATE TABLE Block(BlockNo varchar(10),HouseNo varchar(10),Availability boolean,BHK int)')

#QUERY to add data in table Block
# floor = ['G','F','S']
# for i in range (6):
#     for j in range (3):
#         for k in range (3):
#             cursor.execute("INSERT INTO block VALUES (%s,%s,%s,%s)",(chr(65+i),floor[j]+str(k+1),0,k+1))

#QUERY to create table Resident
#cursor.execute('CREATE Table Resident(Username VARCHAR(100),Password VARCHAR(100), Name VARCHAR(100) , Phone VARCHAR(15) , BlockNo varchar(10),HouseNo varchar(10) ,Join_Date DATE ,  Maintainence_fee BOOLEAN , Due_Date DATE , Admin BOOLEAN)')

# cursor.execute('SELECT * FROM block')

#QUERY to create table Announcement
# cursor.execute('''CREATE Table Announcement(
#                 id INT AUTO_INCREMENT PRIMARY KEY,
#                 Name VARCHAR(255),
#                 announcement_datetime DATETIME,
#                 announcement_text TEXT,              
#                 image1 BLOB,
#                 image2 BLOB,
#                 image3 BLOB
#                 )''')





# # Fetch the results
# results = cursor.fetchall()

# Close the cursor and connection
conn.commit()
cursor.close()
# conn.close()

# # Print the results
# for row in results:
#     print(row)
