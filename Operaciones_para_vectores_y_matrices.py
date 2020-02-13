import Numeros_complejos as NC
import math


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
            vector_respuesta.append(NC.suma(v1[i],v2[i]))
            
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
        vector_respuesta.append(NC.producto(c,v[i]))

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
    
def transpuestaMatrizCompleja(A):
    '''La transpuesta de una matriz compleja es cambiar filas por columnas.El
    Resultado es una matriz'''

    
    filas = len(A)
    columnas = len(A[0])
    matriz_respuesta = [[[0,0]]*filas for x in range(columnas)]

    for i in range(filas):
        for j in range(columnas):
            matriz_respuesta[j][i] = A[i][j]

    return matriz_respuesta

def transpuestaVectorComplejo(v):
    '''La transpuesta de un vector complejo es cambiar las filas por la columna.
    El resultado es una matriz'''

    filas = len(v)
    matriz_respuesta = [v]

    return matriz_respuesta

def conjugadaMatrizCompleja(A):
    '''La conjugada de una matriz compleja es hacer el conjugado a cada punto de
    la matriz.El resultado es una matriz'''

    filas = len(A)
    columnas = len(A[0])

    for i in range(filas):
        for j in range(columnas):
            A[i][j] = NC.conjugado(A[i][j])
    return A
    
def conjugadaVectorComplejo(v):
    '''La conjugada de un vector complejo es hacer el conjugado a cada punto del
    vector matriz.El resultado es una matriz'''

    filas = len(v)

    for i in range(filas):
        v[i] = NC.conjugado(v[i])
    return v

def adjuntaMatrizCompleja(A):
    '''La adjunta de una matriz compleja es la transpuesta de la conjugada.El
    resultado es una matriz'''

    return transpuestaMatrizCompleja(conjugadaMatrizCompleja(A))

def adjuntaVectorComplejo(v):
    '''La adjunta de un vector complejo es la transpuesta de la conjugada.El
    resultado es una matriz'''

    return transpuestaVectorComplejo(conjugadaVectorComplejo(v))

def productoMatricialComplejo(A, B):
    '''El produco de dos matrices complejas es solo posible si el numero de
    columas de A es igual al numero de filas de B, de ser asi se multiplica fila
    por columna y se suman los resultados, esto da como resultado cada punto de
    la matriz respuesta.'''


    matriz_respuesta = []
    filasA = len(A)
    columnasA = len(A[0])
    filasB = len(B)
    columnasB = len(B[0])
    try:
        if columnasA != filasB:
            raise NameError('Error. Las matrices no tienen dimensiones compatibles.')
        
    except NameError:
        print("Error. Las matrices no tienen dimensiones compatibles.")
    else:
        matriz_respuesta = [ [[0,0]]*columnasB for x in range(filasA) ]

        for i in range(filasA):
            for j in range(columnasB):
               for k in range(filasB):
                   matriz_respuesta[i][j] = NC.suma(matriz_respuesta[i][j],
                                                  NC.producto(A[i][k], B[k][j]))
        
        
        return matriz_respuesta

def accionMatrizSobreVectorComplejo(A, v):
    '''La accion de una matriz compleja sobre un vector complejos es el producto
    de de estos, cuando son compatibles (igual que en la multiplicacion matricial.
    El restultado es una vector'''

    for x in range(len(v)):
        v[x] = [v[x]]

    return productoMatricialComplejo(A, v)

def productoInternoVectoresComplejos(v1, v2):
    '''El producto interno entre dos vectores <v1,v2> es la adjunta del v1
    multiplicado por el v2. El resultado es un numero complejo'''
    
    return accionMatrizSobreVectorComplejo(adjuntaVectorComplejo(v1), v2)[0][0]

def normaVectorComplejo(v):
    '''La norma de un vector complejo es la raiz cuadrada del producto interno
    de el mismo.El resultado es un entero'''
    v1 = v
    v2 = v[:]
    
    return productoInternoVectoresComplejos(v1, v2)[0]**0.5

def distanciaVectoresComplejos(v1, v2):
    '''La distancia entre dos vectores complejos es la norma de la resta de los
    mismos.El resultado es un entero'''
    return normaVectorComplejo(adicionVectores(v1, inversoAditivoVector(v2)))

def esMatrizUnitaria(A):
    
    filas = len(A)
    columnas = len(A[0])

    if filas != columnas:
        return False
    else:
        I = [[[0,0]]*filas for x in range(columnas)]
        B = [[[0,0]]*filas for x in range(columnas)]
        for i in range(filas):
            for j in range(columnas):
                B[i][j] = A[i][j]
                if i == j:
                    I[i][j] = [1,1]
                    
        return productoMatricialComplejo(A, adjuntaMatrizCompleja(B)) == I

def esMatrizHermitania(A):
    filas = len(A)
    columnas = len(A[0])
    B = [[[0,0]]*filas for x in range(columnas)]
    for i in range(filas):
            for j in range(columnas):
                B[i][j] = A[i][j]
    return adjuntaMatrizCompleja(B) == A
    
#print(adicionVectores([ [8,3],[-1,-4],[0,-9] ],[ [8,-3],[2,5],[3,0] ]))
#print(multiplicacionEscalarVector([-1,1], [ [-2,5],[-1,-1],[2,-9] ]))            
#print(inversoAditivoVector([ [-5,2],[3,0],[0,-1] ]))
#print(adicionMatrices([[ [-8,-3],[-6,-4],[0,-4] ],[ [-1,8],[6,-10],[8,-5] ],[ [4,0],[8,5],[-7,-9]]],
#                      [[ [-7,-2],[-4,-2],[7,7] ],[ [5,9],[0,3],[6,-5] ],[ [1,5],[-6,-6],[5,8] ]]))
#print(multiplicacionEscalarMatriz([-2,3],
#                                  [[ [3,-2],[8,-4] ],[ [4,-10],[-2,-8]]]))
#print(inversoAditivoMatriz([ [ [7,3],[-1,7] ],[ [-9,-4],[-7,-9] ]]))
#print(transpuestaMatrizCompleja([ [[5,9],[-7,-5],[-1,-4]],[[8,2],[-3,-7],[7,-8]] ]))
#print(transpuestaVectorComplejo([ [1,1],[2,2] ]))
#print(conjugadaMatrizCompleja( [ [[-6,1],[3,8]],[[2,-6],[3,0]]] ))
#print(adjuntaMatrizCompleja( [ [[7,7],[3,8],[8,4]],[[5,0],[8,-6],[-10,-1]]] ))
#print(productoMatricialComplejo( [ [[-6,2],[0,6],[7,2]],[[6,9],[7,7],[-6,-6]],[[5,8],[-6,8],[6,9]] ],
#                                 [ [[9,-6],[-3,-4],[5,-2]],[[3,6],[-1,-5],[0,-5]],[[9,9],[8,-4],[-8,-4]] ]))
#print(productoMatricialComplejo( [[[2,1],[3,0],[1,-1]],[[0,0],[0,-2],[7,-3]],[[3,0],[0,0],[1,-2]]],
#                                 [[[0,-1],[1,0]],[[0,0],[0,1]]]))
#print(accionMatrizSobreVectorComplejo( [[[-1,5],[1,-7],[-6,3]],[[-3,-9],[2,-5],[1,-10]],[[-6,5],[6,-5],[3,-2]]],
#                                       [[1,-3],[4,3],[-3,1]]))
#print(productoInternoVectoresComplejos([ [2,-1],[-8,-5],[-2,-6] ],
#                              [ [6,-3],[5,-1],[-6,-2]]))
#print(normaVectorComplejo( [[4,5],[3,1],[0,-7]] ))
#print(distanciaVectoresComplejos( [[2,7],[4,-1],[2,-4]],
#                                  [[7,8],[2,-8],[1,4]]))
#print(esMatrizUnitaria( [ [[1/(2**0.5),0],[0,1/(2**0.5)]],[[0,1/(2**0.5)],[1/(2**0.5),0]] ] ))
print(esMatrizHermitania( [[[],[],[]],[[],[],[]],[[],[],[]]] ))
