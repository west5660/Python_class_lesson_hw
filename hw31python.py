
class kino:
    def __init__(self,name,rejis,country):
        self.name=name
        self.rejis=rejis
        self.country=country

    def vihod(self,gde='Малибу',were='Kinopoisk',leng='England'):
        print(self.name,'фильм выходит в кинотеатре',gde,'также на площадке сайта',were,'релиз картины будет на',leng,'языке')

film1=kino('Omen','Ivanov R.R.','USA')
film1.vihod()

film2=kino('Zamah','Petrov I.J.','China')
film2.vihod('Red October','Ivi','Китайском')

film3=kino('GoGo','Helen A.B.','Russia')
film3.vihod('Holod','Rutube','Русском')

class horor(kino):
    pug = ['Зомби','Монстры','Маньяк','Психи']
    def hor(self,kem,reliz_data):
        print(self.name,'фильм жанра ужасы, основной злодей',self.pug[kem],reliz_data)


film4=horor('Vii','Petrov V.T.','Brazil')
film4.hor(1,'дата релиза 15 октября 2024')

class comedia(kino):
    humor = ['Клоуны','Животные','Плоский юмор','Пара гоблинов']
    def hum(self,who,reliz):
        print(self.name,'фильм жанра комедия, отвечать за юмор и смех будут',self.humor[who],reliz)

film5=comedia('Masca','Jordj R.T.','Argentina')
film5.hum(3,'дата релиза 17 августа 2025 года')