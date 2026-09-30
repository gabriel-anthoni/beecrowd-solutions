<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1015">
    <img src="https://skillicons.dev/icons?i=java" width="45" alt="Java Logo" />
  </a>

  <h3>beecrowd 1015 — Distância Entre Dois Pontos</h3>

  <p>
    <img src="https://img.shields.io/badge/Linguagem-Java_19-ED8B00?style=flat-square&logo=openjdk&logoColor=white" />
    <img src="https://img.shields.io/badge/N%C3%ADvel-1-orange?style=flat-square"/>
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
      A entrada contém duas linhas de dados; a primeira contém dois valores de ponto flutuante <code>x1</code> e <code>y1</code> e a segunda contém dois valores de ponto flutuante <code>x2</code> e <code>y2</code>.<br><br>
      <b>🧠 Lógica:</b><br>
      • Ler as coordenadas do primeiro ponto (<code>x1</code>, <code>y1</code>) e do segundo ponto (<code>x2</code>, <code>y2</code>).<br>
      • Aplicar a fórmula da distância euclidiana entre dois pontos:<br>
      <code>Distância = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2))</code><br>
      • Exibir o resultado formatado com <b>4 casas decimais</b> utilizando <code>System.out.printf()</code> e quebra de linha <code>\n</code>.<br><br>
      <b>📤 Saída:</b><br>
      Imprima o valor da distância com 4 casas após o ponto decimal e quebra de linha.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input contains two lines of data; the first one contains two floating-point values <code>x1</code> and <code>y1</code> and the second one contains two floating-point values <code>x2</code> and <code>y2</code>.<br><br>
      <b>🧠 Logic:</b><br>
      • Read the coordinates of the first point (<code>x1</code>, <code>y1</code>) and the second point (<code>x2</code>, <code>y2</code>).<br>
      • Apply the Euclidean distance formula between two points:<br>
      <code>Distance = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2))</code><br>
      • Output the distance value formatted to <b>4 decimal places</b> using <code>System.out.printf()</code> with a newline break <code>\n</code>.<br><br>
      <b>📤 Output:</b><br>
      Print the distance value with 4 digits after the decimal point and a newline.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
1.0 7.0
5.0 9.0
```

### 📤 Exemplo de Saída / Example Output

```txt
4.4721
```