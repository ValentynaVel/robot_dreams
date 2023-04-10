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

gl = "https://www.google.co.uk/"
fb = "https://www.facebook.com/"
tw = "https://twitter.com/"
am = "https://www.amazon.co.uk/"
ap = "https://www.apple.com/"

lst_url = [gl, fb, tw, am, ap]
res = requests.get(random.choice(lst_url))
print(res.status_code)
