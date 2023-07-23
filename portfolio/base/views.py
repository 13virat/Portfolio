from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'base/index.html')
def posts(request):
    posts=[
        {
            'headline':'Laboratory Management System',
            'sub_headline':'Designed built & mantained a the lab managment system for FOI Laboratories'
        },
        {
            'headline':'Online Store - CoursePost Title',
            'sub_headline':'Online store with paypal payments intergration and guest user shopping'
        },
        {
            'headline':'Membership Website',
            'sub_headline':'Modulized guide for online courses with step by  step intructions'
        },
    ]
    context={'posts':posts}
    return render(request,'base/posts.html',context)
def post(request):
    return render(request,'base/post.html')
def profile(request):
    return render(request,'base/profile.html')
