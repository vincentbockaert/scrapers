import requests, os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from database import Session
from models import Book, Chapter

load_dotenv()

page = requests.get(os.environ.get("PAGE_URI"))

soup = BeautifulSoup(page.text, 'html.parser')

# print(soup.prettify())

with Session() as session:
    session.add(Book(title="The Book of the New Sun"))
    session.commit()