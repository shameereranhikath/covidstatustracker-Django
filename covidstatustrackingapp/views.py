from django.shortcuts import render
import requests


# Create your views here.
def Home(request):
    url = "https://corona.lmao.ninja/v2/countries/"
    response = requests.get(url).json()
    print(response)
    total_cases = 0
    total_todayCases = 0
    total_deaths = 0
    total_todayDeaths = 0
    total_recovered = 0
    total_todayRecovered = 0
    total_active_cases = 0
    for i in response:
        total_cases += i['cases']
        total_todayCases += i['todayCases']
        total_deaths += i['deaths']
        total_todayDeaths += i['todayDeaths']
        total_recovered += i['recovered']
        total_todayRecovered += i['todayRecovered']
        total_active_cases += i['active']

    print(total_active_cases)
    # print(response)
    # url_country="https://api.first.org/data/v1/countries"
    # url_country="https://api.printful.com/countries"
    # urls=url+'india'
    # response=requests.get(url_country).json()
    # print(response['result'][0]['name'])
    # print(response['data']['TW']['country'])
    # for i in response['data']['country']:
    #     print(i['HK']['country'])
    # dtalist=response
    # for i  in dtalist(0,dtalist.count):
    #     print(i)
    # .json()
    # print(response)
    # print(response["country"])
    # print(response["countryInfo"]['flag'])
    context={'total_cases':total_cases, 'total_todayCases':total_todayCases,
        'total_deaths':total_deaths,
        'total_todayDeaths':total_todayDeaths,
        'total_recovered':total_recovered,
        'total_todayRecovered':total_todayRecovered,
        'total_active_cases':total_active_cases,
             'datas':response}

    return render(request, 'index.html',context)


def India(request):
    url = "https://corona.lmao.ninja/v2/countries/india"
    response = requests.get(url).json()
    print(response['country'])
    return render(request, 'india.html')


# API used
# ----------------
# 1. India state and district wise
# https://api.covid19india.org/state_di...
#
# 2. all countries  api
# https://corona.lmao.ninja/v2/countries
#
# 3. specific country api
# https://corona.lmao.ninja/v2/countrie...
#
# For country flags use
# https://www.countryflags.io
