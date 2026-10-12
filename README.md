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
1  // ---- Programa principal ----
2  MOSTRAR "=== Simulador de Ahorro e Inversión ==="
3  MOSTRAR "(la tasa de interés varía un poco cada año, simulando un mercado real)"
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

