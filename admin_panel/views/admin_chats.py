from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from accounts.models import BaseUser
from accounts.models.organisation import Organisation
from chat.models import ChatMessages


# Permissions Views
def index_users(request):
    if request.user.is_authenticated and request.user.is_superuser:
        try:
            users = BaseUser.objects.all()

            context = {
                "users": users
            }
            return render(request, "admin_panel/chats/index_chats.html", context)
        except ObjectDoesNotExist:
            context = {
                "users": None
            }
            return render(request, "admin_panel/chats/index_chats.html", context)
    return redirect('login_admin_user')


# Permissions Views
def index_chats(request):
    if request.user.is_authenticated and request.user.is_superuser:
        try:
            chats = ChatMessages.objects.all()
            users = BaseUser.objects.all()

            context = {
                "chats": chats,
                "users": users
            }
            return render(request, "admin_panel/chats/index_chats.html", context)
        except ObjectDoesNotExist:
            context = {
                "chat": None,
                "users": None
            }
            return render(request, "admin_panel/chats/index_chats.html", context)
    return redirect('login_admin_user')


def create_chat(request):
    if request.user.is_authenticated and request.user.is_superuser:
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
        return render(request, "admin_panel/chats/edit_chat.html", context)
    return redirect('login_admin_user')
