<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1048">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1048 — Aumento de Salário</h3>

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
      A entrada contém um único valor de ponto flutuante com duas casas decimais, representando o salário atual do funcionário.<br><br>
      <b>🧠 Lógica:</b><br>
      • Leia o valor do salário usando <code>float(input())</code>.<br>
      • Determine a porcentagem do reajuste através das faixas de renda com condicionais (<code>if/elif/else</code>):<br>
      &nbsp;&nbsp;- <code>0.00 ≤ Salário ≤ 400.00</code>: <b>15%</b><br>
      &nbsp;&nbsp;- <code>400.01 ≤ Salário ≤ 800.00</code>: <b>12%</b><br>
      &nbsp;&nbsp;- <code>800.01 ≤ Salário ≤ 1200.00</code>: <b>10%</b><br>
      &nbsp;&nbsp;- <code>1200.01 ≤ Salário ≤ 2000.00</code>: <b>7%</b><br>
      &nbsp;&nbsp;- <code>Salário > 2000.00</code>: <b>4%</b><br>
      • Calcule o valor ganho com o reajuste: <code>Reajuste = Salário · (Percentual / 100)</code>.<br>
      • Calcule o novo salário total: <code>NovoSalário = Salário + Reajuste</code>.<br>
      • Exiba o novo salário e o reajuste com 2 casas decimais, e o percentual aplicado.<br><br>
      <b>📤 Saída:</b><br>
      Imprima <code>Novo salario: ...</code>, <code>Reajuste ganho: ...</code> e <code>Em percentual: ... %</code> conforme o padrão do problema.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input contains a single floating-point value with two decimal places representing the employee's current salary.<br><br>
      <b>🧠 Logic:</b><br>
      • Read the salary value using <code>float(input())</code>.<br>
      • Determine the adjustment percentage based on income brackets using conditionals (<code>if/elif/else</code>):<br>
      &nbsp;&nbsp;- <code>0.00 ≤ Salary ≤ 400.00</code>: <b>15%</b><br>
      &nbsp;&nbsp;- <code>400.01 ≤ Salary ≤ 800.00</code>: <b>12%</b><br>
      &nbsp;&nbsp;- <code>800.01 ≤ Salary ≤ 1200.00</code>: <b>10%</b><br>
      &nbsp;&nbsp;- <code>1200.01 ≤ Salary ≤ 2000.00</code>: <b>7%</b><br>
      &nbsp;&nbsp;- <code>Salary > 2000.00</code>: <b>4%</b><br>
      • Calculate the money raise: <code>Reajuste = Salary · (Percentage / 100)</code>.<br>
      • Calculate the new salary: <code>NovoSalário = Salary + Reajuste</code>.<br>
      • Format the new salary and earned raise to 2 decimal places, along with the percentage rate.<br><br>
      <b>📤 Output:</b><br>
      Print <code>Novo salario: ...</code>, <code>Reajuste ganho: ...</code>, and <code>Em percentual: ... %</code> according to the specified format.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
400.00
```

### 📤 Exemplo de Saída / Example Output

```
Novo salario: 460.00
Reajuste ganho: 60.00
Em percentual: 15 %
```