
Marcelo Schonbrunn

Yann Le Lorier

# Pregunta 1

El propósito de un analizador SLR(1) es ser un poco más capaz que un parser LR(0). Se trata del mismo principio, pero lo que cambia es que se basa en una construcción de una tabla canónica de todos los componentes LR(0). El principal beneficio de usar un analizador SLR(1) por encima de un LR(1) o un Lookahead LR (1) es que la construcción de la tabla de transiciones es pequeña, por lo que es fácil de entender.

## Clases y métodos utilizados

Módulos utilizados:

- ```sys```
- ```pyexecjs```: instalación con ```pip install pyexecjs```

### Lectura de archivos:

- antes de entrar al algoritmo, tenemos una función ```read_instructions(filename)``` que recibe el nombre de un archivo. Esta función se encarga de analizar los documentos de entrada ```action.csv``` y ```goto.csv``` , y de arrojar los resultados en una lista bidimensional convencional de python. En el ejemplo adjunto a este documento obtenemos los siguientes resultados. Decidimos mantener el header del csv para facilitar la columna correspondiente de la acción por tomar:

  - **Action** $\rightarrow$ 

    ```sh
    [['+', '*', 'a', '$'], 
    ['s3', 's4', 's2', ''], 
    ['', '', '', 'accept'], 
    ['r3', 'r3', 'r3', 'r3'], 
    ['s3', 's4', 's2', ''], 
    ['s3', 's4', 's2', ''], 
    ['s3', 's4', 's2', ''], 
    ['s3', 's4', 's2', ''], 
    ['r1', 'r1', 'r1', 'r1'], 
    ['r2', 'r2', 'r2', 'r2']]
    ```

  - **Goto** $\rightarrow$

    ```sh
    [['S'], 
    ['1'], 
    [''], 
    [''], 
    ['5'], 
    ['6'], 
    ['7'], 
    ['8']]
    ```

- Proponemos una función que se encarga de leer las producciones ```read_productions(filename)``` que recibe un nombre de archivo, y que genera otra matriz de la siguiente forma (mismo ejemplo):

  ```sh
  [['S -> +SS', '3'], 
  ['S -> *SS', '3'], 
  ['S -> a', '1']]
  ```

### Algoritmo principal

finalmente, con todas las tablas o matrices listas, podemos correr el algoritmo principal, siguiendo el pseudocódigo visto en clase (el orden de los archivos sí importa):

```sh
python3 LR.py action1.csv goto1.csv producciones1.txt entrada1.txt
```

# Pregunta 2

$$
\begin{align}
&S' \rightarrow S\\
&S \rightarrow +SS\\
&S \rightarrow *SS\\
&S \rightarrow \text{DIGIT DIGITS}\\
&\text{DIGIT} \rightarrow [0-9]\\
&\text{DIGITS} \rightarrow \text{DIGIT DIGITS}\\
&\text{DIGITS} \rightarrow \#
\end{align}
$$

- Calcular FIRST y FOLLOW para cada no terminal y cree el conjunto canónico para el analizador SLR  (el  diagramota), pueden usar lo compartido por Isaac y Simón y extenderlo (20 puntos)

**First**
$$
\text{FIRST}(S) = \{+, *, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}
$$
Por otro lado:
$$
\text{FIRST}(\text{DIGIT}) = \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}
$$
Finalmente:
$$
\text{FIRST}(\text{DIGITS}) = \{\#, 0, 1, 2, 3,4 ,5,6,7,8,9\}
$$
**Follow**

Calculemos Follow de S
$$
\text{FOLLOW}(S) = \{$\}
$$

Ahora, Follow de Digit
$$
\text{FOLLOW}(\text{DIGIT}) = \text{FIRST}(\text{DIGITS}) = \{\#,0,1,2,3,4,5,6,7,8,9\}
$$

Finalmente, Follow de Digits
$$
\text{FOLLOW}(\text{DIGITS}) = \{ \# \}
$$

**Conjunto Canónico**

[DFA](./DFA.png)

- Crear la tabla del analizador SLR para esa gramática,(Action y GOTO)(10 puntos)

**Tabla Action Y GoTo**

| State  | +    | *    | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | #    | $      | S    | DIGIT | DIGITS |
| ------ | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ------ | ---- | ----- | ------ |
| **0**  | s1   | s2   | s3   | s4   | s5   | s6   | s7   | s8   | s9   | s10  | s11  | s12  |      |        | 18   | 13    |        |
| **1**  | s1   | s2   | s3   | s4   | s5   | s6   | s7   | s8   | s9   | s10  | s11  | s12  |      |        | 19   | 13    |        |
| **2**  | s1   | s2   | s3   | s4   | s5   | s6   | s7   | s8   | s9   | s10  | s11  | s12  |      |        | 20   | 13    |        |
| **3**  |      |      | r4   | r4   | r4   | r4   | r4   | r4   | r4   | r4   | r4   | r4   | r4   | r4     |      |       |        |
| **4**  |      |      | r5   | r5   | r5   | r5   | r5   | r5   | r5   | r5   | r5   | r5   | r5   | r5     |      |       |        |
| **5**  |      |      | r6   | r6   | r6   | r6   | r6   | r6   | r6   | r6   | r6   | r6   | r6   | r6     |      |       |        |
| **6**  |      |      | r7   | r7   | r7   | r7   | r7   | r7   | r7   | r7   | r7   | r7   | r7   | r7     |      |       |        |
| **7**  |      |      | r8   | r8   | r8   | r8   | r8   | r8   | r8   | r8   | r8   | r8   | r8   | r8     |      |       |        |
| **8**  |      |      | r9   | r9   | r9   | r9   | r9   | r9   | r9   | r9   | r9   | r9   | r9   | r9     |      |       |        |
| **9**  |      |      | r10  | r10  | r10  | r10  | r10  | r10  | r10  | r10  | r10  | r10  | r10  | r10    |      |       |        |
| **10** |      |      | r11  | r11  | r11  | r11  | r11  | r11  | r11  | r11  | r11  | r11  | r11  | r11    |      |       |        |
| **11** |      |      | r12  | r12  | r12  | r12  | r12  | r12  | r12  | r12  | r12  | r12  | r12  | r12    |      |       |        |
| **12** |      |      | r13  | r13  | r13  | r13  | r13  | r13  | r13  | r13  | r13  | r13  | r13  | r13    |      |       |        |
| **13** |      |      | s3   | s4   | s5   | s6   | s7   | s8   | s9   | s10  | s11  | s12  | s14  |        |      | 16    | 15     |
| **14** |      |      | r15  | r15  | r15  | r15  | r15  | r15  | r15  | r15  | r15  | r15  | r15  | r15    |      |       |        |
| **15** |      |      | r3   | r3   | r3   | r3   | r3   | r3   | r3   | r3   | r3   | r3   | r3   | r3     |      |       |        |
| **16** |      |      | s3   | s4   | s5   | s6   | s7   | s8   | s9   | s10  | s11  | s12  | s14  |        |      | 16    | 17     |
| **17** |      |      | r14  | r14  | r14  | r14  | r14  | r14  | r14  | r14  | r14  | r14  | r14  | r14    |      |       |        |
| **18** |      |      |      |      |      |      |      |      |      |      |      |      |      | accept |      |       |        |
| **19** | s1   | s2   | s3   | s4   | s5   | s6   | s7   | s8   | s9   | s10  | s11  | s12  |      |        | 21   | 13    |        |
| **20** | s1   | s2   | s3   | s4   | s5   | s6   | s7   | s8   | s9   | s10  | s11  | s12  |      |        | 22   | 13    |        |
| **21** |      |      | r1   | r1   | r1   | r1   | r1   | r1   | r1   | r1   | r1   | r1   | r1   | r1     |      |       |        |
| **22** |      |      | r2   | r2   | r2   | r2   | r2   | r2   | r2   | r2   | r2   | r2   | r2   | r2     |      |       |        |

# Pregunta 3

Se ha modificado el código visto en la pregunta 1 para ejecutar acciones semánticas las cuales se encuentran en el archivo de entrada ```producciones2.txt```. La funcion ```readInstructions()``` coloca éstas acciones dentro en el tercer espacio de cada arreglo.

 Como las acciones semánticas están escritas en JavaScript, utilizmos el módulo ```pyexecjs``` para ejecutar las acciones semánticas en un contexto de JS dentro del archivo de python.

 El nuevo arreglo + 
# Pregunta 4

Se ha modificado el código visto en la pregunta 1 para incluir la forma sentencial derecha (Right Sentential Form), o abreviada '*RSF*'. 
Ésta se encuentra dentro del arreglo  ```right_sent``` que se origina al copiar el arreglo ```inputs```
