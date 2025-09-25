"""
This python module is responsible for generating
the html for the standings given a given week in
a yahoo fantasy league.
"""

from jinja2 import Template
from yahoo import get_standings, get_teams
import json

def generate_standings_html(league_key):
    standings = get_standings(league_key)
    teams = get_teams(league_key)

    lookup = {d["team_key"] : d for d in standings}
    merged = []
    for key in teams:
        if key in lookup:
            merged.append({**teams[key], **lookup[key]})

    html_template = Template(open("templates/standings.html").read())

    for team in merged:
        team["points_against"] = round(team["points_against"], 2)

    rendered = html_template.render(standings=merged)

    with open("rendered/standings.html", 'w') as f:
        f.write(rendered)
