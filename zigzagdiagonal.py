def leer_matriz(n, m):
    matriz = []
    for i in range (n):
        while True:
            try:
                fila = list(map(int, input().split()))
                if len(fila) !=m:
                    raise ValueError(f"Error la fila {i+1} debe tener {m} elementos")
                matriz.append(fila)
                break
            except ValueError as e:
                print(e)
                print("Por favor, ingrese ka fila correctamente")
    return matriz


def recorrido_diagonal(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    col = 0
    recorrido =[]

    recorrido.append(matriz[0][0])
    recorrido.append(matriz[0][1])
    recorrido.append(matriz[1][0])
        
    for d in range(2,-1, -1):
        recorrido.append(matriz[d][col])
        col=col+1

    recorrido.append(matriz[1][columnas-1])
    recorrido.append(matriz[filas-1][1])
    recorrido.append(matriz[filas-1][columnas-1])
        
    return recorrido

try:
    n, m = map(int, input("Ingrese el tamanño de la matriz (N, M): ").split())
    if n <= 0 or m <= 0:
        raise ValueError("Error, M y N deben ser mayores que 0")
        
    print("Ingrese la matriz: ")

    matriz = leer_matriz(n, m)

    recorrido= recorrido_diagonal(matriz)

    print("Recorrido:")
    print(" ".join(map(str, recorrido)))
except ValueError as e:
    print(e)