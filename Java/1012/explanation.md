### <img src="https://static.wikia.nocookie.net/duolingo/images/1/17/Brazil_bandera.png/revision/latest?cb=20230710181600&path-prefix=es" width="20"> PT-BR

<!----------------------------------------------------------------------------------------->

<table>
  <tr>
    <th width="300">Linguagem</th>
    <th width="1000">Questão</th>
  </tr>
  <tr>
    <td>
      <p align="center"><img src="https://skillicons.dev/icons?i=java"></p>
      <p align="center"><code>Java 19</code></p>
    </td>
    <td>
      <p align="center"><i>beecrowd | 1012</i></p>
      <h3 align="center">Área</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A entrada contém três valores de ponto flutuante (`double`): $A$, $B$ e $C$.

*Exemplo de entrada:*
```
3.0 4.0 5.2
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

- Ler os três valores de ponto flutuante $A$, $B$ e $C$.
- Calcular as áreas geométricas conforme as fórmulas:
  - **Triângulo Retângulo** (base $A$, altura $C$):
    $$\text{TRIANGULO} = \frac{A \times C}{2.0}$$
  - **Círculo** (raio $C$, $\pi = 3.14159$):
    $$\text{CIRCULO} = 3.14159 \times C^2$$
  - **Trapézio** (bases $A$ e $B$, altura $C$):
    $$\text{TRAPEZIO} = \frac{(A + B) \times C}{2.0}$$
  - **Quadrado** (lado $B$):
    $$\text{QUADRADO} = B^2$$
  - **Retângulo** (lados $A$ e $B$):
    $$\text{RETANGULO} = A \times B$$
- Exibir cada resultado utilizando `System.out.printf()` com **3 casas decimais** e quebra de linha `\n`.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- Imprima cinco linhas de saída, cada uma correspondente a uma das áreas calculadas, formatadas com 3 casas decimais.

*Exemplo de saída:*
```
TRIANGULO: 7.800
CIRCULO: 84.949
TRAPEZIO: 18.200
QUADRADO: 16.000
RETANGULO: 15.000
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
      <p align="center"><img src="https://skillicons.dev/icons?i=java"></p>
      <p align="center"><code>Java 19</code></p>
    </td>
    <td>
      <p align="center"><i>beecrowd | 1012</i></p>
      <h3 align="center">Area</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input contains three floating-point values (`double`): $A$, $B$, and $C$.

*Example Input:*
```
3.0 4.0 5.2
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- Read three floating-point values $A$, $B$, and $C$.
- Calculate the geometric areas using the respective formulas:
  - **Right-angled Triangle** (base $A$, height $C$):
    $$\text{TRIANGULO} = \frac{A \times C}{2.0}$$
  - **Circle** (radius $C$, $\pi = 3.14159$):
    $$\text{CIRCULO} = 3.14159 \times C^2$$
  - **Trapezium** (bases $A$ and $B$, height $C$):
    $$\text{TRAPEZIO} = \frac{(A + B) \times C}{2.0}$$
  - **Square** (side $B$):
    $$\text{QUADRADO} = B^2$$
  - **Rectangle** (sides $A$ and $B$):
    $$\text{RETANGULO} = A \times B$$
- Output each calculated area formatted to **3 decimal places** using `System.out.printf()` with a newline break `\n`.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- Print five lines of output, each corresponding to one of the calculated areas, formatted with 3 decimal places.

*Example Output:*
```
TRIANGULO: 7.800
CIRCULO: 84.949
TRAPEZIO: 18.200
QUADRADO: 16.000
RETANGULO: 15.000
```