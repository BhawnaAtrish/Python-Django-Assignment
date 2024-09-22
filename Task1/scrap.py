import requests
from bs4 import BeautifulSoup
import urllib3

# Suppress the InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://edition.cnn.com/world"
response = requests.get(url, verify=False)

# Check if request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Try to find all links that are within articles or headlines
    articles = soup.find_all("a", href=True)
    
    for article in articles:
        title = article.get_text(strip=True)
        link = article['href']
        
        # Filter out empty titles and links
        if title and link.startswith("/"):
            # Complete the URL if it's a relative link
            link = "https://edition.cnn.com" + link
            print(f"Title: {title}")
            print(f"URL: {link}\n")
else:
    print("Failed to retrieve the webpage.")
