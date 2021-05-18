#
# File                  : api.py
# Date                  : 02/05/2020
# Description           : main REST API for madlib
#
#
#
# Requires              : python 3.x
#                         flask
#                         requests
#
#
# Remarks               : demo code only (no production)
#

from flask import Flask, jsonify, make_response, Response
import requests

GLITCH_URL="https://reminiscent-steady-albertosaurus.glitch.me/"
GLITCH_URL_ADJ=GLITCH_URL + "/adjective"
GLITCH_URL_VERB=GLITCH_URL + "/verb"
GLITCH_URL_NOUN=GLITCH_URL + "/noun"
VERBOSE=False
app = Flask(__name__)

def vprint(msg):
    """
    :param msg: the string to be printed if VERBOSE is True
    """
    if VERBOSE:
        print(msg)

def get_glitch_data(url):
    """
    Sending get request for glitch URL and saving the response as string without quote "

    :param url: the URL of the glitch website
    :return: Tuple of (data, msg)
        data contains the string from the URL invocation if the call of requests is ok (no exceptions), otherwise None
        msg is empty string if the call of requests is ok, otherwise contains error message
    """
    r = requests.get(url, timeout=5)
    data = None
    msg = ""
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        msg = f"Http Error: {errh}"
        vprint(msg)
    except requests.exceptions.ConnectionError as errc:
        msg = f"Connection Error: {errc}"
        vprint(msg)
    except requests.exceptions.Timeout as errt:
        msg = f"Timeout Error: {errt}"
        vprint(msg)
    except requests.exceptions.RequestException as err:
        msg = f"Something Else Error: {err}"
        vprint(msg)
    else:
        data = r.text.replace('"', '')    
    return (data, msg)

@app.route('/madlib', methods=['GET'])
def madlib():
    """
    The REST API to madlib

    :return: string with the templated 'It was a {adjective} day. I went downstairs to see if I could {verb} dinner. I asked, "Does the stew need fresh {noun}?"'
    """
    # sending get request for adjective and saving the response as response object
    adjective, msg = get_glitch_data(url = GLITCH_URL_ADJ)
    if adjective is None:
        templ = f"Getting data from {GLITCH_URL_ADJ} received error with message {msg}"
        return templ
    verb, msg  = get_glitch_data(url = GLITCH_URL_VERB)
    if verb is None:
        templ = f"Getting data from {GLITCH_URL_VERB} received error with message {msg}"
        return templ 
    noun, msg = get_glitch_data(url = GLITCH_URL_NOUN)
    if noun is None:
        templ = f"Getting data from {GLITCH_URL_NOUN} received error with message {msg}"
        return templ

    templ = f'It was a {adjective} day. I went downstairs to see if I could {verb} dinner. I asked, "Does the stew need fresh {noun}?"'
    vprint(f"\nREST API /madlib returns: {templ}")
    return templ

def init_api(host, port, debug=False):
    """
    Start the Flask API process

    :param host: host (IP Address) where Flask is listening for the API request calls
    :param port: the port number where Flask is listening for the API request calls
    :param debug: print the output or not when a request is coming
    :return: None
    """
    global VERBOSE
    if debug:
        VERBOSE = True
    app.run(host=host, port=port, debug=debug)


