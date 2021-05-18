#!/usr/bin/env python
#
# File                  : main.py
# Date                  : 05/17/2021
# Description           : main (driver) application for madlib
#                         application
#
# Requires              : python 3.x
#                         flask
#                         requests
#
#
# Remarks               : demo code only (no production)
#
from api import init_api

DEFAULT_PORT = 9000
DEFAULT_HOST="127.0.0.1"
LOWEST_PORT_NUMBER = 2000
def get_valid_port(port_nr):
    """
    Check the validity of a port number given, if it is valid, return the port number in integer
    Port is valid if it is positive number greater than 2000 (port number 2000 usually is reserved for super user processes).
    if invalid, Here we can either throw an exception or 'silently' reset the port number into valid number (e.g. 9000), but
    I prefer the first option because it is explicit

    :param port_nr: port number
    :return: port number
    :exception: ValueError exception is thrown if the port_nr is the integer value less than 2000
    """
    if port_nr <= LOWEST_PORT_NUMBER:
        raise ValueError("Port number given '{}' is less than {}".format(port_nr, LOWEST_PORT_NUMBER))
    return port_nr

def run(host=DEFAULT_HOST, port=DEFAULT_PORT, verbose=False):
    """
    the main driver for the application.
    It initializes everything (Flask, etc.)

    :param host: the IP Address to listen the incoming socket
    :param port: the port number
    :param verbose: print out debugging message or not
    :return:
    """
    init_api(host=host, port = port, debug=verbose)

if __name__ == "__main__":
    import argparse

    PORT = DEFAULT_PORT
    HOST = DEFAULT_HOST
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default = DEFAULT_PORT,
                        help="port on which the service is listening for incoming (REST API) request, default ({})"
                        .format(DEFAULT_PORT))
    parser.add_argument("-i", "--ip", type=str, default = DEFAULT_HOST,
                        help="IP Address on which the service is listening for incoming (REST API) request, default ({})"
                        .format(DEFAULT_HOST))
    parser.add_argument("-v", "--verbose", default = False, action='store_true',
                        help="print all incoming (REST API) request and outgoing response")
    args = parser.parse_args()
    if args.port:
        try:
            PORT = get_valid_port(args.port)
        except ValueError as err:
            print(err)
            exit(-1)
    if args.ip:
        HOST = args.ip
    run(HOST, PORT, args.verbose)