import sys
from scraper import Scraper
from translator import translate_titles
from text_analysis import analyze_headers

def main():
    print("Starting El País Scraper & Analyzer...")
    
    # 1. Scrape
    scraper = Scraper()
    articles = scraper.scrape_articles()
    
    print(f"\nScraped {len(articles)} articles.")
    
    if not articles:
        print("No articles found.")
        return

    titles = [article['title'] for article in articles]
    
    # 2. Translate
    translated_titles = translate_titles(titles)
    
    # Output results
    print("\n--- Summary ---")
    results = {
        "articles": [],
        "repeated_words": analyze_headers(translated_titles)
    }

    for i, article in enumerate(articles):
        print(f"\nArticle {i+1}:")
        print(f"Original Title: {article['title']}")
        print(f"Translated Title: {translated_titles[i]}")
        # print(f"Content Snippet: {article['content'][:100]}...")
        if article.get('image_url'):
            print(f"Image: {article['image_url']}")
        
        results["articles"].append({
            "original_title": article['title'],
            "translated_title": translated_titles[i],
            "content_snippet": article['content'][:200], # Save snippet
            "image_filename": f"article_{i+1}.jpg" if article.get('image_url') else None
        })

    # Save to JSON
    import json
    with open("results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)
    print("\nResults saved to 'results.json'")

if __name__ == "__main__":
    main()
