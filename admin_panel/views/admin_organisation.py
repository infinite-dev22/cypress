from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from accounts.models.organisation import Organisation, OrganisationProfile


# Organisation Views
def index_organisation(request):
    if request.user.is_authenticated and request.user.is_superuser:
        try:
            orgs = Organisation.objects.all()
            context = {
                "orgs": orgs
            }
            return render(request, "admin_panel/organisation/index_org.html", context)
        except ObjectDoesNotExist:
            context = {
                "orgs": None
            }
            return render(request, "admin_panel/organisation/index_org.html", context)
    else:
        return redirect('login_admin_user')


def create_organisation(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            title = request.POST["title"]
            is_active = request.POST.get("is_active", False)
            description = request.POST["description"]
            org = Organisation(
                title=title,
                is_active=is_active,
                description=description
            )
            org.save()
            org_profile = OrganisationProfile(organisation=org, is_active=is_active)
            org_profile.save()
            return redirect("admin_org")

        return render(request, "admin_panel/organisation/edit_org.html")
    else:
        return redirect('login_admin_user')


def edit_organisation(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            organisation = request.POST["organisation"]
            telephone_1 = request.POST["telephone_1"]
            telephone_2 = request.POST["telephone_2"]
            fax = request.POST["fax"]
            email = request.POST["email"]
            website = request.POST["website"]
            post_address = request.POST["post_address"]
            physical_address = request.POST["physical_address"]
            logo = request.POST["logo"]
            title = request.POST["title"]
            is_active = request.POST.get("is_active", False)
            description = request.POST["description"]
            org = Organisation.objects.get(id=pk)
            org.title = title
            org.is_active = is_active
            org.description = description
            org.save()
            org_profile = OrganisationProfile.objects.all().filter(organisation=org)
            org_profile.organisation = organisation
            org_profile.telephone_1 = telephone_1
            org_profile.telephone_2 = telephone_2
            org_profile.fax = fax
            org_profile.email = email
            org_profile.website = website
            org_profile.post_address = post_address
            org_profile.physical_address = physical_address
            org_profile.logo = logo
            org_profile.is_active = is_active
            org_profile.save()
            return redirect("admin_org")

        org = Organisation.objects.get(id=pk)
        org_profile = OrganisationProfile.objects.all().filter(organisation=org)
        context = {
            "org": org,
            "profile": org_profile
        }
        return render(request, "admin_panel/organisation/edit_org.html", context)
    else:
        return redirect('login_admin_user')


# Organisation Profile Views
def index_organisation_profile(request):
    if request.user.is_authenticated and request.user.is_superuser:
        try:
            org_profiles = OrganisationProfile.objects.all()
            context = {
                "org_profiles": org_profiles
            }
            return render(request, "admin_panel/organisation/index_org_profiles.html", context)
        except ObjectDoesNotExist:
            context = {
                "org_profiles": None
            }
            return render(request, "admin_panel/organisation/index_org_profiles.html", context)
    else:
        return redirect('login_admin_user')


def edit_organisation_profile(request, pk=None):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            organisation = request.POST["organisation"]
            telephone_1 = request.POST["telephone_1"]
            telephone_2 = request.POST["telephone_2"]
            fax = request.POST["fax"]
            email = request.POST["email"]
            website = request.POST["website"]
            post_address = request.POST["post_address"]
            physical_address = request.POST["physical_address"]
            logo = request.POST["logo"]
            is_active = request.POST.get("is_active", False)
            OrganisationProfile(
                organisation=organisation,
                telephone_1=telephone_1,
                telephone_2=telephone_2,
                fax=fax,
                email=email,
                website=website,
                post_address=post_address,
                physical_address=physical_address,
                logo=logo,
                is_active=is_active
            ).save()
            return redirect("admin_org")

        if pk is not None and request.method == "POST":
            organisation = request.POST["organisation"]
            telephone_1 = request.POST["telephone_1"]
            telephone_2 = request.POST["telephone_2"]
            fax = request.POST["fax"]
            email = request.POST["email"]
            website = request.POST["website"]
            post_address = request.POST["post_address"]
            physical_address = request.POST["physical_address"]
            logo = request.POST["logo"]
            is_active = request.POST.get("is_active", False)
            org_profile = OrganisationProfile.objects.get(id=pk)
            org_profile.organisation = organisation
            org_profile.telephone_1 = telephone_1
            org_profile.telephone_2 = telephone_2
            org_profile.fax = fax
            org_profile.email = email
            org_profile.website = website
            org_profile.post_address = post_address
            org_profile.physical_address = physical_address
            org_profile.logo = logo
            org_profile.is_active = is_active
            org_profile.save()
            return redirect("admin_org")

        return render(request, "admin_panel/organisation/edit_profile.html")
    else:
        return redirect('login_admin_user')


def delete_org(request, pk):
    if request.user.is_authenticated:
        Organisation.objects.get(id=pk).delete()
        return redirect('admin_org')
    else:
        return redirect('login_admin_user')
