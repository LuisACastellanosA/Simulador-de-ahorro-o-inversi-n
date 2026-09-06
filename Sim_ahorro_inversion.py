
import random

ARCHIVO_HISTORIAL = "historial.txt"
VARIACION_MAXIMA = 2  # puntos porcentuales que puede variar la tasa cada año


#----- funciones de cálculo -----

def tasa_mensual_equivalente(tasa_anual):
    return (tasa_anual / 100) / 12


def simular_ahorro(monto_mensual, tasa_anual, meta, anios_max):
    balance = 0
    lista_balances = []
    mes_meta = -1
    mes_actual = 0

    for anio in range(anios_max):
        tasa_anual_del_anio = tasa_anual + random.uniform(-VARIACION_MAXIMA, VARIACION_MAXIMA)
        tasa_mensual_del_anio = tasa_mensual_equivalente(tasa_anual_del_anio)

        for mes in range(12):
            balance += monto_mensual
            balance += balance * tasa_mensual_del_anio
            mes_actual += 1
            lista_balances.append([mes_actual, balance])

            if balance >= meta and mes_meta == -1:
                mes_meta = mes_actual

    return lista_balances, mes_meta


# ===== funciones de archivo =====

def guardar_simulacion(monto_mensual, tasa_anual, meta, mes_meta):
    with open(ARCHIVO_HISTORIAL, "a") as archivo:
        archivo.write(
            f"Ahorro mensual: ${monto_mensual} | Tasa anual base: {tasa_anual}% | "
            f"Meta: ${meta} | Mes en que se alcanzó: {mes_meta}\n"
        )


def mostrar_historial():
    try:
        with open(ARCHIVO_HISTORIAL, "r") as archivo:
            print(archivo.read())
    except FileNotFoundError:
        print("Todavía no hay simulaciones guardadas.")


# ===== programa principal =====

def main():
    print("=== Simulador de Ahorro e Inversión ===")
    print("(la tasa de interés varía un poco cada año, simulando un mercado real)\n")

    monto_mensual = float(input("¿Cuánto puedes ahorrar cada mes? $"))
    tasa_anual = float(input("¿Cuál es la tasa de interés anual (%)? "))
    meta = float(input("¿Cuál es tu meta de ahorro? $"))
    anios_max = int(input("¿En cuántos años como máximo quieres revisarlo? "))

    lista_balances, mes_meta = simular_ahorro(monto_mensual, tasa_anual, meta, anios_max)

    balance_final = lista_balances[-1][1]
    print(f"\nSaldo final tras {anios_max} años: ${balance_final:.2f}")

    if mes_meta != -1:
        anios = mes_meta // 12
        meses = mes_meta % 12
        print(f"¡Alcanzas tu meta en el mes {mes_meta} (aprox. {anios} años y {meses} meses)!")
    else:
        print("No alcanzas tu meta dentro del periodo simulado.")

    guardar = input("\n¿Quieres guardar esta simulación? (s/n) ")
    if guardar.lower() == "s":
        guardar_simulacion(monto_mensual, tasa_anual, meta, mes_meta)
        print("Simulación guardada.")

    ver_historial = input("¿Quieres ver simulaciones anteriores? (s/n) ")
    if ver_historial.lower() == "s":
        mostrar_historial()

    print("\n¡Gracias por usar el simulador!")


if __name__ == "__main__":
    main()
