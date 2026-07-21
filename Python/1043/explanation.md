### <img src="https://static.wikia.nocookie.net/duolingo/images/1/17/Brazil_bandera.png/revision/latest?cb=20230710181600&path-prefix=es" width="20"> PT-BR

<!----------------------------------------------------------------------------------------->

<table>
  <tr>
    <th width="300">Linguagem</th>
    <th width="1000">Questão</th>
  </tr>
  <tr>
    <td>
      <p align="center"><img src="https://skillicons.dev/icons?i=python"></p>
      <p align="center"><code>Python 3.11</code></p>
    </td>
    <td>
      <p align="center"><i>beecrowd | 1043</i></p>
      <h3 align="center">Triângulo</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A entrada contém três valores de ponto flutuante na mesma linha.

*Exemplo de entrada:*
```
6.0 4.0 2.0
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

- O objetivo é verificar se os três valores representados por $A$, $B$ e $C$ podem formar um triângulo.
- De acordo com a **desigualdade triangular**, três segmentos de reta só podem formar um triângulo se a soma de quaisquer dois lados for estritamente maior que o terceiro lado restante:
  - $A < B + C$
  - $B < A + C$
  - $C < A + B$
- Se a condição for **verdadeira**:
  - Calculamos o perímetro do triângulo:
    $$\text{Perímetro} = A + B + C$$
- Se a condição for **falsa**:
  - Calculamos a área de um trapézio que tem bases $A$ e $B$ e altura $C$:
    $$\text{Área} = \frac{(A + B) \times C}{2}$$

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- Imprima o resultado com exatamente uma casa decimal, seguido do tipo de medida calculada (`Perimetro = ...` ou `Area = ...`).

*Exemplo de saída:*
```
Area = 10.0
```

---

<!----------------------------------------------------------------------------------------->

### <img src="https://static.wikia.nocookie.net/duolingo/images/7/79/Ingles.png/revision/latest?cb=20230710181050&path-prefix=es" width="20"> EN

<!----------------------------------------------------------------------------------------->

<table>
  <tr>
    <th width="300">Language</th>
    <th width="1000">Problem</th>
  </tr>
  <tr>
    <td>
      <p align="center"><img src="https://skillicons.dev/icons?i=python"></p>
      <p align="center"><code>Python 3.11</code></p>
    </td>
    <td>
      <p align="center"><i>beecrowd | 1043</i></p>
      <h3 align="center">Triangle</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input contains three floating-point values written on a single line.

*Example Input:*
```
6.0 4.0 2.1
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- The objective is to verify if three side lengths represented by $A$, $B$, and $C$ can successfully form a triangle.
- According to the **triangle inequality theorem**, three segments can only form a triangle if the sum of any two sides is strictly greater than the remaining third side:
  - $A < B + C$
  - $B < A + C$
  - $C < A + B$
- If the condition is **true**:
  - Calculate the perimeter of the triangle:
    $$\text{Perimeter} = A + B + C$$
- If the condition is **false**:
  - Calculate the area of a trapezium where $A$ and $B$ are its parallel bases and $C$ is its height:
    $$\text{Area} = \frac{(A + B) \times C}{2}$$

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- Print the calculated value formatted to exactly one decimal place, preceded by the correct metric label (`Perimetro = ...` or `Area = ...`).

*Example Output:*
```
Perimetro = 12.1
```