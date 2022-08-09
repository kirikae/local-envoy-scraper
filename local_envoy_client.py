import os
import requests
import json
import argparse
import logging

from getpass import getpass

logging.basicConfig(format='%(ascitime)s %(levelname)s %(message)s', level=logging.INFO)

##########################
# Parse Arguments
# ------------------------

class Auth:
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

    def get_args(self):
        parser = argparse.ArgumentParser(description='Provide username and password for authenticated endpoints.')
        parser.add_argument('-u', '--username', actions='store_true', default=os.environ.get("ENVOY_USERNAME"), const='envoy', help='Envoy Username, defaults to \'envoy\'')
        parser.add_argument('-p', '--password', actions='store_true', default=os.environ.get("ENVOY_PASSWORD"), help='Envoy password, defaults to last 6-digits of the serial number')
