from __future__ import unicode_literals

from appointments.tests.base import AppointmentDataTestCase, now


class NatalCareDataTestCase(AppointmentDataTestCase):
    "Base class for creating necessary test data."

    def setUp(self):
        super(NatalCareDataTestCase, self).setUp()
        # FIXME: These keywords need to match the handlers
        self.births = self.create_timeline(name='Birth', slug='birth')
        self.pregnancies = self.create_timeline(name='Pregnancy', slug='pregnancy')
        # TODO: Create default milestones for these timelines