from django.shortcuts import render
import requests as Requests   #Renamed to prevent usage confusions between request and requests

def translate(request, the_text):
    '''Handles interaction with Google Translates'''
    
    #request preparation
    headers = {  
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'AndroidTranslate/5.3.0.RC02.#################### 5.1 phone TRANSLATE_OPM5_TEST_1',
    }

    params = {
        'client' : 'at',
        'dt' : ['t', 'ld', 'qca', 'rm', 'bd'],
        'dj' : '1',
        'hl' : '%s',
        'ie' : 'UTF-8',
        'oe' : 'UTF-8',
        'inputm' : '2',
        'otf' : '2',
        'iid' : '##################################'
    }

    payload = {
        'sl' : 'en',    #source language
        'tl' : 'es',    #target language
        'q'  : the_text 
    }
        
    response = Requests.post('https://translate.google.com/translate_a/single', headers = headers, params = params, data = payload) 

    status_code = response.status_code
    if status_code == 200:
        error_msg = ''
        dictio = response.json()
        translated_text = dictio['sentences'][0]['trans']
    else:
        error_msg = 'Google Translate service failure (status code: ' + str(status_code) + ')'
        translated_text = '' 

    return(translated_text, error_msg)


def home(request):
    the_text = request.POST.get('the_text', None)

    #Further validation is possible here if required for specific cases.
    if the_text is None or the_text == '':
        translated_text = ''
        error_msg = ''

    elif the_text is not None:
        translated_text, error_msg = translate(request, the_text)

    return render(request, 'translator/home.html', { 
                'the_text'   : the_text,  
                'translated_text' : translated_text,
                'error_msg'  : error_msg
            })



