class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def set_cpu(self, cpu):
        self.__cpu = cpu

    def get_cpu(self):
        return self.__cpu

    def set_memory(self, memory):
        self.__memory = memory

    def get_memory(self):
        return self.__memory

    def make_computations(self):
        calculation = self.__cpu + self.__memory
        return calculation

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

    def __str__(self):
        return f"Computer with {self.__cpu} CPU cores and {self.__memory} GB of memory."


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def set_sim_cards_list(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def get_sim_cards_list(self):
        return self.__sim_cards_list

    def call(self, sim_card_number, call_to_number):
        print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number}")

    def __str__(self):
        return f"Phone with SIM cards: {', '.join(self.__sim_cards_list)}."


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Построение маршрута до {location}")

    def __str__(self):
        return (f"SmartPhone: CPU - {self.get_cpu()}, Memory - {self.get_memory()}, "
                f"Sim Cards - {', '.join(self.get_sim_cards_list())}")

computer = Computer(cpu=4, memory=16)
phone = Phone(sim_cards_list=["Beeline", "MTS", "MegaCom"])
smartphone1 = SmartPhone(cpu=8, memory=128, sim_cards_list=["Beeline", "MTS"])
smartphone2 = SmartPhone(cpu=6, memory=64, sim_cards_list=["Beeline", "MegaCom"])

print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

phone.call(1, "+996 777 99 88 11")
phone.call(2, "+996 555 22 33 44")
phone.call(4, "+996 123 45 67 89")

smartphone2.use_gps("Kazakhstan")
smartphone2.call(1, "+996 777 77 77 77")
smartphone2.call(2, "+996 555 55 55 55")
