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
      <p align="center"><i>beecrowd | 1051</i></p>
      <h3 align="center">Imposto de Renda</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A entrada contém um valor de ponto flutuante com duas casas decimais, representando o salário de uma pessoa.

*Exemplo de entrada:*
```
3002.00
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

- Leia o valor do salário como um número de ponto flutuante (`float`).
- Verifique progressivamente em qual faixa de imposto o salário se enquadra:
  - Salários até R$ 2000,00 são **Isentos** de imposto (`imposto = 0`).
  - De R$ 2000,01 até R$ 3000,00: aplica-se 8% sobre o valor que excede R$ 2000,00.
  - De R$ 3000,01 até R$ 4500,00: aplica-se 18% sobre o valor que excede R$ 3000,00, somado à taxa fixa máxima acumulada da faixa anterior (R$ 80,00).
  - Acima de R$ 4500,00: aplica-se 28% sobre o valor que excede R$ 4500,00, somado à taxa fixa máxima acumulada das faixas anteriores (R$ 80,00 + R$ 270,00 = R$ 350,00).
- Se o imposto total for 0, exiba a mensagem `"Isento"`. Caso contrário, exiba o resultado no formato `R$ XX.XX`.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- Imprima a mensagem `"Isento"` ou o valor do imposto devido com duas casas decimais após a vírgula/ponto, precedido de `R$ `.

*Exemplo de saída:*
```
R$ 80.36
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
      <p align="center"><i>beecrowd | 1051</i></p>
      <h3 align="center">Taxes</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input contains a floating-point number with two decimal places, representing a salary.

*Example Input:*
```
3002.00
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- Read the income value as a floating-point number (`float`).
- Check progressively which tax bracket the income falls into:
  - Salaries up to R$ 2000.00 are **Tax-free** (`tax = 0`).
  - From R$ 2000.01 to R$ 3000.00: apply an 8% tax on the amount exceeding R$ 2000.00.
  - From R$ 3000.01 to R$ 4500.00: apply an 18% tax on the amount exceeding R$ 3000.00, plus the accumulated maximum tax from the lower bracket (R$ 80.00).
  - Above R$ 4500.00: apply a 28% tax on the amount exceeding R$ 4500.00, plus the accumulated maximum tax from lower brackets (R$ 80.00 + R$ 270.00 = R$ 350.00).
- If the total tax is 0, display `"Isento"`. Otherwise, print the formatted result as `R$ XX.XX`.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- Print `"Isento"` if tax is zero, or the total tax due formatted to two decimal places, preceded by `R$ `.

*Example Output:*
```
R$ 80.36
```