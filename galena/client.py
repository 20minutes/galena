# -*- coding: utf-8 -*-
import socket
from time import time


class Galena(object):
    def __init__(self, host="localhost", port=2003):
        self._addr = (host, port)
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.connect(self._addr)

    def send(self, metric, value, timestamp=None):
        try:
            self._sock.send("%s %g %s\n\n" % (metric, value,
                timestamp or int(time())))
        except socket.error:
            pass  # Failing silently for now
