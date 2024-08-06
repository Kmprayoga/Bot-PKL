from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

username = "Email"
password = "Pass"


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
def facebook_login():


    driver.get("https://www.facebook.com/login/")

    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )

    username_field.send_keys(username)

    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "pass"))
    )

    # Enter password
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)


    try:
        challenge_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "checkpointNextButton"))
        )
        print("Additional login challenge encountered. Please handle manually.")
    except:
        pass

    print("Login attempted. Please check the browser window for success.")

facebook_login()


if __name__ == "__main__":
    facebook_login()
