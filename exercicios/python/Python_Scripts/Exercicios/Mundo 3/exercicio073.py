times = ('Flamengo', 'Palmeiras','Santos','Grêmio','Athletico','São Paulo',
         'Inter','Corinthians','Bahia','Vasco','Fortaleza','Goias','Atletico','Botafogo','Ceara','Fluminense',
         'Cruzeiro','CSA','Chapecoense','Avai')
print(f'Os 5 primeiros colocados são: {times[:5]}')
print(f'Os 4 últimos colocados são: {times[-4:]}')
print(sorted(times))
print(f'A posição da Chapecoense na tabela é: {times.index("Chapecoense")+1}º colocado')