# Si lees esto, 20 años de vida son añadidos a Ricky god :)
# Merge sort
def mergeSort(array,stop_event):
  if len(array) > 1:

    # r is the point or middle from
    #  where the array is divided into two subarrays
    r = len(array)//2

    L = array[:r] # until middle
    M = array[r:] # from middle

    # Sort the two halves
    mergeSort(L,stop_event)
    mergeSort(M,stop_event)

    i = j = k = 0

    # Until we reach either end of either L or M, pick larger among
    # elements L and M and place them in the correct position at the array
    while i < len(L) and j < len(M):
      if L[i] < M[j]:
        array[k] = L[i]
        i += 1
      else:
        array[k] = M[j]
        j += 1
      k += 1
      if stop_event.is_set():
         return
      
    # When we run out of elements in either L or M,
    # pick up the remaining elements and put in A[p..r]
    while i < len(L):
      array[k] = L[i]
      i += 1
      k += 1
      if stop_event.is_set():
         return
    while j < len(M):
      array[k] = M[j]
      j += 1
      k += 1
      if stop_event.is_set():
         return
      

class OrderVec:
    def __init__(self, values: list[int],stop_event) -> None:
        '''
            Constructor

            Args:
                values (list[int]) : [lista que se quiere ordenar]

            Return:

        '''
        self.values = values
        self.heap_sort(stop_event)

    def heapify(self, array: list(), n: int, k: int,stop_event) -> None:
        '''
            Forma un maxHeap

            Args:
                array (list): [Lista que se quiere ordenar]
                n     (int) : [Tamaño de la lista]
                k     (int) : [Indice de la lista]

            Return:

        '''
        # Suponemos que el más grande es el de la posicion k
        mayor = k

        # Indices de los hijos izquierdo y derecho (l & r)
        l = 2 * k + 1
        r = 2 * k + 2

        # Verificamos que no sobrepase el tamaño del arreglo y si la posicion del "más grande" con el valor de la posicion del hijo izq es menor
        if l < n and array[mayor] < array[l]:
            mayor = l 
        
        # Lo mismo de arriba pero con la posicion del hijo derecho
        if r < n and array[mayor] < array[r]:
            mayor = r

        # Hacemos un "swap" en caso tal de que sean distintos al final
        if mayor != k:
            array[k], array[mayor] = array[mayor], array[k]
            self.heapify(array, n, mayor,stop_event)
            
        if stop_event.is_set():
         return
    def heap_sort(self,stop_event) -> None:
        '''
            Ordena la lista

            Args:

            Return:

        '''
        # Definimos el tamaño de nuestro arreglo
        size  = len(self.values)

        # Por temas de optimizacion, se realizara hasta la mitad de los elementos del array y haremos un max heap (arbol donde cada root es mayor que sus hijos)
        for k in range(size//2, -1, -1):
            if stop_event.is_set():
              return
            self.heapify(self.values, size, k,stop_event)


        # Dado nuestro maxHeap anterior, empezamos a extraer los elementos para empezar con el ordenamiento haciendo otro "swap"
        for k in range(size-1, 0, -1):
            if stop_event.is_set():
              return
            self.values[k], self.values[0] = self.values[0], self.values[k]
            # Claramente el indice va a comenzar en 0
            self.heapify(self.values, k, 0,stop_event)
        

def quicksort(a, lo, hi,stop_event):
    """
    Sorts the given list in ascending order using QuickSort algorithm.

    Parameters:
    a (list): List of elements to be sorted.
    lo (int): The lower index of the sub-list to be sorted.
    hi (int): The higher index of the sub-list to be sorted.

    """
    if(lo >= hi):
        return
    p = a[(lo + hi) // 2]       # get pivot as middle element
    i = lo - 1 # lower limit
    j = hi + 1 # upper limit
    while(1): # while 1 can be faster than while True
        while(1):               
            i += 1
            #get position of element greater or equal than pivot
            if(a[i] >= p):
                break
            if stop_event.is_set():
                return
        while(1):               
            j -= 1
            # get position of element smaller or equal than pivot
            if(a[j] <= p):
                break
            if stop_event.is_set():
                return
        if(i >= j):
            break
        # exchange when limits cross
        a[i],a[j] = a[j],a[i]
    #continue recursively
    quicksort(a, lo, j,stop_event)
    quicksort(a, j+1, hi,stop_event)
