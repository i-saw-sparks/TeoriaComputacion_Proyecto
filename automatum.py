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


class Automatum:
    # transiciones[estado_actual][input] = siguiente estado

    transition_tab = [[1, 4, 7, 10],  # state 0
                      [2, 0, 1, 10],  # state 1
                      [3, 1, 2, 2],  # state 2
                      [13, 2, 3, 3],  # state 3
                      [0, 5, 7, 4],  # state 4
                      [4, 6, 5, 5],  # state 5
                      [5, 13, 6, 6],  # state 6
                      [7, 0, 8, 10],  # state 7
                      [8, 7, 9, 8],  # state 8
                      [9, 8, 13, 9],  # state 9
                      [0, 10, 10, 11],  # state 10
                      [10, 11, 11, 12],  # state 11
                      [11, 12, 12, 13],  # state 12
                      [13, 13, 13, 13]]  # state 13

    current_state = 0

    def get_image(self):
        return "state" + str(self.current_state) + ".jpeg"

    def get_next_state(self, input):
        self.current_state = self.transition_tab[self.current_state][input]
        return self.current_state

    def get_next_state_image(self, input):
        self.current_state = self.transition_tab[self.current_state][input]
        return "state" + str(self.current_state) + ".jpeg"
