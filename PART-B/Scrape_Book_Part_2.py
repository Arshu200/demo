import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# Define the MongoDB connection
client = MongoClient("mongodb://localhost:27017/Scrape_Book")
db = client["bookstore"]
collection = db["books"]

# Scrape data from all 50 pages
for page in range(1, 51):
    url = f'http://books.toscrape.com/catalogue/page-{page}.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for book in soup.find_all('article', class_='product_pod'):
        title = book.h3.a['title']
        price = book.select('div p.price_color')[0].text
        availability = book.select('div p.availability')[0].text.strip()
        rating = book.select('p.star-rating')[0]['class'][1]

        # Create a book document and insert it into MongoDB
        book_doc = {
            "title": title,
            "price": price,
            "availability": availability,
            "rating": rating
        }
        collection.insert_one(book_doc)
print("Successfully!! Fetched and Data is added into the Database")
# Close the MongoDB connection
client.close()
