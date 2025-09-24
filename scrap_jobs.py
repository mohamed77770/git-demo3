import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrap():
    headers = {
    "Accept-Language" : "en-US, en;q=0.9"
 }
    response = requests.get('https://wuzzuf.net/search/jobs/?q=machine+learning&a=navbl', headers=headers)
    soup = BeautifulSoup(response.content,'lxml')

    titles = soup.find_all("h2", {'class': 'css-193uk2c'})
    titles_lst = [title.text for title in titles]

    links = [title.a['href'] for title in titles]

    occupations = soup.find_all("div", {'class': 'css-5jhz9n'})
    occupations_lst = [occupation.text for occupation in occupations]

    companies = soup.find_all("a", {'class': 'css-ipsyv7'})
    companies_lst = [company.text for company in companies]

    specs = soup.find_all("div", {'class':'css-1rhj4yg'})
    specs_lst = [spec.text for spec in specs]

    locs = soup.find_all("span", {'class': 'css-16x61xq'})
    locs_lst = [loc.text for loc in locs]

    scrapped_data = {}
    scrapped_data['Title'] = titles_lst
    scrapped_data['Link'] = links
    scrapped_data['Occupation'] = occupations_lst
    scrapped_data['Company'] = companies_lst
    scrapped_data['Specs'] = specs_lst
    scrapped_data['Location'] = locs_lst

    df = pd.DataFrame(scrapped_data)
    df.to_csv('MLjobs.csv', index=False)
    print("Jobs Scraped Successfully")
    return df

if __name__ == '__main__':
    scrap()



