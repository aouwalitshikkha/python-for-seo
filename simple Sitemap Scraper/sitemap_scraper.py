import requests
from xml.etree import ElementTree

def scrape_sitemap(sitemap_url):
    try:
        response = requests.get(sitemap_url)
        response.raise_for_status()  # Check if the request was successful

        # Parse the XML sitemap
        root = ElementTree.fromstring(response.content)
        namespace = {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        urls = []

        # Find all <loc> tags in the sitemap
        for loc in root.findall(".//ns:loc", namespace):
            urls.append(loc.text)

        return urls

    except Exception as e:
        print(f"Error: {e}")
        return []

# Example usage
sitemap_url = "https://example.com/sitemap.xml"
urls = scrape_sitemap(sitemap_url)

if urls:
    print("URLs found in the sitemap:")
    for url in urls:
        print(url)
else:
    print("No URLs found or there was an error.")
