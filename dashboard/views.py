from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from chat.models import ChatMessages


# Create your views here.
@login_required(login_url='login_user')
def dashboard(request):
    chats = ChatMessages.objects.all()
    unread = chats.filter(seen=False)
    context = {
        "chats": unread,
        "new_chats": unread.count()
    }
    return render(request, "dashboard/dashboard.html", context)
