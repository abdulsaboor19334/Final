'''from django.shortcuts import render, get_object_or_404, redirect
from users.models import User, Profile
from business.models import Campaign


def test_view(request):
    if request.method == 'POST':
        name = request.POST.get('campaign')
        business = request.user
        total_budget = request.POST.get('budget')
        fb_buget = request.POST.get('fb_budget')
        insta_budget = request.POST.get('insta_budget')
        twitter_budget = request.POST.get('twitter_budget')
        estimated_reach = request.POST.get('reach')
        package = request.POST.get('package')
        Campaign.objects.create(
            name=name,
            business=business,
            total_budget=total_budget,
            fb_buget=fb_buget,
            insta_budget=insta_budget,
            twitter_budget=twitter_budget,
            estimated_reach=estimated_reach,
            package=package
        )
        return redirect('influencer:campaign-list')
    return render(request, 'business/campaign_create.html', {})


def campaign_list(request):
    return render(request, 'business/campaign_list.html', {})


def profile_create(request):
    if not request.user.profile.is_business and not request.user.profile.is_memer and not request.user.profile.is_influencer:
        if request.method == 'POST':
            user = get_object_or_404(User, id=request.user.id)
            profile = get_object_or_404(Profile, user=request.user)
            if request.POST.get('type') == 'business':
                name = request.POST.get('firstname') + \
                    ' '+request.POST.get('lastname')
                user.name = name
                picture = request.FILES.get('picture')
                profile.phonenumber = request.POST.get('phonenumber')
                profile.picture = picture
                profile.is_business = True
                profile.save()

                # return redirect('influencer:business-dashboard')
            elif request.POST.get('type') == 'memer':
                name = request.POST.get('firstname') + \
                    ' '+request.POST.get('lastname')
                user.name = name
                picture = request.FILES.get('picture')
                profile.picture = picture
                profile.is_memer = True
                profile.phonenumber = request.POST.get('phonenumber')
                profile.save()
                return redirect('influencer:memer-dashboard')
            elif request.POST.get('type') == 'influencer':
                name = request.POST.get('firstname') + \
                    ' '+request.POST.get('lastname')
                user.name = name
                profile.phonenumber = request.POST.get('phonenumber')
                picture = request.FILES.get('picture')
                profile.picture = picture
                profile.is_influencer = True
                profile.save()

                return redirect('influencer:influencer-dashboard')
        return render(request, 'user/profile_create.html', {})

    # elif request.user.profile.is_business:
        # return redirect('influencer:business-dashboard')
    elif request.user.profile.is_memer:
        return redirect('influencer:influencer-dashboard')
    elif request.user.profile.is_influencer:
        return redirect('influencer:memer-dashboard')


def influencers_assignment(request):
    campaign = Campaign.objects.filter(is_active=True)
    context = {
        'campaign': campaign
    }
    return render(request, 'influencer/assignment_list.html', context)


def campaign_detail(request, id):
    campaign = get_object_or_404(Campaign, id=id)
    context = {
        'campaign' : campaign
    }
    return render(request, 'business/campaign_detail.html', context)


def memer_assignment(request):
    campaign = Campaign.objects.filter(is_active=True)
    context = {
        'campaign': campaign
    }
    return render(request, 'memer/list.html', context)


def memer_detail(request):
    return render(request, 'memer/detail.html', {})


def memer_dashboard(request):
    return render(request, 'memer/dashboard.html', {})


def influencer_dashboard(request):
    return render(request, 'influencer/dashboard.html', {})


def login_view(request):
    return render(request, 'user/login.html', {})


def register_view(request):
    return render(request, 'user/register.html', {})


def home(request):
    return render(request,'home.html')
'''
from users.models import User, Profile
from business.models import Campaign

from django.contrib.auth.decorators import login_required

from django.shortcuts import render


@login_required()
def profile(request):
    return render(request, 'influencer/profile.html', {})


@login_required()
def task_list(request):
    return render(request, 'influencer/assignment_list.html', {})


@login_required()
def dashboard(request):
    return render(request, 'influencer/dashboard.html', {})
