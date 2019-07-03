import json

import requests
from django.http import HttpResponse
from django.shortcuts import redirect
from instagram import client #, subscriptions
from lxml import html

from .models import ConfigMSInstagram

# if ConfigMSInstagram.objects.filter().exists():
#     inst = ConfigMSInstagram.objects.first()
#
#     CONFIG = {
#         'client_id': inst.client_id,
#         'client_secret': inst.client_secret,
#         'redirect_uri': inst.redirect_uri
#     }
#
#     unauthenticated_api = client.InstagramAPI(**CONFIG)


def home():
    """Получаю code"""
    if ConfigMSInstagram.objects.filter().exists():
        inst = ConfigMSInstagram.objects.first()

        CONFIG = {
            'client_id': inst.client_id,
            'client_secret': inst.client_secret,
            'redirect_uri': inst.redirect_uri
        }

        unauthenticated_api = client.InstagramAPI(**CONFIG)

    url = u'https://api.instagram.com/oauth/authorize'
    params = {
        u'client_id': CONFIG['client_id'],
        u'client_secret': CONFIG['client_secret'],
        u'grant_type': u'authorization_code',
        u'redirect_uri': CONFIG['redirect_uri']
    }
    # print("home")
    response = requests.get(url, params=params)
    # print(response.status_code)
    if response.status_code == 200:
        # on_recent()
        # print(response.text)
        return redirect('on_recent')
    else:
        print("Error")
    # return HttpResponse(response)
    # try:
    #     url = unauthenticated_api.get_authorize_url() #scope=["likes", "comments"]
    #     return HttpResponse('<a href="%s">Активировать Instagram</a>' % url)
    # except Exception as e:
    #     return HttpResponse("Home error - {}".format(e))


def exchange_code_for_access_token(client_id, client_secret, code, redirect_uri, **kwargs):
    """Получаю access token"""
    url = u'https://api.instagram.com/oauth/access_token'
    data = {
        u'client_id': client_id,
        u'client_secret': client_secret,
        u'code': code,
        u'grant_type': u'authorization_code',
        u'redirect_uri': redirect_uri
    }

    response = requests.post(url, data=data)
    account_data = response.json()
    return account_data


def on_callback(request):
    """Получение и сохранение access token"""
    if ConfigMSInstagram.objects.filter().exists():
        inst = ConfigMSInstagram.objects.first()

        CONFIG = {
            'client_id': inst.client_id,
            'client_secret': inst.client_secret,
            'redirect_uri': inst.redirect_uri
        }

        unauthenticated_api = client.InstagramAPI(**CONFIG)
    code = request.GET.get("code")
    if not code:
        return HttpResponse('Нет code')
    # try:
    # url_token = '/?client_id={}&client_secret={}&grant_type=authorization_code&redirect_uri={}&code={}'.format(
    #     CONFIG['client_id'],
    #     CONFIG['client_secret'],
    #     CONFIG['redirect_uri'],
    #     code
    # )
    # url = 'https://api.instagram.com/oauth/access_token{}'.format(url_token)
    # print(url)
    # r = requests.get(url)
    # if r.status_code == 200:
    #     print(r.json())
    # else:
    #     print("Error requests")
    # print(unauthenticated_api.exchange_user_id_for_access_token(CONFIG['client_id']))
    account_data = exchange_code_for_access_token(
        CONFIG['client_id'],
        CONFIG['client_secret'],
        code,
        CONFIG['redirect_uri']
    )
    if not account_data['access_token']:
        return HttpResponse('Не удалось получить access token')
    # request.session['access_token'] = account_data['access_token']
    # return redirect('on_recent')
    # access_token = account_data['access_token']
    conf = ConfigMSInstagram.objects.first()
    conf.access_token = account_data['access_token']
    conf.save()
    # print(code)
    return on_recent()


def on_recent():
    """Получаю фото"""
    conf = ConfigMSInstagram.objects.first()
    print("on_recent")
    print(conf.access_token)
    if conf.access_token is not None:
        url = 'https://api.instagram.com/v1/users/self/media/recent/?access_token={}'.format(
            conf.access_token)
        r = requests.get(url)
        photos = []
        photos_max = []
        if r.status_code == 200:
            data = r.json()["data"]
            for img in data:
                # print(img.get("images", {}))
                photos_max.append(img.get("images", {}).get("thumbnail", {}).get("url", {}))
                photos.append(img.get("images", {}).get("standard_resolution", {}).get("url", {})) #get("low_resolution", {}).get("url", {}))
        else:
            home()
            # on_recent()
        return photos
    else:
        home()
        # on_recent()


def get_of_tag(tag):
    """Получение изображений по хештегу"""
    conf = ConfigMSInstagram.objects.first()
    # print("get_of_tag")
    # print(conf.access_token)
    if conf.access_token is not None:
        url = 'https://api.instagram.com/v1/tags/test/media/recent/?access_token={}'.format(
            conf.access_token)
        r = requests.get(url)
        photos = []
        photos_max = []
        if r.status_code == 200:
            data = r.json()["data"]
            # print(data)
            for img in data:
                # print(img.get("images", {}))
                photos_max.append(img.get("images", {}).get("thumbnail", {}).get("url", {}))
                photos.append(img.get("images", {}).get("standard_resolution", {}).get("url", {})) #get("low_resolution", {}).get("url", {}))
        else:
            # print(r.status_code)
            home()
            # on_recent()
        return photos
    else:
        home()
        # on_recent()


def instagram_scrap_profile(username):
    """Получаю фото из инстаграма по имени пользователя"""
    url = 'https://www.instagram.com/{}/'.format(username)
    r = requests.get(url)

    if r.status_code == 200:
        r.raise_for_status()
        data = html.fromstring(r.content)
        return data
    else:
        data = {}
    # print(data)
    return data


def instagram_profile_js(username):
    """
    Retrieve the script tags from the parsed page.
    :param username:
    :return:
    """
    try:
        tree = instagram_scrap_profile(username)
        return tree.xpath('//script')
    except AttributeError:
        # logging.exception("scripts not found")
        return None


def instagram_profile_json(username):
    """
    Get the JSON data string from the scripts.
    :param username:
    :return:
    """
    SCRIPT_JSON_PREFIX = 18
    SCRIPT_JSON_DATA_INDEX = 21

    scripts = instagram_profile_js(username)
    source = None

    if scripts:
        for script in scripts:
            if script.text:
                if script.text[0:SCRIPT_JSON_PREFIX] == "window._sharedData":
                    source = script.text[SCRIPT_JSON_DATA_INDEX:-1]

    return source


def pars_image(data):
    """Забираю только фото"""
    photos = []
    if data is not None:
        for data_img in data["entry_data"]["ProfilePage"]: #["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"]:
            for dt in data_img["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"]:
                for img in dt["node"]["thumbnail_resources"]:
                    if img["config_width"] == 640:
                        print(img["src"])
                        photos.append(img.get("src", {}))
        #             photos.append(img.get("thumbnail_resources", {}))
        # print(photos_max)
    return photos


def follow(username):
    """ Получить количество подписчиков
    :param username:
    """
    print(username)
    url = 'https://instagram.com/{}/?__a=1&max_id=endcursor'.format(username)
    r = requests.get(url)
    followers = 0
    if r.status_code == 200:
        data = r.json()
        followers = data.get("graphql", None).get("user", None).get("edge_followed_by", None)#.get("count", None)
    return followers


def instagram_profile_obj(username):
    """
    Retrieve the JSON from the page and parse it to a python dict.
    :param username:
    :return:
    """
    print(username)
    json_data = instagram_profile_json(username)
    data = json.loads(json_data) if json_data else None
    images = pars_image(data)
    return images
    return json.loads(json_data) if json_data else None
