<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1036">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1036 — Fórmula de Bhaskara</h3>

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
      A entrada contém três valores de ponto flutuante (A, B e C).<br><br>
      <b>🧠 Lógica:</b><br>
      • Leia os três valores na mesma linha utilizando <code>input().split()</code> e converta-os para <code>float</code>.<br>
      • Calcule o discriminante Delta: <code>Δ = B² - 4AC</code>.<br>
      • Valide as condições de impossibilidade: se <code>A == 0</code> (divisão por zero) ou <code>Δ < 0</code> (sem raízes reais).<br>
      • Se for impossível, imprima <code>Impossivel calcular</code>.<br>
      • Caso contrário, calcule as raízes R1 e R2 usando Bhaskara: <code>R1 = (-B + √Δ) / (2A)</code> e <code>R2 = (-B - √Δ) / (2A)</code>.<br>
      • Exiba os resultados formatados com 5 casas decimais.<br><br>
      <b>📤 Saída:</b><br>
      Se não for possível calcular, imprima <code>Impossivel calcular</code>. Caso contrário, imprima <code>R1 = X.XXXXX</code> e <code>R2 = X.XXXXX</code>.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input contains three floating-point values (A, B, and C).<br><br>
      <b>🧠 Logic:</b><br>
      • Read the three values on the same line using <code>input().split()</code> and convert them to <code>float</code>.<br>
      • Calculate the discriminant Delta: <code>Δ = B² - 4AC</code>.<br>
      • Validate impossibility conditions: if <code>A == 0</code> (division by zero) or <code>Δ < 0</code> (no real roots).<br>
      • If calculation is impossible, print <code>Impossivel calcular</code>.<br>
      • Otherwise, calculate roots R1 and R2 using Bhaskara: <code>R1 = (-B + √Δ) / (2A)</code> and <code>R2 = (-B - √Δ) / (2A)</code>.<br>
      • Display the results formatted with 5 decimal places.<br><br>
      <b>📤 Output:</b><br>
      If calculation is impossible, print <code>Impossivel calcular</code>. Otherwise, print <code>R1 = X.XXXXX</code> and <code>R2 = X.XXXXX</code>.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
10.0 20.1 5.1
```

### 📤 Exemplo de Saída / Example Output

```txt
R1 = -0.29610
R2 = -1.71390
```