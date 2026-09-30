<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1010">
    <img src="https://skillicons.dev/icons?i=java" width="45" alt="Java Logo" />
  </a>

  <h3>beecrowd 1010 — Cálculo Simples</h3>

  <p>
    <img src="https://img.shields.io/badge/Linguagem-Java_19-ED8B00?style=flat-square&logo=openjdk&logoColor=white" />
    <img src="https://img.shields.io/badge/N%C3%ADvel-3-orange?style=flat-square"/>
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
      O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores: o código de uma peça (<code>int</code>), o número de peças (<code>int</code>) e o valor unitário de cada peça (<code>double</code>).<br><br>
      <b>🧠 Lógica:</b><br>
      • Ler as informações da primeira peça (código, quantidade e preço unitário).<br>
      • Ler as informações da segunda peça (código, quantidade e preço unitário).<br>
      • Calcular o valor total a ser pago multiplicando a quantidade de cada peça pelo seu preço unitário e somando os dois resultados:<br>
      <code>VALOR A PAGAR = (Q1 * P1) + (Q2 * P2)</code><br>
      • Imprimir a mensagem <code>VALOR A PAGAR: R$ </code> seguida pelo valor total formatado com <b>2 casas decimais</b> e quebra de linha <code>\n</code>.<br><br>
      <b>📤 Saída:</b><br>
      Imprima o valor total a ser pago com 2 casas decimais.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input file contains two lines of data. In each line there will be 3 values: code of a product (<code>int</code>), number of units of a product (<code>int</code>), and price for one unit (<code>double</code>).<br><br>
      <b>🧠 Logic:</b><br>
      • Read information for the first product (code, quantity, unit price).<br>
      • Read information for the second product (code, quantity, unit price).<br>
      • Calculate total amount payable by multiplying quantity by unit price for each product and adding them up:<br>
      <code>TOTAL = (Q1 * P1) + (Q2 * P2)</code><br>
      • Output <code>VALOR A PAGAR: R$ </code> followed by the total formatted to <b>2 decimal places</b> and an end-of-line break <code>\n</code>.<br><br>
      <b>📤 Output:</b><br>
      Print the total amount to pay with 2 decimal places.
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