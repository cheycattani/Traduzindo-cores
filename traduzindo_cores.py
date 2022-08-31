# Crie um dicionário de cores em inglês. Em seguida, peça ao usuário para digitar uma cor em português.
# Caso exista a cor no dicionário, imprima a tradução, caso contrário, imprima como "Esta cor não consta no disc."

# Dicionário "cor"
cores ={'vermelho':'red', 'rosa': 'pink', 'preto': 'black', 'azul': 'blue', 'roxo': 'purple', 'amarelo': 'yellow', 'laranja': 'orange', 'azul escuro': 'dark blue',
      'verde': 'green', 'cinza': 'grey', 'branco': 'white'}

cor = input('Digite uma cor em portugês: ')

#O get() é um método usado para pegar o valor de uma dada chave em um dicionário se a chave estiver no dicionário,
# caso ela não exista, o método retorna None ou o valor padrão passado por parâmetro.

print('A tradução dessa cor é', cores.get(cor, 'Esta cor não consta no meu discionário.'))
