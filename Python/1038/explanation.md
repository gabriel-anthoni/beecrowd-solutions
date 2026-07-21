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
      <p align="center"><i>beecrowd | 1038</i></p>
      <h3 align="center">Lanche</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A entrada contém dois valores inteiros: o código de um item (de 1 a 5) e a quantidade deste item, conforme a tabela de preços.

*Exemplo de entrada:*
```
3 2
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

- O problema pede para calcular o valor total de uma compra com base em uma tabela de preços pré-definida:
  - Código 1: Cachorro Quente — R$ 4.00
  - Código 2: X-Salada — R$ 4.50
  - Código 3: X-Bacon — R$ 5.00
  - Código 4: Torrada Simples — R$ 2.00
  - Código 5: Refrigerante — R$ 1.50
- Uma forma extremamente inteligente de resolver isso em Python é mapear os preços diretamente em uma lista ordenada. 
- Como os códigos vão de 1 a 5, acessamos o preço correto na lista usando o índice ajustado: de forma que o código digitado menos 1 aponte para a posição correta.
- Multiplicamos o preço pela quantidade fornecida e exibimos o resultado formatado.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- O arquivo de saída deve conter a mensagem "Total: R$ " seguida pelo valor a ser pago, formatado com 2 casas decimais.

*Exemplo de saída:*
```
Total: R$ 10.00
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
      <p align="center"><i>beecrowd | 1038</i></p>
      <h3 align="center">Snack</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input contains two integer values: the product code (from 1 to 5) and the quantity of this item, according to the price table.

*Example Input:*
```
4 3
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- The goal is to calculate the total amount of an order based on a predefined price table:
  - Code 1: Hot Dog — R$ 4.00
  - Code 2: X-Salad — R$ 4.50
  - Code 3: X-Bacon — R$ 5.00
  - Code 4: Simple Toast — R$ 2.00
  - Code 5: Soft Drink — R$ 1.50
- An extremely clever way to solve this in Python is to map the prices directly into an ordered list.
- Since the product codes range from 1 to 5, we can retrieve the correct price by indexing the list at the product code minus 1.
- We then multiply this price by the quantity and format the total output.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- The output file must contain the message "Total: R$ " followed by the calculated value, formatted with 2 decimal places.

*Example Output:*
```
Total: R$ 6.00
```