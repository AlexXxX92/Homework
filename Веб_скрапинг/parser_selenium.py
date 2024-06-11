from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import json



def wait_element(browser, delay_seconds=1, by=By.CLASS_NAME, value=None):
    return WebDriverWait(browser, delay_seconds).until(
        expected_conditions.presence_of_element_located((by, value))
    )



chrome_path = ChromeDriverManager().install()
options = ChromeOptions()
browser_service = Service(executable_path=chrome_path)
browser = Chrome(service=browser_service)


def links_pages():
    links_page = ["https://spb.hh.ru/search/vacancy?text=Python&salary="
       "1&currency_code=USD&ored_clusters=true&search_period="
       "1&excluded_text=&area=1&area=2&hhtmFrom="
       "vacancy_search_list&hhtmFromLabel=vacancy_search_line"]

    browser.get(links_page[0])

    pages = browser.find_element(By.CLASS_NAME, "pager")
    pages_tag = pages.find_elements(By.TAG_NAME, "a")

    for i in pages_tag:
        link_page = i.get_attribute("href")
        links_page.append(link_page)
    return links_page[:5]

# job_main = browser.find_element(By.CLASS_NAME, "vacancy-serp-content")
def links():
    links = []
    for url in links_pages():
        browser.get(url)
        main_tag = browser.find_element(By.CLASS_NAME, "vacancy-serp-content")
        job_cards = main_tag.find_elements(By.TAG_NAME, "h2")

        for h2 in job_cards:
            tag_link = wait_element(h2, by=By.TAG_NAME, value="a")

            link = tag_link.get_attribute("href")
            links.append({"link": link})

    return links

def top_card_job_new():
    card_job = []
    for url in links():
        browser.get(url["link"])
        vacancy_tag = wait_element(browser, by=By.CLASS_NAME, value="vacancy-description")
        tag_title = wait_element(browser, by=By.CLASS_NAME, value="vacancy-title")
        company_tag = wait_element(browser, by=By.CLASS_NAME, value="vacancy-company-redesigned")


        company_list = company_tag.text.split("\n")
        salary = tag_title.text.split("\n")[1]
        title = tag_title.text.split("\n")[0]
        info = vacancy_tag.text
        company_name = company_list[0]
        company_city = company_list[-1].split(",")[0]

        if "django" in info.lower() or "flask" in info.lower():
            card_job.append({"title": title,
                             "company": company_name,
                             "city": company_city,
                             "salary": salary,
                             "link": url["link"]
                             })

    return card_job

def save_json(list):
    with open("vakancy_selenium.json", "w", encoding='utf-8') as f:
        for i in list:
            json.dump(i, f, ensure_ascii=False)
            f.write('\n')

if __name__ == "__main__":
    save_json(top_card_job_new())
