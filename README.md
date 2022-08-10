Local Envoy Scraper
==================

Work-in-Progress

A python-based scraper for the local Enphase Envoy-S data endpoints.

## Goals

Take the data from Enphase Envoy system on a LAN, and feed it into a time-series database such as Prometheus or InfluxDB.

This is largely being achieved on the back of work already completed in the community:

* thecomputerperson - https://thecomputerperson.wordpress.com/2016/08/03/enphase-envoy-s-data-scraping/
* Robert Mesibov - https://www.datafix.com.au/BASHing/2019-09-06.html
* https://github.com/petercable/solar-observatory
* https://github.com/dlmcpaul/EnphaseCollector
* ... many more...

This is intended primarily to be run in a container, however could be run as a service on a RaspberyPi or other system.

## NOTE

This may not work on Envoy-S running firmware version D7 or newer. This is tested locally on an Envoy using older firmware.
