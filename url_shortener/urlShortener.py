import pyshorteners
import requests


def shortener(url):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url)
    return short_url


def expander(url):
    session = requests.Session()
    resp = session.head(url, allow_redirects=True)
    return resp.url


def urlShortener():
    check = input(
        "Do you want to shorten the url or get the original url? (S/l)"
    ).upper()
    if check == "S":
        og_url = input("Enter the url: ")
        shortend = shortener(og_url)
        print(shortend)
    else:
        short_url = input("Enter the url: ")
        longed = expander(short_url)
        print(longed)


urlShortener()
