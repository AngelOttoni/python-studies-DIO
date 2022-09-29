import sys;

def icm():
    distancia = int(input("Digite a distância entre as torres: "))
    diametro1 = int(input("Digite o diâmetro do Palantír de Sauron: "))
    diametro2 = int(input("Digite o diâmetro do Palantír de Saruman: "))
    return (float(distancia / (diametro1 + diametro2)))

print(f"O valor total de Interferência de Comunicação Mágica (ICM) é de {icm():,.2f}")


#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

# entrada = input().split()

# distancia = int(entrada[0])
# diametro1 = int(entrada[1])
# diametro2 = int(entrada[2])

# print(f"O valor total de Interferência de Comunicação Mágica é de {distancia/(diametro1+diametro2):.2f}")


#-------------------------------------------------------------------------
# def get_value_user():
#     distancia = int(input("Digite a distância entre as torres: "))
#     diametro1 = int(input("Digite o diâmetro do Palatir de Sauron: "))
#     diametro2 = int(input("Digite o diâmetro do Palatir de Saruman: "))
    #icm = (float(distancia / (diametro1 + diametro2)))
    #print(f"O valor total de Interferência de Comunicação Mágica é de {icm:,.2f}")
    
#get_value_user()


#-------------------------------------------------------------------------

# distancia, diametro1, diametro2 = list(map(int,input().split(" ")))


# def icm():
#     return distancia / (diametro1 + diametro2)

# print(f"O valor total de Interferência de Comunicação Mágica (ICM) é de {icm():.2f}")