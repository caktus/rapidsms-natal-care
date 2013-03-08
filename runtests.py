#!/usr/bin/env python
import sys

from django.conf import settings


if not settings.configured:
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        INSTALLED_APPS=(
            'rapidsms',
            'rapidsms.contrib.handlers',
            'appointments',
            'healthcare',
            'healthcare.backends.djhealth',
            'natalcare',
        ),
        HEALTHCARE_STORAGE_BACKEND='healthcare.backends.djhealth.DjangoStorage',
        SITE_ID=1,
        SECRET_KEY='this-is-just-for-tests-so-not-that-secret',
    )


from django.test.utils import get_runner


def runtests():
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True, failfast=False)
    args = sys.argv[1:] or ['natalcare', ]
    failures = test_runner.run_tests(args)
    sys.exit(failures)


if __name__ == '__main__':
    runtests()

