# CNN Latest Articles Scraper

This Python script scrapes the latest article titles and URLs from CNN's "World" section. It uses the `requests` library to fetch the webpage and `BeautifulSoup` from `bs4` to parse the HTML.

## Prerequisites

- Python 3.x
- Internet connection

## Installation

1. Clone this repository or download the script.
2. Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

## How It Works

- The script sends an HTTP request to CNN's world news page (`https://edition.cnn.com/world`).
- It uses `BeautifulSoup` to parse the page's HTML and locate article titles and their respective URLs.
- The script then prints each article's title and URL to the console.

## Usage

Run the script using Python:

```bash
python cnn_scraper.py
```

If successful, the script will output the titles and URLs of the latest articles from CNN's World section.

Example output:

```
Title: World headline 1
URL: https://edition.cnn.com/article-1-url

Title: World headline 2
URL: https://edition.cnn.com/article-2-url
```

## SSL Certificate Warnings

The script disables SSL certificate verification by using the `verify=False` parameter in the `requests` call. You might see an `InsecureRequestWarning`, but it is suppressed by disabling warnings with `urllib3`. Although it is not recommended at production.

- **Warnings**: SSL certificate warnings are suppressed, but in production environments, it's recommended to verify SSL certificates for security purposes.


### How to Use:
1. **Save the script** as `scraper.py`.
2. **Save the `README.md`** and `requirements.txt` files in the same directory as the script.
3. Run `pip install -r requirements.txt` to install dependencies.
4. Run `python scraper.py` to see the latest CNN article titles and URLs.

This setup should provide everything you need to run the scraper successfully!