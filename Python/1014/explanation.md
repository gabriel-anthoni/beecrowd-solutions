<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1014">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1014 — Consumo</h3>

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
      A entrada contém dois valores: um valor inteiro X representando a distância total percorrida (em Km), e um valor real Y representando o total de combustível gasto, com um dígito após o ponto decimal.<br><br>
      <b>🧠 Lógica:</b><br>
      • Leia o valor inteiro de distância usando <code>int(input())</code>.<br>
      • Leia o valor de ponto flutuante do combustível gasto usando <code>float(input())</code>.<br>
      • Divida a distância total pelo combustível consumido para obter o consumo médio: <code>Consumo = X / Y</code>.<br>
      • Utilize f-string para formatar a saída com 3 casas decimais seguida de " km/l".<br><br>
      <b>📤 Saída:</b><br>
      Apresente o valor que representa o consumo médio do automóvel com 3 casas após a vírgula, seguido da mensagem " km/l".
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input file contains two values: one integer value X representing the total distance (in Km) and the second one is a floating point number Y representing the spent fuel total, with a digit after the decimal point.<br><br>
      <b>🧠 Logic:</b><br>
      • Read the total distance as an integer using <code>int(input())</code>.<br>
      • Read the spent fuel total as a float using <code>float(input())</code>.<br>
      • Divide the total distance by the spent fuel to calculate the average consumption: <code>Consumption = X / Y</code>.<br>
      • Use f-string to format the output to 3 decimal places followed by " km/l".<br><br>
      <b>📤 Output:</b><br>
      Present the value that represents the average consumption of the car with 3 decimal places, followed by the message " km/l".
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