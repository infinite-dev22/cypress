from django.shortcuts import render, redirect


# Dashboard Views
# @user_passes_test(lambda u: u.is_superuser, login_url='login_admin_user')
def dashboard_admin(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request, "admin_panel/dashboard.html")
    else:
        return redirect('login_admin_user')
