from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv
import json

options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()), options=options
)


def get_library_policy():
    robots_url = "https://durhamcountylibrary.org/robots.txt"
    driver.get(robots_url)
    print(driver.page_source)
    driver.quit()


# get_library_policy()
# <html><head><meta name="color-scheme" content="light dark"></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">User-agent: *
#     Disallow: /staff/

# User-agent: AdsBot-Google
# Disallow: /


# User-agent: Amazonbot
# Disallow: /


# User-agent: Applebot
# Disallow: /


# User-agent: Applebot-Extended
# Disallow: /


# User-agent: anthropic-ai
# Disallow: /


# User-agent: AwarioRssBot
# Disallow: /


# User-agent: AwarioSmartBot
# Disallow: /


# User-agent: Bytespider
# Disallow: /


# User-agent: CCBot
# Disallow: /


# User-agent: ChatGPT
# Disallow: /


# User-agent: ChatGPT-User
# Disallow: /


# User-agent: ClaudeBot
# Disallow: /


# User-agent: Claude-Web
# Disallow: /


# User-agent: cohere-ai
# Disallow: /


# User-agent: DataForSeoBot
# Disallow: /


# User-agent: Diffbot
# Disallow: /


# User-agent: FacebookBot
# Disallow: /


# User-agent: Google-Extended
# Disallow: /


# User-agent: GPTBot
# Disallow: /


# User-agent: ImagesiftBot
# Disallow: /


# User-agent: magpie-crawler
# Disallow: /


# User-agent: omgili
# Disallow: /


# User-agent: Omgilibot
# Disallow: /


# User-agent: peer39_crawler
# Disallow: /


# User-agent: PerplexityBot
# Disallow: /


# User-agent: YouBot
# Disallow: /</pre></body></html>

## Task 2: Understanding HTML and the DOM for the Durham Library Site

# data-test-id="searchResultItem"


def task2():
    search_url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
    driver.get(search_url)
    body = driver.find_element(By.CSS_SELECTOR, "body")
    search_ul = body.find_element(By.CSS_SELECTOR, 'ul[class="results"]')
    if search_ul:

        titles = search_ul.find_elements(By.CSS_SELECTOR, 'h2[class="cp-title"]')
        authors = search_ul.find_elements(By.CSS_SELECTOR, 'a[class="author-link"]')
        format_info = search_ul.find_elements(By.CSS_SELECTOR, 'class="cp-format-info"')


# task2()
