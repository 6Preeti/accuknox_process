import sqlite3
import pandas as pd;

#load CSV data file
df=pd.read_csv('diabetes.csv')

#Data clean up
df.columns=df.columns.str.strip()

#connect to the sqlite database
connection=sqlite3.connect('database.db')

#load CSV data file to sqlite
df.to_sql('DiabetesPedigreeFunction',connection,if_exists='replace')

#close the connection
connection.close()

