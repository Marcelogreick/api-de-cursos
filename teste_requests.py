import requests


# GET Ratings

ratings = requests.get('http://localhost:8000/api/v2/rating')

print(ratings.status_code)
# print(ratings.json())