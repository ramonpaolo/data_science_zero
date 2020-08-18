from twython import Twython
import csv, json, requests
from bs4 import BeautifulSoup


CONSUMER_KEY, CONSUMER_SECRET, ACCES_TOKEN, ACCES_TOKEN_SECRET = "", "", "", ""
def call_twitter_search_api():
    twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET)

    for status in twitter.search(q='"data science"')["statuses"]:
        user = status["user"]["screen_name"].encode("utf-8")
        text = status["text"].encode("utf-8")
        print(user, ":", text)
        print()

from twython import TwythonStreamer

tweets = []

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if data["lang"] == "en":
            tweets.append(data)
        if len(tweets) >= 1000:
            self.disconnect()

    def on_error(self, status_code, data, headers=None):
        print(status_code, data)
        self.disconnect()

def call_twitter_streaming_api():
    stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, ACCES_TOKEN, ACCES_TOKEN_SECRET)

    stream.statuses.filter(track="data")

if __name__ == "__main__":
    def process(date, symbol, price):
        print(date, symbol, price)


    print("tab delimited stock prices:")

    with open('tab_delimited_stock_prices.txt', 'r', encoding='utf8', newline='') as f:
        reader = csv.reader(f, delimiter='\t')
        # reader = csv.reader(codecs.iterdecode(f, 'utf-8'), delimiter='\t')
        for row in reader:
            date = row[0]
            symbol = row[1]
            closing_price = float(row[2])
            process(date, symbol, closing_price)

    print()

    print("colon delimited stock prices:")

    with open('colon_delimited_stock_prices.txt', 'r', encoding='utf8', newline='') as f:
        reader = csv.DictReader(f, delimiter=':')
        # reader = csv.DictReader(codecs.iterdecode(f, 'utf-8'), delimiter=':')
        for row in reader:
            date = row["date"]
            symbol = row["symbol"]
            closing_price = float(row["closing_price"])
            process(date, symbol, closing_price)

    print()

    print("writing out comma_delimited_stock_prices.txt")

    today_prices = {'AAPL': 90.91, 'MSFT': 41.68, 'FB': 64.5}

    with open('comma_delimited_stock_prices.txt', 'w', encoding='utf8', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        for stock, price in today_prices.items():
            writer.writerow([stock, price])

    print("BeautifulSoup")
    html = requests.get("http://www.example.com").text
    soup = BeautifulSoup(html)
    print(soup)
    print()

    print("parsing json")

    serialized = """{ "title" : "Data Science Book",
                          "author" : "Joel Grus",
                          "publicationYear" : 2014,
                          "topics" : [ "data", "science", "data science"] }"""

    # parse the JSON to create a Python object
    deserialized = json.loads(serialized)
    if "data science" in deserialized["topics"]:
        print(deserialized)

    print()

    # print("GitHub API")
    # print("dates", dates)
    # print("month_counts", month_counts)
    # print("weekday_count", weekday_counts)
    #
    # last_5_repositories = sorted(repos,
    #                              key=lambda r: r["created_at"],
    #                              reverse=True)[:5]
    #
    # print("last five languages", [repo["language"]
    #                               for repo in last_5_repositories])