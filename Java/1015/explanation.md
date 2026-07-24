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
      <p align="center"><i>beecrowd | 1015</i></p>
      <h3 align="center">Distância Entre Dois Pontos</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A entrada contém duas linhas de dados; a primeira linha contém dois valores de ponto flutuante $x_1$ e $y_1$ e a segunda linha contém dois valores de ponto flutuante $x_2$ e $y_2$.

*Exemplo de entrada:*
```
1.0 7.0
5.0 9.0
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

- Ler as coordenadas do primeiro ponto $(x_1, y_1)$ e do segundo ponto $(x_2, y_2)$.
- Aplicar a fórmula da distância euclidiana entre dois pontos no plano cartesiano:
  $$\text{Distância} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$
- Em Java, utilizamos `Math.sqrt()` para a raiz quadrada e `Math.pow()` (ou multiplicação direta) para elevar ao quadrado.
- Formatar o resultado da saída com 4 casas decimais.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- Imprima o valor da distância com 4 casas após o ponto decimal e quebra de linha `\n`.

*Exemplo de saída:*
```
4.4721
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
      <p align="center"><i>beecrowd | 1015</i></p>
      <h3 align="center">Distance Between Two Points</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input contains two lines of data; the first one contains two floating-point values $x_1$ and $y_1$ and the second one contains two floating-point values $x_2$ and $y_2$.

*Example Input:*
```
1.0 7.0
5.0 9.0
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- Read the coordinates of the first point $(x_1, y_1)$ and the second point $(x_2, y_2)$.
- Apply the Euclidean distance formula between two points in a 2D plane:
  $$\text{Distance} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$
- In Java, use `Math.sqrt()` for the square root and `Math.pow()` (or simple multiplication) to square terms.
- Format the output value with 4 decimal places.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- Print the distance value with 4 digits after the decimal point and a newline `\n`.

*Example Output:*
```
4.4721
```