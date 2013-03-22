from __future__ import unicode_literals

from datetime import timedelta

from .base import NatalCareDataTestCase, now
from ..handlers.birth import BirthHandler
from ..handlers.pregnancy import PregnancyHandler


class BirthHandlerTestCase(NatalCareDataTestCase):
    "Keyword handler for adding reporting new births"

    def test_match(self):
        "Record a new birth for patient 'foo'."
        replies = BirthHandler.test('BIRTH foo')
        self.assertEqual(len(replies), 1)
        reply = replies[0]
        self.assertTrue(reply.startswith('Thank you'), reply)

    def test_match_with_date(self):
        "Record a new birth on a given date."
        tomorrow = (now() + timedelta(days=1)).strftime('%Y-%m-%d')
        replies = BirthHandler.test('BIRTH foo %s' % tomorrow)
        self.assertEqual(len(replies), 1)
        reply = replies[0]
        self.assertTrue(reply.startswith('Thank you'), reply)


class PregnancyHandlerTestCase(NatalCareDataTestCase):
    "Keyword handler for adding reporting new pregnancies"

    def test_match(self):
        "Record a new pregnancy for patient 'foo'."
        replies = PregnancyHandler.test('PREGNANCY foo')
        self.assertEqual(len(replies), 1)
        reply = replies[0]
        self.assertTrue(reply.startswith('Thank you'), reply)

    def test_match_with_date(self):
        "Record a new pregnancy on a given date."
        tomorrow = (now() + timedelta(days=1)).strftime('%Y-%m-%d')
        replies = PregnancyHandler.test('PREGNANCY foo %s' % tomorrow)
        self.assertEqual(len(replies), 1)
        reply = replies[0]
        self.assertTrue(reply.startswith('Thank you'), reply)