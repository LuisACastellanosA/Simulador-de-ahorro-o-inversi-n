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
INICIO
1. Inicio
2. PEDIR monto_mensual, tasa_anual, meta, años_max, variacion_max al usuario
3. DEFINIR balance = 0
4. DEFINIR lista_balances = lista vacía
5. DEFINIR mes_meta = -1
6. DEFINIR mes_actual = 0
7. PARA año DESDE 1 HASTA años_max
   7.1. CALCULAR variacion = número aleatorio entre -variacion_max y variacion_max
   7.2. CALCULAR tasa_anual_del_año = tasa_anual + variacion
   7.3. CALCULAR tasa_mensual = (tasa_anual_del_año / 100) / 12
   7.4. PARA mes DESDE 1 HASTA 12
        7.4.1. SUMAR monto_mensual a balance
        7.4.2. SUMAR (balance * tasa_mensual) a balance
        7.4.3. SUMAR 1 a mes_actual
        7.4.4. AGREGAR [mes_actual, balance] a lista_balances
        7.4.5. SI balance >= meta Y mes_meta == -1 ENTONCES
               7.4.5.1. mes_meta = mes_actual
8. MOSTRAR "Saldo final: ", último balance de lista_balances
9. SI mes_meta ≠ -1 ENTONCES
   9.1. MOSTRAR "Meta alcanzada en el mes ", mes_meta
10. SINO
    10.1. MOSTRAR "No se alcanzó la meta en el periodo simulado"
11. PREGUNTAR "¿Guardar esta simulación? (s/n)"
12. SI respuesta == "s" ENTONCES
    12.1. ABRIR archivo "historial.txt" en modo agregar
    12.2. ESCRIBIR monto_mensual, tasa_anual, meta, mes_meta en archivo
    12.3. CERRAR archivo
13. PREGUNTAR "¿Ver simulaciones anteriores? (s/n)"
14. SI respuesta == "s" ENTONCES
    14.1. ABRIR archivo "historial.txt" en modo lectura
    14.2. PARA CADA línea en archivo
          14.2.1. MOSTRAR línea
    14.3. CERRAR archivo
15. Fin



