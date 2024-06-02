import requests

api_key = "648ab7c41f12484a9b7d5b700d3cffd3"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-05-02&sortBy=publishedAt&apiKey=648ab7c41f12484a9b7d5b700d3cffd3"

#make request
request = requests.get(url)

#get a dict with data
content = request.json()

#access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])