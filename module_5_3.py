class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        print(name, number_of_floors)


   # def go_to(self, new_floor):
    #    floor = 0
     #   print(new_floor)

      #  print(f"Дом {self.name} имеет {self.number_of_floors} этажей \n Поднимаемся на {new_floor} - й")

       # if new_floor > self.number_of_floors or new_floor < 1:
            #print(floor + 1)


       # else:
           # for floor in range(new_floor):
                #print(f"{new_floor + 1} - Такого этажа не существует")




#h1 = House('ЖК Горский', 18)
#h2 = House('Домик в деревне', 2)
#h1.go_to(18)
#h2.go_to(2)

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors


    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors


    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors


    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors


    def __ne__(self, other):

        return self.number_of_floors != other.number_of_floors



    def __add__(self, value):
        return self.number_of_floors + 1


    def __iadd__(self, value):
        return

    def __radd__(self, value):
        return




h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)



h1 = House("Эльбрус", 20)
print(h1 == h2)
h1 = House("Эльбрус", 30)
h2 = House("Акация", 30)
print(h1 == h2)  # __eq__
print(h1 < h2)   # __lt__
print(h1 <= h2)  # __le__
print(h1 > h2)   # __gt__
print(h1 >= h2)  # __ge__
print(h1 != h2)  # __ne__
h1 = h1 + 10  # __add__
print(h1)
h1 += 10  # __iadd__
print(h1)
h2 = 10 + h2  # __radd__
print(h2)




#Название: ЖК Эльбрус, кол-во этажей: 10
#Название: ЖК Акация, кол-во этажей: 20
#False
#Название: ЖК Эльбрус, кол-во этажей: 20
#True
#Название: ЖК Эльбрус, кол-во этажей: 30
#Название: ЖК Акация, кол-во этажей: 30
#False
#True
#False
#True
#False

