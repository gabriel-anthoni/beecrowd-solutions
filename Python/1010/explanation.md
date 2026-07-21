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
      <p align="center"><i>beecrowd | 1010</i></p>
      <h3 align="center">Cálculo Simples</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A entrada contém duas linhas de dados. Em cada linha haverá 3 valores: o código de uma peça (inteiro), a quantidade de peças (inteiro) e o valor unitário de cada peça (ponto flutuante).

*Exemplo de entrada:*
```
12 1 5.30
16 2 5.10
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

- Leia duas linhas de entrada utilizando `input().split()` para separar os valores por espaço.
- Converta os códigos e as quantidades de peças para `int()` e os valores unitários para `float()`.
- Calcule o total a pagar multiplicando a quantidade pelo valor de cada produto e somando os resultados:

$$
VALOR = (q_1 \cdot p_1) + (q_2 \cdot p_2)
$$

- utilize f-string para formatar a saída com 2 casas decimais.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- O programa deve exibir o texto `VALOR A PAGAR: R$ ` seguido pelo valor total correspondente a ser pago, com exatamente duas casas decimais.

*Exemplo de saída:*
```
VALOR A PAGAR: R$ 15.50
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
      <p align="center"><i>beecrowd | 1010</i></p>
      <h3 align="center">Simple Calculate</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input file contains two lines of data. In each line, there will be 3 values: a product code (integer), the number of units of the product (integer), and the price for one unit of the product (floating-point).

*Example Input:*
```
12 1 5.30
16 2 5.10
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- Read two lines of input using `input().split()` to separate values by space.
- Convert the product codes and product units to `int()`, and the unit prices to `float()`.
- Calculate the total amount to pay by multiplying the quantity by the price of each product and adding the results:

$$
VALOR = (q_1 \cdot p_1) + (q_2 \cdot p_2)
$$

- use f-string to format the output to 2 decimal places.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- The program must display the text `VALOR A PAGAR: R$ ` followed by the total amount to be paid, with exactly two decimal places.

*Example Output:*
```
VALOR A PAGAR: R$ 15.50
```