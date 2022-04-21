from selenium import webdriver
import time

# Main Function
if __name__ == '__main__':


    # Provide the path of chromedriver present on your system.
    driver = webdriver.Chrome(executable_path="chromedriver")
    driver.set_window_size(1920, 1080)

    # Send a get request to the url
    driver.get('https://www.geeksforgeeks.org/')
    time.sleep(60)
    driver.quit()
    print("Done")