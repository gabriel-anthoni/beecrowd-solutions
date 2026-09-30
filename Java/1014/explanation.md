<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1014">
    <img src="https://skillicons.dev/icons?i=java" width="45" alt="Java Logo" />
  </a>

  <h3>beecrowd 1014 — Consumo</h3>

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
      A entrada contém dois valores: um valor inteiro <code>X</code> representando a distância total percorrida (em km) e um valor real <code>Y</code> representando o total de combustível gasto (em litros).<br><br>
      <b>🧠 Lógica:</b><br>
      • Ler a distância total percorrida <code>X</code> (<code>int</code>) e o combustível gasto <code>Y</code> (<code>double</code>).<br>
      • Calcular o consumo médio dividindo a distância pelo combustível:<br>
      <code>Consumo Médio = X / Y</code><br>
      • Em Java, ao dividir um <code>int</code> por um <code>double</code>, o resultado é promovido para <code>double</code>.<br>
      • Formatar a saída com <b>3 casas decimais</b> seguida da mensagem <code> km/l</code> e quebra de linha <code>\n</code>.<br><br>
      <b>📤 Saída:</b><br>
      Imprima o valor que representa o consumo médio do automóvel com 3 casas após o ponto decimal, seguido da mensagem <code>km/l</code> e quebra de linha.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input contains two values: an integer value <code>X</code> representing the total distance traveled (in km) and a floating-point value <code>Y</code> representing the spent fuel (in liters).<br><br>
      <b>🧠 Logic:</b><br>
      • Read the total distance <code>X</code> (<code>int</code>) and fuel consumed <code>Y</code> (<code>double</code>).<br>
      • Calculate the average consumption by dividing distance by fuel:<br>
      <code>Average Consumption = X / Y</code><br>
      • In Java, dividing an <code>int</code> by a <code>double</code> automatically evaluates to a <code>double</code>.<br>
      • Format the output with <b>3 decimal places</b> followed by <code> km/l</code> and an end-of-line break <code>\n</code>.<br><br>
      <b>📤 Output:</b><br>
      Print the average fuel consumption with 3 digits after the decimal point, followed by <code>km/l</code> and a newline.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
500
35.0
```

### 📤 Exemplo de Saída / Example Output

```txt
14.286 km/l
```