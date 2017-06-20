# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from app.models import User, Message
from django.utils import timezone

# Create your tests here.


class MessageModelTests(TestCase):
    # Setting up 2 testcases

    def setUp(self):
        user_from = User.objects.create(email="ziyang.wang@contrastsecurity.com",
                            password="12345",
                            is_admin=True, first_name="Ziyang",
                            last_name="Wang", user_id=1,
                            created_at=timezone.now(), updated_at=timezone.now(),
                            auth_token="")
        user_to = User.objects.create(email="galen.palmer@contrastsecurity.com",
                            password="12345",
                            is_admin=True, first_name="Galen",
                            last_name="Palmer", user_id=2,
                            created_at=timezone.now(), updated_at=timezone.now(),
                            auth_token="")
        Message.objects.create(creator_id=user_from.id, receiver_id=user_to.id, message="hello", read=False,
                               created_at=timezone.now(), updated_at=timezone.now())
        Message.objects.create(creator_id=user_to.id, receiver_id=user_from.id, message="hi", read=True,
                               created_at=timezone.now(), updated_at=timezone.now())

    # Testing creator_name method
    def test_creator_name(self):
        u1 = User.objects.get(email="ziyang.wang@contrastsecurity.com")
        message_first = Message.objects.get(creator_id=u1.id)
        self.assertEqual(message_first.creator_name(), "Ziyang Wang")

        u2 = User.objects.get(email="galen.palmer@contrastsecurity.com")
        message_second = Message.objects.get(creator_id=u2.id)
        self.assertEqual(message_second.creator_name(), "Galen Palmer")

    # Testing read models
    def test_read(self):
        # Testing type, value of first message
        u1 = User.objects.get(email="ziyang.wang@contrastsecurity.com")
        u2 = User.objects.get(email="galen.palmer@contrastsecurity.com")

        message_first = Message.objects.get(creator_id=u1.id)
        self.assertEqual(message_first.creator_id, u1.id)
        self.assertEqual(message_first.receiver_id, u2.id)
        self.assertEqual(message_first.message, "hello")
        self.assertEqual(message_first.read, False)

        message_second = Message.objects.get(creator_id=u2.id)
        self.assertEqual(message_second.creator_id, u2.id)
        self.assertEqual(message_second.receiver_id, u1.id)
        self.assertEqual(message_second.message, "hi")
        self.assertEqual(message_second.read, True)

    # Testing delete models
    def test_delete(self):
        u1 = User.objects.get(email="ziyang.wang@contrastsecurity.com")
        messages = Message.objects.all()
        self.assertEqual(len(messages), 2)

        message_first = Message.objects.get(creator_id=u1.id)
        message_first.delete()
        messages = Message.objects.all()
        self.assertEqual(len(messages), 1)

        message_second = Message.objects.get(receiver_id=u1.id)
        message_second.delete()
        messages = Message.objects.all()
        self.assertEqual(len(messages), 0)
