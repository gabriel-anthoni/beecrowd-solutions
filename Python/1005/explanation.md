<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1005">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1005 — Média 1</h3>

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
      A entrada contém dois valores de ponto flutuante com uma casa decimal.<br><br>
      <b>🧠 Lógica:</b><br>
      • Leia os dois valores decimais através da função <code>input()</code> convertida para <code>float()</code>.<br>
      • Multiplique cada valor pelo seu respectivo peso (3.5 para o primeiro e 7.5 para o segundo) e divida a soma por 11:<br><code>MEDIA = ((A · 3.5) + (B · 7.5)) / 11</code>.<br>
      • Utilize f-string para formatar a saída com 5 casas decimais.<br><br>
      <b>📤 Saída:</b><br>
      O programa deve exibir o texto <code>MEDIA = </code> seguido pelo resultado correspondente com exatamente 5 casas decimais.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input contains two floating-point values with one digit after the decimal point.<br><br>
      <b>🧠 Logic:</b><br>
      • Read the two decimal values using the <code>input()</code> function converted to <code>float()</code>.<br>
      • Multiply each value by its respective weight (3.5 for the first and 7.5 for the second) and divide their sum by 11:<br><code>MEDIA = ((A · 3.5) + (B · 7.5)) / 11</code>.<br>
      • Use f-string to format the output to 5 decimal places.<br><br>
      <b>📤 Output:</b><br>
      The program must display the text <code>MEDIA = </code> followed by the corresponding result with exactly 5 decimal places.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
5.0
7.1
```

### 📤 Exemplo de Saída / Example Output

```txt
MEDIA = 6.43182
```