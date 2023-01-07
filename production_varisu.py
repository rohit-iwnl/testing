import requests
from datetime import datetime
import time
import pytz
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()
import chromedriver_autoinstaller

def available():
    india = pytz.timezone("Asia/Calcutta") 
    timeInIndia = datetime.now(india)
    current_time = timeInIndia.strftime("%H:%M:%S")
    message="VARISU TICKETS OUT!! at"+current_time
    base_url='https://api.telegram.org/bot5897785242:AAHTwgdMRFOKG0GgNJg0WIawHuF_Xj4fk-c/sendMessage?chat_id=-800086196&text='+message
    requests.get(base_url)

chromedriver_autoinstaller.install()

globalcheck= 0
while(globalcheck!=1):

    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    option.add_argument("--headless")
    option.add_argument("--no-sandbox")
    option.add_argument("disable-dev-ssh-usage")
    option.add_argument("--ignore-certificate-errors")

    theatresList=[]

    path = "https://www.ticketnew.com/Varisu-Movie-Tickets-Online-Show-Timings/Online-Advance-Booking/25739/C/Tirunelveli"
    browser = webdriver.Chrome(executable_path="C:\\Users\Administrator\\Downloads\\chromedriver_win32\\chromeriver.exe",chrome_options=option)
    browser.get(path)
    count= (len(browser.find_elements(By.CLASS_NAME,"tn-entity-details"))) 


    for i in range(1,count):
        css_selector = "div.tn-entity:nth-child("+str(i)+") > div:nth-child(1) > h5:nth-child(1)"
        try:
            theatresList.append(browser.find_element(By.CSS_SELECTOR,css_selector).text)
        except:
            break

    if 'RAM' or 'MUTHURAM' or 'ram' or 'muthuram' in str(theatresList):
        globalcheck=1
        available()
    else:
        globalcheck=0

        
    time.sleep(20)