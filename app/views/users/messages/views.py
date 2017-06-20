from __future__ import unicode_literals

from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from django.utils import timezone

from app.decorators import user_is_authenticated
from app.models import Message
from app.models import User
from app.views import utils


@require_http_methods(["GET", "POST"])
@user_is_authenticated
def user_messages(request, _user_id):

    current_user = utils.current_user(request)

    # Create message on POST and redirect; display all messages on GET
    if request.method == "POST":

        # Create a new message from the sender (should be current user) to the selected receiver
        message = Message(message=request.POST['message'],
                          creator_id=request.POST['creator_id'],
                          receiver_id=request.POST['receiver_id'],
                          created_at=timezone.now(),
                          updated_at=timezone.now())
        message.save()
        return redirect("/users/" + str(current_user.id) + "/messages")
    else:

        # On a GET simply return a list of the current user's received messages
        messages = current_user.received_messages.all()
        return render(request, "users/messages/index.html", {
            'current_user': current_user,
            'receivers': User.objects.all(),
            'messages': messages
        })


@require_http_methods(["GET", "DELETE"])
@user_is_authenticated
def user_message(request, _user_id, message_id):

    current_user = utils.current_user(request)
    message = Message.objects.find(message_id)
    if request.method == "GET":

        # On a GET show the message
        return render(request, "users/messages/show.html", {
            'current_user': current_user,
            'message': message
        })  
    else:

        # On a DELETE delete the message and redirect back to the list page
        message.delete()
        return redirect("/users/" + str(current_user.id) + "/messages")
