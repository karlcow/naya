#!/usr/bin/env python3
"""Tools to manipulate time."""

import datetime


def human_period(created_timestamp, updated_timestamp):
    """Send a string for each period of time.

    - 0 to 60 minutes -> aucune
    - 1h to 1 day ->  x heures apres
    - 1 day to 1 week -> x jours apres
    - more than 1 week -> exact date (16 mars 2009).
    """
    human_time = ''
    date_fmt = '%Y%m%dT%H%M%SZ'
    created = datetime.datetime.strptime(created_timestamp, date_fmt)
    updated = datetime.datetime.strptime(updated_timestamp, date_fmt)
    time_period = updated - created
    seconds = time_period.total_seconds()
    if seconds == 0:
        human_time = 'aucune'
    elif seconds < 86400:
        hours = int(seconds // 3600)
        human_time = '{hours} heures après'.format(hours=hours)
    elif time_period.days < 7:
        human_time = '{days} jours après'.format(days=time_period.days)
    else:
        human_time = datetime.datetime.strftime(updated, '%d %B %Y')
    return human_time
