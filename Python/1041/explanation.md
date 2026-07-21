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
      <p align="center"><i>beecrowd | 1041</i></p>
      <h3 align="center">Coordenadas de um Ponto</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A entrada contém as coordenadas $x$ e $y$ de um ponto em um plano cartesiano, representadas por dois valores de ponto flutuante na mesma linha.

*Exemplo de entrada:*
```
4.5 -2.2
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

- O objetivo é determinar em qual quadrante do plano cartesiano o ponto $(x, y)$ se encontra, ou se ele está sobre um dos eixos ou na origem.
- As regras de posicionamento são:
  - **Origem**: $x = 0$ e $y = 0$.
  - **Eixo X**: o ponto está sobre o eixo horizontal, logo $y = 0$ (e $x \neq 0$).
  - **Eixo Y**: o ponto está sobre o eixo vertical, logo $x = 0$ (e $y \neq 0$).
  - **Quadrantes**:
    - **Q1**: $x > 0$ e $y > 0$ (superior direito).
    - **Q2**: $x < 0$ e $y > 0$ (superior esquerdo).
    - **Q3**: $x < 0$ e $y < 0$ (inferior esquerdo).
    - **Q4**: $x > 0$ e $y < 0$ (inferior direito).

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- Imprima o nome do quadrante correspondente (`Q1`, `Q2`, `Q3` ou `Q4`), `Origem` ou sobre qual eixo o ponto se encontra (`Eixo X` ou `Eixo Y`).

*Exemplo de saída:*
```
Q4
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
      <p align="center"><i>beecrowd | 1041</i></p>
      <h3 align="center">Coordinates of a Point</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input contains the $x$ and $y$ coordinates of a point in a 2D Cartesian plane, represented by two floating-point values on the same line.

*Example Input:*
```
0.1 0.1
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- The goal is to determine which quadrant of the Cartesian plane the point $(x, y)$ belongs to, or whether it lies on one of the axes or at the origin.
- Position boundaries are defined as:
  - **Origem (Origin)**: $x = 0$ and $y = 0$.
  - **Eixo X (X-Axis)**: the point lies on the horizontal axis, meaning $y = 0$ (and $x \neq 0$).
  - **Eixo Y (Y-Axis)**: the point lies on the vertical axis, meaning $x = 0$ (and $y \neq 0$).
  - **Quadrants**:
    - **Q1**: $x > 0$ and $y > 0$ (top-right).
    - **Q2**: $x < 0$ and $y > 0$ (top-left).
    - **Q3**: $x < 0$ and $y < 0$ (bottom-left).
    - **Q4**: $x > 0$ and $y < 0$ (bottom-right).

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- Print the matching quadrant label (`Q1`, `Q2`, `Q3`, or `Q4`), `Origem` or which axis the point is sitting on (`Eixo X` or `Eixo Y`).

*Example Output:*
```
Q1
```