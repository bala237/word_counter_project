from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request, 'home.html')

def result(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddic = {}
    for word in wordlist:
        if word in worddic:
            worddic[word] += 1
        else:
            worddic[word] = 1
    maxword = max(worddic, key= worddic.get)
    return render(request, 'result.html', {'fulltext': fulltext, 'count':len(wordlist), 'worddic':sorted(worddic.items(), key=operator.itemgetter(1), reverse=True), 'maxword':maxword })