<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1006">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1006 — Média 2</h3>

  <p>
    <img src="https://img.shields.io/badge/Linguagem-Python_3.11-3776AB?style=flat-square&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/N%C3%ADvel-1-green?style=flat-square" />
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
      A entrada contém três valores de ponto flutuante com uma casa decimal.<br><br>
      <b>🧠 Lógica:</b><br>
      • Leia os três valores decimais através da função <code>input()</code> convertida para <code>float()</code>.<br>
      • Multiplique cada valor pelo seu respectivo peso (2 para a primeira nota, 3 para a segunda e 5 para a terceira) e divida a soma por 10: <code>MEDIA = ((A · 2) + (B · 3) + (C · 5)) / 10</code>.<br>
      • Utilize f-string para formatar a saída com 1 casa decimal.<br><br>
      <b>📤 Saída:</b><br>
      O programa deve exibir o texto <code>MEDIA = </code> seguido pelo resultado correspondente com exatamente uma casa decimal.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input contains three floating-point values with one digit after the decimal point.<br><br>
      <b>🧠 Logic:</b><br>
      • Read the three decimal values using the <code>input()</code> function converted to <code>float()</code>.<br>
      • Multiply each value by its respective weight (2 for the first grade, 3 for the second, and 5 for the third) and divide their sum by 10: <code>MEDIA = ((A · 2) + (B · 3) + (C · 5)) / 10</code>.<br>
      • Use f-string to format the output to 1 decimal place.<br><br>
      <b>📤 Output:</b><br>
      The program must display the text <code>MEDIA = </code> followed by the corresponding result with exactly 1 decimal place.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
5.0
6.0
7.0
```

### 📤 Exemplo de Saída / Example Output

```txt
MEDIA = 6.3
```