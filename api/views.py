from django.shortcuts import render
import requests
from tomlkit import value
# Create your views here.
def jokes(request):
    if(request.GET.get('dadjokes')):
        url = f"https://icanhazdadjoke.com/"
        response = requests.get(url,headers={"Accept": "application/json"},)
        data = response.json()
        joke = data['joke']
        context ={
            'joke':joke
        }
    elif(request.GET.get('norris')):   
        url = f"https://api.chucknorris.io/jokes/random"
        response = requests.get(url,headers={"Accept": "application/json"},)
        data = response.json()
        norris = data['value']
        image = data['icon_url']
        context ={'value':norris,
        'icon':image}
    else:
        url = f"https://icanhazdadjoke.com/"
        response = requests.get(url,headers={"Accept": "application/json"},)
        data = response.json()
        joke = data['joke']
        context ={
            'joke':joke
        }

    # else:
    #     url = f"https://icanhazdadjoke.com/slack"
    #     response = requests.get(url,headers={"Accept": "application/json"},)
    #     data = response.json()
    #     slack_ = data['attachments']
    #     slacks = []
    #     for slack in slack_:
    #         slacks_dict = {
    #         'fallback':slack['fallback'],
    #         'footer':slack['footer'],
    #         'text':slack['text'],
    #     }
    #         slacks.append(slacks_dict)
    #     context ={'slack':slack}
    return render (request,'api/home.html',context)