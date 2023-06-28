
class Cat:
    city = 'Moscow'
    def __init__(self,name,color):      #метод для создания нового кота точнее объекта
        self.name = name
        self.color = color

    def sleep(self,gde='в корзине'):
        print(self.name,'спит',gde)

    def walk(self,gde='на улице'):
        print(self.name,'Гуляет',gde)

cat1 = Cat('Vasya','red')
print(cat1.name)
cat1.sleep('диван')

cat2 = Cat('Boris','white')
cat2.walk('на улице')

class Lisiy(Cat):
    eda = ['колбаса','салат']
    def cold(self):
        print(self.name,'мерзнет')
    def eat(self,chto):
        print(self.name,'ест',self.eda[chto])

    def __init__(self,name):
        super(Lisiy, self).__init__(name,'Lisiy')

cat3 = Lisiy('monya')
cat3.cold()
cat3.eat(1)
print(cat3.name,cat3.color)

class Auto:
    city = "Moscow"
    def __init__(self,marka,ear,color):
        self.marka = marka
        self.ear = ear
        self.color = color

    def edet(self,kuda='домой'):
        print(self.marka,'едет',kuda)

    def tormoz(self):
        print(self.marka,'тормозит')

    def yskor(self,ogo='на 100 км'):
        print(self.marka,'ускоряется',ogo)

auto1 = Auto('vaz','2008','blue')

auto1.edet('v kosmos')
auto1.tormoz()
auto1.yskor('na 300 mah')

class Gruz(Auto):
    gorod = ['oren','gai']
    def vezy(self):
        print(self.marka,'везет груз')
    def gor(self,kuda,skolko):
        print(self.marka,self.gorod[kuda],skolko)
class Sport(Auto):

    def ooo(self):
        print(self.marka,'захожу на круг')


avto2 = Gruz('kamaz','2008','red')
avto2.vezy()
avto2.gor(1, '40 tonn')
avto3 = Sport('vaz','1980','green')
avto3.ooo()
