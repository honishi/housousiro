#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import logging

from flask import Flask
from flask import render_template

import scrape


TITLE = "といくんの放送カレンダー"
COLORS = ['#dc322f', '#268bd2', '#cb4b16']
COMMUNITIES = "co2448645,co2477623"


app = Flask(__name__)


@app.route("/")
@app.route("/<communities>")
def top(communities=COMMUNITIES):
    communities = communities.split(',')
    events = ""

    index = 0
    for community in communities:
        color = COLORS[index % len(COLORS)]
        events += scrape.crawl_and_generate_events(community, color)
        index += 1

    return render_template('calendar.html', title=TITLE, events=events, communities=communities)


if __name__ == "__main__":
    # logging.getLogger().setLevel(logging.DEBUG)
    logging.getLogger().setLevel(logging.INFO)
    app.run()
