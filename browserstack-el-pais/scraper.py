import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Scraper:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run properly without UI if needed, but for scraping often useful
        # chrome_options.add_argument("--disable-gpu")
        # self.driver = webdriver.Chrome(options=chrome_options)
        # Using default local driver for now, ensure chromedriver is in PATH or managed by selenium manager (selenium 4+)
        self.driver = webdriver.Chrome(options=chrome_options)

    def scrape_articles(self):
        print("Navigating to El País Opinion section...")
        self.driver.get("https://elpais.com/opinion/")
        
        try:
            # Wait for articles to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "article"))
            )
            
            articles_data = []
            # Find first 5 articles
            articles = self.driver.find_elements(By.TAG_NAME, "article")[:5]
            
            for index, article in enumerate(articles):
                try:
                    title_element = article.find_element(By.TAG_NAME, "h2")
                    title = title_element.text
                    link = title_element.find_element(By.TAG_NAME, "a").get_attribute("href")
                    
                    # Get content by visiting the link (or extraction from summary if sufficient, but instructions say 'Visit each article')
                    # Visiting each might be slow in one session, but let's try to extract from main page if possible, 
                    # OR we collect links first and then visit them. 
                    # The instructions say: "Collect article links -> Visit each article -> Extract Title, Content, Image".
                    
                    articles_data.append({
                        "title": title,
                        "link": link
                    })
                except Exception as e:
                    print(f"Error extraction article summary: {e}")
                    
            final_data = []
            for item in articles_data:
                print(f"Scraping article: {item['title']}")
                self.driver.get(item['link'])
                
                # Extract Content
                content = ""
                try:
                    # Generic strategy: look for article body p tags
                    # El Pais specific structure might vary, but p tags inside article body is standard
                    # Checking structure... usually <div class="a_b"> or similar
                    paragraphs = self.driver.find_elements(By.CSS_SELECTOR, "article p")
                    content = " ".join([p.text for p in paragraphs])
                except Exception as e:
                    print(f"Error extracting content: {e}")

                # Extract Image
                image_url = None
                try:
                    # Look for cover image
                    img_element = self.driver.find_element(By.CSS_SELECTOR, "article img")
                    image_url = img_element.get_attribute("src")
                    # Save image
                    if image_url:
                        self.download_image(image_url, f"article_{len(final_data)+1}.jpg")
                except Exception:
                    # No image found
                    pass
                
                final_data.append({
                    "title": item['title'],
                    "content": content,
                    "image_url": image_url
                })
                
            return final_data

        finally:
            self.driver.quit()

    def download_image(self, url, filename):
        if not os.path.exists("images"):
            os.makedirs("images")
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(f"images/{filename}", "wb") as f:
                    f.write(response.content)
            else:
                 print(f"Failed to download image: {url}")
        except Exception as e:
            print(f"Error downloading image: {e}")

if __name__ == "__main__":
    scraper = Scraper()
    data = scraper.scrape_articles()
    for d in data:
        print(d)
