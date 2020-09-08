from django.shortcuts import render
from business.models import Campaign
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from uuid import uuid4
from django.http import JsonResponse




@login_required()
def dashboard(request):
    campaigns = Campaign.objects.filter(business=request.user)
    context = {
        'campaigns': campaigns,
    }
    return render(request, 'business/dashboard.html', context)


@login_required()
def campaign_create(request):
    if request.method == 'POST':
        name = request.POST.get('campaign')
        business = request.user
        fb_buget = request.POST.get('fb_budget')
        insta_budget = request.POST.get('insta_budget')
        twitter_budget = request.POST.get('twitter_budget')
        package = request.POST.get('package')
        Campaign.objects.create(
            name=name,
            business=business,
            #total_budget=total_budget,
            fb_buget=fb_buget,
            insta_budget=insta_budget,
            twitter_budget=twitter_budget,
            #estimated_reach=estimated_reach,
            package=package
        )
        return redirect('business:dashboard')

    return render(request, 'business/campaign_create.html', {})


@login_required()
def campaign_detail(request, id):
    return render(request, 'business/campaign_detail.html', {})

@login_required()
def campaign_list(request):
    campaign = Campaign.objects.filter(business=request.user)
    context = {
        'campaigns':campaign
    }
    return render(request, 'business/campaign_list.html', context)

def fullfill(request):
    rand_token = uuid4()
    return JsonResponse(rand_token)