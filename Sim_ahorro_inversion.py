import math
import os
import random

# el historial se guarda siempre junto a este archivo .py
ARCHIVO_HISTORIAL = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 "historial.txt")
VARIACION_MAXIMA = 2.0  # puntos porcentuales que puede variar la tasa por año
TASA_MINIMA = 0.0  # una cuenta de ahorro no paga intereses negativos
TASA_ALTA = 20.0  # arriba de este valor la tasa se considera poco realista
MESES_POR_ANIO = 12
ANIOS_MAXIMOS = 100  # tope para que la simulación no sea demasiado larga
PORCENTAJE_POCO_MARGEN = 90  # meta alcanzada después de este % del plazo


# ===== funciones de entrada =====

def pedir_numero(mensaje, es_entero, acepta_cero, maximo=None):
    """Pide un número no negativo y repite la pregunta hasta que sea válido.

    Recibe: mensaje, es_entero (bool), acepta_cero (bool) y maximo
    (opcional, valor más alto permitido).
    Devuelve: el número capturado (int o float).
    """
    while True:
        # se aceptan comas como separador de miles, por ejemplo 1,000
        texto = input(mensaje).strip().replace(",", "")
        try:
            if es_entero:
                numero = int(texto)
            else:
                numero = float(texto)
        except ValueError:
            print("Eso no es un número válido, intenta de nuevo.")
            continue

        if not math.isfinite(numero):
            print("Eso no es un número válido, intenta de nuevo.")
        elif maximo is not None and numero > maximo:
            print(f"El valor no puede ser mayor a {maximo}, intenta de nuevo.")
        elif numero > 0:
            return numero
        elif numero == 0 and acepta_cero:
            return numero
        elif numero == 0:
            print("El valor no puede ser cero, intenta de nuevo.")
        else:
            print("El valor no puede ser negativo, intenta de nuevo.")


def preguntar_si_no(mensaje):
    """Pregunta hasta recibir 's' o 'n'.

    Recibe: mensaje. Devuelve: True si la respuesta fue 's', False si fue 'n'.
    """
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta == "s":
            return True
        elif respuesta == "n":
            return False
        else:
            print("Responde solo con 's' o 'n'.")


def pedir_datos():
    """Pide al usuario los datos de la simulación.

    Recibe: nada. Devuelve: monto_mensual, tasa_anual, meta, anios_max.
    """
    monto_mensual = pedir_numero("¿Cuánto puedes ahorrar cada mes? $",
                                 False, False)
    tasa_anual = pedir_numero("¿Cuál es la tasa de interés anual (%)? ",
                              False, True)
    if tasa_anual > TASA_ALTA:
        print(f"Aviso: una tasa mayor a {TASA_ALTA}% anual es poco común; "
              "el resultado puede ser demasiado optimista.")

    meta = pedir_numero("¿Cuál es tu meta de ahorro? $", False, False)
    anios_max = pedir_numero("¿En cuántos años como máximo "
                             f"quieres revisarlo? (máximo {ANIOS_MAXIMOS}) ",
                             True, False, ANIOS_MAXIMOS)
    return monto_mensual, tasa_anual, meta, anios_max


# ===== funciones de cálculo =====

def tasa_mensual_equivalente(tasa_anual):
    """Convierte una tasa anual en porcentaje a tasa mensual en decimal.

    Recibe: tasa_anual (en porcentaje). Devuelve: tasa_mensual (en decimal).
    """
    return (tasa_anual / 100) / MESES_POR_ANIO


def simular_ahorro(monto_mensual, tasa_anual, meta, anios_max):
    """Simula mes a mes el crecimiento del ahorro con una tasa variable.

    Recibe: monto_mensual, tasa_anual, meta, anios_max.
    Devuelve: lista_balances (lista anidada [mes, balance]),
    tasas_anuales (lista con la tasa aplicada cada año) y
    mes_meta (-1 si no se alcanzó la meta).
    """
    balance = 0.0
    lista_balances = []
    tasas_anuales = []
    mes_meta = -1
    mes_actual = 0

    for anio in range(anios_max):
        # la tasa varía un poco cada año, simulando un mercado real
        # con tasa 0% no hay intereses, así que no se aplica variación
        if tasa_anual == 0:
            variacion = 0.0
        else:
            variacion = random.uniform(-VARIACION_MAXIMA, VARIACION_MAXIMA)
        tasa_anual_del_anio = tasa_anual + variacion
        if tasa_anual_del_anio < TASA_MINIMA:
            tasa_anual_del_anio = TASA_MINIMA
        tasas_anuales.append(tasa_anual_del_anio)
        tasa_mensual_del_anio = tasa_mensual_equivalente(tasa_anual_del_anio)

        for mes in range(MESES_POR_ANIO):
            balance += monto_mensual
            balance += balance * tasa_mensual_del_anio
            mes_actual += 1
            lista_balances.append([mes_actual, balance])

            if balance >= meta and mes_meta == -1:
                mes_meta = mes_actual

    return lista_balances, tasas_anuales, mes_meta


def formatear_tiempo(total_meses):
    """Convierte una cantidad de meses en texto de años y meses.

    Recibe: total_meses. Devuelve: texto como '2 años y 1 mes'.
    """
    anios = total_meses // MESES_POR_ANIO
    meses = total_meses % MESES_POR_ANIO

    if anios == 1:
        texto_anios = "1 año"
    else:
        texto_anios = f"{anios} años"

    if meses == 1:
        texto_meses = "1 mes"
    else:
        texto_meses = f"{meses} meses"

    if anios == 0:
        return texto_meses
    elif meses == 0:
        return texto_anios
    else:
        return f"{texto_anios} y {texto_meses}"


# ===== funciones de salida =====

def mostrar_resultado(lista_balances, tasas_anuales, mes_meta, meta,
                      monto_mensual, anios_max):
    """Muestra el saldo final, los intereses y qué tan bien va la meta.

    Recibe: lista_balances, tasas_anuales, mes_meta, meta, monto_mensual,
    anios_max.
    Devuelve: nada (imprime en pantalla).
    """
    total_meses = anios_max * MESES_POR_ANIO
    balance_final = lista_balances[-1][1]
    total_aportado = monto_mensual * total_meses
    intereses = balance_final - total_aportado

    print(f"\nSaldo final tras {formatear_tiempo(total_meses)}: "
          f"${balance_final:.2f}")
    print(f"Tú aportaste ${total_aportado:.2f} y los intereses "
          f"sumaron ${intereses:.2f}.")

    # resumen al cierre de cada año, tomado de la lista anidada
    print("\nAño | Tasa aplicada | Saldo al cierre")
    for registro in lista_balances:
        mes = registro[0]
        balance = registro[1]
        if mes % MESES_POR_ANIO == 0:
            anio = mes // MESES_POR_ANIO
            tasa_del_anio = tasas_anuales[anio - 1]
            print(f"{anio:>3} | {tasa_del_anio:>12.2f}% | ${balance:,.2f}")

    tasa_promedio = sum(tasas_anuales) / len(tasas_anuales)
    print(f"Tasa promedio del periodo: {tasa_promedio:.2f}%\n")

    if mes_meta == -1:
        faltante = meta - balance_final
        porcentaje = balance_final / meta * 100
        print("No alcanzas tu meta dentro del periodo simulado.")
        print(f"Llegas al {porcentaje:.1f}% de la meta; "
              f"te faltan ${faltante:.2f}.")
    elif mes_meta <= total_meses / 2:
        print(f"¡Alcanzas tu meta en {formatear_tiempo(mes_meta)}! "
              "Lo logras en menos de la mitad del plazo.")
    elif mes_meta <= total_meses * PORCENTAJE_POCO_MARGEN / 100:
        print(f"¡Alcanzas tu meta en {formatear_tiempo(mes_meta)}! "
              "Lo logras antes de que termine el plazo.")
    else:
        print(f"¡Alcanzas tu meta en {formatear_tiempo(mes_meta)}! "
              "Lo logras, aunque con poco margen.")


# ===== funciones de archivo =====

def guardar_simulacion(archivo, monto_mensual, tasa_anual, meta, anios_max,
                       balance_final, mes_meta):
    """Agrega una línea con los datos de la simulación al historial.

    Recibe: archivo, monto_mensual, tasa_anual, meta, anios_max,
    balance_final, mes_meta.
    Devuelve: nada.
    """
    if mes_meta == -1:
        texto_resultado = "No se alcanzó la meta"
    else:
        texto_resultado = f"Meta alcanzada en el mes {mes_meta}"

    with open(archivo, "a", encoding="utf-8") as archivo_texto:
        archivo_texto.write(
            f"Ahorro mensual: ${monto_mensual:.2f} | "
            f"Tasa anual base: {tasa_anual:.2f}% | "
            f"Meta: ${meta:.2f} | Plazo: {anios_max} años | "
            f"Saldo final: ${balance_final:.2f} | {texto_resultado}\n"
        )


def mostrar_historial(archivo):
    """Imprime las simulaciones guardadas en el historial.

    Recibe: archivo. Devuelve: nada (imprime en pantalla).
    """
    total_simulaciones = 0
    metas_alcanzadas = 0
    try:
        with open(archivo, "r", encoding="utf-8") as archivo_texto:
            for linea in archivo_texto:
                total_simulaciones += 1
                print(f"{total_simulaciones}. {linea}", end="")
                if "Meta alcanzada" in linea:
                    metas_alcanzadas += 1
    except FileNotFoundError:
        print("Todavía no hay simulaciones guardadas.")
        return

    if total_simulaciones == 0:
        print("Todavía no hay simulaciones guardadas.")
    else:
        print(f"\nSimulaciones guardadas: {total_simulaciones} | "
              f"Metas alcanzadas: {metas_alcanzadas}")


# ===== programa principal =====

def main():
    """Ejecuta el simulador: pide datos, simula, muestra y guarda."""
    print("=== Simulador de Ahorro e Inversión ===")
    print("(la tasa de interés varía un poco cada año, "
          "simulando un mercado real)\n")

    # cada elemento es [numero_simulacion, balance_final, mes_meta]
    resultados_sesion = []
    numero_simulacion = 0
    otra_simulacion = True
    while otra_simulacion:
        numero_simulacion += 1
        print(f"\n--- Simulación {numero_simulacion} ---")
        monto_mensual, tasa_anual, meta, anios_max = pedir_datos()

        lista_balances, tasas_anuales, mes_meta = simular_ahorro(
            monto_mensual, tasa_anual, meta, anios_max)

        mostrar_resultado(lista_balances, tasas_anuales, mes_meta, meta,
                          monto_mensual, anios_max)

        balance_final = lista_balances[-1][1]
        resultados_sesion.append([numero_simulacion, balance_final,
                                  mes_meta])

        if preguntar_si_no("\n¿Quieres guardar esta simulación? (s/n) "):
            guardar_simulacion(ARCHIVO_HISTORIAL, monto_mensual, tasa_anual,
                               meta, anios_max, balance_final, mes_meta)
            print("Simulación guardada.")

        if preguntar_si_no("¿Quieres ver simulaciones anteriores? (s/n) "):
            mostrar_historial(ARCHIVO_HISTORIAL)

        otra_simulacion = preguntar_si_no(
            "\n¿Quieres hacer otra simulación? (s/n) ")

    # si hubo más de una simulación, se comparan usando la lista
    if len(resultados_sesion) > 1:
        print("\n=== Comparación de tus simulaciones ===")
        mejor_resultado = resultados_sesion[0]
        for resultado in resultados_sesion:
            numero = resultado[0]
            saldo = resultado[1]
            mes_meta_resultado = resultado[2]
            if mes_meta_resultado == -1:
                texto_meta = "no alcanzó la meta"
            else:
                texto_meta = (f"meta en "
                              f"{formatear_tiempo(mes_meta_resultado)}")
            print(f"Simulación {numero}: saldo final ${saldo:,.2f}, "
                  f"{texto_meta}")
            if saldo > mejor_resultado[1]:
                mejor_resultado = resultado
        print(f"La simulación con mayor saldo final fue la "
              f"{mejor_resultado[0]}.")

    print("\n¡Gracias por usar el simulador!")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nSimulación cancelada. ¡Hasta luego!")
