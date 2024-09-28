import pandas as pd

# Carregar os critérios de pontuação do arquivo Excel (ou você já pode ter esses valores diretamente no código)
criterios = {
    'ATA': {'V': 7, 'E': 0, 'D': -4, 'GOL': 7, 'ASS': 4, 'STG': 2, 'GC': -10, 'AMA': -4, 'AZUL': -8, 'VER': -16, 'PP': -10, 'GS': 0, 'DD': 0, 'DP': 0},
    'MEI': {'V': 7, 'E': 0, 'D': -4, 'GOL': 8.5, 'ASS': 5, 'STG': 2.5, 'GC': -10, 'AMA': -4, 'AZUL': -8, 'VER': -16, 'PP': -10, 'GS': 0, 'DD': 0, 'DP': 0},
    'ZAG': {'V': 7, 'E': 0, 'D': -4, 'GOL': 10, 'ASS': 6, 'STG': 3, 'GC': -10, 'AMA': -4, 'AZUL': -8, 'VER': -16, 'PP': -10, 'GS': 0, 'DD': 0, 'DP': 0},
    'GK':  {'V': 6, 'E': 0, 'D': -3, 'GOL': 16, 'ASS': 10, 'STG': 4, 'GC': -10, 'AMA': -4, 'AZUL': -8, 'VER': -16, 'PP': -10, 'GS': -5, 'DD': 5, 'DP': 20}
}

# Função para calcular os pontos com base na posição e nos critérios fornecidos
def calcular_pontos(row):
    posicao = row['POSIÇÃO']
    pontos = (row['V'] * criterios[posicao]['V'] +
              row['E'] * criterios[posicao]['E'] +
              row['D'] * criterios[posicao]['D'] +
              row['GOL'] * criterios[posicao]['GOL'] +
              row['ASS'] * criterios[posicao]['ASS'] +
              row['STG'] * criterios[posicao]['STG'] +
              row['GC'] * criterios[posicao]['GC'] +
              row['AMA'] * criterios[posicao]['AMA'] +
              row['AZUL'] * criterios[posicao]['AZUL'] +
              row['VER'] * criterios[posicao]['VER'] +
              row['PP'] * criterios[posicao]['PP'] +
              row['GS'] * criterios[posicao]['GS'] +
              row['DD'] * criterios[posicao]['DD'] +
              row['DP'] * criterios[posicao]['DP'])
    return pontos


df = pd.read_excel('data/testedatasetv2b.xlsx')
df.fillna(0, inplace=True)
df['PTS'] = df.apply(calcular_pontos, axis=1)

df_copas = pd.read_excel('data/copas_mr.xlsx')
df_copas.fillna(0, inplace=True)

df_season = pd.concat([df, df_copas])
df_season.fillna(0, inplace=True)


df_corrida_geral = df_season.groupby('PLAYER').agg({'PTS':'sum', 'GOL':'sum', 'ASS':'sum'})
df_corrida_geral = df_corrida_geral.sort_values(by='PTS', ascending=False)
df_corrida_geral = df_corrida_geral.reset_index()
lider_geral = df_corrida_geral.iloc[0]['PLAYER']

#table
df_table = df_season.groupby('PLAYER').agg({'V':'sum', 'E':'sum', 'D':'sum', 'GOL':'sum', 'ASS':'sum', 'STG':'sum','AMA':'sum', 'AZUL':'sum', 'VER':'sum','FALTA':'sum', 'PTS':'sum'})
df_table = df_table.sort_values(by='PTS', ascending=False)
df_table = df_table.reset_index()
df_table['POS'] = df_table.index.values + 1

#algumas variáveis
lista_partidas = df['PARTIDA'].to_list()
lista_partidas_copas = df_copas['PARTIDA'].to_list()
n_partidas_totais = lista_partidas[-1] + lista_partidas_copas[-1]
n_rodadas_liga = df['RODADA'].unique()[-1]
n_rodadas_copa = df_copas['RODADA'].unique()[-1]

df_top_cinco_artilheiros = df_corrida_geral.sort_values(by='GOL', ascending=False)  
df_top_cinco_artilheiros = df_top_cinco_artilheiros.reset_index()
df_top_cinco_artilheiros = df_top_cinco_artilheiros.drop('index', axis=1)
df_top_cinco_artilheiros = df_top_cinco_artilheiros.iloc[0:5]

df_top_cinco_assistencia = df_corrida_geral.sort_values(by='ASS', ascending=False)  
df_top_cinco_assistencia = df_top_cinco_assistencia.reset_index()
df_top_cinco_assistencia = df_top_cinco_assistencia.drop('index', axis=1)
df_top_cinco_assistencia = df_top_cinco_assistencia.iloc[0:5]

n_gols_temporada = df_season['GOL'].sum()

df_gk = df_season.loc[df_season['POSIÇÃO']=='GK']
df_gk = df_gk.loc[df_gk['PLAYER']!='GK sub']
df_gk = df_gk.loc[df_gk['PLAYER']!='Carlos GK']
df_gk = df_gk.loc[df_gk['PLAYER']!='Victor GK']
df_goleiros_gs = df_gk.groupby('PLAYER').agg({'STG':'mean','GS':'mean','DD':'mean'})
df_goleiros_gs = df_goleiros_gs.sort_values(by='GS', ascending=True)
df_goleiros_gs = df_goleiros_gs.reset_index()

df_liga = pd.read_excel('data/testedatasetv2b.xlsx')
df_liga.fillna(0, inplace=True)
df_liga['PTS'] = df_liga.apply(calcular_pontos, axis=1)

df_copa = pd.read_excel('data/copas_mr.xlsx')
df_copa.fillna(0, inplace=True)  
df_season = pd.concat([df_liga, df_copa])


competicoes = df_season['COMPETIÇÃO'].unique()
lista_rodadas_liga = df_liga['RODADA'].unique()
lista_rodadas_copa = df_copa['RODADA'].unique()

rodadas_liga = lista_rodadas_liga.tolist()
rodadas_copa = lista_rodadas_copa.tolist()
len_liga = len(rodadas_liga)
len_rodada = len(rodadas_copa)
total_rodadas_season = len_liga + len_rodada

lista_criterio = ['GOL','ASS','STG', 'GC', 'AMA', 'AZUL', 'VER', 'PP', 'FALTA', 'PTS']

# lista players

lista_players = df_season['PLAYER'].unique()