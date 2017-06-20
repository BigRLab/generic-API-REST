#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, url_for, jsonify

from main.controllers.controller_factory import ControllerFactory
from main.controllers.custom.custom_controller import CustomController

__author__ = 'Iván de Paz Centeno'


app = Flask(__name__)

def get_site_map():
    links = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        try:
            if "GET" in rule.methods:
                url = url_for(rule.endpoint, **(rule.defaults or {}))
                links.append((url, [m for m in rule.methods]))
        except:
            pass
            # links is now a list of url, endpoint tuples

    return links

@app.route("/site-map")
def site_map():
    return jsonify(get_site_map())


# Custom configuration values (anything). They are accessible from the controller side.
config = {}

controller_factory = ControllerFactory(app, config)

# Services to inject to the controller. They are accessible from the controller side.
services = {}
controller_factory.create_controller(CustomController, services)

print("Visit http://localhost:1050/site-map for a list of endpoints.")

app.run("0.0.0.0", "1050", threaded=True)

controller_factory.release_all()