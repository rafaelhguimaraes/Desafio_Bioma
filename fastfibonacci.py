# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
import math

def fibonacci():
    n = int( input() )                  # converte a string lida em int
    while n > 50:
        n = int( input() )              # entrada sempre tem que ser <= que 50
    oper1 =  pow ( ( (1 + math.sqrt(5))  / 2 ), n) # parte 1 da formula
    oper2 =  pow ( ( (1 - math.sqrt(5))  / 2 ), n) # parte 2 da formula
    result = ( oper1 - oper2 ) / math.sqrt(5)      # formula completa
    print('%.1f'%result)                        
    
    
fibonacci()

    