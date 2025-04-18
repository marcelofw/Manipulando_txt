

# with open("C:/Python/Manipulando_txt/exemplo1.txt", "w", encoding = "utf-8") as arquivo:
#     arquivo.write("Testando método write no arquivo exemplo1.txt")          
#     arquivo.write("\nTestando linha 2")      

# with open("C:/Python/Manipulando_txt/exemplo1.txt", "w", encoding = "utf-8") as arquivo:
#     arquivo.write("Sobrescrevendo conteúdo anterior")

# with open("exemplo1.txt", "r", encoding = "utf-8") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

# with open("exemplo1.txt", "r", encoding = "utf-8") as arquivo:
#     for linha in arquivo:
#         print(f"Linha: ", linha.strip())

# with open("C:/Python/Manipulando_txt/exemplo1.txt", "a", encoding = "utf-8") as arquivo:
#     arquivo.write("\nAdicionando nova linha mantendo o conteúdo anterior")

# with open("exemplo1.txt", "r", encoding = "utf-8") as arquivo:
#     linhas = arquivo.readlines()
#     print(linhas)

# nomes = ["Ana", "Bruno", "Carlos"]
# with open("nomes.txt", "w", encoding = "utf-8") as arquivo:
#     for nome in nomes:
#         arquivo.write(f"{nome}\n")

# with open("exemplo1.txt", "r", encoding = "utf-8") as arquivo:
#     for linha in arquivo:
#         if len(linha.strip()) > 10:
#             print("Linha longa:", linha.strip())

with open("numeros.txt", "w", encoding = "utf-8") as arquivo:
    arquivo.write("1\n2\n3\n4\n5\n")
with open("numeros.txt", "r", encoding = "utf-8") as arquivo:
    numeros = [int(linha.strip()) for linha in arquivo]
print(numeros)









