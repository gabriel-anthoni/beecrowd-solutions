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
      <p align="center"><i>beecrowd | 1015</i></p>
      <h3 align="center">Distância Entre Dois Pontos</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 e y1, e a segunda linha contém dois valores de ponto flutuante x2 e y2.

*Exemplo de entrada:*
```
1.0 7.0
5.9 -4.0
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

- Leia os valores de x e y da primeira linha usando `input().split()` e converta-os para `float()`.
- Faça o mesmo para a segunda linha.
- Calcule a distância de acordo com a fórmula da distância euclidiana:

$$
Distancia = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
$$

- No código, a raiz quadrada é calculada elevando o resultado da soma dos quadrados a `0.5` usando a função `pow()`.
- utilize f-string para formatar a saída com 4 casas decimais.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- Calcule e imprima o valor da distância com exatamente 4 casas decimais após o ponto decimal.

*Exemplo de saída:*
```
11.7610
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
      <p align="center"><i>beecrowd | 1015</i></p>
      <h3 align="center">Distance Between Two Points</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input file contains two lines of data. The first one contains two double values: x1 and y1, and the second one contains two double values: x2 and y2.

*Example Input:*
```
1.0 7.0
5.9 -4.0
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- Read the values of x and y from the first line using `input().split()` and convert them to `float()`.
- Do the same for the second line.
- Calculate the distance according to the Euclidean distance formula:

$$
Distance = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
$$

- In the code, the square root is computed by raising the sum of squares to the power of `0.5` using the `pow()` function.
- Use f-string to format the output with 4 decimal places.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- Calculate and print the distance value with exactly 4 decimal places after the decimal point.

*Example Output:*
```
11.7610
```