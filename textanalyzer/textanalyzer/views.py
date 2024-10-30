from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def contactus(request):
    return render(request, 'contactus.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('check1', 'off')
    fullcaps = request.POST.get('check4', 'off')
    removeline = request.POST.get('check2', 'off')
    extraspaceremover = request.POST.get('check3', 'off')
    charcount = request.POST.get('check5', 'off')

    print("Remove Punctuations --> ",removepunc)
    print("Capitalize --> ", fullcaps)
    print("Remove Newline --> ", removeline)
    print("Remove Extraspace --> ", extraspaceremover)
    print("charcount --> ", charcount)


    if removepunc == 'on':
        punctuations = '''!@#$%^&*()_-={};':"?/><,.\|`~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Puntuations', 'analyzed_text': analyzed }
        djtext = analyzed
    
    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
                analyzed = analyzed + char.upper()
        params = {'purpose': 'Capitalized Text', 'analyzed_text': analyzed}
        djtext = analyzed

    if removeline == 'on':
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed Newline', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        djtext = analyzed
    
    if charcount == 'on':
        count = 0
        for _ in djtext:
            counter = _.split()
            count = count + len(counter)
        params = {'purpose': 'Character Counter', 'analyzed_text': f"The total number of character are {count}"}

    if(removepunc != 'on' and charcount != 'on' and extraspaceremover != 'on' and removeline != 'on' and fullcaps != 'on'):
        return HttpResponse("Please select the operation and try again.")

    return render(request, 'analyze.html', params)
