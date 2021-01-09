# football_api.py
"""
This script reads from the open source api:
https://github.com/openfootball/football.json
and creates a dataset of matchday resultls"
"""
import urllib.request
import json

def read_json_api(url):
    '''
    Reads json data from a url and returns it as
    a dict using the json library.
    ''' 
    json_stream = urllib.request.urlopen(url)
    json_dump = json.loads(json_stream.read())
    return json_dump

def teams_data(teams_url):
    '''
    Reads Football League teams from the openfootball
    database and creates a list of dictionaries.
    '''
    teams = read_json_api(teams_url)['clubs']
    for i, team in enumerate(teams):
        team['team_id']= i
    return teams

def season_data(season_url):
    '''
    Reads the Premiere League results from the openfootball
    database and creates a list of dictionaries for each match.
    '''
    pl = read_json_api(season_url)['matches']
    matches = []
    for matchday in pl:
        if 'score' in matchday.keys():
            match = {'name': matchday['round'],
                     'date': matchday['date'],
                     'home_team': matchday['team1'],
                     'away_team': matchday['team2'],
                     'home_score': matchday['score']['ft'][0],
                     'away_score': matchday['score']['ft'][1],}
        else:
            continue
        if (match['home_score']==None) or (match['away_score']==None):
                match['home_win'] = None
                match['away_win'] = None
                match['tie'] = None
        elif match['home_score'] > match['away_score']:
                match['home_win'] = True
                match['away_win'] = False
                match['tie'] = False
        elif match['home_score']<match['away_score']:
                match['home_win'] = False
                match['away_win'] = True
                match['tie'] = False
        else:
                match['home_win'] = False
                match['away_win'] = False
                match['tie'] = True
        matches.append(match)
    return matches

def main(args):
    url_pl = 'https://raw.githubusercontent.com/openfootball/football.json/master/2018-19/en.1.json'
    return season_data(url_pl)

if __name__ == '__main__':
    import sys
    main(sys.argv)