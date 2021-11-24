from models import Pessoas, Usuarios

#Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Freitas',idade=36)
    print(pessoa)
    pessoa.save()

# Realiza consulta na tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Fabricio').first()
    print(pessoa.idade)

# Altera dados na tabel pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Freitas').first()
    pessoa.nome = 'Fischer'
    pessoa.save()

#Exclui dados na tabela pessoas
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Fischer').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)



if __name__ == '__main__':
        insere_usuario('Fabricio', '1234')
        insere_usuario('Freitas', '4321')
        consulta_todos_usuarios()
      # insere_pessoas()
      # altera_pessoa()
      # exclui_pessoa()
      # consulta_pessoas()

