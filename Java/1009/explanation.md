<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1009">
    <img src="https://skillicons.dev/icons?i=java" width="45" alt="Java Logo" />
  </a>

  <h3>beecrowd 1009 — Salário com Bônus</h3>

  <p>
    <img src="https://img.shields.io/badge/Linguagem-Java_19-ED8B00?style=flat-square&logo=openjdk&logoColor=white" />
    <img src="https://img.shields.io/badge/N%C3%ADvel-2-orange?style=flat-square"/>
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
      A entrada contém o primeiro nome de um vendedor (<code>String</code>), o seu salário fixo (<code>double</code>) e o montante total das vendas efetuadas por ele no mês (<code>double</code>).<br><br>
      <b>🧠 Lógica:</b><br>
      • Ler o nome do vendedor, seu salário fixo e o valor total de suas vendas no mês.<br>
      • Calcular a comissão de <b>15%</b> (ou <code>0.15</code>) sobre o total vendido e somá-la ao salário fixo:<br>
      <code>TOTAL = salary + (totalSales * 0.15)</code><br>
      • Imprimir o resultado com a mensagem <code>TOTAL = R$ </code> seguido pelo valor total a receber com <b>2 casas decimais</b> e quebra de linha <code>\n</code>.<br><br>
      <b>📤 Saída:</b><br>
      Imprima o total que o funcionário deverá receber ao final do mês, com 2 casas decimais.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input contains the seller's first name (<code>String</code>), fixed salary (<code>double</code>), and the total value of sales made by them in the month (<code>double</code>).<br><br>
      <b>🧠 Logic:</b><br>
      • Read the seller's name, fixed salary, and total sales amount.<br>
      • Calculate the <b>15%</b> (or <code>0.15</code>) commission on total sales and add it to the fixed salary:<br>
      <code>TOTAL = salary + (totalSales * 0.15)</code><br>
      • Print the message <code>TOTAL = R$ </code> followed by the final salary formatted to <b>2 decimal places</b> and an end-of-line break <code>\n</code>.<br><br>
      <b>📤 Output:</b><br>
      Print the total money the employee is to receive at the end of the month with 2 decimal places.
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