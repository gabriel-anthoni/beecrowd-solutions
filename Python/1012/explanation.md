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
      <p align="center"><i>beecrowd | 1012</i></p>
      <h3 align="center">Área</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A entrada contém três valores de ponto flutuante com dupla precisão: A, B e C.

*Exemplo de entrada:*
```
3.0 4.0 5.2
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

- Leia os três valores da linha de entrada usando `input().split()` e converta-os para `float()`.
- Calcule a área de cada figura geométrica conforme as fórmulas abaixo:
<br>

- Área do triângulo retângulo que tem A por base e C por altura:

$$
TRIANGULO = \\frac{A \\cdot C}{2}
$$

- Área do círculo de raio C (utilizando $\\pi = 3.14159$):

$$
CIRCULO = \\pi \\cdot C^2
$$

- Área do trapézio que tem A e B por bases e C por altura:

$$
TRAPEZIO = \\frac{(A + B) \\cdot C}{2}
$$

- Área do quadrado que tem lado B:

$$
QUADRADO = B^2
$$

- Área do retângulo que tem lados A e B:

$$
RETANGULO = A \\cdot B
$$

- utilize f-string para formatar a saída com 3 casas decimais para cada cálculo.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- O arquivo de saída deve conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, sempre com a mensagem correspondente e um espaço após os dois pontos, seguida pelo valor com 3 casas decimais.

*Exemplo de saída:*
```
TRIANGULO: 7.800
CIRCULO: 84.949
TRAPEZIO: 18.200
QUADRADO: 16.000
RETANGULO: 12.000
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
      <p align="center"><i>beecrowd | 1012</i></p>
      <h3 align="center">Area</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input file contains three double precision values: A, B and C.

*Example Input:*
```
3.0 4.0 5.2
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- Read the three floating-point values from the input line using `input().split()` and convert them to `float()`.
- Calculate the area of each geometric shape using the formulas:
<br>

- Rectangled triangle area with base A and height C:

$$
TRIANGULO = \\frac{A \\cdot C}{2}
$$

- Circle area with radius C (using $\\pi = 3.14159$):

$$
CIRCULO = \\pi \\cdot C^2
$$

- Trapezium area with bases A and B, and height C:

$$
TRAPEZIO = \\frac{(A + B) \\cdot C}{2}
$$

- Square area with side B:

$$
QUADRADO = B^2
$$

- Rectangle area with sides A and B:

$$
RETANGULO = A \\cdot B
$$

- use f-string to format the output with 3 decimal places for each calculation.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- The output file must contain 5 lines of data. Each line corresponds to one of the described areas, with the corresponding message and one space after the colon, followed by the value with 3 decimal places.

*Example Output:*
```
TRIANGULO: 7.800
CIRCULO: 84.949
TRAPEZIO: 18.200
QUADRADO: 16.000
RETANGULO: 12.000
```