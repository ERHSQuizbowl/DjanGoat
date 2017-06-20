# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client
from app.tests.mixins import AuthRouteTestingWithKwargs
from app.tests.mixins import Pep8ViewsTests

import app.views as views

messages = views.user_messages_views


class PasswordResetPep8Tests(TestCase, Pep8ViewsTests):

    def setUp(self):
        self.path = 'app/views/users/messages/'


# Tests checking that that '/users/:id/messages' properly handles HttpRequests and routing
# Accepts GET and POST requests and refuses all others with an error code 405 (Method not allowed)
# Tested on id #55
class UserMessagesRoutingAndHttpTests(TestCase, AuthRouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:user_messages'
        self.route = '/users/55/messages'
        self.view = messages.user_messages
        self.responses = {
            'exists': 200,
            'GET': 200,
            'POST': 200,
            'PUT': 405,
            'PATCH': 405,
            'DELETE': 405,
            'HEAD': 405,
            'OPTIONS': 405,
            'TRACE': 405
        }
        self.kwargs = {'user_id': 55}
        self.expected_response_content = '55Messages Index!'
        AuthRouteTestingWithKwargs.__init__(self)

# Tests checking that that '/users/:user_id/messages/message_id' properly handles HttpRequests and routing
# Accepts GET, PATCH, PUT, and DELETE requests and refuses all others with an error code 405 (Method not allowed)
# Tested on user_id 55 and message_id 22
class UserShowMessageRoutingAndHttpTests(TestCase, AuthRouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:user_message'
        self.route = '/users/55/messages/22'
        self.view = messages.user_message
        self.responses = {
            'exists': 200,
            'GET': 200,
            'POST': 405,
            'PUT': 200,
            'PATCH': 200,
            'DELETE': 200,
            'HEAD': 405,
            'OPTIONS': 405,
            'TRACE': 405
        }
        self.kwargs = {'user_id': 55, 'message_id': 22}
        self.expected_response_content = 'show user message5522'
        AuthRouteTestingWithKwargs.__init__(self)
