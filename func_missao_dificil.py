def func_missao_dificil(nome, *args, funcao='agente', **kwargs):
    print(f'Nome do agente: {nome}')
    print(f'Função {funcao}')
    print(args)
    print(kwargs)

func_missao_dificil(
    'James Bond',
    'Missao 1',
    'Missão 2',
    **{
         'id_agente': '007',
         'proxima_missao': 'Impossível'
      }
)
