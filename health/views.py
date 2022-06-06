from ast import Return
from asyncio.windows_events import NULL
from cgitb import text
from email.mime import message
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .utilis import get_intent,symptoms
from healthApp.randgenerator import rand
from .models import Usersymptoms,symptoms as Symptoms

# Create your views here.
def chat_bot(request):
    return render(request,'chat-bot.html')

def home(request):
    content={"name":"devu","symptoms":symptoms}
    return render(request, 'home.html',content)
    #return HttpResponse('<h1>hello</h1>')

def get_response(request,intent,session):
    response=''
    print(intent)
    try:
        user_symptoms = Usersymptoms.objects.get(check_up_id=session["checkup_ID"])
    except Usersymptoms.DoesNotExist:
        user_symptoms = Usersymptoms(user=request.user,check_up_id=rand(6))
        user_symptoms.save()
    if intent == "greeting":
        response = 'Hey {}, what symptoms do you have? please enter one of your symptoms.(Ex. headache, vomiting etc.)'.format(request.user.first_name)
    elif intent == "ask_symptoms":
        try:
            main_symp=Symptoms.objects.get(symptom_name=session["message"])
            user_symptoms.my_symptoms.add(main_symp)
        except Symptoms.DoesNotExist:
            response='Please Enter correct Symptoms!'
            return response,session["checkup_ID"]
        response = "Enter one more symptom beside {}. (Enter 'No' if not)".format(session["message"])
    elif intent == "ask_symptoms-no":
        response = ""
    elif intent == "end-chat":
        response = ''
    else:
        response='Invalid Message!'
    return response,user_symptoms.check_up_id


@csrf_exempt
def predict(request):
    text = json.loads(request.body)
    msg = text["message"]
    intent=get_intent(msg)
    res,checkupid=get_response(request,intent,text)
    message={"reply":res,"checkup_ID":checkupid}
    return HttpResponse(json.dumps(message), content_type='application/json')

