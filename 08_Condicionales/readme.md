<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/07_Diccionarios/readme.md">Capítulo anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/09_Bucles/readme.md">Siguiente Capítulo</a>
</h4>

<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/condicionales.png">
</h1>


<h1 align="center">Condicionales</h1><br>

<h4>Índice</h4>


<h4>Índice</h4>

- [1. Condicionales.](#1-condicionales)
- [2. If.](#2-if)
- [3. If else.](#3-if-else)
- [4. If Elif Else.](#4-if-elif-else)
- [5. Short Hands o atajos.](#5-short-hands-o-atajos)
- [6. Condiciones anidadas.](#6-condiciones-anidadas)
- [7. Operadores lógicos](#7-operadores-lógicos)
  - [7.1 If y and](#71-if-y-and)
  - [7.2 If y or](#72-if-y-or)
- [8. Ejercicios](#8-ejercicios)


<a name="1-condicionales"></a>

## 1. Condicionales.

Los condicionales son estructuras que permiten controlar el flujo de un programa ejecutando diferentes bloques de código según si se cumplen o no ciertas condiciones. En temas futuros veremos la gran utilidad que tienen estos.

>[!NOTE]
>Hay que recordad que en python es muy importante las sangrías por no decir que son obligatorias, ahora que empezamos a ver sobre todo estructuras de control.

<a name="2-if"></a>

## 2. If.

El Condicional `If` evalúa la expresión y ejecuta el bloque si la condición es verdadera, en este caso se diferencia bastante de JAVA ya que en python el bloque _If_ se inicia con `:` y en el salto de línea es obligatorio las sangrías, ejemplo:

```python
# Sintaxis
if condicion:
    # Aquí irá el código que se ejecutará si la condición es verdadera
# Ejemplo
a = 5
if a > 0:
    print("el número es mayor que 0")
```

<a name="3-if-else"></a>

## 3. If else.

En el caso del _if_ y el _else_ esto quiere decir que si el bloque _if_ no se ejecuta se deberá ejecutar el bloque _else_, ejemplo.
```python
# Sintaxis
if condicion:
    Se ejecuta esta parte
else:
    Si el if no se cumple, se ejecutará esta otra parte
# Ejemplo
a = 5
if a < 0:
    print("a es menor que 0")
else:
    print("a es mayor que 0")
# al ser a mayor que 0 imprimirá por pantalla el bloque contenido en el else
```

<a name="4-if-elif-else"></a>

## 4. If Elif Else.

Si además de dos condiciones, podemos tener tres o varias más para eso usamos _elif_ que es lo mismo que en JAVA el else if, que lo que hace es entrar a valorar si se cumple otra condición y si es verdadera se ejecutará ese bloque de código, ejemplo:
```python
# Sintaxis
if condicion:
    bloque código
elif condicion:
    bloque código
else:
    bloque código que se ejecutará si no cumple ninguna de las anteriores.
# Ejemplo
a = 0
if a > 0:
    print("a es mayor que 0")
elif a < 0:
    print("a es menor que 0")
else:
    print("a es 0")
# En este caso no se cumplen ni el if ni el elif por lo que se ejecuta el else, prueba a cambiar el valor de a.
```

<a name="5-short-hands-o-atajos"></a>

## 5. Short Hands o atajos.

También podemos escribir el condicional en una sola línea ya que python está diseñado para ser un lenguaje mas simple que JAVA, ejemplo:
```python
# Sintaxis
código que se ejecutará if condicion else código que se ejecuta si no cumple condición.
# Ejemplo
a = 5
print ("a es positivo") if a > 0 else print ("a es negativo")
# como vemos se imprime la primera condición si se cumple el if.
```

<a name="6-condiciones-anidadas"></a>

## 6. Condiciones anidadas.

Dentro de las condiciones podemos anidar otras condiciones para evaluar diferentes opciones, ejemplo.
```python
# Sintaxis
if condicion:
    codigo
    if condicion:
        codigo
# Ejemplo
a = 4
if a > 0:
    print("a es positivo")
    if a % 2 == 0:
        print ("a es par")
    else:
        print ("a es impar")
elif a < 0:
    print("a es negativo")
else:
    print("a es 0")
# Ves probando el valor de a para ver los resultados
```

<a name="7-operadores-lógicos"></a>

## 7. Operadores lógicos

Con los operadores lógicos podemos sustituir los condicionales anidados si lo que queremos evaluar son dos condiciones que se deben cumplir si queremos ejecutar el código.

<a name="71-if-y-and"></a>

### 7.1 If y and

La condición _if_ o _elif_ seguido del operador _and_ significa que se deben cumplir las dos condiciones para ejecutar el código que continua despues de los _:_, ejemplo.
```python
# Sintaxis
if condición and condición:
    código a ejecutar
# Ejemplo
a = 4
if a > 0 and a % 2 == 0:
    print("a es positivo y par")
elif a > 0 and a % 2 != 0:
    print("a es positivo e impar")
elif a < 0:
    print ("a es negativo")
else:
    print ("a es cero")
```

<a name="72-if-y-or"></a>

### 7.2 If y or

En este caso el condicional if más el operador or significa que solo debe cumplirse una condición para que se ejecute el código que sigue a los _:_ del if, ejemplo.
```python
# Sintaxis
if condición or condición:
    bloque que se ejecuta si se cumple una de las dos condiciones.
# Ejemplo
estado_civil = "soltero"  # soltero o casado
edad = 54
if estado_civil == "casado" or edad > 18:
    print("es mayor de edad")
else:
    print("es menor de edad")
# modifica el valor de estado civil o la edad a ver que ocurre, se presupone que para casarte tienes que ser mayor de edad pero puedes estar soltero y ser mayor de edad.
```

🙌 Vamos a por unos pequeños retos como unos breves ejercicios.

<a name="8-ejercicios"></a>

## 8. Ejercicios

- Escribe tu edad en una variable y si tienes más de 18 años que imprima `("eres mayor de edad")` en caso contrario que imprima `("eres menor, que suerte.")`
- Pide al usuario mediante input("igresa tu edad: ") y almacénalo en una variable. Si tiene más de 18 imprime por pantalla `Puedes sacarte el carnet` en caso contrario `aún no puedes sacarte el carnet` y que diga los años que le faltan 'Te faltan años`.
- con la variable de edad compara tu edad y la mia (38) `tecxion_edad = 38` y si yo soy mayor que tú que imprima `tecxion es mayor` en caso contrario `tú eres mayor que tecxion` y si tenemos la misma edad `tenéis la misma edad, ¡genial!`.
- Pide al usuario que ingrese dos números y compáralos, que imprima si a es mayor que b `a es mayor que b` en caso contrario `b es mayor que a` y si son iguales `a es igual a b`
- Pide al usuario que ingrese la nota del examen y clasifica la nota. `de 0 a 5 Suspenso, de 5 a 6 suficiente, de 6 a 7 bien, de 7 a 8 Notable, de 8 a 9 Sobresaliente y de 9 a 10 Matrícula`
- Vamos a crear un pequeño programa que recomiende películas según el género que elija el usuario. Pide al usuario que ingrese un género, si el género existe que muestre las películas de ese género, si no existe que muestre un mensaje tipo `género no encontrado`
  - Diccionario. 
```
peliculas = {
    "acción": ["Misión Imposible", "John Wick", "Mad Max"],
    "comedia": ["Supercool", "Los Hangover", "Scary Movie"],
    "terror": ["El Exorcista", "It", "El Conjuro"]
}
```

[Solución ejercicios](./readme.md)

<h3 align="center">
¡Perfecto! Llegaste al final de los condicionales epero que hasta aquí todo bien, y si tienes alguna duda, viste algún error contacta conmigo. ¡Gracias!
</h3>


<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/07_Diccionarios/readme.md">Capítulo anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/09_Bucles/readme.md">Siguiente Capítulo</a>
</h4>

<h2 align="center">
Creo que es buen momento para recordar que si quieres puede ayudarme a seguir subiendo cursos apoyándome con un café<br>
<br>
   <a href="https://paypal.me/jfmpkiko">
<img src="https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white" alt="Paypal" />  </a><a href="https://coff.ee/tecxart"><img src="https://github.com/tecxion/TecXion/blob/main/Media/cafe1.png" alt="Cafe">

</a>
</h2>