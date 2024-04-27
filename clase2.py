# programa de indice de masa corporal
"""
imc                 diagnostico
bajo peso           <18.5
peso normal         18.5-24.9
sobrepeso           25-29.9
obesidad tipo 1     30-34.9
obesidad tipo 2     35-39.9
obesidad tipo 3     >=40
"""

def imc_peso(peso):

    if not peso > 18.5:
        return print("Bajo Peso")
    
    if not 18.5 < peso > 24.9:
        return print("peso normal")
    
    if not 25 < peso > 29.9:
        return print("sobrepeso")
    
    if not 30 < peso > 34.9:
        return print("obesidad tipo 1")
    
    if not 35 < peso > 39.9:
        return print("obesidad tipo 2")
    
    if not peso < 40:
        return print("obesidad tipo 3")
    

imc_peso(34.7)
