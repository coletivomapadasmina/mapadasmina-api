import pandas

excel_file = 'mapadasmina.xlsx'
candidates = pandas.ExcelFile(excel_file)
df = candidates.parse('Respostas ao formulário 1')
parties=df['Qual é o seu partido?'].unique()
print(parties)
a=df.to_json