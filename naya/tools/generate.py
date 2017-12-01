#!/usr/bin/env python
"""Tools to generate HTML fragments."""

import datetime
import os
from string import Template
import sys

from config import BASE_PATH
from naya.tools.time import human_period


def month_posts_html(month_posts, theme):
    """Create an HTML list of monthly posts.

    This is sorted by creation date.
    This depends on the chosen theme.
    """
    date_fmt = '%Y%m%dT%H%M%SZ'
    template_path = os.path.join(BASE_PATH, 'naya/templates', theme)
    if not os.path.isdir(template_path):
        sys.exit('This {theme} theme is missing.'.format(theme=theme))
    template_file = os.path.join(template_path, 'month_index.tmpl')
    with open(template_file) as f:
        tmpl = f.read()
    li = Template(tmpl)
    html = ''
    for uri in month_posts.keys():
        post_meta = month_posts[uri]
        created = post_meta['created']
        created_dt = datetime.datetime.strptime(created, date_fmt)
        updated = post_meta['updated']
        human_created = datetime.datetime.strftime(created_dt, '%d %B %Y')
        human_updated = human_period(created, updated)
        post_more_meta = {'uri': uri,
                          'human_created': human_created,
                          'human_updated': human_updated}
        post_meta.update(post_more_meta)
        html += li.substitute(post_meta)
    print('HTML: ', html)
    return html
