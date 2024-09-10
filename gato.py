import random
import time

from os import system

# Imprime el tablero
def mostrar_tablero(tablero):
    for fila in tablero:
        print("|".join(fila))
        print("-" * 7)

# Verifica si hay un ganador
def winner_check(tablero, jugador):
    # Verificar filas y columnas
    for i in range(4):
        if all([tablero[i][j] == jugador for j in range(4)]) or all([tablero[j][i] == jugador for j in range(4)]):
            return True
        
    #Verificacion de diagonales
    if tablero[0][0] == jugador and tablero[1][1] == jugador and tablero[2][2] == jugador and tablero[3][3] == jugador:
        return True
    if tablero[0][3] == jugador and tablero[1][2] == jugador and tablero[2][1] == jugador and tablero[3][0] == jugador:
        return True
    return False

# Verifica si el tablero está lleno
def tablero_lleno(tablero):
    return all([cell != " " for fila in tablero for cell in fila])

# Movimiento del jugador
def turno_jugador(tablero):
    while True:
        fila = int(input("Elige una fila (1, 2, 3, 4): ")) - 1
        columna = int(input("Elige una columna (1, 2, 3, 4): ")) - 1
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = "X"
            break
        else:
            print("Posición ocupada, intenta nuevamente.")

# Movimiento de la computadora (al azar)
def turno_computadora(tablero):
    movimientos_computadora = [(i, j) for i in range(4) for j in range(4) if tablero[i][j] == " "]
    movimiento = random.choice(movimientos_computadora)
    tablero[movimiento[0]][movimiento[1]] = "O"



tablero = [[" " for _ in range(4)] for _ in range(4)]
mostrar_tablero(tablero)

while True:
    # Movimiento del jugador
    print("Turno del jugador (X):")
    turno_jugador(tablero)
    mostrar_tablero(tablero)
    
    # Verificar si el jugador ganó
    if winner_check(tablero, "X"):
        print("Ganaste mi pa!")
        break
    
    # Verificar si el tablero está lleno
    if tablero_lleno(tablero):
        print("Empataron mi pa!")
        break
    
    # Movimiento de la computadora
    print("Turno de la computadora (O):")
    turno_computadora(tablero)
    print("Procesando jugada...")
    time.sleep(3)
    system("cls")
    mostrar_tablero(tablero)
    
    # Verificar si la computadora ganó
    if winner_check(tablero, "O"):
        print("La computadora te ganó mi pa!")
        break

    # Verificar si el tablero está lleno
    if tablero_lleno(tablero):
        print("Empataron mi pa!")
        break