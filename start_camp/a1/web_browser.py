import webbrowser


keywords = [
    'python', 'study abroad', 'you',
]



for keyword in keywords:
    url = 'https://www.google.com/search?q='+keyword
    webbrowser.open_new(url)



from darksky import forecast

multicampus = forecast('f36c30487bce21b9a7c33f3fde36cad2',37.501571,127.039724)
print(multicampus['currently']['summary'])
print(multicampus['currently']['temperature'])


# import requests
# url='https://api.darksky.net/forecast/f36c30487bce21b9a7c33f3fde36cad2/37.501571,127.039724'
# res=requests.get(url)
# data=res.json()
# print(data['currently']['summary'])


