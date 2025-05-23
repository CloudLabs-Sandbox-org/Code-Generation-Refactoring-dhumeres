# Programa para extraer cinco cartas de una baraja estándar

import itertools
import random

def draw_cards(num_cards=5):
    # Crear una baraja de cartas (1-13 de cada palo)
    deck = list(itertools.product(range(1, 14), ['Spade', 'Heart', 'Diamond', 'Club']))
    random.shuffle(deck)

    # Verificar que hay suficientes cartas
    if num_cards > len(deck):
        print(f"No hay suficientes cartas en la baraja para extraer {num_cards}.")
        return

    print("You got:")
    for i in range(num_cards):
        value, suit = deck[i]
        print(f"{value} of {suit}")

if __name__ == "__main__":
    draw_cards()