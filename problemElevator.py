# Cristian Camilo Tabares Perez

def elevator(pisosArray, pisoInicial, pisosIngresados, estadoElevador):
    flag = True
    pisoActual = pisoInicial+1
    estadoElevador = "Subiendo"
    
    print(f"Elevado en piso {pisoInicial}")
    print(f"Elevador {estadoElevador}")
    while len(pisosArray) != 0:
        
        # Las impresiones del elevador cuando esta subiendo
        while estadoElevador == "Subiendo" and pisoActual < 30:
            low, hi = float("inf"), -float("inf") # Se usa para conocer el rango de pisos que se salto sin parar
            if pisoActual in pisosArray:
                
                if pisoActual == 29:
                    estadoElevador = "Descendiendo"
                    
                print(f"Elevador en piso {pisoActual}")
                print("Elevador se detiene")
                print(f"Piso ingresado {pisosIngresados[pisoActual]}")
                print(f"Elevador {estadoElevador}")
                
                # Agrega el piso ingresado unicamente si no se ha ingresado antes
                if pisosIngresados[pisoActual] not in pisosArray:
                    pisosArray.append(pisosIngresados[pisoActual])
                
                # Elimina cada piso una vez el elevador ha parado ahi
                pisosArray.remove(pisoActual)
                pisoActual += 1
            
            else:
                # El elevador avanza de pisos mientras no tenga que parar
                while pisoActual not in pisosArray:
                    if pisoActual < low: low = pisoActual
                    elif pisoActual > hi: hi = pisoActual
                    pisoActual += 1
                
                if low < hi:
                    print(f"Elevador en piso {low}, ... {hi}")
                

        
        # Logica similar pero ahora descendiendo
        pisoActual = 28
        while estadoElevador == "Descendiendo" and pisoActual > 0:
                low, hi = float("inf"), -float("inf")
                if pisoActual in pisosArray:
                    
                    if pisoActual == 1:
                        estadoElevador = "se detiene"
                        
                    print(f"Elevador en piso {pisoActual}")
                    print(f"Elevador {estadoElevador}")
                    
                    pisosArray.remove(pisoActual)
                    pisoActual -= 1
                
                else:
                    while pisoActual not in pisosArray:
                        if pisoActual < low: low = pisoActual
                        if pisoActual > hi: hi = pisoActual
                        pisoActual -= 1
                    
                    if low != hi:
                        print(f"Elevador en piso {hi}, ... {low}")

def main():
    pisosArray = [5, 29, 13, 10]
    pisoInicial = 4
    pisosIngresados = {5:2, 29:10, 13:1, 10:1}
    estadoElevador = "idle"
    
    elevator(pisosArray, pisoInicial, pisosIngresados, estadoElevador)
    
main()