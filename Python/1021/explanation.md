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
      <p align="center"><i>beecrowd | 1021</i></p>
      <h3 align="center">Notas e Moedas</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A entrada contém um valor de ponto flutuante com duas casas decimais, representando o valor monetário.

*Exemplo de entrada:*
```
576.73
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

- Leia o valor de ponto flutuante e multiplique-o por 100, arredondando o resultado para o inteiro mais próximo usando `int(round(float(input()) * 100))`. Isso evita erros comuns de imprecisão com números de ponto flutuante em Python.
- Crie duas listas representando os valores das notas e das moedas em centavos para facilitar as operações matemáticas:
  - Notas (em centavos): `[10000, 5000, 2000, 1000, 500, 200]`
  - Moedas (em centavos): `[100, 50, 25, 10, 5, 1]`
- Itere sobre a lista de notas:
  - Calcule a quantidade de notas dividindo o valor restante pela nota atual (`money // bill`).
  - Atualize o valor restante com o resto da divisão (`money %= bill`).
- Repita o mesmo processo iterando sobre a lista de moedas.
- utilize f-string para formatar os valores de exibição dividindo a nota/moeda por 100 para voltar ao formato decimal com `.2f`.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- Imprima a quantidade mínima de notas e moedas necessárias no formato solicitado, indicando "NOTAS:" e "MOEDAS:" como cabeçalhos.

*Exemplo de saída:*
```
NOTAS:
5 nota(s) de R$ 100.00
1 nota(s) de R$ 50.00
1 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
1 nota(s) de R$ 5.00
0 nota(s) de R$ 2.00
MOEDAS:
1 moeda(s) de R$ 1.00
1 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
2 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
3 moeda(s) de R$ 0.01
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
      <p align="center"><i>beecrowd | 1021</i></p>
      <h3 align="center">Banknotes and Coins</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input file contains a floating-point value with two decimal places, representing the monetary value.

*Example Input:*
```
576.73
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- Read the floating-point value and multiply it by 100, rounding the result to the nearest integer using `int(round(float(input()) * 100))`. This prevents common floating-point precision issues in Python.
- Create two lists representing banknotes and coins in cents to make mathematical operations easier:
  - Banknotes (in cents): `[10000, 5000, 2000, 1000, 500, 200]`
  - Coins (in cents): `[100, 50, 25, 10, 5, 1]`
- Iterate through the banknotes list:
  - Calculate the quantity of notes needed by dividing the remaining value by the current note (`money // bill`).
  - Update the remaining value with the remainder of the division (`money %= bill`).
- Repeat the exact same process iterating through the coins list.
- Use f-string to format the display values by dividing the banknote/coin by 100 to show them in a decimal format with `.2f`.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- Print the minimum quantity of banknotes and coins necessary in the requested format, showing "NOTAS:" and "MOEDAS:" as headers.

*Example Output:*
```
NOTAS:
5 nota(s) de R$ 100.00
1 nota(s) de R$ 50.00
1 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
1 nota(s) de R$ 5.00
0 nota(s) de R$ 2.00
MOEDAS:
1 moeda(s) de R$ 1.00
1 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
2 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
3 moeda(s) de R$ 0.01
```