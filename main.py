from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

options = Options()
options.page_load_strategy = 'eager'
login_url = 'https://shopee.co.id/buyer/login?from=https%3A%2F%2Fshopee.co.id%2F&next=https%3A%2F%2Fshopee.co.id%2F'

def purchase(phone, password, item_url):
    driver = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver', options = options)
    wait = WebDriverWait(driver, 10)

    driver.get(login_url)

    wait.until(presence_of_element_located((By.NAME, 'loginKey')))

    # otomatis mengisi nomor handphone
    driver.find_element_by_name('loginKey').send_keys(phone)
    #otomatis mengisi password
    driver.find_element_by_name('password').send_keys(password + Keys.RETURN)

    otp = str (send_OTP())
    driver.find_element_by_css_selector('input[autocomplete="one-time-code"]').send_keys(otp + Keys.RETURN)
    wait.until(presence_of_element_located((By.CLASS_NAME, 'navbar__username')))

    driver.get(item_url)
    variant_XPATH = "//button[contains(., 'Red')]" # ganti Red dengan nama variant di barang
    buy_XPATH = "//button[contains(., 'beli sekarang')]"
    
    wait.until(presence_of_element_located((By.XPATH, variant_XPATH)))
    driver.find_element_by_xpath(variant_XPATH).click()

    wait.until(presence_of_element_located((By.CLASS_NAME, 'product-variation--selected')))
    driver.find_element_by_xpath(buy_XPATH).click()

def send_OTP():
    text = str(input ("Enter OTP: "))
    return text

phone = '' # isi dengan nomor handphone
password = '' # isi dengan password
# url untuk barang yang ingin dibeli
item_url = 'https://shopee.co.id/Miniso-Earphone-in-Ear-Earbuds-Silikon-Headphone-Kabel-Noise-Cancelling-Awet-Headset-Universal-i.40847197.2238861996'

purchase(phone, password, item_url)
