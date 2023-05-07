def calcular():
    monto_inicial = float(input("Ingresar el monto inicial (sin puntos ni comas): "))
    monto_inicial_mostrar = f"${monto_inicial:,.2f}"
    while True:
        cant_meses = input("Ingresar cantidad de meses a calcular: ")
        if cant_meses.isdigit() and int(cant_meses) >= 1:
            cant_meses = int(cant_meses)
            break
        else:
            print("Ingresar un valor valido para los meses")
    porcentaje = float(input("Ingresar el porcentaje ANUAL(sin el signo de %): "))
    if cant_meses > 1:
        agregar_monto_fijo = input("Desea agregar un monto fijo TODOS los meses? (Responder solo con S / N)")
        if agregar_monto_fijo == 'S' or agregar_monto_fijo == 's':
            suma_monto_fijo = float(input("Cuanto es el monto para agregar todos los meses? "))
        else:
            suma_monto_fijo = 0
        # Inicializa la lista de importes mensuales fijos en cero
        importes_mensuales_fijos = [0] * cant_meses

        while True:
            agregar_monto_fijo_mensual = input("Desea agregar un monto fijo en algún mes? (Responder solo con S / N)")
            if agregar_monto_fijo_mensual != 'S' and agregar_monto_fijo_mensual != 's':
                break
            else:
                num_mes_agregar = int(input("En qué mes se agregaría ese importe? "))
                monto_mensual_fijo = float(
                    input("Cuánto es el monto para agregar en el mes " + str(num_mes_agregar) + '? '))
                importes_mensuales_fijos[num_mes_agregar - 1] = monto_mensual_fijo

    porcentaje_mensual = (porcentaje / 100) / 12
    for mes in range(cant_meses):
        if mes >= 1 and suma_monto_fijo:
            monto_inicial = monto_inicial + suma_monto_fijo
        for i, importe_agregar in enumerate(importes_mensuales_fijos):
            if i == mes:  # compara el índice con el mes actual
                monto_inicial += importe_agregar  # suma el importe al monto inicial
        interes_mensual = (monto_inicial * porcentaje_mensual)
        interes_mensual_formato = f"${interes_mensual:,.2f}"
        interes_mensual_formato = interes_mensual_formato.rjust(15)
        monto_final = monto_inicial + interes_mensual
        monto_final_formato = f"${monto_final:,.2f}"
        monto_final_formato = monto_final_formato.rjust(15)
        print("Para el mes " + str(mes+1).zfill(2) + " el interes es de: " + interes_mensual_formato + ".       El monto que queda a fin de este mes es: " + monto_final_formato)
        monto_inicial = monto_final


if __name__ == '__main__':
    calcular()
