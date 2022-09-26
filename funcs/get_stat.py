import requests
from bs4 import BeautifulSoup

def get_stats(): 

    url = "http://www.cnba.pl/poddzial,tabela,25.html"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}

    result = requests.get(url, headers=headers)
    result.encoding = 'utf-8'
    src = result.text
    soup = BeautifulSoup(src, 'lxml')
    teams_info = soup.find('table').find_all('tr')
    final_info = ""
    for team in teams_info[1:13]:
        team_td = team.find_all('td')
        id = team_td[0].text
        name = team_td[1].find('a').text
        matches = team_td[2].text
        wins = team_td[3].text
        loses = team_td[4].text
        points = team_td[5].text 
        info = f"{id} {name} | {matches} matches | {wins} wins | {loses} loses | {points} points \n"
        final_info += info
    return final_info
    
     
