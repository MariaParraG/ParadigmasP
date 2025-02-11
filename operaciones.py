def S(n):
    return n + 1

def A(n):
    return n - 1 if n > 0 else 0

def suma(a, b):
    if b == 0:
        return a
    return suma(S(a), A(b))

def multiplicacion(a, b):
    if b == 0:
        return 0
    return suma(a, multiplicacion(a, A(b)))

def resta(a, b):
    if b == 0:
        return a
    if a == 0:
        return 0
    return resta(A(a), A(b))

def division(a, b):
    if b == 0:
        raise ValueError("División por cero no está definida en los Naturales.")
    if a < b:
        return 0
    return S(division(resta(a, b), b))

if __name__ == "__main__":
    print("Suma 3 + 2 =", suma(3, 2))
    print("Multiplicación 3 * 2 =", multiplicacion(3, 2))
    print("Resta 5 - 3 =", resta(5, 3))
    print("División 6 / 2 =", division(6, 2))
