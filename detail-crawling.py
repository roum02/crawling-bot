from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


TARGET_URL = "https://www.albamon.com/alba-talk/experience"

# ChromeDriver 경로 설정 필요
driver = webdriver.Chrome()  

driver.get(TARGET_URL)

# 페이지 로드 대기
driver.implicitly_wait(10)



# 모든 버튼 요소 찾기
buttons = driver.find_elements(By.CLASS_NAME, "Button_button__S9rjD")

print(len(buttons))


# 브라우저 종료
driver.quit()
