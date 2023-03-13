from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.functions import Coalesce
from django.shortcuts import render, redirect

from accounts.models import BaseUser
from accounts.models.organisation import Organisation
from chat.models import ChatMessages


# Permissions Views
@login_required(login_url='login_user')
def index_users(request):
    try:
        users = BaseUser.objects.all()

        context = {
            "users": users
        }
        return render(request, "chat/index_chats.html", context)
    except ObjectDoesNotExist:
        context = {
            "users": None
        }
        return render(request, "chat/index_chats.html", context)


# Permissions Views
@login_required(login_url='login_user')
def index_chats(request):
    try:
        chats = ChatMessages.objects.all()
        users = BaseUser.objects.all()

        context = {
            "chats": chats,
            "users": users
        }
        return render(request, "chat/chat_detail.html", context)
    except ObjectDoesNotExist:
        context = {
            "chat": None,
            "users": None
        }
        return render(request, "chat/chat_detail.html", context)


@login_required(login_url='login_user')
def create_chat(request):
    if request.method == "POST":
        title = request.POST["title"]
        organisation = request.POST.getlist("organisation")
        is_active = request.POST.get("is_active", False)
        description = request.POST["description"]
        chat = ChatMessages(
            title=title,
            is_active=is_active,
            description=description
        )
        chat.save()
        chat.organisation.set(organisation)
        return redirect("admin_chat")

    organisations = Organisation.objects.all()
    context = {
        "organisations": organisations
    }
    return render(request, "chat/chat_detail.html", context)


@login_required(login_url='login_user')
def chat_details(request, pk):
    user = request.user
    sender = BaseUser.objects.get(id=pk)
    users = BaseUser.objects.all()
    chats = ChatMessages.objects \
        .order_by("created_on", "msg_sender", "msg_receiver") \
        .distinct()
    chat = ChatMessages.objects.all().order_by(Coalesce("created_on", "seen").asc())
    unread = chats.filter(msg_sender=sender, msg_receiver=user, seen=False)
    unread.update(seen=True) if unread.first() and unread.first().msg_receiver == user else ...

    if request.method == "POST":
        message = request.POST["message"]
        msg_sender = user
        receiver = request.POST["receiver"]
        msg_receiver = BaseUser.objects.get(id=receiver)
        ChatMessages(
            body=message,
            msg_sender=msg_sender,
            msg_receiver=msg_receiver
        ).save()
        return redirect("chat_details", pk=pk)

    context = {
        "receiver": user,
        "sender": sender,
        "chats": chats,
        "chat": chat,
        "num": unread.count(),
        "users": users
    }
    return render(request, "chat/chat_detail.html", context)
