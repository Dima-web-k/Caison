from shutil import *
from os import *
from time import *
pathe = str('C:\\Users\\VENOM\\Documents\\Bandicam\\')
rash=str()
l=str()
modes=int(1)
modes2=int(2)
d=str()
m=str()
y=str()
if modes==1:   #Сортировка по типу файлов
    for i in listdir(pathe):
        if i.rfind('.')!=-1:
            rash=i[i.rfind('.')+1::]
            if rash=='txt' or rash=='text' or rash=='log':
                l='Текстовые файлы'
            elif rash=='jpg' or rash=='png' or rash=='bmp' or rash=='gif' or rash=='tif' or rash=='raw':
                l='Изображения'
            elif rash=='doc' or rash=='docx' or rash=='pdf':
                l='Документы'
            elif rash=='xls' or rash=='xlsx':
                l='Таблицы'
            elif rash=='lnk':
                l='Ярлыки'
            elif rash=='zip' or rash=='rar' or rash=='7z':
                l='Архивы'
            elif rash=='mp4' or rash=='avi':
                l='Видео'
            elif rash=='mp3' or rash=='wav':
                l='Музыка'
            else:
                l='Другое'
            if l not in listdir(pathe):
                mkdir(pathe+l)
            move(pathe+i,pathe+l)
elif modes==2: #сортировка по дате 1-день, 2 -месяц, 3-год
    for i in listdir(pathe):
        l=path.getctime(pathe+i)
        d=ctime(l).split(' ')[2]
        m=ctime(l).split(' ')[1]
        y=ctime(l).split(' ')[4]
        if m=='Jan':
            m='01'
        elif m=='Feb':
            m='02'
        elif m=='Mar':
            m='03'
        elif m=='Apr':
            m='04'
        elif m=='May':
            m='05'
        elif m=='Jun':
            m='06'
        elif m=='Jul':
            m='07'
        elif m=='Aug':
            m='08'
        elif m=='Sep':
            m=' 09'
        elif m=='Oct':
            m='10'
        elif m=='Nov':
            m='11'
        elif m=='Dec':
            m='12'
        if modes2==1:
            l=d+'.'+m+'.'+y
        elif modes2==2:
            l=+m+'.'+y
        elif modes2==3:
            l=y
        if l not in listdir(pathe):
                mkdir(pathe+l)
        move(pathe+i,pathe+l)
elif modes==3: #сортировка по размеру
    for i in listdir(pathe):
        if path.getsize(pathe+i)<1024:
            l='Очень маленькие'
        elif path.getsize(pathe+i)<1024**2:
            l='Маленькие'
        elif path.getsize(pathe+i)<1024**3:
            l='Средние'
        else:
            l='Тяжёлые'
        if l not in listdir(pathe):
                mkdir(pathe+l)
        move(pathe+i,pathe+l)