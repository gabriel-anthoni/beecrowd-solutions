<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1045">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1045 — Tipos de Triângulos</h3>

  <p>
    <img src="https://img.shields.io/badge/Linguagem-Python_3.11-3776AB?style=flat-square&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/N%C3%ADvel-4-green?style=flat-square" />
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
      A entrada contém três valores de ponto flutuante A, B e C na mesma linha (A, B, C > 0).<br><br>
      <b>🧠 Lógica:</b><br>
      • Ordene os três valores em ordem decrescente, garantindo <code>A ≥ B ≥ C</code> utilizando <code>sorted(..., reverse=True)</code>.<br>
      • Verifique as condições em ordem:<br>
      &nbsp;&nbsp;1. Se <code>A ≥ B + C</code>: exiba <code>NAO FORMA TRIANGULO</code> e encerre a avaliação.<br>
      &nbsp;&nbsp;2. Classificação pelos ângulos:<br>
      &nbsp;&nbsp;&nbsp;&nbsp;- <code>A² == B² + C²</code>: <code>TRIANGULO RETANGULO</code><br>
      &nbsp;&nbsp;&nbsp;&nbsp;- <code>A² > B² + C²</code>: <code>TRIANGULO OBTUSANGULO</code><br>
      &nbsp;&nbsp;&nbsp;&nbsp;- <code>A² < B² + C²</code>: <code>TRIANGULO ACUTANGULO</code><br>
      &nbsp;&nbsp;3. Classificação pelos lados (adicionalmente):<br>
      &nbsp;&nbsp;&nbsp;&nbsp;- <code>A == B == C</code>: <code>TRIANGULO EQUILATERO</code><br>
      &nbsp;&nbsp;&nbsp;&nbsp;- Apenas dois lados iguais: <code>TRIANGULO ISOSCELES</code><br><br>
      <b>📤 Saída:</b><br>
      Imprima todas as mensagens de classificação aplicáveis ao triângulo fornecido na entrada.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input contains three floating-point values A, B, and C on a single line (A, B, C > 0).<br><br>
      <b>🧠 Logic:</b><br>
      • Sort the three values in descending order so that <code>A ≥ B ≥ C</code> using <code>sorted(..., reverse=True)</code>.<br>
      • Evaluate conditions in order:<br>
      &nbsp;&nbsp;1. If <code>A ≥ B + C</code>: print <code>NAO FORMA TRIANGULO</code> and stop further checks.<br>
      &nbsp;&nbsp;2. Classification by angles:<br>
      &nbsp;&nbsp;&nbsp;&nbsp;- <code>A² == B² + C²</code>: <code>TRIANGULO RETANGULO</code><br>
      &nbsp;&nbsp;&nbsp;&nbsp;- <code>A² > B² + C²</code>: <code>TRIANGULO OBTUSANGULO</code><br>
      &nbsp;&nbsp;&nbsp;&nbsp;- <code>A² < B² + C²</code>: <code>TRIANGULO ACUTANGULO</code><br>
      &nbsp;&nbsp;3. Classification by sides (additionally):<br>
      &nbsp;&nbsp;&nbsp;&nbsp;- <code>A == B == C</code>: <code>TRIANGULO EQUILATERO</code><br>
      &nbsp;&nbsp;&nbsp;&nbsp;- Exactly two sides equal: <code>TRIANGULO ISOSCELES</code><br><br>
      <b>📤 Output:</b><br>
      Print all classification messages that apply to the input triangle.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
7.0 5.0 2.0
```

### 📤 Exemplo de Saída / Example Output

```
NAO FORMA TRIANGULO
```