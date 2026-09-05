# Simulador de ahorro o inversión
Programa de consola en Python que simula el crecimiento de un ahorro o inversión mes a mes, aplicando interés compuesto con una pequeña variación anual aleatoria en la tasa. A partir del monto mensual, la tasa y una meta del usuario, indica en qué mes se alcanza y permite guardar cada simulación para compararla luego con otros escenarios.

## Problema que busca resolver
Muchas personas posponen ahorrar ya que no logran visualizar el efecto real que tiene el tiempo y el interés compuesto sobre su dinero. Sin herramientas que muestre el crecimiento de forma conctreta, es dificil entender por qué empezar a ahorrar antes (incluso con una cantidad minima de dinero) hace diferencias a largo plazo, o por qué conviene mover el ahorro de algo que no te trae ganancias a uno que si.

## Contexto
Según la Encuesta Nacional de Inclusión Financiera (ENIF) 2024 del INEGI, 33.6% de la población mexicana de 18 a 70 años no cuenta con ningún tipo de ahorro. De quienes sí ahorran, apenas 8.2% lo hace exclusivamente en instrumentos formales (los que realmente generan), mientras que 36.6% ahorra solo de manera informal (por ejemplo, guardado en casa o en tandas), donde el dinero no crece con el tiempo.

"Fuente: INEGI, Encuesta Nacional de Inclusión Financiera (ENIF) 2024."
https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2025/enif/ENIF2024_CP.pdf

## La importancia de esto
Considero que seria de gran ayuda tener una herramienta facil de usar que muestre, mes a mes, cómo crece un ahorro según el monto depositado y la tasa de interés aplicada puede ayudar a que estudiantes y personas que apenas comienzan su vida financiera entiendad de alguna forma el efecto del interés compuesto, motivarse a plantearse metas de ahorro que puedan ser medibles/realistas. Algo que considero yo se deberia de enseñar de forma práctica a todos en general.

## Funcion / Objetivo
Simular el crecimiento de ahorro o inversión a partir de datos definidos por el usuario, mostrando el avance u evolucion con el tiempo y si es posible alcanzar una meta que se estableció.

## Pseudocodigo

```text
INICIO

FUNCION pedir_datos()
    // Recibe: nada
    // Devuelve: monto_mensual, tasa_anual, meta, años_max
    LEER monto_mensual
    LEER tasa_anual
    LEER meta
    LEER años_max
    DEVOLVER monto_mensual, tasa_anual, meta, años_max
FIN FUNCION

FUNCION tasa_mensual_equivalente(tasa_anual)
    // Recibe: tasa_anual (en porcentaje)
    // Devuelve: tasa_mensual (en decimal)
    tasa_mensual = (tasa_anual / 100) / 12
    DEVOLVER tasa_mensual
FIN FUNCION

FUNCION simular_ahorro(monto_mensual, tasa_anual, meta, años_max)
    // Recibe: monto_mensual, tasa_anual, meta, años_max
    // Devuelve: lista_balances (lista anidada: [mes, balance] por cada mes),
    //           mes_meta (-1 si no se alcanzó)
    balance = 0
    lista_balances = LISTA VACÍA
    mes_meta = -1
    mes_actual = 0

    PARA año DESDE 1 HASTA años_max
        // la tasa varía un poco cada año, simulando un mercado real
        tasa_anual_del_año = tasa_anual + NUMERO_ALEATORIO_ENTRE(-VARIACION_MAXIMA, VARIACION_MAXIMA)
        tasa_mensual_del_año = tasa_mensual_equivalente(tasa_anual_del_año)

        PARA mes DESDE 1 HASTA 12
            balance = balance + monto_mensual
            balance = balance + (balance * tasa_mensual_del_año)
            mes_actual = mes_actual + 1
            AGREGAR [mes_actual, balance] A lista_balances

            SI balance >= meta Y mes_meta == -1 ENTONCES
                mes_meta = mes_actual
            FIN SI
        FIN PARA
    FIN PARA

    DEVOLVER lista_balances, mes_meta
FIN FUNCION

FUNCION guardar_simulacion(archivo, monto_mensual, tasa_anual, meta, mes_meta)
    // Recibe: archivo, monto_mensual, tasa_anual, meta, mes_meta
    // Devuelve: nada (escribe en archivo)
    ABRIR archivo EN MODO agregar
    ESCRIBIR monto_mensual, tasa_anual, meta, mes_meta EN archivo
    CERRAR archivo
FIN FUNCION

FUNCION mostrar_historial(archivo)
    // Recibe: archivo
    // Devuelve: nada (imprime en pantalla)
    ABRIR archivo EN MODO lectura
    PARA CADA línea EN archivo
        MOSTRAR línea
    FIN PARA
    CERRAR archivo
FIN FUNCION

// ---- Programa principal ----
monto_mensual, tasa_anual, meta, años_max = pedir_datos()
lista_balances, mes_meta = simular_ahorro(monto_mensual, tasa_anual, meta, años_max)

MOSTRAR "Saldo final:", lista_balances[último][1]

SI mes_meta != -1 ENTONCES
    MOSTRAR "Meta alcanzada en el mes", mes_meta
SINO
    MOSTRAR "No se alcanzó la meta en el periodo simulado"
FIN SI

PREGUNTAR "¿Guardar esta simulación? (s/n)"
SI respuesta == "s" ENTONCES
    guardar_simulacion(archivo, monto_mensual, tasa_anual, meta, mes_meta)
FIN SI

PREGUNTAR "¿Ver simulaciones anteriores? (s/n)"
SI respuesta == "s" ENTONCES
    mostrar_historial(archivo)
FIN SI

FIN
```

