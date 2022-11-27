import random

class_list = ['yishake.abate',
'ankita.adhikari',
'ben.alderfer',
'andrew.arledge',
'matthew.arledge',
'sushant.baniya',
'micah.buckwalter',
'rebekah.copeland',
'anna.filipkowski',
'bri.garcia-sanchez',
'bishal.ghimire',
'adnan.hamdan',
'david.joslyn',
'ben.knutsson',
'abriham.mekonnen',
'andrew.nord',
'hizkia.permata',
'nati.seifu',
'ronav.subedi',
'katie.tanous',
'rhythm.timsina',
'joshua.wenger',
'erik.wilkinson']

pick = random.choice(class_list)
pick1 = random.choice(class_list)

if len(pick)>len(pick1):
    print(pick, "has defeated", pick1)
elif len(pick)==len(pick1):
    ("oops, seems to be a fair match")
else:
    print(pick1, "has defeated ", pick)




