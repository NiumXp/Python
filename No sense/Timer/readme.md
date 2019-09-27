# Timer
Um simples contador utilizando threading.

# Demonstração
> Código
```python
from timer import Timer
from random import randint
from time import sleep

def write(*message, separator: str=' ', delay: int=0.005, end='\n') -> None:
    'Escreve letra por letra na tela a cada `delay` segundos.'
    for character in list(separator.join(message)):
        print(character, end='', flush=True); sleep(delay)
    print(end=end)

write("Voltamos a programação normal daqui a pouco!")

timer = Timer(timeout=5) #Cria um timer com um tempo de cinco segundos

@timer.event
def on_timeout() -> None:
    #Quando acabar o tempo do Timer, está função será executada
    write("Olá pessoal! Voltamos com o programa!")

@timer.event
def on_decrease() -> None:
    #Toda vez que um segundo "cair" do Timer, está função será executada
    write(f"P{'i' * randint(1, 10)}.")

timer.start() #Inicia o Timer

sleep(0.1)
write("Procurando mais propagandas...")

timer.wait_timeout() #Espera o tempo esgotar para continuar
sleep(1.5)

write('Fim do programa!')
```
> Saída
![Apresentação do Projeto](https://i.imgur.com/t8Vs9aW.gif)
