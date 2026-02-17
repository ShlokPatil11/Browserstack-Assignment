from collections import Counter
import re

def analyze_headers(titles):
    print("\nAnalyzing repeated words in headers...")
    
    combined = " ".join(titles).lower()
    # Extract words, ignoring punctuation
    words = re.findall(r'\b\w+\b', combined)
    
    counter = Counter(words)
    
    repeated_words = {word: count for word, count in counter.items() if count > 2}
    
    print("Repeated words (> 2 times):")
    for word, count in repeated_words.items():
        print(f"{word}: {count}")
        
    return repeated_words
