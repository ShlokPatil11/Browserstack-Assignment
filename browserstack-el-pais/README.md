# BrowserStack Assignment

This project is an assignment scrapes the El País Opinion section, translates article titles, performs word frequency analysis, and runs cross-browser tests using BrowserStack.

## Tech Stack
- Python
- Selenium
- BrowserStack
- Google Translate API
- Requests
- Concurrent Futures

## Setup Instructions

1. **Clone the repository** (if applicable) and navigate to the project directory:
   ```bash
   cd browserstack-el-pais
   ```

2. **Install requirements**:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Mac/Linux
   # source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   - The project uses a `.env` file for configuration. A template is provided.
   - Open `.env` and add your credentials:
     ```ini
     # BrowserStack Credentials (Required for Cross-Browser Testing)
     BROWSERSTACK_USERNAME=your_username
     BROWSERSTACK_ACCESS_KEY=your_access_key

     # RapidAPI Credentials (Required for Translation)
     RAPIDAPI_KEY=your_rapidapi_key
     RAPIDAPI_HOST=google-translate113.p.rapidapi.com
     ```
   - **Note**: `RAPIDAPI_KEY` is required for `main.py` (translation). `BROWSERSTACK` credentials are only needed if running `browserstack_runner.py`.

## Usage

### Local Execution (Scraping & Analysis)
Run the main script to scrape articles, translate titles, and analyze text locally:
```bash
python main.py
```
This will:
- Launch a headless Chrome browser.
- Scrape the first 5 articles from El Pais Opinion.
- Download cover images to the `images/` folder.
- Translate titles to English.
- Print repeated words (>2 occurrences).

### BrowserStack Execution (Cross-Browser Testing)
Run the tests in parallel on BrowserStack:
```bash
python browserstack_runner.py
```
Tested browsers:
- Chrome (Windows 11)
- Firefox (Windows 11)
- Edge (Windows 11)
- Safari (MacOS)
- iPhone 13 (Mobile Safari)

## Sample Output
- **Console**: Displays translation and word frequency analysis.
- **`images/`**: Contains downloaded cover images.
- **`results.json`**: A detailed report of the scraping, translation, and analysis.
