<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1020">
    <img src="https://skillicons.dev/icons?i=java" width="45" alt="Java Logo" />
  </a>

  <h3>beecrowd 1020 — Idade em Dias</h3>

  <p>
    <img src="https://img.shields.io/badge/Linguagem-Java_19-ED8B00?style=flat-square&logo=openjdk&logoColor=white" />
    <img src="https://img.shields.io/badge/N%C3%ADvel-4-orange?style=flat-square"/>
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
      • Ler o total de dias (<code>int</code>).<br>
      • Calcular a quantidade de anos dividindo por 365:<br>
      <code>Anos = Total / 365</code><br>
      • Calcular a quantidade de meses obtendo o resto da divisão por 365 e dividindo por 30:<br>
      <code>Meses = (Total % 365) / 30</code><br>
      • Calcular a quantidade de dias restantes:<br>
      <code>Dias = (Total % 365) % 30</code><br>
      • Exibir a quantidade de anos, meses e dias em linhas separadas no formato especificado, garantindo a quebra de linha <code>\n</code> ao final.<br><br>
      <b>📤 Saída:</b><br>
      Imprima a saída conforme o modelo especificado com a quantidade de anos, meses e dias.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input contains an integer value representing a person's age in days.<br><br>
      <b>🧠 Logic:</b><br>
      • Read the total age in days (<code>int</code>).<br>
      • Calculate years by dividing by 365:<br>
      <code>Years = Total / 365</code><br>
      • Calculate months from the remainder divided by 30:<br>
      <code>Months = (Total % 365) / 30</code><br>
      • Calculate remaining days:<br>
      <code>Days = (Total % 365) % 30</code><br>
      • Output the total years, months, and days on separate lines following the specified format, ending with a newline break <code>\n</code>.<br><br>
      <b>📤 Output:</b><br>
      Print the output according to the specified pattern with the total years, months, and days.
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