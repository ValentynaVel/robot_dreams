# 1. Написати програму, яка буде робити запит на один із 5 сайтів і друкувати статус-код відповіді,
# назву сайту, а також довжину HTML-коду із відповіді.
# Вибір сайту для здійснення запиту має бути здійснений випадковим чином (random).
# Сайти:
# google.com,
# facebook.com,
# twitter.com,
# amazon.com,
# apple.com.

import random
import requests

lst_url = [
    "https://www.google.co.uk/",
    "https://www.facebook.com/",
    "https://twitter.com/",
    "https://www.amazon.co.uk/",
    "https://www.apple.com/"]

res = requests.get(random.choice(lst_url))
print(res.status_code, len(res.text), random.choice(lst_url))

