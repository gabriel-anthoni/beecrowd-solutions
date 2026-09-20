<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1041">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1041 — Coordenadas de um Ponto</h3>

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
      A entrada contém dois valores de ponto flutuante na mesma linha representando as coordenadas x e y de um ponto no plano cartesiano.<br><br>
      <b>🧠 Lógica:</b><br>
      • Leia os valores de x e y utilizando <code>map(float, input().split())</code>.<br>
      • Avalie a posição do ponto usando estruturas condicionais (<code>if/elif/else</code>):<br>
      &nbsp;&nbsp;- <code>x == 0</code> e <code>y == 0</code>: <code>Origem</code><br>
      &nbsp;&nbsp;- <code>x == 0</code> e <code>y ≠ 0</code>: <code>Eixo Y</code><br>
      &nbsp;&nbsp;- <code>y == 0</code> e <code>x ≠ 0</code>: <code>Eixo X</code><br>
      &nbsp;&nbsp;- <code>x > 0</code> e <code>y > 0</code>: <code>Q1</code><br>
      &nbsp;&nbsp;- <code>x < 0</code> e <code>y > 0</code>: <code>Q2</code><br>
      &nbsp;&nbsp;- <code>x < 0</code> e <code>y < 0</code>: <code>Q3</code><br>
      &nbsp;&nbsp;- <code>x > 0</code> e <code>y < 0</code>: <code>Q4</code><br><br>
      <b>📤 Saída:</b><br>
      Imprima o nome do quadrante (<code>Q1</code>, <code>Q2</code>, <code>Q3</code>, <code>Q4</code>), <code>Origem</code>, ou o eixo correspondente (<code>Eixo X</code>, <code>Eixo Y</code>).
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input contains two floating-point values on a single line representing the x and y coordinates of a point in a 2D Cartesian plane.<br><br>
      <b>🧠 Logic:</b><br>
      • Read the x and y values using <code>map(float, input().split())</code>.<br>
      • Evaluate the position of the point using conditional statements (<code>if/elif/else</code>):<br>
      &nbsp;&nbsp;- <code>x == 0</code> and <code>y == 0</code>: <code>Origem</code><br>
      &nbsp;&nbsp;- <code>x == 0</code> and <code>y ≠ 0</code>: <code>Eixo Y</code><br>
      &nbsp;&nbsp;- <code>y == 0</code> and <code>x ≠ 0</code>: <code>Eixo X</code><br>
      &nbsp;&nbsp;- <code>x > 0</code> and <code>y > 0</code>: <code>Q1</code><br>
      &nbsp;&nbsp;- <code>x < 0</code> and <code>y > 0</code>: <code>Q2</code><br>
      &nbsp;&nbsp;- <code>x < 0</code> and <code>y < 0</code>: <code>Q3</code><br>
      &nbsp;&nbsp;- <code>x > 0</code> and <code>y < 0</code>: <code>Q4</code><br><br>
      <b>📤 Output:</b><br>
      Print the matching quadrant label (<code>Q1</code>, <code>Q2</code>, <code>Q3</code>, <code>Q4</code>), <code>Origem</code>, or the corresponding axis (<code>Eixo X</code>, <code>Eixo Y</code>).
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
4.5 -2.2
```

### 📤 Exemplo de Saída / Example Output

```txt
Q4
```