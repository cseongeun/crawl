import requests
from bs4 import BeautifulSoup

# 웹 페이지에 GET 요청을 보냅니다.
url = "https://www.imdb.com/chart/top"
response = requests.get(url)

# 요청이 성공했는지 확인합니다.
if response.status_code == 200:
    # HTML 문서를 BeautifulSoup으로 파싱합니다.
    soup = BeautifulSoup(response.text, "html.parser")

    # 영화 순위를 포함하는 요소를 찾습니다.
    movie_list = soup.select('div/span/div/div/div[3]/table/tbody')
    # movie_list = soup.find("tbody", class_="lister-list")

    # 각 영화 순위를 출력합니다.
    movies = movie_list.find_all("tr")
    for movie in movies:
        title_column = movie.find("td", class_="titleColumn")
        title = title_column.find("a").get_text()
        rating = movie.find("strong").get_text()
        print(f"Title: {title}")
        print(f"Rating: {rating}")
        print()
