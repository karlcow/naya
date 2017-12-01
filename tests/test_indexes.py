#!/usr/bin/env python
"""Tests for index generation."""

import unittest

from naya.tools.generate import month_posts_html
from naya.tools.parse import extract_month_entries
from naya.tools.update import update_month_index


class TestIndexes(unittest.TestCase):
    """Tests for index generation."""

    def setUp(self):
        """Set up tests."""
        self.maxDiff = None
        self.month_index = {
            '/2020/03/16/what': {
                'title': 'What do you need?',
                'created': '20200316T201010Z',
                'updated': '20200316T201010Z'},
            '/2020/03/20/where': {
                'title': 'Where is that?',
                'created': '20200320T010220Z',
                'updated': '20200321T030220Z'}
            }
        self.html_list = """<ul class='month'>
        <li class='post'>
          <a class='title' href='/2020/03/16/what'>What do you need?</a>,
            <time class="created"
                  datetime='20200316T201010Z'>16 mars 2020</time>,
            <time class="updated"
                  datetime='20200316T201010Z'>16 mars 2020</time>
        </li>
        <li class='post'>
          <time class="created"
                datetime='20200320T010220Z'>20 mars 2020</time>:
          <a class='title' href='/2020/03/20/where'>Where is that?</a>,
          <time class="updated"
                datetime='20200321T030220Z'>21 mars 2020</time>
        </li>
        </ul>
        """
        self.html_month_naya = """<li class='post'><a class='title' href='/2020/03/16/what'>What do you need?</a>, <time class="created" datetime='20200316T201010Z'>16 mars 2020</time> (<time class="updated" datetime='20200316T201010Z'>aucune</time>)</li>
<li class='post'><a class='title' href='/2020/03/20/where'>Where is that?</a>, <time class="created" datetime='20200320T010220Z'>20 mars 2020</time> (<time class="updated" datetime='20200321T030220Z'>1 jours après</time>)</li>
"""  # noqa

    def tearDown(self):
        """Tear down the tests."""
        pass

    def test_updated_month_index(self):
        """Month: A new updated date for an existing URI."""
        new_date = {
            '/2020/03/16/what': {
                'title': 'What do you need?',
                'created': '20200316T201010Z',
                'updated': '20200316T230000Z'}
            }
        new_date_index = {
            '/2020/03/16/what': {
                'title': 'What do you need?',
                'created': '20200316T201010Z',
                'updated': '20200316T230000Z'},
            '/2020/03/20/where': {
                'title': 'Where is that?',
                'created': '20200320T010220Z',
                'updated': '20200321T030220Z'}
            }
        self.assertDictEqual(
            update_month_index(self.month_index, new_date), new_date_index)

    def test_new_entry_month_index(self):
        """Month: A new entry in the list of posts."""
        # adding a new entry to the list
        # not necessary at the end.
        new_entry = {'/2020/03/18/who': {
                     'title': 'Who is she?',
                     'created': '20200317T150000Z',
                     'updated': '20200318T150000Z'}}
        new_entry_index = {
            '/2020/03/16/what': {
                'title': 'What do you need?',
                'created': '20200316T201010Z',
                'updated': '20200316T201010Z'},
            '/2020/03/18/who': {
                'title': 'Who is she?',
                'created': '20200317T150000Z',
                'updated': '20200318T150000Z'},
            '/2020/03/20/where': {
                'title': 'Where is that?',
                'created': '20200320T010220Z',
                'updated': '20200321T030220Z'}
            }
        self.assertDictEqual(
            update_month_index(self.month_index, new_entry), new_entry_index)

    def test_extract_month_entries(self):
        """From an HTML month list to a data structure.

        We want to make it non dependent on the markup order,
        but fetchable through attributes.
        """
        self.assertDictEqual(
            extract_month_entries(self.html_list), self.month_index)

    def test_generate_month_index_template_choice(self):
        """Create the html fragment with a specific template."""
        month_posts = self.month_index
        theme = 'naya201712'
        html_posts = month_posts_html(month_posts, theme)
        self.assertEqual(html_posts, self.html_month_naya)

    def test_wrong_template_name(self):
        """A wrong template name must exit with an error message."""
        theme = 'foobar'
        with self.assertRaises(SystemExit) as sysexit:
            month_posts_html({}, theme)
        self.assertEqual(sysexit.exception.code,
                         'This {theme} theme is missing.'.format(theme=theme))
