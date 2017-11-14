from django.http import HttpResponse
from django.shortcuts import render

# Return a "view" to the user when sending a request
def home(request):
    return render(request, 'home.html')

def translate(request):
    original = request.GET['original_text'].lower()

    words = original.split(" ") # split by spaces
    new_words = "" # empty array for translations
    for word in words:
        temp = ""
        if word[0] in ["a", "e", "i", "o", "u"]:
            # vowel
            temp += "way "
        else:
            # consonant
            temp = word[1:] + word[0] + "ay "
        new_words += temp

    return render(request, 'translate.html',
    {
        'original':original,
        'translation':new_words
    })

def about(request):
    return render(request, 'about.html')
