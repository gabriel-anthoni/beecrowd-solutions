<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1022">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1022 — TDA Racional</h3>

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
      A entrada contém um valor inteiro N correspondente ao número de casos de teste. Cada caso de teste contém uma linha representando uma operação entre duas frações.<br><br>
      <b>🧠 Lógica:</b><br>
      • Importe o módulo <code>math</code> para utilizar a função <code>math.gcd</code> (Máximo Divisor Comum).<br>
      • Leia a quantidade de casos de teste com <code>int(input())</code>.<br>
      • Para cada operação, divida a entrada com <code>.split()</code> e mapeie N1, D1, o operador e N2, D2.<br>
      • Realize o cálculo da fração de acordo com o operador:<br>
      &nbsp;&nbsp;- Soma (+): <code>(N1 · D2 + N2 · D1) / (D1 · D2)</code><br>
      &nbsp;&nbsp;- Subtração (-): <code>(N1 · D2 - N2 · D1) / (D1 · D2)</code><br>
      &nbsp;&nbsp;- Multiplicação (*): <code>(N1 · N2) / (D1 · D2)</code><br>
      &nbsp;&nbsp;- Divisão (/): <code>(N1 · D2) / (N2 · D1)</code><br>
      • Calcule o MDC entre o numerador e o denominador com <code>math.gcd(num, den)</code>.<br>
      • Divida ambos pelo MDC utilizando divisão inteira <code>//</code> para obter a fração simplificada.<br><br>
      <b>📤 Saída:</b><br>
      Para cada caso de teste, exiba a fração resultante sem simplificação, seguida pelo sinal de igualdade e a fração totalmente simplificada.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input contains an integer value N corresponding to the number of test cases. Each subsequent test case contains a line representing an operation between two fractions.<br><br>
      <b>🧠 Logic:</b><br>
      • Import the <code>math</code> module to use <code>math.gcd</code> (Greatest Common Divisor).<br>
      • Read the number of test cases using <code>int(input())</code>.<br>
      • For each operation, split the line using <code>.split()</code> and map N1, D1, the operator, and N2, D2.<br>
      • Calculate the fraction according to the operator:<br>
      &nbsp;&nbsp;- Addition (+): <code>(N1 · D2 + N2 · D1) / (D1 · D2)</code><br>
      &nbsp;&nbsp;- Subtraction (-): <code>(N1 · D2 - N2 · D1) / (D1 · D2)</code><br>
      &nbsp;&nbsp;- Multiplication (*): <code>(N1 · N2) / (D1 · D2)</code><br>
      &nbsp;&nbsp;- Division (/): <code>(N1 · D2) / (N2 · D1)</code><br>
      • Compute the GCD using <code>math.gcd(num, den)</code>.<br>
      • Divide both numerator and denominator by the GCD using integer division <code>//</code> to find the simplified fraction.<br><br>
      <b>📤 Output:</b><br>
      For each test case, print the resulting fraction without simplification, followed by an equal sign and the fully simplified fraction.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```
4
1 / 2 + 3 / 4
1 / 2 - 3 / 4
2 / 3 * 6 / 6
1 / 2 / 3 / 4
```

### 📤 Exemplo de Saída / Example Output

```
10/8 = 5/4
-2/8 = -1/4
12/18 = 2/3
4/6 = 2/3
```