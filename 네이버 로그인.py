from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주소 이동
driver.get("https://www.naver.com")

# 로그인 버튼 클릭
driver.find_element(by=By.CSS_SELECTOR, value="#account > div > a").click()

# 아이디 값  입력
driver.find_element(by=By.CSS_SELECTOR, value="#id").send_keys("test")
time.sleep(1)

driver.find_element(by=By.CSS_SELECTOR, value="#pw").send_keys("test")
time.sleep(1)

# 로그인 버튼 클릭
driver.find_element(by=By.CSS_SELECTOR, value="#log\.login").click()
