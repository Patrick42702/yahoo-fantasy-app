from yahoo_oauth import OAuth2
from yahoo_fantasy_api import Game
import sys
import json

oauth = OAuth2(None, None, from_file='oauth2.json')
game = Game(oauth, 'nfl')

def get_standings(league_id):
    league = game.to_league(league_id)
    return league.standings()

def get_teams(league_id):
    league = game.to_league(league_id)
    return league.teams()

def get_matchups(league_id):
    league = game.to_league(league_id)
    return league.matchups(10)
