# pip install beautifulsoup4 lxml requests pandas openpyxl
# url: https://books.toscrape.com/

#importing the necessary libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_data(url):
    response = requests.get(url)  # calling the "GET" request to send a request to the url
    soup = BeautifulSoup(response.text, "lxml")  # parsing the page using 'lxml'

    books = soup.find_all("article", class_="product_pod")  # finding all article tags with product_pod class
    data = []

    for book in books:
        item = {}
        item["Title"] = book.find("h3").find("a")["title"]  # getting the title of the book from the 'title' attribute of the 'a' tag inside 'h3'
        item["Price"] = book.find("p", class_="price_color").text[1:]  # Extracting price from the text of each <p> element with class name as 'price_color'

        data.append(item)

    return data

def export_data(data):
    df = pd.DataFrame(data)  # creating a dataframe
    df.to_excel("book.xlsx")  # saving it into an excel file named 'book.xlsx'
    df.to_csv("books.csv")  # saving it into a csv file named 'books.csv'

if __name__ == '__main__':
    data = get_data("https://books.toscrape.com/")  # getting the data from the website
    print("Titles and Prices:")
    for item in data:
        print(f"Title: {item['Title']}, Price: {item['Price']}")
    export_data(data)  # calling export function to write this data into an excel & csv file format
    print("Web Scraping Done!")
