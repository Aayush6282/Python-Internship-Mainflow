import requests
from bs4 import BeautifulSoup

# Function to scrape a webpage
def scrape_webpage(url):
    try:
        # Fetch the content from the URL
        response = requests.get(url, timeout=10)
        
        # Checking if the request was successful
        if response.status_code == 200:
            # Parsing the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract and print all text content
            page_text = soup.get_text()
            print("Page Text:")
            print(page_text)
            
            with open('page_text.txt', 'w', encoding='utf-8') as f:
                f.write(page_text)
            print("\nPage text saved to 'page_text.txt'")
            
            # Extract and print all links
            print("\nLinks:")
            links = []
            for link in soup.find_all('a', href=True):
                link_info = f"Text: {link.text.strip()}, URL: {link['href']}"
                links.append(link_info)
                print(link_info)
            
            with open('links.txt', 'w', encoding='utf-8') as f:
                f.write("\n".join(links))
            print("\nLinks saved to 'links.txt'")
            
            # Extract and print all images
            print("\nImages:")
            images = []
            for img in soup.find_all('img', src=True):
                img_info = f"Image Source: {img['src']}, Alt Text: {img.get('alt', 'No alt text')}"
                images.append(img_info)
                print(img_info)
            
            with open('images.txt', 'w', encoding='utf-8') as f:
                f.write("\n".join(images))
            print("\nImage information saved to 'images.txt'")
        
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# URL of the webpage to scrape (User input)
url = input("Enter the URL of the webpage to scrape: ").strip()

# Call the function to scrape the webpage
scrape_webpage(url)

