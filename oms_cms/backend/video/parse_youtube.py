import requests
import re
import datetime
from PIL import Image
import os

from django.conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def parse_api(id):
    url = "https://www.googleapis.com/youtube/v3/videos?id=%s&key=AIzaSyDkrAJNMuZYwjTYaIqSXPGGf6LJvlODVcc&part=snippet,contentDetails&fields=items(id,snippet/thumbnails/high/url,contentDetails/duration)" % id
    r = requests.get(url)
    if r.status_code == 200:
        q = r.json()
        for data in q.get('items'):
            preview = data.get("snippet", None).get("thumbnails", None).get("high", None).get("url", None)
            duration = data.get("contentDetails", None).get("duration", None)
            p = requests.get(preview)
            out = open(BASE_DIR+"/video/image/img.jpeg", "wb")
            out.write(p.content)
            out.close()

            date = datetime.datetime.now()
            imagePath = BASE_DIR+"/video/image/img.jpeg"
            way = "video/image/img{}.jpeg".format(date.strftime("%Y-%m-%d-%H-%M-%S"))
            outputPath = os.path.join(settings.MEDIA_ROOT, way) #"oms_cms/media" +

            quality = "100"
            im = Image.open(imagePath)
            im.save(outputPath, 'JPEG2000', quality=quality)
            return way, duration


def parse_duration(duration):
    t = re.findall(r'\d+', duration)
    if len(t) == 3:
        hour = t[0]
        minute = t[1]
        second = t[2]
        time = int(hour) * 60 * 60 + int(minute) * 60 + int(second)
    elif len(t) == 2:
        minute = t[0]
        second = t[1]
        time = int(minute) * 60 + int(second)
    else:
        second = t[0]
        time = second
    return time


# def parse_duration(duration):
#     t = re.findall(r'\d+', duration)
#     time = '0:00:00'
#     if len(duration) == 10:
#         time = '{}:{}:{}'.format(t[0], t[1], t[2])
#     elif len(duration) == 9:
#         hour = t[0]
#         minute = t[1]
#         second = t[2]
#         if len(minute) != 1 and len(second) == 1:
#             time = '{}:{}:0{}'.format(hour, minute, second)
#         elif len(minute) == 1 and len(second) != 1:
#             time = '{}:0{}:{}'.format(hour, minute, second)
#     elif len(duration) == 8:
#         time = '{}:0{}:0{}'.format(t[0], t[1], t[2])
#     elif len(duration) == 7:
#         minute = t[0]
#         second = t[1]
#         if len(minute) != 1 and len(second) == 1:
#             time = '0:{}:0{}'.format(minute, second)
#         elif len(minute) == 1 and len(second) != 1:
#             time = '0:0{}:{}'.format(minute, second)
#         else:
#             time = '0:{}:{}'.format(minute, second)
#     elif len(duration) == 6:
#         time = '0:0{}:0{}'.format(t[0], t[1])
#     elif len(duration) == 5:
#         time = '0:00:{}'.format(t[0])
#     elif len(duration) == 4:
#         time = '0:00:0{}'.format(t[0])
#     return time


def parse(link):
    u, id = re.split('=', link)
    preview, duration = parse_api(id)
    time = parse_duration(duration)
    url = "https://www.youtube.com/embed/{}".format(id)
    return preview, time, url, id
