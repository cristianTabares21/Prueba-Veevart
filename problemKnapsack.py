
# Cristian Camilo Tabares Perez

# Solucion de knapsack con memorización
def knapsack(elements, cap, idx, memo):
    ans = 0
    # Si la solucion ya se ha calculado antes, solo la obtiene de la memoria
    if (idx, cap) in memo:
        ans = memo[(idx, cap)]
        
    else:
        if idx == 0 or cap == 0: ans = 0 # si ya se llego a la primera posicion o no hay mas capacidad, la respuesta es 0
        elif elements[idx-1][0] > cap: knapsack(elements, cap, idx-1, memo) # Si el peso del objeto es superior a la capacidad de la mochina, solo avanza al siguiente
        else:
            # Calcula la mejor opcion entre avanzar sin llevar el objeto y llevandolo
            ans = max(knapsack(elements, cap, idx-1, memo), knapsack(elements, cap-elements[idx-1][0], idx-1, memo) + elements[idx-1][1])
        memo[(idx, cap)] = ans
    return ans


def main():
    # (wi, vi) cada tupla representa el peso del objeto y el beneficio que otorga
    elements = [(2, 3), (3, 4), (4, 5), (5, 6)]
    cap = 8 # Capacidad maxima de la mochila
    memo = {}
    
    # La funcion unicamente retorna el beneficio obtenido
    ans = knapsack(elements, cap, len(elements), memo)
    print(f"Beneficio obtenido: {ans}")
    
main()