import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()), options=options
)


def task6():

    results = []
    search_url = "https://owasp.org/www-project-top-ten/"
    driver.get(search_url)
    body = driver.find_element(By.CSS_SELECTOR, "body")
    top10_h2 = body.find_element(
        By.CSS_SELECTOR, 'h2[id="top-10-web-application-security-risks"]'
    )
    top10_ul = top10_h2.find_element(By.XPATH, "following-sibling::ul")
    if top10_ul:
        risks_list = top10_ul.find_elements(By.CSS_SELECTOR, "a")
        if len(risks_list) > 0:
            for risk in risks_list:
                title = risk.find_element(By.CSS_SELECTOR, "strong").text
                url = risk.get_attribute("href")
                results.append({"Title": title, "Url": url})
    driver.quit()

    with open("owasp_top_10.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Url"])
        for vulnerability in results:
            writer.writerow([vulnerability["Title"], vulnerability["Url"]])


task6()
