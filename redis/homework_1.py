import requests
import json

nasa_request = requests.get("https://api.nasa.gov/planetary/apod?api_key=qro0G9f81pFRQyz4qJx06FXeYGbB2JcgjBZQSxTd&date=2017-01-20")

nasa_text  = json.loads(nasa_request.text)
url = nasa_text["url"]

print(url)
