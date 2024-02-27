from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponseRedirect,HttpResponse
from .logicFile.fileHandler import handle_uploaded_file
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
# Create your views here.

def summarize(text, per):
    nlp = spacy.load('en_core_web_sm')
    doc= nlp(text)
    
    tokens=[token.text for token in doc]
    word_frequencies={}
    for word in doc:
        if word.text.lower() not in list(STOP_WORDS):
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
    max_frequency=max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word]=word_frequencies[word]/max_frequency
    sentence_tokens= [sent for sent in doc.sents]
    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():                            
                    sentence_scores[sent]=word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent]+=word_frequencies[word.text.lower()]
    select_length=int(len(sentence_tokens)*per)
    summary=nlargest(select_length, sentence_scores,key=sentence_scores.get)
    final_summary=[word.text for word in summary]
    summary=''.join(final_summary)
    print("Length of summary is - ",len(summary))
    return summary

def uploadFile(request):
    if request.method == "POST":
        print("Value of request is "+str(request.POST))
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            print("Filename ",request.FILES)
            resultStr = handle_uploaded_file(request.FILES["file"])
            resultStr = resultStr.replace(r"\r\n","")
            condenseParameter = request.POST.get('condenseValue')
            summary = summarize(resultStr,float(condenseParameter))
            summaryDetails = {'summary':summary}
            return render(request,'summary.html',{'summaryDetails':summaryDetails})
            
        
    else:
        form = UploadFileForm()
    return render(request,"upload.html",{"form":form})