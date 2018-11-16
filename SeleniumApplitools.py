from selenium import webdriver
from applitools.eyes import Eyes

class HelloWorld:

    eyes = Eyes()

    # Initialize the eyes SDK and set your private API key.
    eyes.api_key = 'd98KRpwEL5RjJM110nZP15za103rgm41hxmeUve48vCxgj84110'

    try:

        # Open a Chrome browser.
        driver = webdriver.Chrome()

        # Start the test and set the browser's viewport size to 800x600.
        eyes.open(driver=driver, app_name='Google Test', test_name='My first Selenium Python test!',
        viewport_size={'width': 800, 'height': 600})

        # Navigate the browser to the "hello world!" web-site.
        driver.get('https://www.google.lk')

        # Visual checkpoint #1.
        eyes.check_window('Google');

        # Click the 'Click me!' button.
        driver.find_element_by_id('lst-ib').send_keys('Selenium')
        driver.find_element_by_id('hplogo').click()

        # Visual checkpoint #2.
        eyes.check_window('Google')


        # End the test.
        eyes.close()

    finally:

        # Close the browser.
        driver.quit()

        # If the test was aborted before eyes.close was called, ends the test as aborted.
        eyes.abort_if_not_closed()