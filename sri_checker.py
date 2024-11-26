import requests
from bs4 import BeautifulSoup

def check_sri_vulnerability(url):
    try:
        # Fetch the webpage content
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all <script> and <link> tags
        scripts = soup.find_all('script', src=True)
        links = soup.find_all('link', href=True, rel=lambda x: x and 'stylesheet' in x)

        # Check for missing SRI in <script> tags
        print("\n[Checking <script> tags]")
        for script in scripts:
            if 'integrity' not in script.attrs:
                print(f"Missing SRI: {script['src']}")

        # Check for missing SRI in <link> tags
        print("\n[Checking <link> tags]")
        for link in links:
            if 'integrity' not in link.attrs:
                print(f"Missing SRI: {link['href']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to fetch the webpage. Details: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("Subresource Integrity (SRI) Vulnerability Checker")
    url = input("Enter the URL of the website (e.g., https://mesbahinfo.com): ").strip()

    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url  # Add https if not provided by the user

    print(f"\nChecking SRI for: {url}")
    check_sri_vulnerability(url)
