# -*- coding: utf-8 -*-
try:
    from django.conf import settings
except ImportError:
    settings = None

from client import Galena

__all__ = ['Galena', 'galena']

if settings:
    try:
        host = getattr(settings, 'GRAPHITE_HOST', 'localhost')
        port = getattr(settings, 'GRAPHITE_PORT', 2003)
        galena = Galena(host, port)
    except ImportError:
        galena = None
