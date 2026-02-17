import os
from dotenv import load_dotenv

load_dotenv()

# BrowserStack Credentials
BROWSERSTACK_USERNAME = os.getenv("BROWSERSTACK_USERNAME") or "your_username"
BROWSERSTACK_ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY") or "your_access_key"

# RapidAPI Credentials
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST")

# Browser Capabilities
BROWSERS = [
    {
        "browserName": "Chrome",
        "browserVersion": "latest",
        "bstack:options": {
            "os": "Windows",
            "osVersion": "11"
        }
    },
    {
        "browserName": "Firefox",
        "browserVersion": "latest",
        "bstack:options": {
            "os": "Windows",
            "osVersion": "11"
        }
    },
    {
        "browserName": "Edge",
        "browserVersion": "latest",
        "bstack:options": {
            "os": "Windows",
            "osVersion": "11"
        }
    },
    {
        "browserName": "Safari",
        "browserVersion": "latest",
        "bstack:options": {
            "os": "OS X",
            "osVersion": "Monterey"
        }
    },
    {
        "browserName": "iPhone",
        "browserVersion": "15",
        "bstack:options": {
            "deviceName": "iPhone 13",
            "realMobile": "true"
        }
    }
]
