<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1017">
    <img src="https://skillicons.dev/icons?i=java" width="45" alt="Java Logo" />
  </a>

  <h3>beecrowd 1017 — Gasto de Combustível</h3>

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
      A entrada contém dois valores inteiros: o tempo gasto na viagem (em horas) e a velocidade média durante a mesma (em km/h).<br><br>
      <b>🧠 Lógica:</b><br>
      • Ler o tempo de viagem (<code>int</code>) e a velocidade média (<code>int</code>).<br>
      • Calcular a distância total percorrida:<br>
      <code>Distância = Tempo * Velocidade Média</code><br>
      • Sabendo que o carro faz 12 km/l, calcular a quantidade de combustível gasta:<br>
      <code>Litros = Distância / 12.0</code><br>
      • Exibir o resultado formatado com <b>3 casas decimais</b> utilizando <code>System.out.printf()</code> e quebra de linha <code>\n</code>.<br><br>
      <b>📤 Saída:</b><br>
      Imprima a quantidade de litros de combustível gasta com 3 casas após o ponto decimal e quebra de linha.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input file contains two integer values: the spent time in the trip (in hours) and the average speed during the trip (in km/h).<br><br>
      <b>🧠 Logic:</b><br>
      • Read the travel time (<code>int</code>) and average speed (<code>int</code>).<br>
      • Calculate the total distance traveled:<br>
      <code>Distance = Time * Average Speed</code><br>
      • Given that the car does 12 km/l, calculate the spent fuel in liters:<br>
      <code>Liters = Distance / 12.0</code><br>
      • Output the fuel spent formatted to <b>3 decimal places</b> using <code>System.out.printf()</code> with a newline break <code>\n</code>.<br><br>
      <b>📤 Output:</b><br>
      Print the amount of fuel spent in liters with 3 digits after the decimal point and a newline.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
10
85
```

### 📤 Exemplo de Saída / Example Output

```txt
70.833
```