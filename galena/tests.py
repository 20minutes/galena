# -*- coding: utf-8 -*-
import unittest
from mock import patch, Mock

from galena import Galena


class TestGalena(unittest.TestCase):
    @patch('socket.socket')
    def test_send_metric(self, mock):
        socket = Mock()
        mock.return_value = socket
        galena = Galena()
        galena.send("tiger.flu", 1, 1311003170)
        self.assertTrue(mock.called)
        self.assertEquals(socket.method_calls[0], (
            'connect', (('localhost', 2003),), {}
        ))
        self.assertEquals(socket.method_calls[1], (
            'send', ('tiger.flu 1 1311003170',), {}
        ))

if __name__ == '__main__':
    unittest.main()
