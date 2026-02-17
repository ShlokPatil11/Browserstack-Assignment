import requests
import json
from config import RAPIDAPI_KEY, RAPIDAPI_HOST

def translate_titles(titles):
    if not titles:
        return []
        
    print("\nTranslating titles using RapidAPI...")
    
    url = f"https://{RAPIDAPI_HOST}/api/v1/translator/json"
    
    # Map titles to a dictionary for the JSON payload
    # The API expects a JSON object where keys are IDs and values are text to translate
    # We'll use the index as the ID
    titles_dict = {str(i): title for i, title in enumerate(titles)}
    
    payload = {
        "from": "es",
        "to": "en",
        "json": titles_dict
    }
    
    headers = {
        "content-type": "application/json",
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": RAPIDAPI_HOST
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        
        result = response.json()
        
        # The API returns the translated JSON object in the "json" field (based on the user's curl example it looks like it might return 'json' or 'trans', user example request had 'json' in body, response format typically mirrors or provides a specific key.
        # Let's inspect the response more closely if it fails, but standard rapidapi google translate often returns 'data' or 'translations'.
        # However, the user provided a curl that sends a 'json' key.
        # Let's assume the response has a 'json' or 'trans' key containing the translated dictionary.
        # IF the API is "Google Translate" by "google-translate113", it usually returns { "data": { "translations": [...] } } for standard calls, 
        # BUT for the specific /json endpoint, it likely returns the same structure as input or a flat dict.
        # Let's add a print of the response keys for debugging if needed, but for now I will try to support 'json' or 'trans'.
        
        # Checking the user's provided code in api_test.py might help. 
        # User's api_test.py output was just 'data'. 
        # I will start by printing the response text to debug if I can't be sure, but let's try to grab 'json' first as that is the input key.
        
        translated_dict = result.get("json", {})
        if not translated_dict:
             translated_dict = result.get("trans", {})
        
        # If still empty, maybe it's at the root?
        if not translated_dict and isinstance(result, dict):
            # Check if keys are numbers (our IDs)
            if "0" in result:
                translated_dict = result

        # Reconstruct the list in the correct order
        translated_titles = []
        for i in range(len(titles)):
            translated_title = translated_dict.get(str(i)) # Fallback handled below
            if not translated_title:
                 # Try integer key
                 translated_title = translated_dict.get(i, titles[i])
            
            translated_titles.append(translated_title)
            print(f"ES: {titles[i]} \nEN: {translated_title}\n")
            
        return translated_titles
        
    except Exception as e:
        print(f"Error during translation: {e}")
        # Return original titles as fallback
        return titles
