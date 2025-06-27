def bonAppetit(factura, k, b):
    
    total_sin_articulo = sum(factura) - factura[k]
    
    parte_anna = total_sin_articulo // 2
    
    if parte_anna == b:
        print("Bon Appetit")
    else:
        print(b - parte_anna)

