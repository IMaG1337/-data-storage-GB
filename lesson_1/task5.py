"""
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из
байтовового в строковый тип на кириллице
"""

import subprocess

ping_yandex = ['ping', 'yandex.ru']
ping_youtube = ['ping', 'youtube.com']

sub_ping_yandex = subprocess.Popen(ping_yandex, stdout=subprocess.PIPE)
sub_ping_youtube = subprocess.Popen(ping_youtube, stdout=subprocess.PIPE)
br_ya = 0
br_gogle = 0
for line in sub_ping_yandex.stdout:
    print(line.decode('utf-8'))
    br_ya += 1
    if br_ya > 5:
        break
for line in sub_ping_youtube.stdout:
    print(line.decode('utf-8'))
    br_gogle += 1
    if br_gogle > 5:
        break

