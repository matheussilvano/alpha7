import re
import os
os.system('cls')

# Texto fornecido
texto = input('Insira o comentário pós kick-off: ')

# Expressões regulares para extrair informações específicas

bancos_regex = re.search(r'Bancos que serão utilizados: (.*?), serviços: (.*?)(?=Para a demanda de Cartões)', texto, re.DOTALL)
bancos_info = [bancos_regex.group(1).strip() if bancos_regex else None]
servicos_info = bancos_regex.group(2).strip().split(', ')

operadoras_regex = re.findall(r'Para a demanda de Cartões: (.*?),', texto)
operadoras_info = [operadora.strip() for operadora in operadoras_regex]

cnpj_regex = re.search(r'Cliente CNPJ: (.*?)[•]', texto, re.MULTILINE)
cnpj_info = cnpj_regex.group(1).strip() if cnpj_regex else None

# RESUMO TÉCNICO
os.system('cls')
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
    print(f'''|{operadora}|{cnpj_info}|(x)|(x)|Aguardando DI preenchido|''')

# BANCOS
print('''||BANCO||CNPJ||SERVIÇO||CONTA||AGÊNCIA||STATUS||AÇÃO||''')
for banco in bancos_info:
    for servico in servicos_info:
        print(f'|{banco}|{cnpj_info}|{servico}|(x)|(x)|(x)|Aguardando relacionamento|')
