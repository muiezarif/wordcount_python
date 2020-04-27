# from django.http import HttpResponse
import operator

from django.shortcuts import render


def index(request):
    return render(request, 'home.html')


def eggs(request):
    return render(request, 'eggs.html')


def about(request):
    return render(request, 'about.html')


def count(request):
    fulltext = request.GET['message']
    word_list = fulltext.split()

    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
        sorted_words = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(word_list), 'dictionary': sorted_words})
