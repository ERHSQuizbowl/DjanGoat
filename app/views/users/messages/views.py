from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from django.template.loader import get_template

from app.models import Message
from app.models import User

@require_http_methods(["GET", "POST"])
def user_messages(request, user_id):
    current_user = User(email="tests@example.com", first_name="Tester", last_name="McTestsalot")
    messages = []
    message = Message(message="This is a test message")
    return render(request, "users/messages/index.html", {
        'current_user': current_user,
        'messages': messages,
        'message': message
    })


@require_http_methods(["GET"])
def new_user_message(request, user_id):
    return HttpResponse(str(user_id) + "New Message!")


@require_http_methods(["GET", "PATCH", "PUT", "DELETE"])
def user_message(request, user_id, message_id):
    current_user = User(email="tests@example.com", first_name="Tester", last_name="McTestsalot")
    message = Message(message="This is a test message.")
    return render(request, "users/messages/show.html", {
        'current_user': current_user,
        'message': message
    })
