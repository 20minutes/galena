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

Copyright and license
---------------------

Copyright 2012 20 Minutes

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this work except in compliance with the License. You may obtain a copy of the License in the LICENSE file, or at:

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.