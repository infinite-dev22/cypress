from django.shortcuts import render, redirect

from chat.models import ChatMessages


# Dashboard Views
# @user_passes_test(lambda u: u.is_superuser, login_url='login_admin_user')
def dashboard_admin(request):
    if request.user.is_authenticated and request.user.is_superuser:
        chats = ChatMessages.objects.all()
        unread = chats.filter(seen=False)
        context = {
            "chats": unread,
            "new_chats": unread.count()
        }
        return render(request, "admin_panel/dashboard.html", context)
    else:
        return redirect('login_admin_user')
