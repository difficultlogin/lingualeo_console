#!/usr/bin/env python3

import sys, json, base64
import urllib
import urllib.request
import urllib.parse
from auth import *

if not sys.argv[1].startswith('-'):
	word = sys.argv[1]
else:
	word_ru = sys.argv[2]

	if sys.argv[1] == '-ru':
		url = 'http://lingualeo.com/translate.php?q=%s&from=&source=ru&target=en' % urllib.parse.quote_plus(word_ru)
		translate = urllib.request.urlopen(url)
		translate_obj = json.loads(translate.read().decode('utf-8'))
		word = translate_obj['translation']

url = 'http://lingualeo.com/ru/userdict3/getTranslations?word_value=%s&groupId=&_=1454259456529' % word
response = urllib.request.urlopen(url)
response_str = response.read().decode('utf-8')
response_obj = json.loads(response_str)

translate_value = response_obj['userdict3']['translations'][0]['translate_value']

data_word = {
	'word_id' : response_obj['userdict3']['word_id'],
	'speech_part_id' : 0,
	'groupId' : 'dictionary',
	'translate_id' : response_obj['userdict3']['translations'][0]['translate_id'],
	'translate_value' : translate_value,
	'user_word_value' : word,
	'from_syntrans_id' : '',
	'to_syntrans_id' : '',
}

headers = {
	'X-Requested-With': 'XMLHttpRequest',
}

add_word = session.post('http://lingualeo.com/userdict3/addWord', data=data_word, headers=headers)
print(translate_value)