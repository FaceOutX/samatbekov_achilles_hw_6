class Computer:
    def __init__(self,cpu,memory):
        self.__cpu = cpu
        self.__memory = memory
        
    @property
    def cpu(self):
        return self.__cpu
    
    @cpu.setter
    def cpu(self, cpu):
        self.__cpu = cpu

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, memory):
        self.__memory = memory

def make_computations(self):
    result = self.__cpu + self.__memory
    return result

def __str__(self):
    return f'Computer with {self.__memory} GB memory'

def __eq__(self, other):
    return self.__memory == other.memory
def __ne__(self, other):
    return self.__memory != other.memory
def __lt__(self, other):
    return self.__memory < other.memory
def __le__(self, other):
    return self.__memory <= other.memory
def __gt__(self, other):
    return self.__memory > other.memory
def __ge__(self, other):
    return self.__memory >= other.memory




cpu = Computer(200,500)

class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def call(self,sim_card_number, call_to_number):
        if sim_card_number < len(self.__sim_cards_list):
            sim_card = self.__sim_cards_list[sim_card_number]
            print(f'Calling {sim_card} from SIM Card-{sim_card_number + 1} - {sim_card}')
        else:
            print(f'Invalid SIM Card-{sim_card_number + 1}')

phone = Phone(['Beeline','Megacom','O!'])
phone.call(1, '+996 222 23 31 14')
phone.call(2, '+996 555 23 31 14')
phone.call(3, '+996 700 23 31 14')

class Smartphone(Computer, Phone):
    def __init__(self):
        pass

def use_gps(self, location):
    print(f'Calculating route to {location} using GPS...')
    def __str__(self):
        return f'Smartphone with {self.__memory} GB memory and SIM Cards: {self.__sim_cards_list}'

computer1 = Computer(800,500)
phone1 = Phone(['Beeline','Megacom','O!'])
smartphone1 = Smartphone(['Beeline', 'Megacom','O!'])
smartphone2 = Smartphone(32,['O!'])

print(computer1)
print(phone1)
print(smartphone1)
print(smartphone2)

smartphone1.use_gps('Home')
smartphone2.use_gps('Work')

computer2 = Computer(16)
print(computer1==computer2)
print(computer1!=computer2)
print(computer1<computer2)
print(computer1<=computer2)
print(computer1>computer2)
print(computer1>=computer2)