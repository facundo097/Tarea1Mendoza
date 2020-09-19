class ERROR(Exception):
    pass


def basic_ops(x, y, z):  # define función
    x_digit = x.lstrip('-').isdigit()  # valida si es número entero
    if x_digit is False:  # si no es número entero...
        raise ERROR("Un valor no es un número entero.")  # código error
    elif int(x) > 127 or int(x) < -127:  # si es mayor a 127 o menor a -127...
        raise ERROR("Un número es mayor a 127 o menor a -127.")  # código error
    y_digit = y.lstrip('-').isdigit()  # valida si es número entero
    if y_digit is False:  # si no es número entero...
        raise ERROR("Un valor no es un número entero.")  # código error
    elif int(y) > 127 or int(y) < -127:  # sies mayor a 127 o menor a -127...
        raise ERROR("Un número es mayor a 127 o menor a -127.")  # código error
    z_digit = z.lstrip('-').isdigit()  # valida si es número entero
    if z_digit is False:  # si no es número entero...
        raise ERROR("Un valor no es un número entero.")  # código error
    elif int(z) > 4 or int(z) < 1:  # si es mayor a 127 o menor a -127...
        raise ERROR("El selector de operaciones no es válido.")  # código error
    if int(z) == 1:  # si se seleccionó la operación 1...
        return int(x) + int(y)  # retorna el resultado
    elif int(z) == 2:  # si se seleccionó la operación 2...
        return int(x) - int(y)  # retorna el resultado
    elif int(z) == 3:  # si se seleccionó la operación 3...
        return int(x) & int(y)  # retorna el resultado
    elif int(z) == 4:  # si se seleccionó la operación 4...
        return int(x) | int(y)  # retorna el resultado


def array_ops(x0, x1, x2, x3, x4, y0, y1, y2, y3, y4, z):  # define función
    cont1 = 0  # contador para el arreglo 1
    cont2 = 0  # contador para el arreglo 2
    array1 = [x0, x1, x2, x3, x4]  # declara el arreglo 1
    array2 = [y0, y1, y2, y3, y4]  # declara el arreglo 2
    index = 0
    while cont1 < 5:  # se inicia ciclo que agrega 5 enteros al arreglo 1
        num_digit = array1[index].lstrip('-').isdigit()  # valida si es entero
        if num_digit is False:  # si no es entero...
            raise ERROR("Un valor no es un número entero.")  # código error
        # si es mayor a 127 o menor a -127...
        elif int(array1[index]) > 127 or int(array1[index]) < -127:
            # código error
            raise ERROR("Un número  es mayor a 127 o menor a -127.")
        else:   # si el número es válido...
            cont1 = cont1 + 1  # suma 1 a la condicional del ciclo
            index = index + 1  # pasa al siguiente índice
    index = 0  # resetea el índice
    while cont2 < 5:  # se inicia ciclo que agrega 5 enteros al arreglo 1
        num2_digit = array2[index].lstrip('-').isdigit()  # valida si es entero
        if num2_digit is False:  # si no es entero...
            # código error
            raise ERROR("Un valor no corresponde a un número entero.")
        # si es mayor a 127 o menor a -127...
        elif int(array2[index]) > 127 or int(array2[index]) < -127:
            # código error
            raise ERROR("Un número es mayor a 127 o menor a -127.")
        else:  # si el número es válido...
            cont2 = cont2 + 1  # suma 1 a la condicional del ciclo
            index = index + 1  # pasa al siguiente índice
    # identifica elementos de arreglo 1 como enteros
    array1 = [int(x0), int(x1), int(x2), int(x3), int(x4)]
    # identifica elementos de arreglo 2 como enteros
    array2 = [int(y0), int(y1), int(y2), int(y3), int(y4)]
    z_digit = z.lstrip('-').isdigit()  # valida si es entero
    if z_digit is False:   # si no es entero...
        raise ERROR("Un valor no corresponde a un número entero.")
    # si es mayor a 127 o menor a -127...
    elif int(z) > 4 or int(z) < 1:
        # código error
        raise ERROR("El selector de operaciones introducido no es válido.")
    x = 0  # variable para indexar elementos de los arreglos
    ready = 0  # contador que indica cuando la operación está lista
    res = []  # arreglo resultante de la operación
    if int(z) == 1:  # si se seleccionó la operación 1...
        while ready < 5:  # incia ciclo realiza todas las operaciones
            # realiza operación entre elementos con índice x de cada arreglo
            y = array1[x] + array2[x]
            res.append(int(y))  # agrega resultado de operación a nuevo arreglo
            x = x + 1  # se continua con el siguiente índice
            ready = ready + 1  # suma 1 a la condicional del ciclo
        print('La suma de los arreglos es: ')  # imprime el nuevo arreglo
        return res
    elif int(z) == 2:  # si se seleccionó la operación 2...
        while ready < 5:  # incia ciclo realiza todas las operaciones
            # realiza operación entre elementos con índice x de cada arreglo
            y = array1[x] - array2[x]
            res.append(int(y))  # agrega resultado de operación a nuevo arreglo
            x = x + 1  # se continua con el siguiente índice
            ready = ready + 1  # suma 1 a la condicional del ciclo
        print('La resta de los arreglos es: ')  # imprime el nuevo arreglo
        return res
    elif int(z) == 3:  # si se seleccionó la operación 3...
        while ready < 5:  # incia ciclo realiza todas las operaciones
            # realiza operación entre elementos con índice x de cada arreglo
            y = array1[x] & array2[x]
            res.append(int(y))  # agrega resultado de operación a nuevo arreglo
            x = x + 1  # se continua con el siguiente índice
            ready = ready + 1  # suma 1 a la condicional del ciclo
        print('El AND entre los arreglos es: ')  # imprime el nuevo arreglo
        return res
    elif int(z) == 4:  # si se seleccionó la operación 4...
        while ready < 5:  # incia ciclo realiza todas las operaciones
            # realiza operación entre elementos con índice x de cada arreglo
            y = array1[x] | array2[x]
            res.append(int(y))  # agrega resultado de operación a nuevo arreglo
            x = x + 1  # se continua con el siguiente índice
            ready = ready + 1  # suma 1 a la condicional del ciclo
        print('El OR entre los arreglos es: ')  # imprime el nuevo arreglo
        return res

    def test_basic_ops():
        # Casos de éxito
        assert basic_ops('2', '3', '1') == 5
        assert basic_ops('8', '3', '2') == 5
        assert basic_ops('1', '0', '3') == 0
        assert basic_ops('0', '1', '4') == 1
        # Caso de error por introducir un decimal
        assert basic_ops('2.001', '3', '1') == 5
        # Caso de error por introducir un número mayor a 127
        assert basic_ops('128', '3', '1') == 131
        # Caso de error por introducir un número selector de operación inválido
        assert basic_ops('9', '3', '0') == 1

    def test_array_ops():
        # Casos de éxito
        assert array_ops('1', '2', '3', '4', '5', '1', '2', '3', '4', '5', '1') == [2, 4, 6, 8, 10]
        assert array_ops('1', '2', '3', '4', '5', '1', '2', '3', '4', '5', '2') == [0, 0, 0, 0, 0]
        assert array_ops('1', '0', '1', '0', '1', '1', '1', '0', '0', '1', '3') == [1, 0, 0, 0, 1]
        assert array_ops('1', '0', '1', '1', '0', '0', '1', '0', '1', '0', '4') == [1, 1, 1, 1, 0]
        # Caso de error por introducir un valor no numérico
        assert array_ops('uno', '2', '3', '4', '5', '1', '2', '3', '4', '5', '1') == [2, 4, 6, 8, 10]
        # Caso de error por introducir un número menor a -127
        assert array_ops('-128', '2', '3', '4', '5', '1', '2', '3', '4', '5', '1') == [2, 4, 6, 8, 10]
        # Caso de error por introducir un número selector de operación inválido
        assert array_ops('1', '2', '3', '4', '5', '1', '2', '3', '4', '5', '5') == 1
