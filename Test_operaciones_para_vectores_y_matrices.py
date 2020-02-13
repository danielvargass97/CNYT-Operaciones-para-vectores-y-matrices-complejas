import Operaciones_para_vectores_y_matrices as OVM

def test_adicionVectores():
    assert OVM.adicionVectores([ [8,3],[-1,-4],[0,-9] ],[ [8,-3],[2,5],[3,0] ]) == [[16, 0], [1, 1], [3, -9]],''

def test_multiplicacionEscalarVector():
    assert OVM.multiplicacionEscalarVector([-1,1], [ [-2,5],[-1,-1],[2,-9] ]) == [[-3, -7], [2, 0], [7, 11]],''

def test_inversoAditivoVector():
    assert OVM.inversoAditivoVector([ [-5,2],[3,0],[0,-1] ]) == [[5, -2], [-3, 0], [0, 1]],''

def test_adicionMatrices():
    assert OVM.adicionMatrices([[ [-8,-3],[-6,-4],[0,-4] ],[ [-1,8],[6,-10],[8,-5] ],[ [4,0],[8,5],[-7,-9]]],
                      [[ [-7,-2],[-4,-2],[7,7] ],[ [5,9],[0,3],[6,-5] ],[ [1,5],[-6,-6],[5,8] ]]) == [[[-15, -5], [-10, -6], [7, 3]], [[4, 17], [6, -7], [14, -10]], [[5, 5], [2, -1], [-2, -1]]],''

def test_multiplicacionEscalarMatriz():
    assert OVM.multiplicacionEscalarMatriz([-2,3],
                                  [[ [3,-2],[8,-4] ],[ [4,-10],[-2,-8]]]) == [[[0, 13], [-4, 32]], [[22, 32], [28, 10]]],''

def test_inversoAditivoMatriz():
    assert OVM.inversoAditivoMatriz([ [ [7,3],[-1,7] ],[ [-9,-4],[-7,-9] ]]) == [[[-7, -3], [1, -7]], [[9, 4], [7, 9]]],''

def test_transpuestaMatrizCompleja():
    assert OVM.transpuestaMatrizCompleja([ [[5,9],[-7,-5],[-1,-4]],[[8,2],[-3,-7],[7,-8]] ]) == [[[5, 9], [8, 2]], [[-7, -5], [-3, -7]], [[-1, -4], [7, -8]]],''

def test_transpuestaVectorComplejo():
    assert OVM.transpuestaVectorComplejo([ [1,1],[2,2] ]) == [[[1, 1], [2, 2]]],''
    
def test_conjugadaMatrizCompleja():
    assert OVM.conjugadaMatrizCompleja( [ [[-6,1],[3,8]],[[2,-6],[3,0]]] ) == [[[-6, -1], [3, -8]], [[2, 6], [3, 0]]], ''

def test_adjuntaMatrizCompleja():
    assert OVM.adjuntaMatrizCompleja( [ [[7,7],[3,8],[8,4]],[[5,0],[8,-6],[-10,-1]]] ) == [[[7, -7], [5, 0]], [[3, -8], [8, 6]], [[8, -4], [-10, 1]]],''

def test_productoMatricialComplejo():
    assert OVM.productoMatricialComplejo( [ [[-6,2],[0,6],[7,2]],[[6,9],[7,7],[-6,-6]],[[5,8],[-6,8],[6,9]] ],
                                 [ [[9,-6],[-3,-4],[5,-2]],[[3,6],[-1,-5],[0,-5]],[[9,9],[8,-4],[-8,-4]] ]) == [[[-33, 153], [120, 0], [-44, -22]], [[87, 0], [-26, -117], [107, 70]], [[0, 165], [147, 26], [69, -36]]],''
    assert OVM.productoMatricialComplejo( [[[2,1],[3,0],[1,-1]],[[0,0],[0,-2],[7,-3]],[[3,0],[0,0],[1,-2]]],
                                 [[[0,-1],[1,0]],[[0,0],[0,1]]]) == None,''
def test_accionMatrizSobreVectorComplejo():
    assert OVM.accionMatrizSobreVectorComplejo( [[[-1,5],[1,-7],[-6,3]],[[-3,-9],[2,-5],[1,-10]],[[-6,5],[6,-5],[3,-2]]],
                                       [[1,-3],[4,3],[-3,1]]) == [[[54, -32]], [[0, 17]], [[41, 30]]],''

def test_productoInternoVectoresComplejos():
    assert OVM.productoInternoVectoresComplejos([ [2,-1],[-8,-5],[-2,-6] ],
                              [ [6,-3],[5,-1],[-6,-2]]) == [4, 1],''

def test_normaVectorComplejo():
    assert OVM.normaVectorComplejo( [[4,5],[3,1],[0,-7]] ) == 10.0,''
    
def test_distanciaVectoresComplejos():
    assert OVM.distanciaVectoresComplejos( [[2,7],[4,-1],[2,-4]],
                                  [[7,8],[2,-8],[1,4]]) == 12.0,''
def test_esMatrizUnitaria():
    assert OVM.esMatrizUnitaria( [ [[1/(2**0.5),0],[0,1/(2**0.5)]],[[0,1/(2**0.5)],[1/(2**0.5),0]] ] ) == True,''
    assert OVM.esMatrizUnitaria( [[[0,1],[1,0],[0,0]],[[0,0],[0,1],[1,0]],[[1,0],[0,0],[0,1]]] ) == False,''
    
def test_esMatrizHermitania():
    assert OVM.esMatrizHermitania( [[[3,0],[2,-1],[0,-3]],[[2,1],[0,0],[1,-1]],[[0,3],[1,1],[0,0]]] ) == True,''
    assert OVM.esMatrizHermitania( [[[1,0],[3,-1]],[[3,1],[0,1]]] ) == False,''
def test_productoTensorial():
    assert OVM.productoTensorial( [[[1,1],[0,0]],[[1,0],[0,1]]],
                         [[[-1,2],[-2,-2],[0,2]],[[2,3],[3,1],[2,2]],[[-2,1],[1,-1],[2,1]]]) == [[[-3, 1], [0, -4], [-2, 2], [0, 0], [0, 0], [0, 0]], [[-1, 5], [2, 4], [0, 4], [0, 0], [0, 0], [0, 0]], [[-3, -1], [2, 0], [1, 3], [0, 0], [0, 0], [0, 0]], [[-1, 2], [-2, -2], [0, 2], [-2, -1], [2, -2], [-2, 0]], [[2, 3], [3, 1], [2, 2], [-3, 2], [-1, 3], [-2, 2]], [[-2, 1], [1, -1], [2, 1], [-1, -2], [1, 1], [-1, 2]]],''

    
if __name__ == '__main__':
    test_adicionVectores()
    test_multiplicacionEscalarVector()
    test_inversoAditivoVector()
    test_adicionMatrices()
    test_multiplicacionEscalarMatriz()
    test_inversoAditivoMatriz()
    test_transpuestaMatrizCompleja()
    test_transpuestaVectorComplejo()
    test_conjugadaMatrizCompleja()
    test_adjuntaMatrizCompleja()
    test_productoMatricialComplejo()
    test_accionMatrizSobreVectorComplejo()
    test_productoInternoVectoresComplejos()
    test_normaVectorComplejo()
    test_distanciaVectoresComplejos()
    test_esMatrizUnitaria()
    test_esMatrizHermitania()
    test_productoTensorial()
    print('Prueba exitosa')
