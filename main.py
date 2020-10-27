from selenium import webdriver
from time import sleep
from secrets import username, password
from selenium.webdriver.common.keys import Keys
from datetime import date
from datetime import timedelta

class gymBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://www.sport.ed.ac.uk/online-booking')

        sleep(2)

        log_b = self.driver.find_element_by_xpath('//*[@id="logindisplay"]/div/div/a[1]')
        log_b.click()

        sleep(2)

        username_in = self.driver.find_element_by_xpath('//*[@id="UserName"]')
        username_in.send_keys(username)

        password_in = self.driver.find_element_by_xpath('//*[@id="Password"]')
        password_in.send_keys(password)

        login_button = self.driver.find_element_by_xpath('//*[@id="LogOn"]/div/form/div/fieldset/p[4]/input')
        login_button.click()

        sleep(2)

    def search(self):
        self.driver.find_element_by_xpath('//*[@id="SiteID"]/option[3]').click()

        sleep(2)

        self.driver.find_element_by_xpath('//*[@id="Activity"]/option[3]').click()

        sleep(2)

        day = self.driver.find_element_by_xpath('//*[@id="SearchDate"]').click()

        sleep(1)

        day.clear()

        today = date.today() + timedelta(days=3)

        day.send_keys(today.strftime("%m/%d/%Y"))
        day.send_keys(Keys.ENTER)
        day.click()
        day.send_keys(Keys.ENTER)

        sleep(2)        

        self.driver.find_element_by_xpath('//*[@id="English_TimeFrom"]/option[2]').click()

        sleep(2)

        self.driver.find_element_by_xpath('//*[@id="SearchButtonDiv"]/input').click()

        sleep(2)

    def checkout(self):

        self.driver.find_element_by_xpath('//*[@id="basketControl_1_2"]').click()

        sleep(2)

        self.driver.find_element_by_xpath('//*[@id="TermsAccepted"]').click()

        sleep(2)

        self.driver.find_element_by_xpath('//*[@id="CheckoutSubmit"]').click()

        sleep(2)

        self.driver.find_element_by_xpath('//*[@id="CentralRegion"]/div[2]/div[2]/div/div/p/a').click()


if __name__ == "__main__":
    bot = gymBot()
    bot.login()
    sleep(2)
    bot.search()
    #bot.checkout()











