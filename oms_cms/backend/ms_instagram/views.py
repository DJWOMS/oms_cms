import logging

import requests
from django.http import HttpResponse
from django.shortcuts import redirect
from instagram import client, subscriptions

from .models import ConfigMSInstagram


# logging.basicConfig(
#     filename='logs/ms_instagram.log',
#     format="%(levelname)-10s %(lineno)d %(asctime)s %(message)s",
#     level=logging.INFO
# )
#
# log = logging.getLogger('ms')

#
# CONFIG = {}
#
# unauthenticated_api = ''
#
# try:
#     inst = ConfigMSInstagram.objects.first()
#     CONFIG = {
#         'client_id': inst.client_id,
#         'client_secret': inst.client_secret,
#         'redirect_uri': inst.redirect_uri
#     }
#     unauthenticated_api = client.InstagramAPI(**CONFIG)
# except Exception as e:
#     print(e)
#
#
# def add_conf():
#     if ConfigMSInstagram.objects.filter().exists():
#         inst = ConfigMSInstagram.objects.first()
#     global CONFIG
#     CONFIG = {
#         'client_id': inst.client_id,
#         'client_secret': inst.client_secret,
#         'redirect_uri': inst.redirect_uri
#     }
#     global unauthenticated_api
#     unauthenticated_api = client.InstagramAPI(**CONFIG)
#
#
# def home(request):
#     """Получаю code"""
#     # add_conf()
#
#     # url = u'https://api.instagram.com/oauth/authorize'
#     # params = {
#     #     u'client_id': CONFIG['client_id'],
#     #     u'client_secret': CONFIG['client_secret'],
#     #     u'grant_type': u'authorization_code',
#     #     u'redirect_uri': CONFIG['redirect_uri']
#     # }
#     #
#     # response = requests.get(url, params=params)
#     # if response.status_code == 200:
#     #     return redirect('on_recent')
#     # else:
#     #     print("Error")
#     # return HttpResponse(response)
#     try:
#         url = unauthenticated_api.get_authorize_url() #scope=["likes", "comments"]
#         return HttpResponse('<a href="%s">Активировать Instagram</a>' % url)
#     except Exception as e:
#         return HttpResponse("Home error - {}".format(e))
#
#
# def exchange_code_for_access_token(client_id, client_secret, code, redirect_uri, **kwargs):
#     """Получаю access token"""
#     url = u'https://api.instagram.com/oauth/access_token'
#     data = {
#         u'client_id': client_id,
#         u'client_secret': client_secret,
#         u'code': code,
#         u'grant_type': u'authorization_code',
#         u'redirect_uri': redirect_uri
#     }
#
#     response = requests.post(url, data=data)
#     # log.info("response - {}".format(response))
#     account_data = response.json()
#     return account_data
#
#
# def on_callback(request):
#     """Получение и сохранение access token"""
#     code = request.GET.get("code", None)
#     # print("callback")
#     if code is None:
#         return HttpResponse('Нет code')
#     # try:
#     # url_token = '/?client_id={}&client_secret={}&grant_type=authorization_code&redirect_uri={}&code={}'.format(
#     #     CONFIG['client_id'],
#     #     CONFIG['client_secret'],
#     #     CONFIG['redirect_uri'],
#     #     code
#     # )
#     # url = 'https://api.instagram.com/oauth/access_token{}'.format(url_token)
#     # print(url)
#     # r = requests.get(url)
#     # if r.status_code == 200:
#     #     print(r.json())
#     # else:
#     #     print("Error requests")
#     # print(unauthenticated_api.exchange_user_id_for_access_token(CONFIG['client_id']))
#     #
#     # log.info("client_secret - {}".format(CONFIG['client_secret']))
#     account_data = exchange_code_for_access_token(
#         CONFIG['client_id'],
#         CONFIG['client_secret'],
#         code,
#         CONFIG['redirect_uri']
#         # 'http://127.0.0.1:8000/insta/oauth_callback/'
#     )
#     # return HttpResponse(account_data)
#     # log.info("account_data - {}".format(account_data['account_data']))
#     # log.info("access_token - {}".format(account_data['access_token']))
#
#     if not account_data:
#         return HttpResponse('Не удалось получить access token ')
#     request.session['access_token'] = account_data['access_token']
#     conf = ConfigMSInstagram.objects.first()
#     conf.access_token = account_data['access_token']
#     conf.save()
#     return redirect('on_recent')
#
#
# def on_recent(request):
#     """Получаю фото"""
#     if 'access_token' in request.session:
#         access_token = request.session['access_token']
#     else:
#         return HttpResponse('Нет Access Token')
#
#     url = 'https://api.instagram.com/v1/users/self/media/recent/?access_token={}'.format(access_token)
#     r = requests.get(url)
#     photos = []
#     if r.status_code == 200:
#         data = r.json()["data"]
#         for img in data:
#             photos.append('<img src="%s"/>' % img.get("images", {}).get("low_resolution", {}).get("url", {}))
#     else:
#         data = {}
#     return data
