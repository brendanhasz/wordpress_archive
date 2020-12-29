import os
import requests
import sys
from urllib.request import urlopen, urlretrieve

from bs4 import BeautifulSoup


def get_soup(url):
    html = str(urlopen(url).read())
    return BeautifulSoup(html, "html.parser")


def get_post_links(url):
    soup = get_soup(url)
    links = [e.find("a")["href"] for e in soup.find_all('h2')]
    return links[1:]  # first is always a link to the home page


def download_images(url, folder):
    soup = get_soup(url)
    img_links = [e["src"] for e in soup.find_all("img")]
    img_links = img_links[2:-1]  # first two and last one are theme stuff
    img_links = [e for e in img_links if "gravatar.com" not in e]
    for link in img_links:
        fname = link.split("/")[-1]
        try:
            urlretrieve(link, f"{folder}/{fname}")
        except:
            print(f"Failed to get {link}")
            pass  # ¯\_(ツ)_/¯


if __name__ == "__main__":

    # Command line arguments
    base_url = sys.argv[1]
    start_year = int(sys.argv[2])
    end_year = int(sys.argv[3])
    output_dir = sys.argv[4]

    # Get a list of all post links and dates
    print("Finding all the post links...")
    links = []
    dates = []
    for year in range(start_year, end_year+1):
        for month in range(1, 13):
            try:
                new_links = get_post_links(f"{base_url}/{year}/{month}")
                links += new_links
                dates += [f"{year}_{month:02d}" for _ in new_links]
            except:
                pass

    # Create the output directory
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    # Download em all
    for date, link in zip(dates, links):
        print(f"Downloading {link}")
        fname = f"{date}_{link.split('/')[-2].replace('-', '_')}"
        folder = f"{output_dir}/{fname}"
        if not os.path.exists(folder):
            os.mkdir(folder)
        urlretrieve(link, f"{folder}/{fname}.html")
        download_images(link, folder)
