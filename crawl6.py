from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import io, base64
import requests
from PIL import Image

# 아래로 스크롤하기
def scroll_down():
    driver.execute_script("window.scrollTo(0, 5000)")
    time.sleep(2)

# base64 데이터 -> JPG
def base64ToJpg(base64_str, filename):
    image_data = base64_str.split(',')[1]
    image = Image.open(io.BytesIO(base64.b64decode(image_data)))
    # 이미지저장
    image.save(filename, "JPEG") 

# url 데이터 -> JPG
def urlToJpg(url, filename):
    response = requests.get(url)
    image = Image.open(io.BytesIO(response.content()))
    # 이미지저장
    image.save(filename, 'JPEG')


## 시작
url = 'https://www.google.co.kr/imghp'

driver = webdriver.Chrome()
driver.get(url)
time.sleep(1)

query = "고양이"

# 검색창 요소
search_input = driver.find_element(By.ID, 'APjFqb')
# 검색창에 검색어 입력
search_input.send_keys(query)
# 검색창에서 엔터 
search_input.send_keys(Keys.ENTER)
time.sleep(2)

# 마지막 이미지 처리 인덱스
last_index = 0 
image_index = 0
while True:
    # 이미지 모두 가져오기
    all_images = driver.find_elements(By.CLASS_NAME, "rg_i")
    images = all_images[last_index:]
    last_index = len(all_images)

    # 각 이미지 src 속성 출력
    for image in images:
        src_path = image.get_attribute('src')

        if src_path is None:
            continue
       
        if src_path.startswith('https'):
            print("URL 이미지가 저장됨!")
            urlToJpg(src_path, f"images/{query}-{image_index}.jpg")
        elif src_path.startswith("data:image/jpeg;base64"):
            print("Base64 이미지가 저장됨!")
            base64ToJpg(src_path, f"images/{query}-{image_index}.jpg")

        image_index += 1


    # 아래로 스크롤
    scroll_down()
