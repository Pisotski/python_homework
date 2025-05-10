import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import json
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()), options=options
)


def task3():
    search_url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
    driver.get(search_url)
    body = driver.find_element(By.CSS_SELECTOR, "body")
    search_ul = body.find_element(By.CSS_SELECTOR, 'ul[class="results"]')
    results = []
    # Main loop: You iterate through the list of li entries.
    # For each, you find the entry that contains title of the book,
    # and get the text for that entry.
    # Then you find the entries that contain the authors of the book,
    # and get the text for each.
    # If you find more than one author, you want to join the author names
    # with a semicolon ; between each.
    # Then you find the div that contains the format and the year,
    # and then you find the span entry within it that contains this information.
    # You get that text too.  You now have three pieces of text.
    # Create a dict that stores these values, with the keys being Title, Author, and Format-Year.
    # Then append that dict to your results list.

    if search_ul:
        list_items = search_ul.find_elements(
            By.CSS_SELECTOR, 'li[class="row cp-search-result-item"]'
        )
        if len(list_items) > 0:
            for li in list_items:
                title_el = li.find_element(
                    By.CSS_SELECTOR, "h2.cp-title a span.title-content"
                )
                title = title_el.text.strip()
                authors_el = li.find_elements(
                    By.CSS_SELECTOR, "span.cp-author-link span a"
                )
                authors = [el.text.strip() for el in authors_el]
                authors_str = ";".join(authors)
                format_and_year_el = li.find_element(
                    By.CSS_SELECTOR, "span.display-info-primary"
                )
                format_and_year = format_and_year_el.text.strip()
                results.append(
                    {
                        "Title": title,
                        "Authors": authors_str,
                        "Format-Year": format_and_year,
                    }
                )
    driver.quit()

    df = pd.DataFrame(results)
    print(df)
    with open("get_books.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Authors", "Format-Year"])
        for book in results:
            writer.writerow([book["Title"], book["Authors"], book["Format-Year"]])

    with open("get_books.json", "w") as json_file:
        json.dump(results, json_file, indent=4)

    return results


# task3()
