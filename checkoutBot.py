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
    def __init__(self, path, color = 'Taupe', width = 'Wide', size = '40'):
        self.options = Options()
        self.options.add_experimental_option("excludeSwitches", ["disable-popup-blocking"])
        self.options.add_argument("--disable-popup-blocking")
        self.options.add_argument('--profile-directory=Default') 
        self.options.add_argument("--disable-notifications")


        self.service = Service(executable_path=path)
        self.driver = webdriver.Chrome(service = self.service, options = self.options)
        # self.driver.switch_to.alert.dismiss()
        self.driver.maximize_window()
        self.color = color
        self.width = width
        self.size = size

    def search_product_and_add_to_cart(self): # here i have specific item
        self.driver.get("https://www.birkenstock.com/ca/boston-suede-leather/boston-suede-suedeleather-softfootbed-eva-u_46.html?dwvar_boston-suede-suedeleather-softfootbed-eva-u__46_width=N")
        time.sleep(8)
        
        # remove ads first 
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//iframe[@id="attentive_creative"]')))
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='page1']//button[@id='closeIconContainer']")))

        self.close_ads = self.driver.find_element(By.XPATH, "//div[@id='page1']//button[@id='closeIconContainer']")
        self.close_ads.click()
        
        # then choose color of shoes 
        # actually i want to buy this one - but i'll test the second one

        colors = {'Taupe': '560771', "Mocha": '660461', "Mink": '1009543', "Black": '660473'}

        for color in colors:
            if color == self.color:
                self.color_id = colors[color] 
        print(self.color_id)

        try:
            WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH, f"//img[@class='variant-image' and contains(@src, {self.color_id})]")))
            self.choose_color = self.driver.find_element(By.XPATH, f"//img[@class='variant-image' and contains(@src, {self.color_id})]")
            self.choose_color.click()
        except:
            print("not clickable")

        # now check width of shoes

        widths = {'Wide': 'Regular/Wide', "Narrow": 'Medium/Narrow'}
        for width in widths:
            if width == self.width:
                self.width_code = widths[width]
        print(self.width_code)

        try:
            WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH, f"//*[@class='swatchanchor width-type width' and contains(@data-value, {self.width_code})]")))
            self.choose_width = self.driver.find_element(By.XPATH, f"//*[@class='swatchanchor width-type width' and contains(@data-value, {self.width_code}) and contains(@aria-label, 'Width {self.width_code}')]")
            self.choose_width.click()
        except:
            print("not clickable, there's an error when choose width of shoes!")


        # now choose size - if not available, send notificaion - here i wanna size 40. not available
        # if available, use xpath: //*[@class="swatchanchor " and contains(@data-size, "41")] 
        size = self.size 
        
        try:
            WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH, f'//*[@class="swatchanchor " and contains(@data-size, {size})]')))
            self.choose_width = self.driver.find_element(By.XPATH, f'//*[@class="swatchanchor " and contains(@data-size, {size})]')
            self.choose_width.click()
        except:
            print("Item may not be available at this time!")

        # now we can add to cart
        # //button[@id="add-to-cart"]

        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH, f'//button[@id="add-to-cart"]')))
        self.add_to_cart = self.driver.find_element(By.XPATH, f'//button[@id="add-to-cart"]')
        self.add_to_cart.click()

    def view_cart_and_checkout(self):
        # //button[@id="add-to-cart"]
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH, f'//button[@id="add-to-cart"]')))
        self.add_to_cart = self.driver.find_element(By.XPATH, f'//button[@id="add-to-cart"]')
        self.add_to_cart.click()
        






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

        


        
####### when color is Mink, there's an error need to be fixed 
client = CheckoutBot(path = "/Users/miaoz/Desktop/github_projects/bot/chromedriver_mac64/chromedriver", color = 'Black', width= 'Wide', size = '40')
client.search_product_and_add_to_cart()
if client.search_product_and_add_to_cart():
    client.view_cart_and_checkout()
else:
    print("item not available at this moment.")



# https://www.birkenstock.com/ca/boston-suede-leather/boston-suede-suedeleather-softfootbed-eva-u_46.html?dwvar_boston-suede-suedeleather-softfootbed-eva-u__46_width=N


# notes: when color is Mink, there's an error. Other colors working