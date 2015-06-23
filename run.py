#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import logging

from flask import Flask
from flask import render_template

import scrape


app = Flask(__name__)


colors = ['#dc322f', '#268bd2', '#cb4b16']

@app.route("/")
@app.route("/<communities>")
def top(communities="co2448645,co2477623"):
    events = ""

    index = 0
    for community in communities.split(','):
        events += scrape.generate_calendar_events(scrape.crawl(community), colors[index % len(colors)])
        index += 1

    return render_template('calendar.html', events = events)


if __name__ == "__main__":
    # logging.getLogger().setLevel(logging.DEBUG)
    logging.getLogger().setLevel(logging.INFO)
    app.run()
