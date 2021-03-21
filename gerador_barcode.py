# requeriments
#deve instalar o python-barcode
#pip install python-barcode[images]

from barcode import Code128
from barcode.writer import ImageWriter

#Gera o código de barras e salvar no caminho desejado
with open(r'test1.jpeg', 'wb') as f:
    Code128('210321000101', writer=ImageWriter()).write(f)


