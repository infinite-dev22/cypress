from django.shortcuts import render, redirect

from accounts.models.organisation import Organisation


def index_organisation(request):
    # TODO document why this method is empty
    pass


def edit_organisation(request, pk=None):
    if request.method == "POST":
        title = request.POST["title"]
        org_type = request.POST["org_type"]
        is_active = request.POST.get("is_active", False)
        description = request.POST["description"]
        org = Organisation(title, is_active, description)
        org.organisation_type.set(org_type)
        org.save()
        return redirect("admin_org")

    if pk is not None and request.method == "POST":
        title = request.POST["title"]
        org_type = request.POST["org_type"]
        is_active = request.POST.get("is_active", False)
        description = request.POST["description"]
        org = Organisation.objects.get(id=pk)
        org.title = title
        org.organisation_type.set(org_type)
        org.is_active = is_active
        org.description = description
        org.save()
        return redirect("admin_org")
    elif pk is not None and request.method != "POST":
        org_type = Organisation.objects.get(id=pk)
        context = {
            "type": org_type
        }
        return render(request, "", context)
    else:
        return render(request, "accounts/admin/edit_org.html")


def show_organisation(request):
    # TODO document why this method is empty
    pass


def delete_organisation(request):
    # TODO document why this method is empty
    pass
