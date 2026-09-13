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
 2  CONSTANTE ARCHIVO_HISTORIAL = "historial.txt"
 3  CONSTANTE VARIACION_MAXIMA = 2   // puntos porcentuales que puede variar la tasa cada año
 4  FUNCION pedir_datos()
 5      // Recibe: nada
 6      // Devuelve: monto_mensual, tasa_anual, meta, años_max
 7      LEER monto_mensual
 8      LEER tasa_anual
 9      LEER meta
10      LEER años_max
11      DEVOLVER monto_mensual, tasa_anual, meta, años_max
12  FIN FUNCION
13  FUNCION tasa_mensual_equivalente(tasa_anual)
14      // Recibe: tasa_anual (en porcentaje)
15      // Devuelve: tasa_mensual (en decimal)
16      tasa_mensual = (tasa_anual / 100) / 12
17      DEVOLVER tasa_mensual
18  FIN FUNCION
19  FUNCION simular_ahorro(monto_mensual, tasa_anual, meta, años_max)
20      // Recibe: monto_mensual, tasa_anual, meta, años_max
21      // Devuelve: lista_balances (lista anidada: [mes, balance] por cada mes),
22      //           mes_meta (-1 si no se alcanzó)
23      balance = 0
24      lista_balances = LISTA VACÍA
25      mes_meta = -1
26      mes_actual = 0
27      PARA año DESDE 1 HASTA años_max
28          // la tasa varía un poco cada año, simulando un mercado real
29          tasa_anual_del_año = tasa_anual + NUMERO_ALEATORIO_ENTRE(-VARIACION_MAXIMA, VARIACION_MAXIMA)
30          tasa_mensual_del_año = tasa_mensual_equivalente(tasa_anual_del_año)
31          PARA mes DESDE 1 HASTA 12
32              balance = balance + monto_mensual
33              balance = balance + (balance * tasa_mensual_del_año)
34              mes_actual = mes_actual + 1
35              AGREGAR [mes_actual, balance] A lista_balances
36              SI balance >= meta Y mes_meta == -1 ENTONCES
37                  mes_meta = mes_actual
38              FIN SI
39          FIN PARA
40      FIN PARA
41      DEVOLVER lista_balances, mes_meta
42  FIN FUNCION
43  FUNCION guardar_simulacion(archivo, monto_mensual, tasa_anual, meta, mes_meta)
44      // Recibe: archivo, monto_mensual, tasa_anual, meta, mes_meta
45      // Devuelve: nada (escribe en archivo)
46      ABRIR archivo EN MODO agregar
47      ESCRIBIR monto_mensual, tasa_anual, meta, mes_meta EN archivo
48      CERRAR archivo
49  FIN FUNCION
50  FUNCION mostrar_historial(archivo)
51      // Recibe: archivo
52      // Devuelve: nada (imprime en pantalla)
53      INTENTAR
54          ABRIR archivo EN MODO lectura
55          PARA CADA línea EN archivo
56              MOSTRAR línea
57          FIN PARA
58          CERRAR archivo
59      SI EL ARCHIVO NO EXISTE ENTONCES
60          MOSTRAR "Todavía no hay simulaciones guardadas."
61      FIN INTENTAR
62  FIN FUNCION
63  // ---- Programa principal ----
64  MOSTRAR "=== Simulador de Ahorro e Inversión ==="
65  MOSTRAR "(la tasa de interés varía un poco cada año, simulando un mercado real)"
66  monto_mensual, tasa_anual, meta, años_max = pedir_datos()
67  lista_balances, mes_meta = simular_ahorro(monto_mensual, tasa_anual, meta, años_max)
68  balance_final = lista_balances[último][1]
69  MOSTRAR "Saldo final tras", años_max, "años:", balance_final
70  SI mes_meta != -1 ENTONCES
71      años = mes_meta DIV 12
72      meses = mes_meta MOD 12
73      MOSTRAR "Meta alcanzada en el mes", mes_meta, "(aprox.", años, "años y", meses, "meses)"
74  SINO
75      MOSTRAR "No se alcanzó la meta en el periodo simulado"
76  FIN SI
77  PREGUNTAR "¿Guardar esta simulación? (s/n)"
78  LEER guardar
79  SI guardar == "s" ENTONCES
80      guardar_simulacion(ARCHIVO_HISTORIAL, monto_mensual, tasa_anual, meta, mes_meta)
81      MOSTRAR "Simulación guardada."
82  FIN SI
83  PREGUNTAR "¿Ver simulaciones anteriores? (s/n)"
84  LEER ver_historial
85  SI ver_historial == "s" ENTONCES
86      mostrar_historial(ARCHIVO_HISTORIAL)
87  FIN SI
88  MOSTRAR "¡Gracias por usar el simulador!"
89  FIN
```

