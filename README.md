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
 1  INICIO
 2  FUNCION pedir_datos()
 3      // Recibe: nada
 4      // Devuelve: monto_mensual, tasa_anual, meta, años_max
 5      LEER monto_mensual
 6      LEER tasa_anual
 7      LEER meta
 8      LEER años_max
 9      DEVOLVER monto_mensual, tasa_anual, meta, años_max
10  FIN FUNCION
11  FUNCION tasa_mensual_equivalente(tasa_anual)
12      // Recibe: tasa_anual (en porcentaje)
13      // Devuelve: tasa_mensual (en decimal)
14      tasa_mensual = (tasa_anual / 100) / 12
15      DEVOLVER tasa_mensual
16  FIN FUNCION
17  FUNCION simular_ahorro(monto_mensual, tasa_anual, meta, años_max)
18      // Recibe: monto_mensual, tasa_anual, meta, años_max
19      // Devuelve: lista_balances (lista anidada: [mes, balance] por cada mes),
20      //           mes_meta (-1 si no se alcanzó)
21      balance = 0
22      lista_balances = LISTA VACÍA
23      mes_meta = -1
24      mes_actual = 0
25      PARA año DESDE 1 HASTA años_max
26          // la tasa varía un poco cada año, simulando un mercado real
27          tasa_anual_del_año = tasa_anual + NUMERO_ALEATORIO_ENTRE(-VARIACION_MAXIMA, VARIACION_MAXIMA)
28          tasa_mensual_del_año = tasa_mensual_equivalente(tasa_anual_del_año)
29          PARA mes DESDE 1 HASTA 12
30              balance = balance + monto_mensual
31              balance = balance + (balance * tasa_mensual_del_año)
32              mes_actual = mes_actual + 1
33              AGREGAR [mes_actual, balance] A lista_balances
34              SI balance >= meta Y mes_meta == -1 ENTONCES
35                  mes_meta = mes_actual
36              FIN SI
37          FIN PARA
38      FIN PARA
39      DEVOLVER lista_balances, mes_meta
40  FIN FUNCION
41  FUNCION guardar_simulacion(archivo, monto_mensual, tasa_anual, meta, mes_meta)
42      // Recibe: archivo, monto_mensual, tasa_anual, meta, mes_meta
43      // Devuelve: nada (escribe en archivo)
44      ABRIR archivo EN MODO agregar
45      ESCRIBIR monto_mensual, tasa_anual, meta, mes_meta EN archivo
46      CERRAR archivo
47  FIN FUNCION
48  FUNCION mostrar_historial(archivo)
49      // Recibe: archivo
50      // Devuelve: nada (imprime en pantalla)
51      ABRIR archivo EN MODO lectura
52      PARA CADA línea EN archivo
53          MOSTRAR línea
54      FIN PARA
55      CERRAR archivo
56  FIN FUNCION
57  // ---- Programa principal ----
58  monto_mensual, tasa_anual, meta, años_max = pedir_datos()
59  lista_balances, mes_meta = simular_ahorro(monto_mensual, tasa_anual, meta, años_max)
60  MOSTRAR "Saldo final:", lista_balances[último][1]
61  SI mes_meta != -1 ENTONCES
62      MOSTRAR "Meta alcanzada en el mes", mes_meta
63  SINO
64      MOSTRAR "No se alcanzó la meta en el periodo simulado"
65  FIN SI
66  PREGUNTAR "¿Guardar esta simulación? (s/n)"
67  SI respuesta == "s" ENTONCES
68      guardar_simulacion(archivo, monto_mensual, tasa_anual, meta, mes_meta)
69  FIN SI
70  PREGUNTAR "¿Ver simulaciones anteriores? (s/n)"
71  SI respuesta == "s" ENTONCES
72      mostrar_historial(archivo)
73  FIN SI
74  FIN
```

