class Virus:
    def __init__(self, name, infection_rate, mortality_rate):
        self.name = name
        self.infection_rate = infection_rate
        self.mortality_rate = mortality_rate

    def display(self,item):
        print("{}. {} - Basic Reproduction Number (R0): {}, Mortality_rate: {}".format(item,self.name,self.infection_rate*20, self.mortality_rate))
