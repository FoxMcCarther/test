import requests
import json
import codecs


print('Welcome to the user analyser\n')
#username = input("Please enter a username: ")
username = 'JasonW7'
text_File = codecs.open("rawData.txt", encoding="utf-8", mode="w")

r = requests.get(r'http://www.reddit.com/user/'+username+'/comments/.json')
#data = r.json()
nextPage = "Initial"

#This loops through the comments on the rest of the pages, The functions are essentially exactly as they appear above
while nextPage is not None:
    data = json.loads(r.text)
  
    for child in data['data']['children']:
        try:
            print(child['data']['body'] + '\n')
            temp = child['data']['body']
            temp = temp.translate(str.maketrans('.!;,?~()\'\"[]', '            '))
            text_File.write(temp + ' ')
        except:
            print('This case happens when a link is posted with no body')
            pass
    nextPage = data['data']['after']
    print(str(nextPage))
    if nextPage is not None:
        r = requests.get(r'http://www.reddit.com/user/'+username+'/.json?count=25&after='+nextPage)



text_File.close()
