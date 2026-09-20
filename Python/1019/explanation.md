<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1019">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1019 — Conversão de Tempo</h3>

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
      A entrada contém um valor inteiro correspondente ao tempo total em segundos.<br><br>
      <b>🧠 Lógica:</b><br>
      • Leia o valor inteiro de segundos usando <code>int(input())</code>.<br>
      • Calcule as horas dividindo o total de segundos por 3600 (divisão inteira <code>//</code>): <code>Horas = TotalSegundos // 3600</code>.<br>
      • Calcule os minutos: <code>Minutos = (TotalSegundos // 60) % 60</code>.<br>
      • Calcule os segundos restantes: <code>Segundos = TotalSegundos % 60</code>.<br>
      • Utilize f-string para formatar a saída no padrão <code>horas:minutos:segundos</code>.<br><br>
      <b>📤 Saída:</b><br>
      Imprima o tempo lido convertido para o formato <code>horas:minutos:segundos</code>.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input contains an integer value representing the total time in seconds.<br><br>
      <b>🧠 Logic:</b><br>
      • Read the total seconds as an integer using <code>int(input())</code>.<br>
      • Calculate the hours by dividing the total seconds by 3600 (integer division <code>//</code>): <code>Hours = TotalSeconds // 3600</code>.<br>
      • Calculate the minutes: <code>Minutes = (TotalSeconds // 60) % 60</code>.<br>
      • Calculate the remaining seconds: <code>Seconds = TotalSeconds % 60</code>.<br>
      • Use f-string to format the output in the standard <code>hours:minutes:seconds</code> format.<br><br>
      <b>📤 Output:</b><br>
      Print the read time converted to the format <code>hours:minutes:seconds</code>.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
140211
```

### 📤 Exemplo de Saída / Example Output

```txt
38:56:51
```