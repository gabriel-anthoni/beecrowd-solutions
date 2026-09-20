<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1009">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1009 — Salário com Bônus</h3>

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
      A entrada contém o primeiro nome de um vendedor (string), o seu salário fixo (ponto flutuante) e o total de vendas efetuadas por ele no mês em dinheiro (ponto flutuante).<br><br>
      <b>🧠 Lógica:</b><br>
      • Leia o nome do vendedor usando <code>input()</code>.<br>
      • Leia o salário fixo e o montante total de vendas usando <code>input()</code> convertidos para <code>float()</code>.<br>
      • Calcule o total a receber somando o salário fixo a 15% de comissão sobre as vendas efetuadas: <code>TOTAL = salary + (sales · 0.15)</code>.<br>
      • Utilize f-string para formatar a saída com 2 casas decimais.<br><br>
      <b>📤 Saída:</b><br>
      O programa deve exibir o texto <code>TOTAL = R$ </code> seguido pelo valor total que o funcionário deve receber, com exatamente duas casas decimais.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input contains a seller's first name (string), their fixed salary (floating-point), and the total sale value made by them in the month (floating-point).<br><br>
      <b>🧠 Logic:</b><br>
      • Read the seller's name using <code>input()</code>.<br>
      • Read the fixed salary and total sales value using <code>input()</code> converted to <code>float()</code>.<br>
      • Calculate the total earnings by adding the fixed salary to a 15% commission on total sales: <code>TOTAL = salary + (sales · 0.15)</code>.<br>
      • Use f-string to format the output to 2 decimal places.<br><br>
      <b>📤 Output:</b><br>
      The program must display the text <code>TOTAL = R$ </code> followed by the total amount the employee is to receive, with exactly two decimal places.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
JOAO
500.00
1230.30
```

### 📤 Exemplo de Saída / Example Output

```
TOTAL = R$ 684.54
```