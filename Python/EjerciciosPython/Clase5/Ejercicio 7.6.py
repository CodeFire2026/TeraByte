#Ejercicio 4: Calculadora de Impuestos}
#Crear una función para calcular el total de un pago incluyendo
#un impuesto apLicado(IVA)
#Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto *impuestos/100)
#Proporcione el monto del impuesto: 21%
#Pago con impuesto: xxxxxx



def calcular_pago_total (pago_sin_impuestos, impuesto_porcentaje):
    total = pago_sin_impuestos + (pago_sin_impuestos * impuesto_porcentaje / 100)
    return total

monto_usuario = float(input('ingrese el monto sin impuestos: '))
iva =  21
resultado = calcular_pago_total(monto_usuario , iva)

print(f'El pago con impuestos a pagar es: {resultado}')