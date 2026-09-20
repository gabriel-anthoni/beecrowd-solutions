<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1012">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1012 — Área</h3>

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
      A entrada contém três valores de ponto flutuante com dupla precisão: A, B e C.<br><br>
      <b>🧠 Lógica:</b><br>
      • Leia os três valores da linha de entrada usando <code>input().split()</code> e converta-os para <code>float()</code>.<br>
      • Calcule a área de cada figura geométrica conforme as fórmulas:<br>
      &nbsp;&nbsp;- Triângulo: <code>(A · C) / 2</code><br>
      &nbsp;&nbsp;- Círculo: <code>π · C²</code> (utilizando <code>π = 3.14159</code>)<br>
      &nbsp;&nbsp;- Trapézio: <code>((A + B) · C) / 2</code><br>
      &nbsp;&nbsp;- Quadrado: <code>B²</code><br>
      &nbsp;&nbsp;- Retângulo: <code>A · B</code><br>
      • Utilize f-string para formatar a saída com 3 casas decimais para cada cálculo.<br><br>
      <b>📤 Saída:</b><br>
      O arquivo de saída deve conter 5 linhas de dados com as mensagens correspondentes seguidas pelos valores das áreas formatados com 3 casas decimais.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input file contains three double precision values: A, B and C.<br><br>
      <b>🧠 Logic:</b><br>
      • Read the three values from the input line using <code>input().split()</code> and convert them to <code>float()</code>.<br>
      • Calculate the area of each geometric shape using the formulas:<br>
      &nbsp;&nbsp;- Triangle: <code>(A · C) / 2</code><br>
      &nbsp;&nbsp;- Circle: <code>π · C²</code> (using <code>π = 3.14159</code>)<br>
      &nbsp;&nbsp;- Trapezium: <code>((A + B) · C) / 2</code><br>
      &nbsp;&nbsp;- Square: <code>B²</code><br>
      &nbsp;&nbsp;- Rectangle: <code>A · B</code><br>
      • Use f-string to format the output with 3 decimal places for each calculation.<br><br>
      <b>📤 Output:</b><br>
      The output file must contain 5 lines of data with the corresponding labels followed by the calculated area values formatted with 3 decimal places.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
3.0 4.0 5.2
```

### 📤 Exemplo de Saída / Example Output

```txt
TRIANGULO: 7.800
CIRCULO: 84.949
TRAPEZIO: 18.200
QUADRADO: 16.000
RETANGULO: 12.000
```