#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import jsonify
from main.controllers.controller import route, Controller
from main.exceptions.invalid_request import InvalidRequest

__author__ = "Ivan de Paz Centeno"


class CustomController(Controller):
    """
    Controller for /detection-requests/faces/ URL
    """

    def __init__(self, flask_web_app, available_services, config):
        """
        Constructor of the Face Detection controller.
        :param flask_web_app: web app from Flask already initialized.
        :param available_services: list of services filtered to be compatible with this controller.
        :param config: config object containing all the service definitions.
        """
        Controller.__init__(self, flask_web_app, available_services, config)

        self.exposed_methods += [
            self.custom_route_example,
            self.custom_route_exception_example
        ]

        self._init_exposed_methods()

    @route("/custom-route/example", methods=['GET'])
    def custom_route_example(self):
        """
        Retrieves the services available for face detection.
        """
        return jsonify({"message":"HELLO"})


    @route("/custom-route/exception-example", methods=['GET'])
    def custom_route_exception_example(self):
        """
        Retrieves the services available for face detection.
        """
        raise InvalidRequest("Raising exception as a test", status_code=505)
