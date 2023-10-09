from lib.Person import Person
person1=Person("Иван", "Петров", 2 )
person2=Person("Генадий", "Соломонов", 10 )
person3=Person("Василий", "Львов", 0 )

print(f"1.{str(person1)}\n2.{str(person2)}\n3.{str(person3)}")
print("Кого уволим?")
dismiss=int(input())
if(dismiss==1):
    del(person1)
elif(dismiss==2):
    del(person2)
elif(dismiss==3):
    del(person3)
else:
    print("У нас нет такого сотрудника")


input()