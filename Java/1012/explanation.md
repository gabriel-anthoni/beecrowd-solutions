<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1012">
    <img src="https://skillicons.dev/icons?i=java" width="45" alt="Java Logo" />
  </a>

  <h3>beecrowd 1012 — Área</h3>

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
      A entrada contém três valores de ponto flutuante (<code>double</code>): <code>A</code>, <code>B</code> e <code>C</code>.<br><br>
      <b>🧠 Lógica:</b><br>
      • Ler os três valores de ponto flutuante <code>A</code>, <code>B</code> e <code>C</code>.<br>
      • Calcular as áreas geométricas conforme as fórmulas:<br>
      - <b>Triângulo Retângulo:</b> <code>(A * C) / 2.0</code><br>
      - <b>Círculo:</b> <code>3.14159 * C²</code><br>
      - <b>Trapézio:</b> <code>((A + B) * C) / 2.0</code><br>
      - <b>Quadrado:</b> <code>B²</code><br>
      - <b>Retângulo:</b> <code>A * B</code><br>
      • Exibir cada resultado utilizando <code>System.out.printf()</code> com <b>3 casas decimais</b> e quebra de linha <code>\n</code>.<br><br>
      <b>📤 Saída:</b><br>
      Imprima cinco linhas de saída, cada uma correspondente a uma das áreas calculadas, formatadas com 3 casas decimais.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input contains three floating-point values (<code>double</code>): <code>A</code>, <code>B</code>, and <code>C</code>.<br><br>
      <b>🧠 Logic:</b><br>
      • Read three floating-point values <code>A</code>, <code>B</code>, and <code>C</code>.<br>
      • Calculate the geometric areas using the respective formulas:<br>
      - <b>Right-angled Triangle:</b> <code>(A * C) / 2.0</code><br>
      - <b>Circle:</b> <code>3.14159 * C²</code><br>
      - <b>Trapezium:</b> <code>((A + B) * C) / 2.0</code><br>
      - <b>Square:</b> <code>B²</code><br>
      - <b>Rectangle:</b> <code>A * B</code><br>
      • Output each calculated area formatted to <b>3 decimal places</b> using <code>System.out.printf()</code> with a newline break <code>\n</code>.<br><br>
      <b>📤 Output:</b><br>
      Print five lines of output, each corresponding to one of the calculated areas, formatted with 3 decimal places.
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
RETANGULO: 15.000
```