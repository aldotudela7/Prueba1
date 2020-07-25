#predict.py

import read_data
import pandas as pd

# Putting season data in dataframes
url_pl = 'https://raw.githubusercontent.com/openfootball/football.json/master/2018-19/en.1.json'
data = read_data.season_data(url_pl)
url_pl_teams = 'https://raw.githubusercontent.com/openfootball/football.json/master/2018-19/en.1.clubs.json'
teams = pd.DataFrame(read_data.teams_data(url_pl_teams))

# Adding a column with teams ids
data = pd.DataFrame(data)
data = data.merge(teams, left_on='home_team', right_on='name', how='left')
data = data.rename(columns = {'team_id': 'home_id', 'name_x':'name'}).drop(['code','key','name_y'], axis=1)
data = data.merge(teams, left_on='away_team', right_on='name', how='left')
data = data.rename(columns = {'team_id': 'away_id', 'name_x':'name'}).drop(['code','key','name_y'], axis=1)

# import numpy as np
# import pymc3 as pymc
# from pymc3 import Model, Normal, Deterministic, Gamma, Poisson, sample, model_to_graphviz, find_MAP

# observed_home_goals = data.home_score.values
# observed_away_goals = data.away_score.values
# home_team = data.home_id.values
# away_team = data.away_id.values
# num_teams = len(data.home_id.unique())
# num_games = len(home_team)

# g = data.groupby('away_id')
# att_starting_points = np.log(g.away_score.mean())
# g = data.groupby('home_id')
# def_starting_points = -np.log(g.away_score.mean())

# with Model() as model:
#     # Priors for unknown model parameters
#     home = Normal('home', mu=0, tau=0.001, testval=0)
#     tau_att = Gamma('tau_att', alpha=0.1, beta=0.1, testval=10)
#     tau_def = Gamma('tau_def', alpha=0.1, beta=0.1, testval=10)
#     intercept = Normal('intercept', mu=0, tau=0.0001, testval=0)

#     # team-specific parameters
#     atts_star = Normal("atts_star", 
#                         mu=0, 
#                         tau=tau_att,
#                         shape = num_teams,
#                         testval = att_starting_points)
#     defs_star = Normal("defs_star", 
#                         mu=0, 
#                         tau=tau_def,
#                         shape = num_teams,
#                         testval = def_starting_points)
    
#     # trick to code the sum to zero contraint
#     atts = Deterministic('atts', atts_star-atts_star.mean())
#     defs = Deterministic('defs', defs_star-defs_star.mean())
    
#     home_theta = Deterministic('home_theta', np.exp(intercept + home + atts[home_team] + defs[away_team]))
#     away_theta = Deterministic('away_theta', np.exp(intercept + atts[away_team] + defs[home_team]))

#     home_goals = Poisson('home_goals', 
#                           mu=home_theta,
#                           observed=observed_home_goals)
#     away_goals = Poisson('away_goals', 
#                           mu=away_theta,
#                           observed=observed_away_goals)

# # model_to_graphviz(model).render('test', view=True)

# with model:
#     trace = sample(1000, tune=1000, cores=3)

# # map_estimate = find_MAP(model=model)