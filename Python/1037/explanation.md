<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1037">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1037 — Intervalo</h3>

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
      A entrada contém um único número de ponto flutuante.<br><br>
      <b>🧠 Lógica:</b><br>
      • Leia o valor utilizando <code>float(input())</code>.<br>
      • Verifique a qual intervalo o valor pertence usando estruturas condicionais (<code>if/elif/else</code>):<br>
      &nbsp;&nbsp;- <code>0 ≤ x ≤ 25</code>: <code>Intervalo [0,25]</code><br>
      &nbsp;&nbsp;- <code>25 < x ≤ 50</code>: <code>Intervalo (25,50]</code><br>
      &nbsp;&nbsp;- <code>50 < x ≤ 75</code>: <code>Intervalo (50,75]</code><br>
      &nbsp;&nbsp;- <code>75 < x ≤ 100</code>: <code>Intervalo (75,100]</code><br>
      • Se o número for menor que 0 ou maior que 100, exiba <code>Fora de intervalo</code>.<br><br>
      <b>📤 Saída:</b><br>
      Imprima a mensagem com o intervalo correspondente ou <code>Fora de intervalo</code>.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input contains a single floating-point number.<br><br>
      <b>🧠 Logic:</b><br>
      • Read the value using <code>float(input())</code>.<br>
      • Determine which interval the value belongs to using conditional statements (<code>if/elif/else</code>):<br>
      &nbsp;&nbsp;- <code>0 ≤ x ≤ 25</code>: <code>Intervalo [0,25]</code><br>
      &nbsp;&nbsp;- <code>25 < x ≤ 50</code>: <code>Intervalo (25,50]</code><br>
      &nbsp;&nbsp;- <code>50 < x ≤ 75</code>: <code>Intervalo (50,75]</code><br>
      &nbsp;&nbsp;- <code>75 < x ≤ 100</code>: <code>Intervalo (75,100]</code><br>
      • If the number is less than 0 or greater than 100, display <code>Fora de intervalo</code>.<br><br>
      <b>📤 Output:</b><br>
      Print the corresponding interval message or <code>Fora de intervalo</code>.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
25.01
```

### 📤 Exemplo de Saída / Example Output

```txt
Intervalo (25,50]
```