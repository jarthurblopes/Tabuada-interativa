from time import sleep  # Importa a função sleep da biblioteca time
while True:
    num = int(input('Quer ver a tabuada de qual valor? (Digite um número negativo para sair): '))
    if num < 0:
        break  # Encerra o loop se o número for negativo
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')  # Exibe a tabuada de 1 a 10
print('Finalizando...')
sleep(2)
print('Programa finalizado. Volte sempre!')