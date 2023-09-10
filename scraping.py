import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# get the content
url = "http://books.toscrape.com/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    book_titles = []
    book_prices = []
    book_ratings = []

    # scrape the data
    for book in soup.find_all('h3'):
        title = book.a.attrs['title']
        book_titles.append(title)

    for price in soup.find_all('p', class_='price_color'):
        book_prices.append(price.text)

    for rating in soup.find_all('p', class_='star-rating'):
        rating_class = rating.attrs['class'][-1]
        book_ratings.append(rating_class)

    # store the data
    data = {
        'Title': book_titles,
        'Price': book_prices,
        'Rating': book_ratings
    }

    df = pd.DataFrame(data)

    # visualize the data
    rating_counts = df['Rating'].value_counts()
    rating_counts.plot(kind='bar', color='skyblue')
    plt.title('Book Ratings')
    plt.xlabel('Rating')
    plt.ylabel('Count')
    plt.show()

else:
    print("Failed to retrieve the web page")