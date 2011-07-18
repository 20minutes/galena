Galena
======

Galena is a simple client for graphite/carbon [Graphite](http://graphite.wikidot.com).

To install it :

    pip install galena

To use it :

    from galena import Galena
    galena = Galena(host="localhost", port=2003)
    galena.send("tiger.flu", 12)

To suggest a feature or report a bug :
https://github.com/20minutes/galena/issues
