
from selenium import webdriver
import sys, time

browser = webdriver.Firefox(executable_path='')
browser.get('')


try:
    if sys.argv[1]:
        login_id  = str(sys.argv[1])
except:
    pass

try:
    if sys.argv[2]:
        password = str(sys.argv[2])
except:
    pass

try:
    if sys.argv[3]:
        inputText = str(sys.argv[3]) 
except:
    pass


account = browser.find_element_by_name("userID")
account.send_keys(login_id)

password = browser.find_element_by_name("pwd")
password.send_keys(password)

time.sleep(0.5)

# ログイン
button = browser.find_element_by_xpath("//input[@type='submit']")
button.click()

time.sleep(1)

nippo = browser.find_element_by_xpath("//a[@href='schedule/daily_report.asp']")
nippo.click()

time.sleep(0.5)

today = browser.find_element_by_xpath("//a[@href='javascript:report(2018,4,26)']")
today.click()

time.sleep(1)

allHandles = browser.window_handles

print(allHandles[0])
print(allHandles[1])

browser.switch_to_window(allHandles[1])

# 別モーダルで開く要素の取得
textArea= browser.find_element_by_name("report")
textArea.clear()
textArea.send_keys(inputText)
button = browser.find_element_by_xpath("//input[@type='submit']")
button.click()

time.sleep(0.5)

closeButton = browser.find_element_by_xpath("//input[@type='button']")
closeButton.click()

time.sleep(0.5)

browser.switch_to_window(allHandles[0])

time.sleep(0.5)

browser.close()
