import yahoo_fantasy_api as yfa
from yahoo import get_matchups
import json

def generate_weekly_report(league_id):
    matchups = get_matchups(league_id)
    with open("json/matchups.json", 'w') as f:
        f.write(json.dumps(matchups))

if __name__ == "__main__":
    generate_weekly_report("449.l.228237")
