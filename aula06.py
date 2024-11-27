
#dados da lista
nomes = ["Ana", "Joao", "Paula", "Matheus"]
idades =[18, 26, 15, 25]

#exbindo a lista completa
print(nomes)
print(idades)

#separação do código
#quebra de linha e separação com #
print(f'\n{'#'*80}\n')


print("acessando o primeiro nome da lista nomes: ", nomes[0])   #nomes[0]
print("acessando o segunda idade da lista de idades: ", idades[1]) #idades[1]

print(f'\n{'#'*80}\n')

# o tamanho de uma lista é retornado pela função len()
print("Tamanho da lista nomes: ", len(nomes)) #len(nomes)
print("Tamanho da lista idades: ", len(idades)) #len(idades)

print(f'\n{'#'*80}\n')

print("Idades sem modificação", idades)
idades[2] = 16 #alterando o valor da posição 2 para 16
print("idades após a modificação: ", idades)

print(f'\n{'#'*80}\n')

print("nomes sem modificação", nomes)
#adicionando um novo nome na lista nomes na ultima posição
nomes.append("Carlos") 
print("nomes após a modificação: ", nomes)

print(f'\n{'#'*80}\n')

print("Idades sem modificação", idades)
#insere um novo item na lista baseado na posição
#insert(posição, valor)
idades.insert(1, 50)
print("idades após a modificação: ", idades)

print(f'\n{'#'*80}\n')

print("nomes sem modificação", nomes)
#removendo um item por valor da lista
nomes.remove("Ana") 
print("nomes após a modificação: ", nomes)

print(f'\n{'#'*80}\n')


print("idades sem modificação", idades)
#removendo um item por valor da lista
idades.pop(2) 
print("idades após a modificação: ", idades)

print(f'\n{'#'*80}\n')

print("nomes sem ordenação: ", nomes)
#para ordenar uma lista usamos o sort() (alfabetica ou númerica)
#para colocar a lista do z para o a o do maior ao menor, usamos sort(reverse=True) 
nomes.sort()
print("nomes após a ordenação: ", nomes)

print(f'\n{'#'*80}\n')

print("nomes sem reversão: ", idades)
#para reverter uma lista usamos o reverse()
idades.reverse() 
print("nomes após a reversão: ", idades)

print(f'\n{'#'*80}\n')

print("lista nomes: ", nomes)
#index() retorna a posição em que o valor está localizado 
paula = nomes.index("Paula")
print("Paula esta na posição: ", paula)


