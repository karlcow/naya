#!/usr/bin/env python
"""Tools to parse HTML data."""

import sys
import xml.etree.ElementTree as et


def extract_month_entries(html_fragment):
    """Return a dictionary of entries extracted from an html fragment.

    The CSS schema is
    .month contains a list .post
    Each .post contains
        .title
            where 'href' is the URI
            and textContent is the post title.
        .created with a datetime of the blog post published date
        .updated with a datetime of the blog post updated date
    In the future, it could be cool to imagine to load a CSS selector Schema
    and extract information fron any fragment with the Schema.
    """
    month_root = et.fromstring(html_fragment)
    posts = {}
    if month_root.attrib['class'] == 'month':
        for post in month_root:
            post_meta = {}
            for item in post:
                if item.attrib['class'] == 'title':
                    uri = item.attrib['href']
                    post_meta['title'] = item.text
                if item.attrib['class'] == 'created':
                    post_meta['created'] = item.attrib['datetime']
                if item.attrib['class'] == 'updated':
                    post_meta['updated'] = item.attrib['datetime']
            posts.update({uri: post_meta})
    else:
        sys.exit('Invalid HTML fragment for months')
    return posts
