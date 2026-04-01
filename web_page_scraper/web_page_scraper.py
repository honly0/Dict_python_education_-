import requests
from bs4 import BeautifulSoup
import os
import string
import sys




def stage1():
    url = input("Input the URL:\n> ").strip()
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            print("Invalid quote resource!")
            return
        data = response.json()
        if "content" not in data:
            print("Invalid quote resource!")
            return
        print(data["content"])
    except Exception:
        print("Invalid quote resource!")




def stage2():
    url = input("Input the URL:\n> ").strip()
    if "imdb.com" not in url or "/title/" not in url:
        print("Invalid movie page!")
        return
    try:
        response = requests.get(url, headers={"Accept-Language": "en-US,en;q=0.5"}, timeout=10)
        if response.status_code != 200:
            print("Invalid movie page!")
            return
        soup = BeautifulSoup(response.content, "html.parser")
        title_tag = soup.find("title")
        desc_tag = soup.find("meta", {"name": "description"})
        if not title_tag or not desc_tag:
            print("Invalid movie page!")
            return
        title = title_tag.text.split(" - IMDb")[0].strip()
        description = desc_tag.get("content", "").strip()
        if not title or not description:
            print("Invalid movie page!")
            return
        print({"title": title, "description": description})
    except Exception:
        print("Invalid movie page!")




def stage3():
    url = input("Input the URL:\n> ").strip()
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            print(f"The URL returned {response.status_code}!")
            return
        with open("source.html", "wb") as f:
            f.write(response.content)
        print("Content saved.")
    except Exception as e:
        print(f"Error: {e}")




def clean_filename(title):
    title = title.strip()
    translator = str.maketrans("", "", string.punctuation)
    title = title.translate(translator)
    title = title.replace(" ", "_")
    return title + ".txt"


def fetch_articles_from_page(page_url, article_type, folder):
    headers = {"Accept-Language": "en-US,en;q=0.5"}
    response = requests.get(page_url, headers=headers, timeout=15)
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.find_all("article")
    saved = []

    for article in articles:
        type_tag = article.find("span", {"data-test": "article.type"})
        if not type_tag or type_tag.text.strip() != article_type:
            continue

        link_tag = article.find("a", {"data-track-action": "view article"})
        if not link_tag:
            continue

        article_url = "https://www.nature.com" + link_tag["href"]
        title = link_tag.text.strip()
        filename = clean_filename(title)

        art_response = requests.get(article_url, headers=headers, timeout=15)
        if art_response.status_code != 200:
            continue

        art_soup = BeautifulSoup(art_response.content, "html.parser")
        body = art_soup.find("div", {"class": lambda c: c and "body" in c})
        if not body:
            # try article body tag
            body = art_soup.find("div", attrs={"data-article-body": True})
        if not body:
            continue

        text = body.get_text(separator="\n").strip()
        filepath = os.path.join(folder, filename)
        with open(filepath, "wb") as f:
            f.write(text.encode("utf-8"))
        saved.append(filename)

    return saved


def stage4():
    base_url = "https://www.nature.com/nature/articles?sort=PubDate&year=2022&page=3"
    folder = "."
    saved = fetch_articles_from_page(base_url, "News", folder)
    print(f"Saved articles: {saved}")




def stage5():
    num_pages = int(input("> ").strip())
    article_type = input("> ").strip()

    base_url = "https://www.nature.com/nature/articles?sort=PubDate&year=2022&page={}"

    for page_num in range(1, num_pages + 1):
        folder = f"Page_{page_num}"
        os.makedirs(folder, exist_ok=True)
        url = base_url.format(page_num)
        fetch_articles_from_page(url, article_type, folder)

    print("Saved all articles.")



if __name__ == "__main__":
    stage = sys.argv[1] if len(sys.argv) > 1 else "5"
    stages = {"1": stage1, "2": stage2, "3": stage3, "4": stage4, "5": stage5}
    stages.get(stage, stage5)()
