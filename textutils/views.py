from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

def modify(request):
  """ returns the text by modifying data """
  text = request.POST.get("data")
  arr = [
    request.POST.get('rmpunc','off'),
    request.POST.get('rmnewline', 'off'),
    request.POST.get('toupper', 'off'),
    request.POST.get('tolower', 'off'),
    request.POST.get('totitle', 'off'),
    request.POST.get('rmwhspace', 'off')
    ]
  if arr[0] == 'on':
    text = rmpunc(text)
  if arr[1] == 'on':
    text = rmnewline(text)
  if arr[2] == 'on':
    text = toupper(text)
  if arr[3] == 'on':
    text = tolower(text)
  if arr[4] == 'on':
    text = totitle(text)
  if arr[5] == 'on':
    text = rmwhspace(text)
  
  context = {'text':text}
  if 'on' not in arr:
    context['message'] = 'No option is choosed'
    context['type'] = 'Error'
    return HttpResponseRedirect(request, 'main/index.html',context)
  return render(request, 'main/mod.html',context)


def index(request,isinit=True,isCont=False):
  """ server the home page """
  
  if isCont is False:
    context = {
      'problem':False
    }
  return render(request, 'main/index.html', context)

def rmpunc(data):
  """ removes punctuation marks """
  text = ""
  punc = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
  for letter in data:
    if letter not in punc:
      text += letter
  return text
  
def rmnewline(data):
  """ removes new lines """
  text = data.replace("\n","")
  return text
  
def toupper(data):
  """ converts text to uppercase """
  text = data.upper()
  return text
  
def tolower(data):
  """ converts text to lowercase """
  text = data.lower()
  return text
  
def totitle(data):
  """ make every character of word capital """
  return data.title()
  
def rmwhspace(data):
  """ removes white spaces from text """
  text = data
  while True:
    temp = text
    text = text.replace("  "," ")
    if temp is text:
      break
  return text