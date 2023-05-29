from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
import sys
import os

# for this project, i'm going to check the availability and buy the shoes on birkenstock website
# all steps work now. If you have an account, probably you'll have your shipping address already, then i just stop at the payment method step.

product_url = 'https://www.birkenstock.com/ca/boston-suede-leather/boston-suede-suedeleather-softfootbed-eva-u_46.html?dwvar_boston-suede-suedeleather-softfootbed-eva-u__46_width=N'



class CheckoutBot:
    def __init__(self, path, color = 'Taupe', width = 'Wide', size = '40'):
        self.options = Options()
        self.options.add_experimental_option("useAutomationExtension", False)
        self.options.add_experimental_option("excludeSwitches",["enable-automation"])
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

    def search_product(self, try_again = True): # here i have specific item

        self.driver.get("https://www.birkenstock.com/ca/boston-suede-leather/boston-suede-suedeleather-softfootbed-eva-u_46.html?dwvar_boston-suede-suedeleather-softfootbed-eva-u__46_width=N")
        time.sleep(8)
        
        # remove ads first 
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//iframe[@id="attentive_creative"]')))
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='page1']//button[@id='closeIconContainer']")))

        self.close_ads = self.driver.find_element(By.XPATH, "//div[@id='page1']//button[@id='closeIconContainer']")
        self.close_ads.click()
        
        # then choose color of shoes 
        # actually i want to buy Taupe - but i'll test the second one

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

        time.sleep(5)
        widths = {'Wide': 'Regular/Wide', "Narrow": 'Medium/Narrow'}
        for width in widths:
            if width == self.width:
                self.width_code = widths[width]
        print(self.width_code)

        time.sleep(3)
        try:
            WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH, f"//*[@class='swatchanchor width-type width' and contains(@data-value, {self.width_code})]")))
            self.choose_width = self.driver.find_element(By.XPATH, f"//*[@class='swatchanchor width-type width' and contains(@data-value, {self.width_code}) and contains(@aria-label, 'Width {self.width_code}')]")
            self.choose_width.click()
        except:
            print("not clickable, there's an error when choose width of shoes!")


        # now choose size - if not available, send notificaion - here i wanna size 40. not available
        # if available, use xpath: //*[@class="swatchanchor " and contains(@data-size, "41")] 
        size = self.size 
        
        time.sleep(4)

        try:
            WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH, f'//*[@class="swatchanchor " and contains(@data-size, {size})]')))
            self.choose_width = self.driver.find_element(By.XPATH, f'//*[@class="swatchanchor " and contains(@data-size, {size})]')
            self.choose_width.click()
        except:
            if try_again:
                try:
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@class="swatchanchor " and contains(@data-size, {size})]')))
                    self.choose_width = self.driver.find_element(By.XPATH, f'//*[@class="swatchanchor " and contains(@data-size, {size})]')
                    self.choose_width.click()
                except:
                    print("Item may not be available at this time!")
                    sys.exit(1)


    def add_to_cart_and_checkout(self):
        # //button[@id="add-to-cart"]
        time.sleep(3)

        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH, f'//button[@id="add-to-cart"]')))
        self.add_to_cart = self.driver.find_element(By.XPATH, f'//button[@id="add-to-cart"]')
        self.driver.execute_script("arguments[0].click();", self.add_to_cart)
        # self.add_to_cart.click()
        print("add to cart click")

        time.sleep(3)
        # then go to cart 
        # //*[@class='button cart-link']
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, f"//div[@class='overlay-actions']//a[@class='button cart-link']")))
        self.add_to_cart2= self.driver.find_element(By.XPATH, f"//div[@class='overlay-actions']//a[@class='button cart-link']")
        self.driver.execute_script("arguments[0].click();", self.add_to_cart2)
        # self.add_to_cart2.click()
        print("add to cart successfully!")

        time.sleep(3)

        #### add your info for checkout
        ### coz the price is high, i dont want to do the auto purchasing at this momemnt 
        ### more codes coming! And i'll add my shipping info to place an order later! :D


    def login(self):
        # after adding to cart, click checkout with account
        # //input[@id='cart-guestcheckout-false']

        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH, f"//label[@class='label' and @for='cart-guestcheckout-false']")))
        self.login = self.driver.find_element(By.XPATH, f"//label[@class='label' and @for='cart-guestcheckout-false']")
        self.driver.execute_script("arguments[0].click();", self.login)
        print("login with acct")

        # enter email
        self.driver.implicitly_wait(5)
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH, f"*//form[contains(@class, 'guestcheckout')]//fieldset//div[contains(@class, 'username')]//input[contains(@class, 'email')]")))
        print("maybe work")
        self.enter_email = self.driver.find_element(By.XPATH, f"*//form[contains(@class, 'guestcheckout')]//fieldset//div[contains(@class, 'username')]//input[contains(@class, 'email')]")
        print("find it!")
        self.driver.execute_script("arguments[0].click();", self.enter_email)
        self.enter_email.click()
        self.enter_email.send_keys(f"{email}")

        # enter password
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH, f"*//form[contains(@class, 'guestcheckout')]//fieldset//div[contains(@class, 'password')]//input[contains(@class, 'password')]")))
        print("maybe work")
        self.enter_email = self.driver.find_element(By.XPATH, f"*//form[contains(@class, 'guestcheckout')]//fieldset//div[contains(@class, 'password')]//input[contains(@class, 'password')]")
        print("find it!")
        self.driver.execute_script("arguments[0].click();", self.enter_email)
        self.enter_email.click()
        self.enter_email.send_keys(f"{password}")

        # proceed to checkout
        # <button class="button button-large xlt-continueCheckout" type="submit" value="Proceed to checkout" name="dwfrm_cart_checkoutCart">
        # //button[@class='button button-large xlt-continueCheckout']

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//button[@class='button button-large xlt-continueCheckout']")))
        self.checkout= self.driver.find_element(By.XPATH, f"//button[@class='button button-large xlt-continueCheckout']")
        self.driver.execute_script("arguments[0].click();", self.checkout)
        print("let's do checkout")

    def login_directly(self):
        # https://www.birkenstock.com/ca/login
        self.driver.get("https://www.birkenstock.com/ca/login")
        time.sleep(8)

         # remove ads first 
        WebDriverWait(self.driver, 60).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//iframe[@id="attentive_creative"]')))
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='page1']//button[@id='closeIconContainer']")))

        self.close_ads = self.driver.find_element(By.XPATH, "//div[@id='page1']//button[@id='closeIconContainer']")
        self.close_ads.click()

        # check login_button
        # //*[@id="dwfrm_login_username_d0cfuetszctr"]
        # //div[@class='form-row username required form-row-input']//input[@class='input-text input-email email required filled-out' and @aria-label='Your email address and @id='dwfrm_login_username_d0cfuetszctr']
        self.driver.implicitly_wait(5)
        self.driver.switch_to.default_content()  # This method is used to come out of all the frames and switch the focus at the page. Once we move out, it loses the access to the elements inside the frames in the page.
        # *//input[@class='input-text input-email email required filled-out' and @aria-label='Your email address']
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH, f"*//form[@class='clearfix']//fieldset//div[contains(@class, 'username')]//input[contains(@class, 'email')]")))
        print("maybe work")
        self.enter_email = self.driver.find_element(By.XPATH, f"*//form[@class='clearfix']//fieldset//div[contains(@class, 'username')]//input[contains(@class, 'email')]")
        print("find it!")
        self.driver.execute_script("arguments[0].click();", self.enter_email)
        self.enter_email.click()
        self.enter_email.send_keys(f"{email}")

        # enter password
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH, f"*//form[@class='clearfix']//fieldset//div[contains(@class, 'password')]//input[contains(@class, 'password')]")))
        print("maybe work")
        self.enter_email = self.driver.find_element(By.XPATH, f"*//form[@class='clearfix']//fieldset//div[contains(@class, 'password')]//input[contains(@class, 'password')]")
        print("find it!")
        self.driver.execute_script("arguments[0].click();", self.enter_email)
        self.enter_email.click()
        self.enter_email.send_keys(f"{password}")

        # proceed to checkout
        # <button class="button button-large xlt-continueCheckout" type="submit" value="Proceed to checkout" name="dwfrm_cart_checkoutCart">
        # //button[@class='button button-large xlt-continueCheckout']


        # proceed to checkout

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//button[@class='button button-large xlt-continueCheckout']")))
        self.checkout= self.driver.find_element(By.XPATH, f"//button[contains(@class, 'continueCheckout']")
        self.driver.execute_script("arguments[0].click();", self.checkout)
        self.checkout.click()
        print("let's do checkout")


       
####### when color is Mink, there's an error need to be fixed 

email = os.getenv("email")
password = os.getenv("password")
print(email)
client = CheckoutBot(path = "/Users/miaoz/Desktop/github_projects/bot/chromedriver_mac64/chromedriver", color = 'Black', width= 'Wide', size = '40')

client.search_product(try_again = True)
print("next step, add to cart:)")
client.add_to_cart_and_checkout()
time.sleep(5)
client.login()

# client.login_directly()

