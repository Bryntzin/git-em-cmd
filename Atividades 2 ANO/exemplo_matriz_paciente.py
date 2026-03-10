#1- Genero
#2- Casado/solteiro
#3- Filhos

patients=[
    [1,1,0] #luiz
    [0,0,1] #ana
    [1,0,1] #mario
]
def contar_homens_casados(patients):
    return sum(1 for p in patients if p[0]==1 and p[1]==1)

def contar_mulheres_com_filhos(patients):
    return sum(1 for p in patients  if p[0]==0 and p[2]==1)
#executando as funções 

homens_Casados=contar_homens_casados(patients)
mulheres_com_filhos=contar_mulheres_com_filhos(patients)

#exibindo os resultados

print(f"total de homens casados:{homens_Casados}")
print(f"Total de mulheres com filhos:{mulheres_com_filhos}")