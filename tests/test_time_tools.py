#!/usr/bin/env python
"""Tests for things related to time modifications."""

import unittest

from naya.tools.time import human_period


class TestTime(unittest.TestCase):
    """Tests for time modification."""

    def setUp(self):
        """Set up tests."""
        pass

    def tearDown(self):
        """Tear down the tests."""
        pass

    def test_convert_human_scale(self):
        """Test we get the right relative time expression."""
        # Aucune mise à jour
        created = '20200316T201010Z'
        updated = '20200316T201010Z'
        self.assertEqual(human_period(created, updated), 'aucune')
        # plus d'une heure
        updated = '20200316T224210Z'
        self.assertEqual(human_period(created, updated), '2 heures après')
        # plus d'une journée
        updated = '20200318T224210Z'
        self.assertEqual(human_period(created, updated), '2 jours après')
        # plus d'une semaine
        updated = '20200418T224210Z'
        self.assertEqual(human_period(created, updated), '18 avril 2020')
