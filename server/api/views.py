from django.shortcuts import render
from django.views.generic import View
import requests


class SearchLeaderboards(View):
    '''searches the top leadersboards'''

    def get(self, request):
        template = 'leaderboards.html'
        url = "https://www.callofduty.com/api/papi-client/leaderboards/v2/title/mw/platform/psn/time/alltime/type/core/mode/career/page/1"
        payload={}
        headers = {
        
        }

        pre_res = requests.request("GET", url, headers=headers, data=payload)

        response = pre_res.text

        print(type(response))

        context = {'response': response}
        return render(request, template, context )