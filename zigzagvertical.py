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

def recorrido_zigzag(matriz, n):
    resultado = []
    for j in range(n):
        if j % 2 == 0:
            for i in range(len(matriz)):
                resultado.append(matriz[i][j])  
        else:
            for i in range(len(matriz)-1, -1, -1):
                resultado.append(matriz[i][j])  
    return resultado


try:
    n, m = map(int, input("Ingrese el tamanño de la matriz (N, M): ").split())
    if n <= 0 or m <= 0:
        raise ValueError("Error, M y N deben ser mayores que 0")
        
    print("Ingrese la matriz A: ")
    matriz = leer_matriz(n, m)
    zigzag_resultado = recorrido_zigzag(matriz, n)


    print("Matriz en zig zag:")
    print(" ".join(map(str, zigzag_resultado)))
    

except ValueError as e:
    print(e)