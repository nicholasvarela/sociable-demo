from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import handleSearchForm
from .twitterAPIRunner import getTweetsByUserName, getTrendTopics
# Create your views here.

def homeWithHandle(request, handle):
    
    Tweet.objects.all().delete()
    
   
    handle1 = handle.replace("?fname=" , "")

    if request.method == "POST":
        form = handleSearchForm(request.POST)
        if form.is_valid():
            form.save()
        tempObject = Handle.objects.last()
        handle1 = tempObject.at

    tweetResponse = getTweetsByUserName(handle1) 

    for i in tweetResponse:
        newTweet = Tweet(text = i[0], score = i[1])
        #print(i[1])
        newTweet.save()

    
    tweet = Tweet.objects.all()
    form = handleSearchForm()

    tweet = Tweet.objects.all()
    form = handleSearchForm()
    average = -1
    count = 0
    for i in tweet: 
        count +=1
        total += i.score
    total = total / count

    passData= {'tweets' : tweet, "handle": handle, "form": form, 'average': total, 'count': count}
    return render(request, 'tweets/home.html', passData)

def home(request):
    handle = 'nytimes'
    Tweet.objects.all().delete()

    if request.method == "POST":
        handle = ''
        form = handleSearchForm(request.POST)
        if form.is_valid():
            form.save()
        tempObject = Handle.objects.last()
        handle = tempObject.at

        
    tweetResponse = getTweetsByUserName(handle)
    if tweetResponse == "throwError":
        return redirect('pages/error')


    for i in tweetResponse:
        newTweet = Tweet(text = i[0], score = i[1])
        #print(i[1])
        newTweet.save()
        
    tweet = Tweet.objects.all()
    form = handleSearchForm()
    average = -1
    count = 0
    for i in tweet: 
        count +=1
        average += i.score
    trends = getTrendTopics()
    passData= {'tweets' : tweet, "handle": handle, "form": form, 'average': average/count, 'count': count, 'trends': trends}
    return render(request, 'tweets/home.html', passData)

def about(request):
    form = handleSearchForm()
    
    passData = {'form' : form}
    return render(request,'tweets/about.html',passData)

def error(request):
    form = handleSearchForm()
    
    passData = {'form' : form}
    return render(request,'tweets/error.html',passData)

