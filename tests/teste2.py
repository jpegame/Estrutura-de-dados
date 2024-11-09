from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def falar(self):
        pass
    
class Cachorro(Animal):
    def falar(self):
        print('Au au!')
        
        
class Gato(Animal):
    def falar(self):
        print('Miau!')
        
class Passaro(Animal):
    def __init__(self):
        super().__init__()
        
def main():
    cachorro = Cachorro()
    cachorro.falar()
    
    gato = Gato()
    gato.falar()
    
    passaro = Passaro()
    passaro.falar()
    
main()