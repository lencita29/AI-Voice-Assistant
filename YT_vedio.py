from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MusicPlayer:
    def __init__(self):
        # Install ChromeDriver and get its path
        driver_path = ChromeDriverManager().install()

        # Set up the ChromeDriver service
        service = Service(driver_path)

        # Initialize Chrome WebDriver using the service
        self.driver = webdriver.Chrome(service=service)

    def play(self, query):
        self.query = query
        self.driver.get("https://www.youtube.com/results?search_query=" + query)

        try:
            # Wait for the video preview to be present
            video_preview = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'ytd-video-renderer#dismissable'))
            )

            # Click on the first video in the search results
             # Click on the first video in the search results
            first_video = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'ytd-video-renderer#dismissable'))
            )
            first_video.click()

            # Optional: Wait for the video player to load and play automatically
            video_player = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'video.html5-main-video'))
            )

            

            # Wait indefinitely until user input
            input("Press Enter to close the browser...")

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.driver.quit()  # Quit the WebDriver session when done

# Make instance of this class
#music_player = MusicPlayer()
#music_player.play('dynamite by bts')  # Enter a query
