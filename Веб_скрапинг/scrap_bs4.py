import json
import requests
from bs4 import BeautifulSoup
from fake_headers import Headers

def get_headers():
    return Headers(browser="chrome", os="win").generate()




def pagers_link():
    pagers = ["https://spb.hh.ru/search/vacancy?L_save_area=true&text=python&excluded_text"
               "=&area=1&area=2&salary=1&currency_code=USD&experience=doesNotMatter&order_by"
               "=relevance&search_period=1&items_on_page=50&hhtmFrom=vacancy_search_filter"
                ]

    main_response = requests.get(pagers[0], headers=get_headers())
    main_html = main_response.text
    main_soup = BeautifulSoup(main_html, "lxml")

    pager = main_soup.find("div", class_="pager")
    tag_a = pager.find_all("a")
    for a in tag_a:
        pager_link = a["href"]
        link = f"https://spb.hh.ru{pager_link}"
        pagers.append(link)

    return pagers[:5]



def link_vacancy():
    links = []
    for pager in pagers_link():
        main_response = requests.get(pager, headers=get_headers())
        main_html = main_response.text
        main_soup = BeautifulSoup(main_html, "lxml")

        content = main_soup.find("div", id="a11y-main-content")
        h2_tag = content.find_all("h2")

        for h2 in h2_tag:
            a_tag = h2.find("a")
            link = a_tag["href"]
            links.append(link)

    return links

def top_new_vacancy():
    vakancy = []
    for url in link_vacancy():
        card_response = requests.get(url, headers=get_headers())
        card_html = card_response.text
        card_soup = BeautifulSoup(card_html, "lxml")

        card_info = card_soup.find("div", class_="vacancy-description")
        info = card_info.text.replace('\n', '')
        if "django" in info.lower() or "flask" in info.lower():
            title_info = card_soup.find("h1", class_="bloko-header-section-1")

            company_name = card_soup.find("div", class_="vacancy-company-details")
            city_info = card_soup.find("p", class_="vacancy-creation-time-redesigned")
            salary_info = card_soup.find("span", class_="magritte-text___pbpft_3-0-4"
                                                        " magritte-text_style-primary___AQ7MW_3-0-4"
                                                        " magritte-text_typography-label-1-regular___pi3R-_3-0-4"
                                         )

            title = title_info.text.replace("\xa0", ' ')
            salary = salary_info.text.replace("\xa0", ' ')
            company = company_name.text.replace("\xa0", ' ')
            city = "Санкт-Петербург" if city_info.text.split()[-1] == "Санкт-Петербурге" else "Москва"

            vakancy.append({"title": title,
                            "company": company,
                            "city": city,
                            "salary": salary,
                            "link": url
                            })

    return vakancy

def save_json(list):
    with open("vakancy_bs4.json", "w", encoding='utf-8') as f:
        for i in list:
            json.dump(i, f, ensure_ascii=False)
            f.write('\n')

if __name__ == "__main__":
    save_json(top_new_vacancy())
