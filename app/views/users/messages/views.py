from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.utils import timezone

from app.decorators import user_is_authenticated
from app.models import Message
from app.models import User
from app.views import utils

@require_http_methods(["GET", "POST"])
@user_is_authenticated
def user_messages(request, user_id):

    current_user = utils.current_user(request)
    messages = current_user.received_messages.all()
    message = Message(message="This is a test message")

    # Create message on POST and redirect; display all messages on GET
    if request.method == "POST":
        message = Message(message=request.POST['message'],
                          creator_id=request.POST['creator_id'],
                          receiver_id=request.POST['receiver_id'],
                          created_at=timezone.now(),
                          updated_at=timezone.now())
        message.save()
        return redirect("/users/"+ str(current_user.user_id) +"/messages")
    else:
        return render(request, "users/messages/index.html", {
            'current_user': current_user,
            'receivers': User.objects.all(),
            'messages': messages,
            'message': message
        })

@require_http_methods(["GET", "DELETE"])
@user_is_authenticated
def user_message(request, user_id, message_id):

    # TODO: temporary current user
    current_user = utils.current_user(request)
    message = Message.objects.find(message_id)
    if request.method == "GET":
        return render(request, "users/messages/show.html", {
            'current_user': current_user,
            'message': message
        })  
    else:
        message.delete()
        return redirect("/users/"+ str(current_user.user_id) +"/messages")

