# -*- coding: utf-8 -*-
"""ATH.ENA-reporting App settings.
"""


WSGI_OPTS = {
    'server': 'gunicorn',
    'reloader': True,
    'port': 5000,
    'host': '0.0.0.0',
}

DEBUG = True
