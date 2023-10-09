class Person:
    '''
    Рабочий обладает следующими свойствами:
    - qualification - квалификация рабочего, по умолчанию 1
    - name - имя рабочего, по умолчанию name
    - second name - фамилия рабочего,по умолчанию secname
    '''
   
    __second_name="secname"
    __qualification=1
    __name="name"

    def __init__(self):
         pass
    
    def __init__(self,name,secname, qualific):
        self.__name = name
        self.__qualification = qualific
        self.__second_name=secname
    
    def __del__(self):
        print(f"До свидания, мистер {self.name} {self.second_name}")


    @property
    def qualification(self):
       return self.__qualification
    @property
    def happiness(self):
       return self.__happiness
    
    @property
    def name(self):
       return self.__name
    
    @property
    def second_name(self):
       return self.__second_name
    
    def __str__(self):
        return f"Person:{self.name},{self.second_name}, {self.qualification}"


