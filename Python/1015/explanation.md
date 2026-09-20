<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1015">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1015 — Distância Entre Dois Pontos</h3>

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
      A entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 e y1, e a segunda linha contém dois valores de ponto flutuante: x2 e y2.<br><br>
      <b>🧠 Lógica:</b><br>
      • Leia os valores de x e y da primeira linha usando <code>input().split()</code> e converta-os para <code>float()</code>.<br>
      • Faça o mesmo para a segunda linha.<br>
      • Calcule a distância de acordo com a fórmula da distância euclidiana: <code>Distancia = √((x₂ - x₁)² + (y₂ - y₁)²)</code>.<br>
      • No código, a raiz quadrada é calculada elevando a soma dos quadrados a <code>0.5</code> usando a função <code>pow()</code>.<br>
      • Utilize f-string para formatar a saída com 4 casas decimais.<br><br>
      <b>📤 Saída:</b><br>
      Calcule e imprima o valor da distância com exatamente 4 casas decimais após o ponto decimal.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input file contains two lines of data. The first one contains two double values: x1 and y1, and the second one contains two double values: x2 and y2.<br><br>
      <b>🧠 Logic:</b><br>
      • Read the values of x and y from the first line using <code>input().split()</code> and convert them to <code>float()</code>.<br>
      • Do the same for the second line.<br>
      • Calculate the distance according to the Euclidean distance formula: <code>Distance = √((x₂ - x₁)² + (y₂ - y₁)²)</code>.<br>
      • In the code, the square root is computed by raising the sum of squares to <code>0.5</code> using the <code>pow()</code> function.<br>
      • Use f-string to format the output with 4 decimal places.<br><br>
      <b>📤 Output:</b><br>
      Calculate and print the distance value with exactly 4 decimal places after the decimal point.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
1.0 7.0
5.9 -4.0
```

### 📤 Exemplo de Saída / Example Output

```txt
11.7610
```