from __future__ import unicode_literals

from appointments.handlers.new import NewHandler


class PregnancyHandler(NewHandler):
    prefix = ''
    keyword = 'pregnancy|pre'

    def parse_message(self, text):
        "Tokenize message text."
        result = {'keyword': 'pregnancy'} # FIXME: This much match the timeline name
        tokens = text.strip().split()
        result['name'] = tokens.pop(0)
        if tokens:
            # Remaining tokens should be a date string
            result['date'] = ' '.join(tokens)
        return result