import requests

def check_http_header(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            print("HTTP Headers:")
            for key, value in response.headers.items():
                print(f"{key}: {value}")
                
            missing_headers = set(['Content-Type', 'Cache-Control', 'Expires']) - set(response.headers.keys())
            if missing_headers:
                print("\nMissing Headers:")
                for header in missing_headers:
                    print(header)
        else:
            print(f"Request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage
url = input("Enter the URL: ")
check_http_header(url)
