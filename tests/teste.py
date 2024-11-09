import random

def get_sample(lista_numeros, n):
    if n > len(lista_numeros):
        return lista_numeros, []
    result = random.sample(lista_numeros, n)
    
    for item in result:
        lista_numeros.remove(item)
    
    return result, lista_numeros

def main():
    num_pessoas = int(input("Digite o número de pessoas: "))
    num_questoes = int(input("Digite o número de questões: "))
    
    lista_numeros = [i for i in range(1, num_questoes + 1)]
    for _ in range(num_pessoas):
        sample_size = (num_questoes // num_pessoas) + (1 if num_questoes % num_pessoas > 0 else 0)
        sample, lista_numeros = get_sample(lista_numeros, sample_size)
        print(sample)
    
main()