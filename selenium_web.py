from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class infow():
    def __init__(self):
        # Configure Chrome options to ignore certificate errors
        chrome_options = Options()
        chrome_options.add_argument('--ignore-certificate-errors')

        # Install ChromeDriver and get its path
        driver_path = ChromeDriverManager().install()

        # Set up the ChromeDriver service
        service = Service(driver_path)

        # Initialize Chrome WebDriver using the service and options
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")
        search=self.driver.find_element_by_xpath('//*[@id="searchInput]') #find element by xpath to search something and press enter
        #triggers  the search bar in the page and stores in the search variable
        search.click()
        search.send_keys(query)
        #trigger the enter button
        enter=self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        enter.click()


# Make instance of this class
assist = infow()
assist.get_info("neutron stars")  # Enter a query
