produtos = ["Arroz", "Feijão","Oléo","Açucar","Macarrão"]
quantidades = [10, 25 , 5, 20, 15]

print(f'\n{'#'*80}\n')


print(produtos)
print(quantidades)

print(f'\n{'#'*80}\n')


print("o primeiro produto da lista: ", produtos[0])
print("A segunda quantidade: ", quantidades[1])

print(f'\n{'#'*80}\n')

print("O número de produtos é: ", len(produtos))
print("a quantidade é: ", len(quantidades))

print(f'\n{'#'*80}\n')

quantidades[3] = 65
print(quantidades)

print(f'\n{'#'*80}\n')

produtos.append("Sal")
quantidades.append(40)
print(produtos)
print(quantidades)

print(f'\n{'#'*80}\n')

produtos.insert(1, "Cafe")
quantidades.insert(1, 10)
print(produtos)
print(quantidades)

print(f'\n{'#'*80}\n')

produtos.remove("Feijão")
print(produtos)

print(f'\n{'#'*80}\n')

quantidades.pop(2)  
print(quantidades)

print(f'\n{'#'*80}\n')

produtos.sort()
print(produtos)

print(f'\n{'#'*80}\n')

quantidades.reverse()
print(quantidades)

print(f'\n{'#'*80}\n')

Sal = produtos.index("Sal")
print("o sal está na posição: ", Sal)