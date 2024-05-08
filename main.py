import re
import os
os.system('cls')
# Texto fornecido
texto = '''Prezados, boa tarde!

Kick Off realizado com o cliente ERIC MARCELO M B VIEIRA, no dia 30/04/2024, pela Implantação Nexxera.
Segue abaixo as informações que levantamos para o início da implantação:
Bancos que serão utilizados: Sicredi, serviços: Conciliação, Pagamento, DDA, Cobrança.
Para a demanda de Cartões: Redecard, 1 CNPJ/Ponto de Venda. Para a demanda de Cartões: Cielo, 2 CNPJ/Ponto de Venda.
Contato chave / ponto focal do projeto: Maria (67)99962-7326
Seguem informações importantes:

Cliente:

• Operador responsável pela implantação será Matheus Silvano no telefone (48)21065255 - ou setor (48)21065218, e-mail implantacao.cartoes@nexxera.com

Alpha7:

• Cliente CNPJ: 08.107.186/0001-94
• Caixa postal: UPAMAMBAI.UPAMAMBAI
• Senha: Upamambai08107186

Qualquer dúvida estamos à disposição.'''

# Expressões regulares para extrair informações específicas

bancos_regex = re.search(r'Bancos que serão utilizados: (.*?), serviços: (.*?)(?=Para a demanda de Cartões)', texto, re.DOTALL)
bancos_info = [bancos_regex.group(1).strip() if bancos_regex else None]
servicos_info = bancos_regex.group(2).strip().split(', ')

operadoras_regex = re.findall(r'Para a demanda de Cartões: (.*?),', texto)
operadoras_info = [operadora.strip() for operadora in operadoras_regex]

cnpj_regex = re.search(r'Cliente CNPJ: (.*?)$', texto, re.MULTILINE)
cnpj_info = cnpj_regex.group(1).strip() if cnpj_regex else None

# RESUMO TÉCNICO
operadoras_str = ', '.join(operadoras_info) if len(operadoras_info) > 1 else operadoras_info[0]
bancos_str = ', '.join(bancos_info) if len(bancos_info) > 1 else bancos_info[0]
print(f'''{{panel:title=RESUMO TÉCNICO|borderStyle=dashed|borderColor=#000000|titleBGColor=#97acd1|bgColor=#e0e6ff}}
||ITEM||STATUS||OBS||
|Situação da demanda:|Aguardando DI| |
|Responsável:|Cliente| |
|Ação necessária:|Acompanhar relacionamentos bancários e operadoras.| |
|Instituições contempladas:|Operadoras: {operadoras_str}
Bancos: {bancos_str}| |
|Prazo:|A Definir| |
{{panel}}''')

# OPERADORAS E CNPJ
print('||OPERADORA||CNPJ||EC||STATUS||AÇÃO||')
for operadora in operadoras_info:
    print('''|{operadora}|{cnpj}|(x)|(x)|Aguardando DI preenchido|'''.format(operadora=operadora, cnpj=cnpj_info))

# BANCOS
print('''||BANCO||CNPJ||SERVIÇO||CONTA||AGÊNCIA||STATUS||AÇÃO||''')
for servico in servicos_info:
    print('|SICREDI|08.107.186/0001-94|{servico}|(x)|(x)|(x)|Aguardando relacionamento|'.format(servico=servico))
