from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time


# for this project, i'm going to check the availability and buy the shoes on birkenstock website

product_url = 'https://www.birkenstock.com/ca/boston-suede-leather/boston-suede-suedeleather-softfootbed-eva-u_46.html?dwvar_boston-suede-suedeleather-softfootbed-eva-u__46_width=N'



class CheckoutBot:
    def __init__(self, path):
        self.options = Options()
        self.options.add_experimental_option("excludeSwitches", ["disable-popup-blocking"])
        self.options.add_argument("--disable-popup-blocking")
        self.options.add_argument('--profile-directory=Default') 
        self.options.add_argument("--disable-notifications")


        self.service = Service(executable_path=path)
        self.driver = webdriver.Chrome(service = self.service, options = self.options)
        # self.driver.switch_to.alert.dismiss()
        self.driver.maximize_window()

    def login(self):
        from selenium.webdriver.common.action_chains import ActionChains
        # //*[@id="wrapper"]/div[1]/header[1]/div[1]/div[3]/ul/li[2]/a/i
        self.driver.get("https://www.birkenstock.com/ca/login")
        wait = WebDriverWait(self.driver, 10)

        try:
            time.sleep(15)
            wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/main/div/div/div/button')))
            element = self.driver.find_element(By.CSS_SELECTOR, '/html/body/div[2]/div/main/div/div/div/button').click()
            ActionChains(self.driver).move_to_element(element).perform() # I assume br is your webdriver
            element.click()
        except:
            print("could not click")

        # username = self.driver.find_element(By.XPATH, '//*[@id="dwfrm_login_username_d0gprxzxjoqn"]')
        # username.send_keys("zhengmiao0810@gmail.com")

        






    def search_product(self): # here i have specific item
        self.driver.get("https://www.birkenstock.com/ca/boston-suede-leather/boston-suede-suedeleather-softfootbed-eva-u_46.html?dwvar_boston-suede-suedeleather-softfootbed-eva-u__46_width=N")
        time.sleep(30)
        
        # self.driver.switch_to.alert.dismiss()

        self.close_ads = self.driver.find_element(By.XPATH, '//*[@id="closeIconSvg"]').click()

        # self.search = self.driver.find_element(By.XPATH, '//*[@id="product-content"]/div[3]/div[2]/ul/li[1]/div[2]/div/div/div/div[1]/div/div/a/img').click()
        self.search = self.driver.find_element(By.XPATH, '//*[@id="product-content"]/div[3]/div[2]/ul/li[1]/div[2]/div/div/div/div[2]/div/div/a/img')
        self.driver.switch_to.alert.dismiss()
        self.search.click()


client = CheckoutBot(path = "/Users/miaoz/Desktop/github_projects/bot/chromedriver_mac64/chromedriver")
client.login()



# https://www.birkenstock.com/ca/boston-suede-leather/boston-suede-suedeleather-softfootbed-eva-u_46.html?dwvar_boston-suede-suedeleather-softfootbed-eva-u__46_width=N