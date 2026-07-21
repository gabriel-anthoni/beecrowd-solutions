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
      <p align="center"><i>beecrowd | 1022</i></p>
      <h3 align="center">TDA Racional</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A entrada contém um valor inteiro N correspondente ao número de casos de teste. Cada caso de teste subsequente contém uma linha representando uma operação entre duas frações (ex: `1 / 2 + 3 / 4`).

*Exemplo de entrada:*
```
4
1 / 2 + 3 / 4
1 / 2 - 3 / 4
2 / 3 * 6 / 6
1 / 2 / 3 / 4
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

- Importe o módulo `math` para poder utilizar a função de cálculo do Máximo Divisor Comum (`math.gcd`).
- Leia a quantidade total de operações com `int(input())`.
- Para cada operação, divida a entrada usando `.split()` e mapeie os numeradores, denominadores e o operador correspondente baseado em seus índices:
  - $N1$ no índice 0, $D1$ no índice 2.
  - Operador $OP$ no índice 3.
  - $N2$ no índice 4, $D2$ no índice 6.
- Realize o cálculo da fração de acordo com o operador matemático fornecido:
<br>

- **Soma (`+`):**

$$
\frac{N1 \cdot D2 + N2 \cdot D1}{D1 \cdot D2}
$$

- **Subtração (`-`):**

$$
\frac{N1 \cdot D2 - N2 \cdot D1}{D1 \cdot D2}
$$

  - **Multiplicação (`*`):**

$$
\frac{N1 \cdot N2}{D1 \cdot D2}
$$

- **Divisão (`/`):**

$$
\frac{N1 \cdot D2}{N2 \cdot D1}
$$

- Calcule o Máximo Divisor Comum (MDC) entre o numerador (`num`) e o denominador (`den`) usando `math.gcd(num, den)`.
- Divida de forma inteira (`//`) tanto o numerador quanto o denominador pelo MDC encontrado para obter a fração simplificada.
- Imprima a fração original resultante e a sua forma simplificada no formato exigido.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- Para cada caso de teste, exiba a fração resultante sem simplificação, seguida pelo sinal de igualdade e a fração totalmente simplificada.

*Exemplo de saída:*
```
10/8 = 5/4
-2/8 = -1/4
12/18 = 2/3
4/6 = 2/3
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
      <p align="center"><i>beecrowd | 1022</i></p>
      <h3 align="center">Rational TDA</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input contains an integer value N corresponding to the number of test cases. Each subsequent test case contains a line representing an operation between two fractions (e.g., `1 / 2 + 3 / 4`).

*Example Input:*
```
4
1 / 2 + 3 / 4
1 / 2 - 3 / 4
2 / 3 * 6 / 6
1 / 2 / 3 / 4
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- Import the `math` module to be able to use the Greatest Common Divisor function (`math.gcd`).
- Read the total number of operations using `int(input())`.
- For each operation, split the input line using `.split()` and map the numerators, denominators, and operator based on their indices:
  - $N1$ at index 0, $D1$ at index 2.
  - Operator $OP$ at index 3.
  - $N2$ at index 4, $D2$ at index 6.
- Perform the fraction calculation based on the given mathematical operator:
<br>

- **Addition (`+`):**

$$
\frac{N1 \cdot D2 + N2 \cdot D1}{D1 \cdot D2}
$$

- **Subtraction (`-`):**

$$
\frac{N1 \cdot D2 - N2 \cdot D1}{D1 \cdot D2}
$$

- **Multiplication (`*`):**

$$
\frac{N1 \cdot N2}{D1 \cdot D2}
$$

- **Division (`/`):**

$$
\frac{N1 \cdot D2}{N2 \cdot D1}
$$

- Compute the Greatest Common Divisor (GCD) between the numerator (`num`) and the denominator (`den`) using `math.gcd(num, den)`.
- Use integer division (`//`) to divide both the numerator and denominator by the GCD to find the simplified fraction.
- Print the original fraction and its simplified version in the required format.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- For each test case, print the resulting fraction without simplification, followed by an equal sign and the fully simplified fraction.

*Example Output:*
```
10/8 = 5/4
-2/8 = -1/4
12/18 = 2/3
4/6 = 2/3
```