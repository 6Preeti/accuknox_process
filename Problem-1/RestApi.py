import requests
import sqlite3

# Fetch data from Google Books API
response = requests.get('https://www.googleapis.com/books/v1/volumes?q=subject:fiction&maxResults=10')
data = response.json().get('items', [])

# Connect to SQLite database
conn = sqlite3.connect('books.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS books
             (title TEXT, author TEXT, publication_year INTEGER)''')

# Insert data into table
for book in data:
    volume_info = book.get('volumeInfo')
    if volume_info:
        title = volume_info.get('title')
        author = volume_info.get('authors')[0] if volume_info.get('authors') else None
        publication_year = volume_info.get('publishedDate')[:4] if volume_info.get('publishedDate') else None
        if all([title, author, publication_year]):
            c.execute("INSERT INTO books VALUES (?, ?, ?)", (title, author, int(publication_year)))

# Commit changes and close connection
conn.commit()
conn.close()

