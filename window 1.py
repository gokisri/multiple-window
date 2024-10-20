from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# The rest of your code


class MovingBetweenWindows:
    def __init__(self, web_url):
        self.url = web_url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.dashboard_locator = "/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a"

    def windows(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            wait = WebDriverWait(self.driver, 10)
            parent_window_handle = self.driver.current_window_handle
            print("Window ID of HomePage : ", parent_window_handle)

            # Open two new windows
            for _ in range(2):
                self.driver.execute_script("window.open('https://www.cowin.gov.in/our-partner')")

            all_window_handles = self.driver.window_handles
            print(all_window_handles)

            # Switch to and close two new windows
            for window in all_window_handles:
                if window != parent_window_handle:
                    self.driver.switch_to.window(window)
                    print(f"Switched to window: {window}")
                    sleep(2)  # Wait for demo purposes
                    self.driver.close()

            # Switch back to the parent window (homepage)
            self.driver.switch_to.window(parent_window_handle)
            print("Back to HomePage")

        except Exception as error:
            print("ERROR:", error)
        finally:
            print("SUCCESS: Automation completed!")
            self.driver.quit()

if __name__ == "__main__":
    url = "https://www.cowin.gov.in/"
    automation = MovingBetweenWindows('https://www.cowin.gov.in/our-partner')
    automation.windows()
