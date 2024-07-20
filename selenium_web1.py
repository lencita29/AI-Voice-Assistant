from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class infow():
    def __init__(self):
        # Install ChromeDriver and get its path
        driver_path = ChromeDriverManager().install()

        # Set up the ChromeDriver service
        service = Service(driver_path)

        # Initialize Chrome WebDriver using the service
        self.driver = webdriver.Chrome(service=service)

    def get_info(self, query):
        self.query = query
        self.driver.get("https://www.wikipedia.org")

        try:
            # Wait for the search input field to be clickable
            search = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="searchInput"]'))
            )
            
            # Enter the search query
            search.send_keys(self.query)
            
            # Submit the search
            enter = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="search-form"]/fieldset/button'))
            )
            enter.click()

            # Wait indefinitely until user input
            input("Press Enter to close the browser...")
            
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.driver.quit()  # Quit the WebDriver session when done

# Make instance of this class
#assist = infow()
#assist.get_info("neutron stars")  # Enter a query
#make the assistant to speak only first few lines of the searched content by exporting selenium_web1.py

