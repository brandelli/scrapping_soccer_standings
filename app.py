from bs4 import BeautifulSoup as bs
import requests
import matplotlib.pyplot as plt

def main():
    URL = "https://fbref.com/en/comps/24/Serie-A-Stats"
    page = requests.get(URL, timeout=5)
    page_content = bs(page.content, "html.parser")
    table_wrapper = page_content.find('div', attrs={'class': 'table_outer_container'})
    head = get_head_data(table_wrapper)
    table_rows = get_rows_data(table_wrapper)
    print_table(head, table_rows)
    

def print_table(head, table_rows):
    print(' '.join(head))
    for row in table_rows:
        print(' '.join(row))

def get_head_data(table_wrapper):
    thead = table_wrapper.find('thead')
    ths = thead.find_all('th')
    return [val.text for val in ths]

def get_rows_data(table_wrapper):
    clean_rows = []
    table = table_wrapper.find('tbody')
    rows = table.find_all('tr')
    for row in rows:
        clean_tds = []
        th = row.find('th').text
        tds = row.find_all('td')
        clean_tds.append(th)
        clean_tds.extend([val.text for val in tds])
        clean_rows.append(clean_tds)
    
    return clean_rows

if  __name__ == '__main__':
    main()