import json
import re


# read json file from test.json
def read_json():
    with open('test.json') as f:
        data = json.load(f)

    return data


json_data = read_json()
print(json_data)


# search multiple words
def search_multiple_words(search_words):
    # search_words = [search_words]

    # split input string to separate input string
    search_words = search_words.split(' ')

    ascending_list = []

    for line in json_data:
        if any(word in line for word in search_words):
            ascending_list.append(line)

    # Search result ordering by total character ascending
    ascending_list.sort()  # sorts normally by alphabetical order
    ascending_list.sort(key=len, reverse=True)  # sorts by descending length

    for i in ascending_list:
        print(i)


# check if the input users is not less than 3 or more than 50
while True:
    search_words = input('search words: ')

    # check if the input is alphanumeric, dash dot and comma
    if not re.match('[a-zA-Z0-9\-\.\,]', search_words):
        print('Only allow alpanumeric, dash, dot and comma')

    if len(search_words) <= 3 or len(search_words) > 50:
        print('Please don"t input less than 3 word or more than 50 word')
    else:
        search_multiple_words(search_words)
        break
