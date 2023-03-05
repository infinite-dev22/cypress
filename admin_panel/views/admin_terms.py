from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render

from echelon.models import Term


# Permissions Views
def index_terms(request):
    if request.user.is_authenticated and request.user.is_superuser:
        try:
            terms = Term.objects.all()

            context = {
                "terms": terms
            }
            return render(request, "admin_panel/terms/index_terms.html", context)
        except ObjectDoesNotExist:
            context = {
                "terms": None
            }
            return render(request, "admin_panel/terms/index_terms.html", context)
    return redirect('login_admin_user')


def create_term(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            name = request.POST["name"]
            starts_on = request.POST["starts_on"]
            ends_on = request.POST["ends_on"]
            is_active = request.POST.get("is_active", True)
            term = Term(
                name=name,
                starts_on=starts_on,
                ends_on=ends_on,
                is_active=is_active,
            )
            term.save()
            return redirect("admin_term")
        return render(request, "admin_panel/terms/edit_term.html")
    return redirect('login_admin_user')


def edit_term(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            name = request.POST["name"]
            starts_on = request.POST["starts_on"]
            ends_on = request.POST["ends_on"]
            is_active = request.POST.get("is_active", True)
            term = Term.objects.get(id=pk)
            term.name = name
            term.starts_on = starts_on
            term.ends_on = ends_on
            term.is_active = is_active
            term.save()
            return redirect("admin_term")

        term = Term.objects.get(id=pk)
        context = {
            "term": term,
        }
        print(term)
        return render(request, "admin_panel/terms/edit_term.html", context)
    return redirect('login_admin_user')


def delete_term(request, pk):
    if request.user.is_authenticated:
        Term.objects.get(id=pk).delete()
        return redirect('admin_term')
    return redirect('login_admin_user')
