<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1020">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1020 — Idade em Dias</h3>

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
      A entrada contém um valor inteiro correspondente à idade de uma pessoa em dias.<br><br>
      <b>🧠 Lógica:</b><br>
      • Leia o valor inteiro de dias usando <code>int(input())</code>.<br>
      • Obtenha a quantidade de anos dividindo de forma inteira por 365: <code>Anos = TotalDias // 365</code>.<br>
      • Obtenha a quantidade de meses dividindo o resto da divisão dos anos por 30: <code>Meses = (TotalDias % 365) // 30</code>.<br>
      • Obtenha a quantidade de dias restantes aplicando o resto da divisão por 30 no saldo restante: <code>Dias = (TotalDias % 365) % 30</code>.<br>
      • Utilize f-string para formatar a saída com quebras de linha para cada unidade temporal.<br><br>
      <b>📤 Saída:</b><br>
      Imprima a saída formatada contendo a quantidade de anos, meses e dias, conforme o exemplo fornecido.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input file contains one integer value.<br><br>
      <b>🧠 Logic:</b><br>
      • Read the total days as an integer using <code>int(input())</code>.<br>
      • Obtain the number of years by dividing the total days by 365 (integer division <code>//</code>): <code>Years = TotalDays // 365</code>.<br>
      • Obtain the number of months by taking the remainder of days after subtracting years, and dividing it by 30: <code>Months = (TotalDays % 365) // 30</code>.<br>
      • Obtain the remaining days by applying the modulo operator <code>%</code> by 30 on the remaining days: <code>Days = (TotalDays % 365) % 30</code>.<br>
      • Use f-string to format the output with line breaks for each time unit.<br><br>
      <b>📤 Output:</b><br>
      Print the output formatted with the number of years, months, and days, as shown in the example.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
400
```

### 📤 Exemplo de Saída / Example Output

```txt
1 ano(s)
1 mes(es)
5 dia(s)
```