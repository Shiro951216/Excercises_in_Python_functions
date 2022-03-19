# Función que devuelve la factorización de un número natural mediante una lista que contiene las siguientes dos listas :
# lista de factores primos
# lista de exponentes

def factorizar(n):

    # Definiendo a n como número natural maayor a 1

    if n > 1 :
        
        # definimos la función que devuelve si un número es primo o no
        
        def primo(n):
            is_primo = True
            for i in range(2,n):
                if n % i == 0:
                    is_primo = False
                    break
            return is_primo
                    
        if primo(n):
            return [[n],[1]]
        
        primos = []

        # Aquí obtendremos la lista de primos menores al número en cuestión y lo agregamos a una lista de números primos(primos)
        
        for i in range(2,n):
            if primo(i):
                primos.append(i)

        f_primos = []

        # Hallamos los factores primos de n y los agregamos a la lista de factores primos (f_primos)
        
        for i in primos:
            if n % i == 0:
                f_primos.append(i)

        potencias = []
        
        # Contamos las veces que puede dividir cada factor primo a n y lo guardamos en la lista de exponentes (potencias)
        
        for i in f_primos:
            count = 0
            while n % i == 0:
                n /= i
                count += 1
            potencias.append(count)

        return [f_primos, potencias]

    else:
        return None
