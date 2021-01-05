#self created file

from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    removenewline=request.POST.get('removenewline','off')
    extraspace=request.POST.get('extraspace','off')
    capsall=request.POST.get('capsall','off')
    quoteall=request.POST.get('quoteall','off')
    
    analyzed=""
    tasks=[]
    puncs='''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    if removepunc == "on":
        
        for c in djtext:
            if c not in puncs:
                analyzed+=c
        djtext=analyzed
        tasks.append(' Punctuation Removal ')
    if removenewline == "on":

        analyzed=""
        for c in djtext:
            if c!='\n' and c!='\r':
                analyzed+=c

        tasks.append(' new line removal ')
        djtext=analyzed
    if extraspace =="on":
        analyzed=""
        for i in range(len(djtext)-1):
            if not (djtext[i]==' ' and djtext[i+1]==' '):
                analyzed+=djtext[i]
        analyzed+=djtext[len(djtext)-1]
        djtext=analyzed
        tasks.append(' extra space removal ')
    if capsall == "on":
        analyzed=""
        for c in djtext:
            analyzed+=c.upper()
        djtext=analyzed
        tasks.append( 'Capitalize all letters ')
    if quoteall == "on":
        analyzed=""
        for c in djtext:
            analyzed+="'"+c+"'"
        djtext=analyzed
        tasks.append( 'Quote all letters ')
    
    if len(tasks)==0:
        tasks.append( 'No changes applied ' )

    return render(request,"analyze.html",{'purpose':tasks,'analysed_text':djtext})

