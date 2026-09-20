<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1017">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1017 — Gasto de Combustível</h3>

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
      A entrada contém dois valores inteiros: o tempo gasto na viagem (em horas) e a velocidade média durante a mesma (em km/h).<br><br>
      <b>🧠 Lógica:</b><br>
      • Leia o tempo de viagem (em horas) e a velocidade média (em km/h) usando <code>int(input())</code>.<br>
      • Calcule a distância total percorrida multiplicando o tempo pela velocidade média: <code>Distancia = Tempo · Velocidade</code>.<br>
      • Calcule a quantidade de combustível consumida dividindo a distância total pelo consumo médio do automóvel (12 km/L): <code>Litros = Distancia / 12</code>.<br>
      • Utilize f-string para formatar a saída com 3 casas decimais.<br><br>
      <b>📤 Saída:</b><br>
      Imprima a quantidade de litros necessária para realizar a viagem, com três dígitos após o ponto decimal.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input file contains two integers: the spent time in the trip (in hours) and the average speed during the trip (in km/h).<br><br>
      <b>🧠 Logic:</b><br>
      • Read the spent time (in hours) and average speed (in km/h) using <code>int(input())</code>.<br>
      • Calculate the total distance traveled by multiplying the spent time by the average speed: <code>Distance = Time · Speed</code>.<br>
      • Calculate the spent fuel by dividing the total distance by the average car consumption (12 km/L): <code>Liters = Distance / 12</code>.<br>
      • Use f-string to format the output to 3 decimal places.<br><br>
      <b>📤 Output:</b><br>
      Print how many liters of fuel would be needed to do this trip, with three digits after the decimal point.
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