
from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def count(request):
	full_text = request.GET['full_text']
	word_list = full_text.split()

	word_dictionary = {}

	for word in word_list:
		if word in word_dictionary:
			#Increase
			word_dictionary[word] += 1
		else:
			#add to the dictionary
			word_dictionary[word] = 1	

									              # 튜플의 두번째 값, 즉 '본문에서 등장한 빈도값'value를 기준으로 sorting하겠다! 
	sorted_words = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse = 1) # reverse = true		
		  # word_dictionary.items()  will convert the dictionary into a list
		  # key와 value를 튜플로 구성. (key, value) 이런식으로! 그리고 이러한 튜풀 쌍들을 list에 넣음!
		  # [(key1, value1), (key2, value2), (key3, value3), ...] 이렇게!!     

	# 즉, sorted_words를 이용해... 우린 각각 단어들이 많이 언급된 순으로 이 dictonary를 정렬해줄 수 있음!! 	                                       
	 
	return render(request, 'count.html', {'full_text':full_text, 'count':len(word_list), 'sorted_words':sorted_words})
                                                                                         