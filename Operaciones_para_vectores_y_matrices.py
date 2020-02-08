import Numeros_complejos as NC


def adicionVectores(v1,v2):
    '''La adicion de dos vectores complejos es posible si ambos tienen la misma
    cantidad de filas, se hace punto a punto.El resultado es un vector'''
    
    vector_respuesta = []
    try:
        a = len(v1) - len(v2)
        if a != 0:
            raise NameError('Vectores con diferentes dimensiones')
        
    except NameError:
        print("No se puede sumar los vectores porque no son compatibles")
    else:
        
        for i in range(0,len(v1)):
            aux = []
            aux.append(NC.suma(v1[i],v2[i]))
            vector_respuesta.append(aux)
        return vector_respuesta

def inversoAditivoVector(v):
    '''El inverso aditivo de un vector complejo es el resultado de multiplicar
    -1 a todo el vector. El resultado es un vector'''

    return multiplicacionEscalarVector([-1,0], v)

def multiplicacionEscalarVector(c,v):
    '''La multiplicacion de un escalar por un vector se realiza multiplicando
    cada punto del vector por el escalar. El resultado es un vector'''

    vector_respuesta = []
    for i in range(0, len(v)):
        vector_respuesta.append([NC.producto(c,v[i])])

    return vector_respuesta

def adicionMatrices(A,B):
    '''La adicion de matrices es posible si ambas matrices tienen el mismo
    numero de flas y de columas. El resultado es una matriz'''

    matriz_respuesta = []
    try:
        filas = len(A)-len(B)
        columnas = len(A[0]) - len(B[0])
        if filas != 0 and columnas != 0:
            raise NameError('Matrices con diferentes dimensiones')
    except NameError:
        print('No se pueden sumar las matrices porque no son compatibles')

    else:
        for i in range(0, len(A)):
            aux_fila = []
            for j in range(0, len(A[0])):
                aux_fila.append(NC.suma(A[i][j], B[i][j]))
            matriz_respuesta.append(aux_fila)

        return matriz_respuesta

def multiplicacionEscalarMatriz(c, A):
    '''La multiplicacion de un escalar por un vector se realiza multiplicando
    cada punto de la matriz por el escalar. El resultado es una matriz'''

    matriz_respuesta = []

    for i in range(0, len(A)):
            aux_fila = []
            for j in range(0, len(A[0])):
                aux_fila.append(NC.producto(c, A[i][j]))
            matriz_respuesta.append(aux_fila)

    return matriz_respuesta

def inversoAditivoMatriz(A):
    '''El inverso aditivo de una matriz compleja es el resultado de multiplicar
    -1 a toda la matriz. El resultado es una matriz'''

    return multiplicacionEscalarMatriz([-1,0],A)
    
    
                

#print(adicionVectores([ [8,3],[-1,-4],[0,-9] ],[ [8,-3],[2,5],[3,0] ]))
#print(multiplicacionEscalarVector([-1,1], [ [-2,5],[-1,-1],[2,-9] ]))            
#print(inversoAditivoVector([ [-5,2],[3,0],[0,-1] ]))
#print(adicionMatrices([[ [-8,-3],[-6,-4],[0,-4] ],[ [-1,8],[6,-10],[8,-5] ],[ [4,0],[8,5],[-7,-9]]],
#                      [[ [-7,-2],[-4,-2],[7,7] ],[ [5,9],[0,3],[6,-5] ],[ [1,5],[-6,-6],[5,8] ]]))
#print(multiplicacionEscalarMatriz([-2,3],
#                                  [[ [3,-2],[8,-4] ],[ [4,-10],[-2,-8]]]))
print(inversoAditivoMatriz([ [ [7,3],[-1,7] ],[ [-9,-4],[-7,-9] ]]))
