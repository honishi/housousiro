#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import logging
import re

import pyquery
import requests


HISTORY_URL = 'http://com.nicovideo.jp/live_archives/'


def crawl(community):
    history_response = requests.get(HISTORY_URL + community)
    # logging.debug(history_response.content)

    history_html = history_response.content
    query = pyquery.PyQuery(history_html)

    histories = []
    should_skip_header = True

    for history in query.items('.live_history>tr'):
        if should_skip_header:
            should_skip_header = False
            continue

        date = convert_datetime_string(history('.date').text())
        user = history('.user').text()
        title = history('.title').text()
        desc = history('.desc').text()
        logging.debug(date.strftime("%Y/%m/%d %H:%M:%S") + "," + user + "," + title + "," + desc)

        histories.append((date, user, title, desc))

    logging.debug(histories)
    return histories


def generate_calendar_events(histories, color):
    events = ""
    for history in histories:
        event = ("{"
                 "title: '" + history[2] + "',"
                 "start: '" + history[0].strftime("%Y-%m-%dT%H:%M:%S") + "',"
                 "color: '" + color + "'"
                 "},\n")
        events += event
    return events


def convert_datetime_string(string):
    # convert datetime string like '2015/06/04 開演：20:00' or '2015/05/04 開場：05:57 開演：06:00' to datetime object.
    cleansed = re.sub("開.+：", "", string)
    datetime_object = datetime.datetime.strptime(cleansed, "%Y/%m/%d %H:%M")

    return datetime_object


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    histories = crawl('co2477623')
    events = generate_calendar_events(histories, 'red')

    logging.debug(events)
