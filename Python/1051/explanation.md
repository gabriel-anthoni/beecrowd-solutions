<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1051">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1051 — Imposto de Renda</h3>

  <p>
    <img src="https://img.shields.io/badge/Linguagem-Python_3.11-3776AB?style=flat-square&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/N%C3%ADvel-2-green?style=flat-square" />
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
      A entrada contém um valor de ponto flutuante com duas casas decimais, representando o salário de uma pessoa.<br><br>
      <b>🧠 Lógica:</b><br>
      • Leia o salário com <code>float(input())</code>.<br>
      • Verifique a faixa de tributação progressiva usando condicionais (<code>if/elif/else</code>):<br>
      &nbsp;&nbsp;- <code>Salário ≤ 2000.00</code>: <b>Isento</b><br>
      &nbsp;&nbsp;- <code>2000.01 ≤ Salário ≤ 3000.00</code>: 8% sobre a quantia acima de R$ 2000.00<br>
      &nbsp;&nbsp;- <code>3000.01 ≤ Salário ≤ 4500.00</code>: 18% sobre a quantia acima de R$ 3000.00 + R$ 80.00 fixos<br>
      &nbsp;&nbsp;- <code>Salário > 4500.00</code>: 28% sobre a quantia acima de R$ 4500.00 + R$ 350.00 fixos<br>
      • Se for isento, exiba <code>Isento</code>; caso contrário, exiba o imposto formatado como <code>R$ XX.XX</code> com duas casas decimais.<br><br>
      <b>📤 Saída:</b><br>
      Imprima <code>Isento</code> ou o valor do imposto devido no formato <code>R$ XX.XX</code>.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input contains a single floating-point number with two decimal places representing a salary.<br><br>
      <b>🧠 Logic:</b><br>
      • Read the salary using <code>float(input())</code>.<br>
      • Determine progressive tax brackets using conditionals (<code>if/elif/else</code>):<br>
      &nbsp;&nbsp;- <code>Salary ≤ 2000.00</code>: <b>Tax-free</b><br>
      &nbsp;&nbsp;- <code>2000.01 ≤ Salary ≤ 3000.00</code>: 8% on amount exceeding R$ 2000.00<br>
      &nbsp;&nbsp;- <code>3000.01 ≤ Salary ≤ 4500.00</code>: 18% on amount exceeding R$ 3000.00 + R$ 80.00 fixed<br>
      &nbsp;&nbsp;- <code>Salary > 4500.00</code>: 28% on amount exceeding R$ 4500.00 + R$ 350.00 fixed<br>
      • If tax-free, print <code>Isento</code>; otherwise, print total tax formatted as <code>R$ XX.XX</code> with 2 decimal places.<br><br>
      <b>📤 Output:</b><br>
      Print <code>Isento</code> or the total calculated tax formatted as <code>R$ XX.XX</code>.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
3002.00
```

### 📤 Exemplo de Saída / Example Output

```
R$ 80.36
```