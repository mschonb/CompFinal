# Pregunta 2

Marcelo Schonbrunn

Yann Le Lorier
$$
\begin{align}
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
\text{FIRST}(S) = \{  \}
$$
Por otro lado:
$$
\text{FIRST}(\text{DIGIT}) = \{ \}
$$
Finalmente:
$$
\text{FIRST}(\text{DIGITS}) = \{ \}
$$
**Follow**
$$
\text{FOLLOW}(S) = \{  \}
$$

$$
\text{FOLLOW}(\text{DIGIT}) = \{  \}
$$

$$
\text{FOLLOW}(\text{DIGITS}) = \{  \}
$$



```mermaid
stateDiagram
[*] --> 
```



- Crear la tabla del analizador SLR para esa gramática,(Action y GOTO)(10 puntos)

**Tabla Action Y GoTo**

| 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | S    | DIGIT | DIGITS |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----- | ------ |
|      |      |      |      |      |      |      |      |      |      |      |       |        |
|      |      |      |      |      |      |      |      |      |      |      |       |        |
|      |      |      |      |      |      |      |      |      |      |      |       |        |
|      |      |      |      |      |      |      |      |      |      |      |       |        |
|      |      |      |      |      |      |      |      |      |      |      |       |        |
|      |      |      |      |      |      |      |      |      |      |      |       |        |
|      |      |      |      |      |      |      |      |      |      |      |       |        |
|      |      |      |      |      |      |      |      |      |      |      |       |        |
|      |      |      |      |      |      |      |      |      |      |      |       |        |

