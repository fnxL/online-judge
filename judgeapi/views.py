import requests
import json
from time import time, sleep
from django.shortcuts import render, HttpResponse, Http404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from judge.models import *
 
# Create your views here.

def problem_page(request, problem_id):
    problem = Problems.objects.get(id=problem_id)
    title = problem.title
    statement = problem.problem_statement
    test_cases = problem.test_cases
    correct_output = problem.correct_output
    time_limit = problem.time_limit
    sample_input = problem.input_data
    sample_output = problem.output_data
    
    cont = {
        'title': title,
        'statement': statement,
        'sample_input': sample_input,
        'sample_output': sample_output,
        'timelimit': time_limit,
    }  
    if request.method == 'POST':
        if request.user.is_authenticated:
            language = request.POST.get('language')
            sourcecode = request.POST.get('sourcecode')
            status_code, data = execute(sourcecode,language,test_cases,time_limit)
            if status_code == 400:
                #Compile Error occured
                build_err = data
                messages.success(request, build_err)

            elif status_code == 300:
                msg = "Time Limit Exceeded"
                messages.success(request, msg)
                obj = Submissions.objects.create(user=request.user, problemid=problem_id,sourcecode=sourcecode,verdict="TLE")


            elif status_code == 200:
                # Compare with correct_output & give verdict
                # messages.success(request, data)
                # print(status_code,data)
                out = data.rstrip()
                #print(repr(out))
                
                correct_output = correct_output.replace('\r','')
                #print(repr(correct_output))
                if correct_output == out:
                    msg = "Accepted"
                    messages.success(request, msg)
                    obj = Submissions.objects.create(user=request.user, problemid=problem_id,sourcecode=sourcecode,verdict="AC")
                    #Mark this Problem as Solved for this user.
                    obj2 = Data.objects.create(user=request.user, problemid=problem_id,status=True)
                    
                else:
                    #WA --> Submission History
                    msg = "Wrong Answer"
                    messages.success(request,msg)
                    obj = Submissions.objects.create(user=request.user, problemid=problem_id,sourcecode=sourcecode,verdict="WA")
 
        else:
            return redirect('login')
   
     
    return render(request, "pages/problempage.html", context=cont, status=200)


# Only works for problem statement which contains first line as number of test cases.
# Assume this as our own compiler
#Status Code, Data
def execute(sourcecode,language,test_cases, time_limit):
    index = int(language)
    lang = ['c','cpp','java','python3','javascript']
    create_session = "http://api.paiza.io/runners/create"
    """
    Parameters:
    sourcecode --> string
    language --> string
    input --> string
    longpoll --> false
    longpoll_timeout --> time_limit
    api_key --> guest
    """
    get_details = "http://api.paiza.io/runners/get_details"
    """
    Parameters:
    id --> ID Generated by create_session request.
    """
    source = sourcecode.replace('\r','')
    testcases = test_cases.replace('\r','')
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
    }
    

    data = {
        'source_code': source,
        'language': lang[index],
        'input': test_cases,
        'longpoll': False,
        'longpoll_timeout': time_limit,
        'api_key': 'guest' 
    }
    response = requests.post(create_session, params=data)
    response = json.loads(response.text)
    session_id = response['id']

    status_data = {
        'id': session_id,
        'api_key': 'guest'
    }
    sleep(3)
    resp = requests.get(get_details, params=status_data)
    session_response = json.loads(resp.text)
    code_status = session_response['status']

    print(json.dumps(session_response, indent=3))  
    status_code = 0
    if code_status == "completed":
        # Handle Compile errors first
        if session_response['result'] == "failure":
            # Compile Errors/Build Errors
            if index == 3:
                build_err = session_response['stderr']
            else:
                build_err = session_response['build_stderr']
        
            status_code = 400
            return status_code, build_err

        
        elif session_response['result'] == "timeout":
          
            time = session_response['time']
            res = "timeout"
            
            status_code = 300
            return status_code, res

  
        elif session_response['result'] == "success":
            code_output = session_response['stdout']
            status_code = 200
            print("OK")
            return status_code, code_output



         
    
     



    
 
     
