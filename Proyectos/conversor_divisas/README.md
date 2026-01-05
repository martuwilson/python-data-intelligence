# Proyecto del Día 2: Cambio de Divisas

## Aclaración

Como este es tu primer proyecto, va a estar detalladamente guiado con instrucciones para cada una de las celdas. A medida que avancemos en el curso, los proyectos serán menos guiados, y más complejos. Este proyecto es sencillo para que comencemos con algo fácil, y además porque aún no hemos aprendido suficientes herramientas como para hacer programas más funcionales, pero aún así te va a sorprender cómo pudimos unir todo lo aprendido hoy y realizar un buen desafío.

## Consigna

Vas a crear un código que simule el funcionamiento de una máquina de cambio de divisas. Por el momento nuestra máquina sólo recibe dólares y devuelve euros ¡No es poco para ser tu primer programa!

Tu máquina va a necesitar disponer de variables que le brinden la siguiente información:

- Nombre del usuario
- Fecha en que se realiza la operación
- Momento del día (día, tarde o noche)
- Cantidad de dólares a cambiar

Con todo eso, la máquina va a imprimir en pantalla (en diferentes líneas por supuesto) un mensaje que incluya los siguientes requisitos:

- Un saludo de bienvenida
- Información de la cantidad de dolares que va a entregar el usuario
- Información de la cantidad de euros que va a recibir
- Detalle específico de cuántos billetes de €10, de €1, y el saldo en monedas que le serán entregados
- Un saludo de despedida
## Nota importante

No hay una única manera de hacer esto. En programación siempre hay muchos caminos para lograr el mismo objetivo. Mientras que logres cumplir con la consigna, cualquier abordaje (sensato) es válido.

En las siguientes celdas te iré proporcionando las instrucciones específica para que puedas desarrollar el proyecto paso a paso. De todos modos, si te sientes valiente, puedes abrir un nuevo cuaderno en blanco y hacerlo todo desde cero por tí mismo. Si lo logras, felicitaciones, pero si te encuentras bloqueado en algún momento, nada de sentir vergüenza. Te vuelves a este cuaderno, y lo sigues con mis instrucciones.

## ⚠️ Nota súper-mega-archi importante

La idea no sólo es aprender, sino fundamentalmente **divertirse**. Programar es hermoso, es desafiante, es la oportunidad de concentrarnos en un problema y poner lo mejor de nosotros para resolverlo.

Eso no significa que si no lo puedes resolver no te vas a divertir. Todo lo contrario. Si bien resolver problemas por uno mismo es emocionante y excitante, una de las sensaciones más placenteras que he experimentado, es creer que algo es imposible, y que luego alguien en quien confío me muestre el camino para lograrlo. Se llama **"momento Eureka"**, y espero que te atrevas a experimentarlo tu también.

## Instrucciones paso a paso

### 1. Saludo inicial
Escribe el código necesario para saludar al usuario, antes de comenzar sus operaciones. Vas a crear tres variables que contengan, respectivamente, el nombre del usuario, la fecha del día en que está haciendo la operación, y un saludo que puede ser Buenos días, Buenas tardes o Buenas noches.

### 2. Mensaje de bienvenida
Crea una variable llamada `bienvenida` que concatene toda la información anterior en un solo mensaje que salude al usuario que va a usar el servicio de cambio de divisas. Puedes poner la creatividad que gustes en este mensaje.

> **Pista:** Recuerda que en la lección operaciones vimos cómo puedes concatenar strings para formar una sola cadena de texto.

### 3. Cantidad de dólares
Crea una variable numérica llamada `dolares` que almacene la cantidad de dólares que quieres cambiar por euros. Ten en cuenta que los valores en moneda suelen expresarse con números decimales, por lo que sería ideal utilizar un valor de tipo `float`.

### 4. Cálculo de euros
Crea una variable llamada `euros_a_recibir` que guarde el resultado de calcular cuántos euros corresponden para la cantidad de dolares ingresada en la variable `dolares`. El tipo de cambio que usaremos es de **0.88**.

### 5. Distribución de billetes y monedas
Nuestra máquina (imaginaria), solo entrega billetes de €10, y de €1 (los decimales los entregará en monedas). Crea 3 variables para cada uno de esos valores (`billetes_10`, `billetes_1` y `monedas`), que contengan los cálculos necesarios para saber cuánto valor en monedas, y cuántos billetes de cada tipo recibirá el usuario.

### 6. Mensaje final
Finalmente escribe una serie de declaraciones `print()` que expresen el mensaje completo, mostrando los siguientes elementos:

- Mensaje de bienvenida
- Información sobre los dólares que entregará
- Información sobre los euros que recibirá
- Detalle de billetes y monedas que le serán entregados
- Saludo de despedida

> **Importante:** Cómo aún no hemos aprendido a concatenar números y texto en la misma línea de impresión, en muchas ocasiones deberás crear líneas separadas para que el mensaje se muestre como en el siguiente ejemplo:
> 
> ```
> Dolares a entregar:
> 150.45
> ```