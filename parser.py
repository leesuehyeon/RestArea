import json
import os
import django

# Django 설정 로드
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.base")
django.setup()

from map.models import Rest

def parsing():
    with open('data.json', encoding='utf-8') as file:
        data = json.load(file)  # 제이슨 파일 열어서 데이터 불러오기

    post = []

    for entry in data['DATA']:
        post.append({
            'name': entry['r_area_nm'],
            'location': entry['r_detl_add'],
            'latitude': entry['la'],
            'longitude': entry['lo']
        })

    return post


if __name__=='__main__':
    post = parsing()

    for i in range(len(post)):
        Rest(
            name=post[i]['name'],
            location=post[i]['location'],
            latitude=post[i]['latitude'],
            longitude=post[i]['longitude']
        ).save()

    print("suceed")
    # name = entry.get('R_AREA_NM')  # 정수를 문자열로 변환
    # location = entry.get('R_DETL_ADD')
    # latitude = entry.get('LA')
    # longitude = entry.get('LO')

    # 모델에 데이터 저장
   # Rest.objects.create(name=name, location=location, latitude=latitude, longitude=longitude)
