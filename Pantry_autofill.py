"""uses the top 1k ingrients csv file to autofill the pantry table of the FoodieFindz database"""
from csv import reader
from sqlite3 import connect

conn = connect("FoodieFindz_database.db")
c= conn.cursor()
with open('top-1k-ingredients.csv', newline='') as file:
    reader = reader(file)
    for row in reader:
        name, id = row[0].split(";")
        
        
    