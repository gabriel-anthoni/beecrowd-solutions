<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1010">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1010 — Cálculo Simples</h3>

  <p>
    <img src="https://img.shields.io/badge/Linguagem-Python_3.11-3776AB?style=flat-square&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/N%C3%ADvel-3-green?style=flat-square" />
  </p>

</div>

---

### 📌 Resumo / Overview

<table align="center" width="100%">
  <tr>
    <th width="50%">🇧🇷 Português (PT-BR)</th>
    <th width="50%">🇺🇸 English (EN)</th>
  </tr>
  <tr>
    <td valign="top">
      <b>📥 Entrada:</b><br>
      A entrada contém duas linhas de dados. Em cada linha haverá 3 valores: o código de uma peça (inteiro), a quantidade de peças (inteiro) e o valor unitário de cada peça (ponto flutuante).<br><br>
      <b>🧠 Lógica:</b><br>
      • Leia duas linhas de entrada utilizando <code>input().split()</code> para separar os valores por espaço.<br>
      • Converta os códigos e as quantidades de peças para <code>int()</code> e os valores unitários para <code>float()</code>.<br>
      • Calcule o total a pagar multiplicando a quantidade pelo valor de cada produto e somando os resultados: <code>VALOR = (q₁ · p₁) + (q₂ · p₂)</code>.<br>
      • Utilize f-string para formatar a saída com 2 casas decimais.<br><br>
      <b>📤 Saída:</b><br>
      O programa deve exibir o texto <code>VALOR A PAGAR: R$ </code> seguido pelo valor total correspondente a ser pago, com exatamente duas casas decimais.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input file contains two lines of data. In each line, there will be 3 values: a product code (integer), the number of units of the product (integer), and the price for one unit of the product (floating-point).<br><br>
      <b>🧠 Logic:</b><br>
      • Read two lines of input using <code>input().split()</code> to separate values by space.<br>
      • Convert the product codes and product units to <code>int()</code>, and the unit prices to <code>float()</code>.<br>
      • Calculate the total amount to pay by multiplying the quantity by the price of each product and adding the results: <code>VALOR = (q₁ · p₁) + (q₂ · p₂)</code>.<br>
      • Use f-string to format the output to 2 decimal places.<br><br>
      <b>📤 Output:</b><br>
      The program must display the text <code>VALOR A PAGAR: R$ </code> followed by the total amount to be paid, with exactly two decimal places.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
12 1 5.30
16 2 5.10
```

### 📤 Exemplo de Saída / Example Output

```
VALOR A PAGAR: R$ 15.50
```