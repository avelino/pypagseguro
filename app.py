# -*- encoding: utf-8 -*-

import web 
import lasagna2 as lasagna
from pagseguro import Pagseguro # Para o carrinho
import pagseguro

token = 'jbdskjbvwdobvwoub29ub'

urls = (
  r"/", "index",
  r"/retorno/?", "retornoAutomatico",
)
app = web.application(urls, globals()) #, web.reloader)

class index:
  def GET(self):
    f=web.input(id=0)
    cart = ''
    if f.id:
      carrinho = Pagseguro(email_cobranca='mike@visie.com.br', tipo='CP', ref_transacao='compra_n_20050')
      if f.id == '1':
        carrinho.item(id='ASDFG15', desc='Bola quadrada', qtd=2, valor=14)
      if f.id == '2':
        carrinho.item(id='ASDFG19', desc='Carrinho HotWeels', qtd=3, valor=21)
      if f.id == '3':
        carrinho.item(id='ADDAG11', desc='Boneca Barbicha', qtd=1, valor=95.2)


      cart = carrinho.mostra(imprime=False, imgBotao=4)
    return lasagna.run("templates/index.pt", {
      'carrinho': cart,
    })


# Para manipular o retorno, eis o método

def manipularRetorno(args):
  print 'Executando a função somente se for validado!'


class retornoAutomatico:
  def GET(self):
    return ''
  def POST(self):
    ##############################################################################
    # Fazendo a validação via retorno automático funcionar.                      #
    # O método retorno recebe um dicionário de inputs, o token e uma função      #
    # de manipulação, que será executada caso a validação junto ao pagseguro     #
    # seja válida.                                                           =D  #
    ##############################################################################
    pagseguro.retorno(web.input(), token, manipularRetorno)

    return 'Obrigado por comprar conosco!'

if __name__=="__main__":
  app.run()