from main import *

def test_somar():
    assert somar(10, 10) == 20

def test_subtrair():
    assert subtrair(10, 10) == 0

def test_multiplicar():
    assert multiplicar(10, 10) == 100

def test_dividir():
    assert dividir(10, 5) == 2.0

def test_resto():
    assert resto(9, 2) == 1

print(somar(10, 10))
print(subtrair(10, 10))
print(multiplicar(10, 10))
print(dividir(10, 5))
print(resto(9, 2))

test_somar()
test_subtrair()
test_multiplicar()
test_dividir()
test_resto()