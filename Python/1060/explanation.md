<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1060">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1060 — Números Positivos</h3>

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
      A entrada é composta por seis valores, negativos e/ou positivos, do tipo ponto flutuante (<code>float</code>), um por linha.<br><br>
      <b>🧠 Lógica:</b><br>
      • Inicialize um contador <code>positivos = 0</code>.<br>
      • Utilize um laço <code>for _ in range(6)</code> para ler 6 valores de ponto flutuante com <code>float(input())</code>.<br>
      • Para cada valor, verifique se ele é estritamente maior que zero (<code>valor > 0</code>).<br>
      • Se for positivo, incremente o contador: <code>positivos += 1</code>.<br>
      • Exiba o resultado final formatado como <code>X valores positivos</code>.<br><br>
      <b>📤 Saída:</b><br>
      Imprima a quantidade total de valores positivos lidos no formato <code>X valores positivos</code>.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input consists of six floating-point values (<code>float</code>), positive and/or negative, one per line.<br><br>
      <b>🧠 Logic:</b><br>
      • Initialize a counter variable <code>positives = 0</code>.<br>
      • Use a <code>for _ in range(6)</code> loop to read 6 floating-point values using <code>float(input())</code>.<br>
      • For each value, check if it is strictly greater than zero (<code>value > 0</code>).<br>
      • If positive, increment the counter: <code>positives += 1</code>.<br>
      • Output the final count formatted as <code>X valores positivos</code>.<br><br>
      <b>📤 Output:</b><br>
      Print the total count of positive numbers read, formatted as <code>X valores positivos</code>.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
7
-5
6
-3.4
4.6
12
```

### 📤 Exemplo de Saída / Example Output

```
4 valores positivos
```