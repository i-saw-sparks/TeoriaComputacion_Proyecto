"""
Estados:
0 - Estable
1-Hidratada   2-Sobre Hidratada   3-Ahogada
4-Asoleada    5-Muy asoleada      6-Quemada
7-Fertilizado 8-Sobre Fertilizado 9-Podrida
10-Saludable  11-Intoxicada       12-Muy intoxicada
13-Muerta

Entradas:
0-Regar
1-Asolear
2-Fertilizar
3-Pesticida
"""
n_states = 14;
n_inputs = 4;
transiciones = [[0 for x in range(n_states)] for y in range(n_inputs)]

current_state = 0;

def suma():
    return 1+2