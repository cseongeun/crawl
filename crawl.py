import requests
from bs4 import BeautifulSoup

# 웹 페이지에 GET 요청을 보냅니다.
url = "http://quotes.toscrape.com"
response = requests.get(url)

# 요청이 성공했는지 확인합니다.
if response.status_code == 200:
    # HTML 문서를 BeautifulSoup으로 파싱합니다.
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 명언 요소들을 찾습니다.
    quotes = soup.find_all("div", class_="quote")
    
    # 명언을 출력합니다.
    for quote in quotes:
        text = quote.find(class_="text").get_text()
        author = quote.find(class_="author").get_text()
        print(f"{text} - {author}")