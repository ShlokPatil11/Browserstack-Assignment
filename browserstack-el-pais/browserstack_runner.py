from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY, BROWSERS
import json
import time

def run_session(browser):
    bstack_options = browser.get("bstack:options", {})
    bstack_options["userName"] = BROWSERSTACK_USERNAME
    bstack_options["accessKey"] = BROWSERSTACK_ACCESS_KEY
    
    options = webdriver.ChromeOptions()
    options.set_capability('bstack:options', bstack_options)
    options.set_capability('browserName', browser['browserName'])
    options.set_capability('browserVersion', browser['browserVersion'])
    
    # Initialize the remote Web Driver using BrowserStack remote URL
    # and desired capabilities defined above
    driver = webdriver.Remote(
        command_executor="https://hub-cloud.browserstack.com/wd/hub",
        options=options
    )

    try:
        # Example test: Navigate to El País and check title
        driver.get("https://elpais.com/")
        print(f"[{browser['browserName']}] Page title: {driver.title}")
        
        # Check if title contains 'EL PAÍS'
        if "EL PAÍS" in driver.title:
            driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title matched"}}')
        else:
            driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title mismatch"}}')
            
    except Exception as e:
        print(f"[{browser['browserName']}] Test failed: {e}")
        driver.execute_script(f'browserstack_executor: {{"action": "setSessionStatus", "arguments": {{"status":"failed", "reason": "{str(e)}"}} }}')
    finally:
        driver.quit()

def run_parallel_tests():
    print("Starting BrowserStack parallel execution...")
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(run_session, BROWSERS)

if __name__ == "__main__":
    if "your_username" in BROWSERSTACK_USERNAME or "your_access_key" in BROWSERSTACK_ACCESS_KEY:
        print("Error: Please set your BrowserStack credentials in config.py or environment variables.")
        sys.exit(1)
    run_parallel_tests()
