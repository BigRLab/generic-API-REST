#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, url_for, jsonify

from main.controllers.controller_factory import ControllerFactory
from main.controllers.custom.custom_controller import CustomController

__author__ = 'Iván de Paz Centeno'


app = Flask(__name__)


@app.route("/site-map")
def site_map():
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

    return jsonify(links)


config = {}
services = {}


controller_factory = ControllerFactory(app, config)
controller_factory.create_controller(CustomController)


app.run("0.0.0.0", "1050", threaded=True)

controller_factory.release_all()