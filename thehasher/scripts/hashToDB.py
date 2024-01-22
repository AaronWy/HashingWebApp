import csv 
from io import StringIO
import sqlite3 


def loadToDB(csv_data): 
    try: 
        conn = sqlite3.connect("/Users/aaron/Projects/mysite/db.sqlite3")
        cursor = conn.cursor()
        with open(csv_data,'r',newline='') as csvfile: 
            csv_reader = csv.reader(csvfile)

            for row in csv_reader:
                cursor.execute("INSERT INTO thehasher_hashcatmode (number, name, Category) VALUES (?,?,?)",row)


        conn.commit()
        conn.close()
    

    except Exception as e: 
        print(f"Error: {e}")




csvFile = "./hashcat_data.csv"
loadToDB(csvFile)