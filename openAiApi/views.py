import json
from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.http import JsonResponse

from openAiApi.extract_transcipt import extract_transcript
from openAiApi.generate_completion import generate_completion
from openAiApi.prompt import SYSTEM_PROMPT_TIMESTAMP, USER_PROMPT_TIMESTAMP
from .forms import YouTubeURLForm
import youtube_dl
from youtube_transcript_api import YouTubeTranscriptApi
import requests
import openai

def Login(request):
    return render(request,'Login.html')
def index(request):
    return render(request,'index.html')
def Logout(request):
    logout(request)
    return redirect('home') 

def generate_timestamps(request):

    if request.method == 'POST':
        form = YouTubeURLForm(request.POST)
        if form.is_valid():
            youtube_url = form.cleaned_data['youtube_url']
            transcript=extract_transcript(youtube_url)
            mapOfTimeStamps = {}
            PROMPT = f"""
            {SYSTEM_PROMPT_TIMESTAMP}
            {USER_PROMPT_TIMESTAMP}
            {transcript}
            """
            timestamps =generate_completion(PROMPT)
            if timestamps:
                text = timestamps.strip()
                lines = text.split("\n")
                values_lines = [line for line in lines if ":" in line]
                try:
                    for value in values_lines:
                        # remove "" and , and ()
                            value = str(value).split(":")
                            value[1]=value[1].strip('()" ,')
                            #  convert from real number to (minutes,seconds)
                            minutes= int(value[1]) // 60
                            remaining_seconds = int(value[1]) % 60
                            value[1] = f"{minutes}.{remaining_seconds:02d}"
                            mapOfTimeStamps[value[1]]=value[0]
                except :
                        mapOfTimeStamps["error"]="No timestamps Founded"
                return render(request, 'generate_timestamps.html', {'form': form , 'timestamps':mapOfTimeStamps})
            else:
                return render(request, 'generate_timestamps.html', {'form': form , 'error_message':'No timestamps available'})
    else:
        form = YouTubeURLForm()
    return render(request, 'generate_timestamps.html', {'form': form})


