from bs4 import BeautifulSoup as bs
import requests
from flask_restful import Resource

leagues = [
    {
        'id': 1,
        'country' : 'Brasil',
        'url': 'https://fbref.com/pt/comps/24/Serie-A-Stats'
    },
    {
        'id': 2,
        'country' : 'Inglaterra',
        'url': 'https://fbref.com/pt/comps/9/Premier-League-Stats'
    },
    {
        'id': 3,
        'country': 'Espanha',
        'url': 'https://fbref.com/pt/comps/12/La-Liga-Stats'
    }

]

class Leagues(Resource):
    def get(self):
        return leagues, 200

class League(Resource):
    def get(self, id):
        for league in leagues:
            print(league.get('id'))
            if(id == league["id"]):
                return league, 200
        return "Item not found for the id: {}".format(id), 404

class Standing(Resource):
    def get(self, id):
        for league in leagues:
            if(id == league["id"]):
                url = league.get('url')
                page = requests.get(url, timeout=5)
                page_content = bs(page.content, "html.parser")
                table_wrapper = page_content.find('div', attrs={'class': 'table_outer_container'})
                response = {
                    'table_head': self.get_head_data(table_wrapper),
                    'table_rows': self.get_rows_data(table_wrapper)
                }
                return response, 200
        return "Item not found for the id: {}".format(id), 404
    
    def get_head_data(self, table_wrapper):
        thead = table_wrapper.find('thead')
        ths = thead.find_all('th')
        return [val.text for val in ths]

    def get_rows_data(self, table_wrapper):
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
