from django.shortcuts import render, redirect, get_object_or_404
from users.models import User, Profile



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

                return redirect('business:dashboard')
            elif request.POST.get('type') == 'memer':
                name = request.POST.get('firstname') + \
                    ' '+request.POST.get('lastname')
                user.name = name
                picture = request.FILES.get('picture')
                profile.picture = picture
                profile.is_memer = True
                profile.phonenumber = request.POST.get('phonenumber')
                profile.save()
                return redirect('memer:dashboard')
            elif request.POST.get('type') == 'influencer':
                name = request.POST.get('firstname') + \
                    ' '+request.POST.get('lastname')
                user.name = name
                profile.phonenumber = request.POST.get('phonenumber')
                picture = request.FILES.get('picture')
                profile.picture = picture
                profile.is_influencer = True
                profile.save()

                return redirect('business:dashboard')
        return render(request, 'user/profile_create.html', {})
    elif request.user.profile.is_memer:
        return redirect('memer:dashboard')
    elif request.user.profile.is_influencer:
        return redirect('influencer:dashboard')
