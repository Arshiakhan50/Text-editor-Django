from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    
    return render(request,'index.html')

def analyze(request):
    # text input 
    text =request.GET.get('text','default')

    # check box input 
    removepunc =request.GET.get('removepunc','off')
    fullcaps =request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremove=request.GET.get('extraspaceremove','off')
    charcount=request.GET.get('charcount','off')

    # intializing the vaireable
    analyzed=""
    purpose=""

    # condition for remove puncuation
    if removepunc=="on": 
        analyzed=""
        puntuation =list('''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~''')
        purpose+= "Removepuntuation "
        for char in text:
            if char not in puntuation:
                analyzed+=char
        text = analyzed

    # condition for full caps
    if fullcaps=="on":
        analyzed=""
        purpose+="FULLCAPS "
        analyzed=text.upper()
        text=analyzed         
    
    #condition for bnew line removal
    if newlineremover=="on":
        analyzed=""
        purpose+="NewLineremoved "   
        for char in text:
            if char!="\n" and char!="\r":
                analyzed+=char
        text=analyzed 

    # condition for extra space removsl
    if extraspaceremove =="on":
        analyzed=""
        purpose+="extraspaceremoved "
        for index,char in enumerate(text):
            if text[index]==" " and text[index+1]==" ":
                analyzed+=text[index]
        text=analyzed 

    if charcount=="on":
        purpose+="charcount "
        analyzed+=f"\n\nno of char in enter text is {len(text)}"
        
    else:
        analyzed=text            

    # passing the value of variable to html file 
    # here we can use analyzed_text in html file (analyze.html) to acess analyzed
    params ={'purpose':purpose,'analyzed_text':analyzed}

    # rendering the (analyzed.html)
    # render take deafult argument "request" , file to render and distionary of variables
    return render(request, 'analyze.html' ,params)

