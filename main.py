from ast import match_case

from estoque import cadastra_item, pesquisa_item,deleta_item,altera_quantidade_item


print("** Caixa de Ferramentas ** ")
print("***** Menu de opções *****")
print("\n")
print("1. Cadastrar item")
print("2. Pesquisar item")
print("3. Deletar item")
print("4. Alterar quantidade do item")
op = input("Digite sua opção: ")

if op =="1":
    cadastra_item()
        
elif op=="2":
    pesquisa_item()
elif op=="3":
    deleta_item()
elif op=="4":
    altera_quantidade_item()
else:
    print("Opção invalida")
