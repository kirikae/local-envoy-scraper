#!/usr/bin/env python

import os
import time
import requests
import json
import argparse
import logging

from getpass import getpass

logging.basicConfig(format='%(ascitime)s %(levelname)s %(message)s', level=logging.INFO)

auth = HTTPDigestAuth(user, password)

solar_arrays = arrays(array_name, panel_serials)

# Different endpoints with potential info on the system
system = "/home.json"
inventory = "/inventory.json?deleted=1"
production = "/production.json?details=1"
controller = "/info.xml"
wifi_info = "/admin/lib/wireless_display.json?site_info=0"
wan_info = "/admin/lib/network_display.json"
meter_stream = "/stream/meter"
device_meters = "/ivp/meters"
power_meters = "/ivp/meters/readings"
production = "/api/v1/production"
inverter_production = "/api/v1/production/inverters"

stream_gauges = {
    'p': Gauge('meter_active_power_watts', 'Active Power', ['type', 'phase']),
    'q': Gauge('meter_reactive_power_watts', 'Reactive Power', ['type', 'phase']),
    's': Gauge('meter_apparent_power_watts', 'Apparent Power', ['type', 'phase']),
    'v': Gauge('meter_voltage_volts', 'Voltage', ['type', 'phase']),
    'i': Gauge('meter_current_amps', 'Current', ['type', 'phase']),
    'f': Gauge('meter_frequency_hertz', 'Frequency', ['type', 'phase']),
    'pf': Gauge('meter_power_factor_ratio', 'Power Factor', ['type', 'phase']),
}

production_gauges = {
    'activeCount': Gauge('production_active_count', 'Active Count', ['type']),
    'wNow': Gauge('power_now_watts', 'Active Count', ['type']),
    'whToday': Gauge('production_today_watthours', 'Total production today', ['type']),
    'whLastSevenDays': Gauge('production_7days_watthours', 'Total production last seven days', ['type']),
    'whLifetime': Gauge('production_lifetime_watthours', 'Total production lifetime', ['type']),
}

consumption_gauges = {
    'wNow': Gauge('consumption_now_watts', 'Active Count', ['type']),
    'whToday': Gauge('consumption_today_watthours', 'Total consumption today', ['type']),
    'whLastSevenDays': Gauge('consumption_7days_watthours', 'Total consumption last seven days', ['type']),
    'whLifetime': Gauge('consumption_lifetime_watthours', 'Total consumption lifetime', ['type']),
}

inverter_gauges = {
    'last': Gauge('inverter_last_report_watts', 'Last reported watts', ['serial', 'location']),
    'max': Gauge('inverter_max_report_watts', 'Max reported watts', ['serial', 'location']),
}

class Options:
    """
    Define any auth options that may be required
    For local access to the Envoy system a simple
    Username and Password is required.
    By default this is:
    username = envoy
    password = <last 6 digits of the Envoy serial number
    """

    def __init__(self):
        self.username = args.username
        self.password = args.password

    def get_opts(self):
        parser = argparse.ArgumentParser(description='Provide username and password for authenticated endpoints.')
        parser.add_argument('-u', '--username', actions='store_true', default=os.environ.get("ENVOY_USERNAME"), const='envoy', help='Envoy Username, defaults to \'envoy\'')
        parser.add_argument('-p', '--password', actions='store_true', default=os.environ.get("ENVOY_PASSWORD"), help='Envoy password, defaults to last 6-digits of the serial number')
