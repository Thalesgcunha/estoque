import mysql.connector as bd

def conecta_bd():
    con = bd.connect(
        user='root',
        password = '1234',
        host = 'localhost',
        database = 'estoque'
    )
    
    return con

def cadastra_item():
    description = input('Insira a decrição do item: ')
    quantity = input('Insira a quantidade disponível: ')
    con = conecta_bd()
    cursor = con.cursor()
    query = "insert into itens (description,quantity) values ('"+description+"','"+quantity+"')"
    cursor.execute(query)
    con.commit()
    print("Item cadastrado")
    
    con.close()

def pesquisa_item():
    description = input('Insira o item que deseja pesquisar: ')
    con = conecta_bd()
    cursor = con.cursor()
    query = "select id,description,quantity from itens where description like '%" + description + "%'"
    cursor.execute(query)
    result = cursor.fetchall()
    if (result):
        print("\nItens Encontrados:\n***************")
        for item in result:
            itens = list(item)
            print("Codigo: "+str(itens[0])+"\nItem: " + itens[1] + "\nQuantidade: " + str(itens[2]) + "\n****************")
    else:
        print("Item não encontrado")

    con.close()

def deleta_item():
    id = input('Insira o codigo do item que deseja deletar: ')
    con = conecta_bd()
    cursor = con.cursor()
    query = "delete from itens where id = " + id
    cursor.execute(query)
    con.commit()
    print("Item deletado")
    con.close()

def altera_quantidade_item():
    id = input('Insira o codigo do item que deseja alterar: ')
    new_quantity = input('Digite a nova quantidade: ')
    con = conecta_bd()
    cursor = con.cursor()
    query = "update itens set quantity = " + new_quantity + " where id = " + id
    cursor.execute(query)
    con.commit()
    print("Quantidade alterada")
    con.close()