"""
In this problem, the task is to read a code of a product 1, the number of 
units of product 1, the price for one unit of product 1, the code of a 
product 2, the number of units of product 2 and the price for one unit of 
product 2. After this, calculate and show the amount to be paid.

Input
The input file contains two lines of data. In each line there will be 3 
values: two integers and a floating value with 2 digits after the decimal 
point.

Output
The output file must be a message like the following example where "Valor
 a pagar" means Value to Pay. Remember the space after ":" and after "R$" 
 symbol. The value must be presented with 2 digits after the point.
"""

linha1 = input().split()
codigo_produto_1 = int(linha1[0])
unidades_produto_1 = int(linha1[1])
preco_unidade_produto_1 = float(linha1[2])

linha2 = input().split()
codigo_produto_2 = int(linha2[0])
unidades_produto_2 = int(linha2[1])
preco_unidade_produto_2 = float(linha2[2])

valor_a_pagar = (unidades_produto_1 * preco_unidade_produto_1) + (unidades_produto_2 * preco_unidade_produto_2)

print(f"VALOR A PAGAR: R$ {valor_a_pagar:.2f}")