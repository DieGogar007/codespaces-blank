class Package():
    W_GR_100=1.0
    def __init__(self, 
                 id:int=0, 
                 weigth:float=1.0, 
                 cost:float=1.0, 
                 description:str='Description.'):
        
        self.__id=id
        self.__weight=weigth
        self.__cost=cost
        self.__description=description

    def get_id(self):
        return self.__id

    def set_id(self):
        self.__id=0

    def get_weight(self):
        return self.__weight

    def set_weight(self):
        self.__weight=1

    def set_description(self):
        self.__description='description'

    def get_description(self):
        return self.__description

    def set_cost(self):
        self.__cost=1.0

    def get_cost(self):
        return self.__cost

    def calculate(self):
        print("COSTO TOTAL DE ENVIO $ ", (self.__cost*self.__weight))
    
    def _Str_(self):
        print("ID: ",self.__id,"\nWEIGHT: ", self.__weight,"\nW_GR_100:",
              W_GR_100,"\nDESCRIPTION:", self.__description,"\nCOST: ",self.__cost)

class StandardPackage(Package):
    def __init__(self, 
                 id:int=0, 
                 weigth:float=1.0,
                 cost:float=1.0,
                 description:str='Description.', 
                 fixedfee:float=0):
        
        self.__id=id
        self.__weight=weigth
        self.__cost=cost
        self.__description=description
        self.__fixedfee=fixedfee

    def get_id(self):
        return self.__id

    def set_id(self):
        self.__id=0

    def get_weight(self):
        return self.__weight

    def set_weight(self):
        self.__weight=1

    def get_description(self):
        return self.__description
        
    def set_description(self):
        self.__description='description'

    def get_cost(self):
        return self.__cost
        
    def set_cost(self):
        self.__cost=1.0

    def get_fixedfee(self):
        return self.__fixedfee

    def set_fixedfee(self):
        self.__fixedfee=0 
    
    def calculate(self):
        print("COSTO DE ENVIO $ ", ((self.__cost*self.__fixedfee) + self.__weight))

    def _Str_(self):
        print("\nFixed Fee", self.__fixedfee)

class OverweightPackage(Package):
    def __init__(self,
                 id, 
                 weigth=1, 
                 cost=0, 
                 description='Description.', 
                 overweight=0):
        
        self.__id=id
        self.__weight=weigth
        self.__cost=cost
        self.__description=description
        self.__overweigth=overweight

    def get_id(self):
        return self.__id

    def set_id(self):
        self.__id=0

    def get_weight(self):
        return self.__weight

    def set_weight(self):
        self.__weight=1

    def get_description(self):
        return self.__description
        
    def set_description(self):
        self.__description='description'

    def get_cost(self):
        return self.__cost

    def set_cost(self):
        self.__cost=1.0
        
    def get_overweight(self):
        return self.__overweigth

    def set_overweight(self):
        self.__overweigth=0 

    def calculate(self):
        print("COSTO DE ENVIO CON SOBREPESO $ ",((self.__cost*self.__weight) + self.__overweigth))

class Person():

    def __init__(self, 
                 name='Name', 
                 lastname='Lastname', 
                 userid=0, 
                 phonenumber=0):
        
        self.__name=name
        self.__lastname=lastname
        self.__userid = userid 
        self.__phonenumber = phonenumber 

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name='Name'

    def get_lastname(self):
        return self.__lastname
    
    def set_lastname(self):
        self.__lastname='Lastname' 

    def get_userid(self):
        return self.__userid

    def set_userid(self):
        self.__userid=0 

    def get_phonenumber(self):
        return self.__phonenumber

    def set_phonenumber(self):
        self.__phonenumber=0

    def _Str_(self):
        print("NAME: ", self.__name, "\nLAST NAME: ",
              self.__lastname, "\nUSERID: ", self.__userid, "\nPHONE NUMBER: ",self.__phonenumber)    
        
class Address():
    def __init__(self, 
                 street_number=0,
                 house_number=0, 
                 neighborhood='Neighborhood'):
        
        self.__street_number=street_number 
        self.__house_number=house_number
        self.__neighborhood=neighborhood
    
    def set_street_number(self):
        self.__street_number=0 

    def get_street_number(self):
        return self.__street_number

    def set_house_number(self):
        self.__house_number=0 

    def get_house_number(self):
        return self.__house_number
    
    def set_neighborhood(self):
        self.__neighborhood='Neighborhood'

    def get_neighborhood(self):
        return self.__neighborhood
    
    def _Str_(self):
        print("STREET NUMER: ", self.__street_number, "HOUSE NUMBER", self.set_house_number,
              "NEIGHBORHOOD: ", self.__neighborhood)
        
class Delivor(Person):
    def _init_(self,
                 name: str= "", 
                 lastname: str="",
                 dnicard: int = 0,
                 birthdate: str="",
                 phone: int = 0,
                 idperson: str="",
                 date: str ="",
                 time: str ="",
                 sender=Person(),
                 receiver=Person(),
                 sender_add=Address(),
                 receiver_add=Address(),
                 contact=Person(),
                 items=[Package()]):
         
         self.__idpersona = idperson 
         self.__date = date
         self.__time = time

         self.__sender = Person() 
         if (sender != Person):
            print ("\nEl valor es incorrecto")
         else:
            self.__sender = Person()
            
         self.__receiver = Person() 
         if (receiver != Person):
            print ("\nEl valor es incorrecto")
         else:
            self.__receiver = Person() 
            
         self.__sender_add = Address() 
         if (sender_add!= Address()):
            print ("\nEl valor es incorrecto")
         else:
            self.__sender_add = Address()
            
         self.__receiver_add = Address() 
         if (receiver_add!= Address()):
            print ("\nEl valor es incorrecto")
         else:
            self.__receiver_add = Address()
            
         self.__contact = Person() 
         if (contact != Person):
            print ("\nEl valor es incorrecto")
         else:
            self.__contact = Person() 
            
         self.__items = [Package()] 
         if (items != Package()):
            print ("\nNULLL")
         else:
            self.__items = Package()
         
         def get_idpersona(self):
            return self.__idpersona
    
         def set_idpersona(self, idpersona):
            self.__idpersona = idpersona
        
         def get_date(self):
            return self.__date

         def set_date(self, date):
            self.__date = date


         def get_time(self):
            return self.__time
    
         def set_time(self, time):
            self.__time = time
        
         def get_sender(self):
            return self.__sender
    
         def set_sender(self, sender):
            if type (sender) != Person:
                print ("\n¡¡El dato ingresado es inválido!!, por favor ingrese un nuevo dato")
            else:
                self.__sender = Person( ) 
        
         def get_receiver(self):
            return self.__receiver
    
         def set_receiver(self, receiver): 
            if type (receiver) != Person:
                print ("\n¡¡El dato ingresado es inválido!!, por favor ingrese un nuevo dato")
            else:
                self.__receiver = Person() 
        
         def get_sender_add(self):
            return self.__sender_add

    def set_sender_add(self, sender_add):
         if type (sender_add) != Address:
            print ("\n¡¡El dato ingresado es inválido!!, por favor ingrese un nuevo dato")
         else:
            self.__sender_add = Address()
        
    def get_receiver_add(self):
        return self.__receiver_add
    
    def set_receiver_add(self, receiver_add):
        if type (receiver_add) != Address:
            print ("\n¡¡El dato ingresado es inválido!!, por favor ingrese un nuevo dato")
        else:
            self.__receiver_add = Address()

    def get_contact(self):
        return self.__contact
    
    def set_contact(self, contact):
        if type (contact) != Person:
            print ("\n¡¡El dato ingresado es inválido!!, por favor ingrese un nuevo dato")
        else:
            self.__contact = Person() 
    
    def get_items(self):
        return self.__items
    
    def set_items(self, items):
        if (items != Package()):
            print ("\n¡¡El dato ingresado es inválido!!, por favor ingrese un nuevo dato")
        else:
            self.__items = [Package()]
    
    def str(self):
        print("*ID: ", self.__idpersona,
              "\n*DATE: ", self.__date, 
              "\n*TIME: ", self.__time, 
              "\n*PERSONA QUE LO ENVIA: " ,self.__sender, 
              "\n*PERSONA QUE LO RECIBE= ", self.__receiver,
              "\n*DIRECCION DE QUIEN LO ENVIA= ", self.__sender_add,
              "\n*DIRECCION DE QUIEN LO RECIBE= ", self.__receiver_add)