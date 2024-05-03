import os
from time import sleep

while True:
  print('''Portal Alpha7
[1] Gerador de email
[2] Gerador de comentario''')
  menu = input('Escolha a opcao desejada :')
  os.system('clear')
  if menu == '1'
    print('GERADOR DE EMAIL')
    print('''[1] Email inicial
[2] Email de conclusao''')
    email = input('Escolha a opcao desejada :')
    os.system('clear')
    print('EMAIL INICIAL')
    gdi = input('Digite o numero da gdi: ')
    razao_social = input('Digite a razao social do cliente: ')
    cnpj = input('Digite o CNPJ matriz do cliente: ')
    nome_responsavel = input('Digite o nome do responsavel: ')
    ramal = input('Digite o seu ramal: ')
    caixa_postal = input('Digite a caixa postal do cliente: ')
    senha = input('Digite a senha do cliente: ')
    os.system('clear')
    print(f'''Assunto: GDI-{gdi} - {razao_social} - {cnpj}

Prezados, bom dia!

Seguem informações importantes:

Cliente:
• Operadora responsável pela implantação será {nome_responsavel} no telefone (48) 2106.{ramal] ou (48) 2106.5741, e-mail implantacao.cartoes@nexxera.com
• Estamos aguardando o Documento de Implantação (em anexo) do cliente preenchido conforme orientações do kick-off.
• Site da implantação: https://implantacaoalpha7.nexxera.com/

 Alpha7:
• CNPJ Cliente: {cnpj}
• Caixa postal: {caixa_postal}    
• Senha: {senha}

Em caso de dúvidas, estamos à disposição.''')
