from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from alert import Alert
import time
import logging

logging.basicConfig(filename='botbupa.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.info('Script start')

class BotBupa:

    def __init__(self, url):
        self.url = url
        self.email = "your-email-add@gmail.com"

    def check_slot_by_time(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument('--disable-dev-shm-usage')
        browser = webdriver.Chrome(options=chrome_options)

        browser.get(self.url)

        ind_element = browser.find_element(By.ID, "ContentPlaceHolder1_btnInd")
        ind_element.click()

        input_element = browser.find_element(By.ID, "ContentPlaceHolder1_SelectLocation1_txtSuburb")
        input_element.send_keys("3000") # the australian post code where you want the booking from

        search_element = browser.find_element(By.CLASS_NAME, "postcode-search")
        search_element.click()

        time.sleep(10)

        slots_availability = WebDriverWait(browser, 30).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'tdloc_availability')))
        slots_loc = WebDriverWait(browser,30).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'tdlocNameTitle')))

        for avail, loc  in zip(slots_availability, slots_loc):
            if avail.text != "No available slot":
                slot_time = avail.text

                # The date slots you want the booking for
                if "07/07" in slot_time or "08/07" in slot_time or "09/07" in slot_time or "10/07" in slot_time:
                    print("### Perfect slot found! ###")
                    print("Perfect slot available in " + loc.text + " at " + slot_time)

                    Alert.email_alert(loc.text + " is available !!! ", loc.text + " Available " + " At " + slot_time + " Book now " + self.url ,self.email)

        logging.info("closing")
        browser.quit()