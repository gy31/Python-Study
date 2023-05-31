import requests
from bs4 import BeautifulSoup

response = requests.get("https://naver.com")
html = response.text

soup = BeautifulSoup(html, 'html.parser')
word = soup.select_one("#ke_kbd_btn")

print(word.text)