from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from alert import Alert


class BotBupa:

    def __init__(self, url, date):
        self.url = url
        self.date = date
        self.email = "adityagorman@gmail.com"

    def check_slot_by_time(self):
        options = Options()
        #options.add_argument("--headless")
        #options.headless = False
        options.add_experimental_option("detach", True)

        # browser init and call product url
        service = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service, options=options)
        browser.maximize_window()
        browser.get(self.url)

        ind_element = browser.find_element(By.ID, "ContentPlaceHolder1_btnInd")
        ind_element.click()

        input_element = browser.find_element(By.ID, "ContentPlaceHolder1_SelectLocation1_txtSuburb")
        input_element.send_keys("POST CODE/LOCATION")

        search_element = browser.find_element(By.CLASS_NAME, "postcode-search")
        search_element.click()

        slots_availability = WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'tdloc_availability')))
        slots_loc = WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'tdlocNameTitle')))

        for avail, loc  in zip(slots_availability, slots_loc):
            if avail.text != "No available slot":
                slot_time = avail.text
                if "10/07" in slot_time or "11/07" in slot_time: # dates to check
                    print("### Perfect slot found! ###")
                    print("Perfect slot available in" + loc.text + " at " + slot_time)
                    Alert.email_alert(loc.text + " is available !!!", loc.text + "Available" + "At" + slot_time + "Book now" + self.url ,self.email)
            
        browser.quit()
            
            


    

        