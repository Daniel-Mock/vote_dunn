import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def get_ips():
    ip_list = []
    f = open("proxy_list.txt", "r")
    for line in f:
        ip_list.append(line[:-1])
    return ip_list

if __name__ == '__main__':
    ip_list = get_ips()
    id = 'answer819418781'
    for ip in ip_list:
        c = webdriver.ChromeOptions()
        c.add_argument("--incognito")
        c.add_argument(f'--proxy-server={ip}')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=c)
        driver.delete_all_cookies()
        url = "https://www.lougrozaaward.com/22finalists#:~:text=Lou%20Groza%20Award%20Announces%20Final%20Three&text=Christopher%20Dunn%20of%20NC%20State,for%2D25%20on%20field%20goals"
        driver.get(url)
        button = driver.find_element("id",id).click()
        driver.find_element(By.XPATH, '//*[@id="ContentContainer"]/form/div/div[5]/input[1]').click()
        driver.quit()
        time.sleep(1)
