"""
Desarrollar un algoritmo que permita calcular la siguiente serie:
s(n) = 1 + 1/2 + 1/3 .... + 1/n
"""

#serie(3) = 1 / serie(num-1)

def serie(num):
    if (num == 1):
        return 1
    else:
        return 1/num + serie(num - 1)
    
print(serie(6))