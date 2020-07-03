# standings.py

import read_data
from print_plot import printTable, plotGoals

def unique_list(dic, column):
    raw_list = [i[column] for i in dic]
    unique = list(set(raw_list))
    return unique

def results(teams, season):
    matchdays = unique_list(season, 'name')
    for team in teams:
        team['gf'] = 0
        team['ga'] = 0
        team['gdiff'] = 0
        team['played'] = 0
        team['points'] = 0
        team['wins'] = 0
        team['ties'] = 0
        team['losses'] = 0
        for matchday in matchdays:
            for result in season:
                if matchday == result['name']:
                    if team['code'] == result['home_team']:
                        if result['home_win']:
                            team[matchday] = 'win'
                            team['type_'+matchday.split(' ')[1]] = 'home'
                            team['gf_'+matchday.split(' ')[1]] = result['home_score']
                            team['ga_'+matchday.split(' ')[1]] = result['away_score']
                            team['gdiff_'+matchday.split(' ')[1]] = result['home_score']-result['away_score']
                            team['gf'] += result['home_score']
                            team['ga'] += result['away_score']
                            team['gdiff'] = team['gf']-team['ga']
                            team['played'] += 1
                            team['points'] += 3
                            team['wins'] += 1
                        elif result['tie']:
                            team[matchday] = 'tie'
                            team['type_'+matchday.split(' ')[1]] = 'home'
                            team['gf_'+matchday.split(' ')[1]] = result['home_score']
                            team['ga_'+matchday.split(' ')[1]] = result['away_score']
                            team['gdiff_'+matchday.split(' ')[1]] = result['home_score']-result['away_score']
                            team['gf'] += result['home_score']
                            team['ga'] += result['away_score']
                            team['gdiff'] = team['gf']-team['ga']
                            team['played'] +=1
                            team['points'] += 1
                            team['ties'] += 1
                        elif result['away_win']:
                            team[matchday] = 'loss'
                            team['type_'+matchday.split(' ')[1]] = 'home'
                            team['gf_'+matchday.split(' ')[1]] = result['home_score']
                            team['ga_'+matchday.split(' ')[1]] = result['away_score']
                            team['gdiff_'+matchday.split(' ')[1]] = result['home_score']-result['away_score']
                            team['gf'] += result['home_score']
                            team['ga'] += result['away_score']
                            team['gdiff'] = team['gf']-team['ga']
                            team['played'] +=1
                            team['losses'] +=1
                        else:
                            team[matchday] = None
                    elif team['code'] == result['away_team']:
                        if result['away_win']:
                            team[matchday] = 'win'
                            team['type_'+matchday.split(' ')[1]] = 'away'
                            team['gf_'+matchday.split(' ')[1]] = result['away_score']
                            team['ga_'+matchday.split(' ')[1]] = result['home_score']
                            team['gdiff_'+matchday.split(' ')[1]] = result['away_score']-result['home_score']
                            team['gf'] += result['away_score']
                            team['ga'] += result['home_score']
                            team['gdiff'] = team['gf']-team['ga']
                            team['played'] +=1
                            team['points'] +=3
                            team['wins'] +=1
                        elif result['tie']:
                            team[matchday] = 'tie'
                            team['type_'+matchday.split(' ')[1]] = 'away'
                            team['gf_'+matchday.split(' ')[1]] = result['away_score']
                            team['ga_'+matchday.split(' ')[1]] = result['home_score']
                            team['gdiff_'+matchday.split(' ')[1]] = result['away_score']-result['home_score']
                            team['gf'] += result['away_score']
                            team['ga'] += result['home_score']
                            team['gdiff'] = team['gf']-team['ga']
                            team['played'] += 1
                            team['points'] += 1
                            team['ties'] +=1
                        elif result['home_win']:
                            team[matchday] = 'loss'
                            team['type_'+matchday.split(' ')[1]] = 'away'
                            team['gf_'+matchday.split(' ')[1]] = result['away_score']
                            team['ga_'+matchday.split(' ')[1]] = result['home_score']
                            team['gdiff_'+matchday.split(' ')[1]] = result['away_score']-result['home_score']
                            team['gf'] += result['away_score']
                            team['ga'] += result['home_score']
                            team['gdiff'] = team['gf']-team['ga']
                            team['played'] +=1
                            team['losses'] +=1
                        else:
                            team[matchday] = None
                    else: continue
    return teams

    
url_pl = 'https://raw.githubusercontent.com/openfootball/football.json/master/2019-20/en.1.json'
data = read_data.season_data(url_pl)
url_pl_teams = 'https://raw.githubusercontent.com/openfootball/football.json/master/2019-20/en.1.clubs.json'
teams = read_data.teams_data(url_pl_teams)
res = results(teams, data)
plotGoals(res, 'LIV')
columns = ['name', 'played', 'wins', 'ties', 'losses', 'points', 'gdiff']
printTable(res, columns)


# if __name__ == '__main__':
#     import sys
#     main(sys.argv)