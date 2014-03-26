import requests
import json
import codecs


print('Welcome to the user analyser\n')
#username = input("Please enter a username: ")
username = 'JasonW7'
text_File = codecs.open("rawData.txt", encoding="utf-8", mode="w")
final_Results = codecs.open("refinedData.txt", encoding="utf-8", mode="w")

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


counter = 0
print('\n\n\n-----This is the results of the top 10-----\n')
final_Results.write('-Below is a list of your top 10 used words-\n\n')
final_Results.write('|Word|Count|\n:--:|:--:\n')
#    print ('')
final_Results.write('\n^-Please ^send ^a ^message ^for ^suggestions ^on ^removing ^words ^from ^the ^analysis-\n\n')


text_File.close()
final_Results.close()
