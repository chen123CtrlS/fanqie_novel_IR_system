from django.shortcuts import render,HttpResponse,redirect
# Create your views here.
from novel_search.utils.load_invert_index import *


with open(r"novel_search/utils/abstract.pickle", 'rb') as f:
    data = pickle.load(f),
abstract_frequency_dict = data[0]['frequency_dict']
abstract_length = data[0]['abstract_length']
abstract_inverted_index = data[0]['inverted_index']
abstract_data = data[0]['data']

with open(r"novel_search/utils/chapter.pickle", 'rb') as f:
    data = pickle.load(f),
frequency_dict = data[0]['frequency_dict']
chapter_length = data[0]['chapter_length']
inverted_index = data[0]['inverted_index']
all_chapters = data[0]['all_chapters']

def index(request):
    """
    搜索主页
    """
    return render(request,'home.html')

def result(request):
    """
    展示结果
    """
    print(request.GET)
    c_query = request.GET.get('context','')
    a_query = request.GET.get('abstract', '')

    abstract_res = evaluate(abstract_inverted_index, abstract_length, abstract_data, abstract_frequency_dict, a_query)
    context_res = evaluate1(inverted_index, chapter_length, all_chapters, frequency_dict, c_query)

    print(len(abstract_res))
    print(len(context_res))
    print(context_res)

    return render(request, 'show.html', {'abstract_res': abstract_res, "context_res": context_res, "c_query":c_query, "a_query":a_query})
