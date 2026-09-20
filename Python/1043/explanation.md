<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1043">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1043 — Triângulo</h3>

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
      A entrada contém três valores de ponto flutuante A, B e C na mesma linha.<br><br>
      <b>🧠 Lógica:</b><br>
      • Leia os valores de A, B e C utilizando <code>map(float, input().split())</code>.<br>
      • Verifique a condição de existência de um triângulo pela <b>desigualdade triangular</b>:<br>
      &nbsp;&nbsp;<code>(A + B > C) and (A + C > B) and (B + C > A)</code><br>
      • Se for verdadeiro, calcule o perímetro: <code>Perímetro = A + B + C</code> e exiba no formato <code>Perimetro = X.X</code>.<br>
      • Se for falso, calcule a área de um trapézio de bases A e B e altura C: <code>Área = ((A + B) · C) / 2</code> e exiba no formato <code>Area = X.X</code>.<br>
      • Formate o resultado com exatamente 1 casa decimal.<br><br>
      <b>📤 Saída:</b><br>
      Imprima a mensagem <code>Perimetro = ...</code> se formar um triângulo, ou <code>Area = ...</code> caso contrário, com 1 casa decimal.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input contains three floating-point values A, B, and C on a single line.<br><br>
      <b>🧠 Logic:</b><br>
      • Read the A, B, and C values using <code>map(float, input().split())</code>.<br>
      • Check the triangle existence condition using the <b>triangle inequality theorem</b>:<br>
      &nbsp;&nbsp;<code>(A + B > C) and (A + C > B) and (B + C > A)</code><br>
      • If true, calculate the perimeter: <code>Perimeter = A + B + C</code> and print as <code>Perimetro = X.X</code>.<br>
      • If false, calculate the area of a trapezium with bases A and B and height C: <code>Area = ((A + B) · C) / 2</code> and print as <code>Area = X.X</code>.<br>
      • Format the result to exactly 1 decimal place.<br><br>
      <b>📤 Output:</b><br>
      Print <code>Perimetro = ...</code> if a triangle is formed, or <code>Area = ...</code> otherwise, formatted with 1 decimal place.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
6.0 4.0 2.0
```

### 📤 Exemplo de Saída / Example Output

```txt
Area = 10.0
```