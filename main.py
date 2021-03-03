import requests
from bs4 import BeautifulSoup
from re import sub


def get_html(url):
    """
    Get the source code of the page.
    Returns the code in the text.
    """
    result = requests.get(url)
    return result.text


def get_data(html):
    """
    Get the items you were looking for in the previous article.
    Returns the contents of the elements to find.
    """
    soup = BeautifulSoup(html, "lxml")

    # Find the latest article.
    article = soup.find("div", {"class": "preview-card__content"})  # to find items in this article
    title = article.find("h2", {"class": "preview-card__title"}).getText()
    link = article.find("a", {"class": "no-link"}).get("href")
    description = article.find("div", {"class": "preview-card__text"}).getText()
    likes = article.find("span", {"class": "reaction__count"}).getText()
    likes = sub("\s+|", "", likes)  # remove spaces and hyphens

    print("Last news!".upper())
    print(f"Title: {title}")
    print(f"Link: https://proglib.io{link}")
    print(f"Description: {description}")
    print(f"Likes: {likes}")


def main():
    html = get_html("https://proglib.io/")
    get_data(html)


if __name__ == "__main__":
    main()
