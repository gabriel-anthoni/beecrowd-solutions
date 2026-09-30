<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1019">
    <img src="https://skillicons.dev/icons?i=java" width="45" alt="Java Logo" />
  </a>

  <h3>beecrowd 1019 — Conversão de Tempo</h3>

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
      A entrada contém um valor inteiro representando o tempo total em segundos.<br><br>
      <b>🧠 Lógica:</b><br>
      • Ler o tempo total em segundos (<code>int</code>).<br>
      • Calcular as horas dividindo por 3600:<br>
      <code>Horas = Total / 3600</code><br>
      • Calcular os minutos dividindo o restante por 60:<br>
      <code>Minutos = (Total / 60) % 60</code><br>
      • Calcular os segundos restantes:<br>
      <code>Segundos = Total % 60</code><br>
      • Exibir o resultado formatado no padrão <code>horas:minutos:segundos</code> com quebra de linha <code>\n</code>.<br><br>
      <b>📤 Saída:</b><br>
      Imprima o tempo lido convertido para o formato <code>horas:minutos:segundos</code>.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input contains an integer value representing the total time in seconds.<br><br>
      <b>🧠 Logic:</b><br>
      • Read the total seconds (<code>int</code>).<br>
      • Calculate hours by dividing by 3600:<br>
      <code>Hours = Total / 3600</code><br>
      • Calculate minutes from the remaining duration:<br>
      <code>Minutes = (Total / 60) % 60</code><br>
      • Calculate remaining seconds:<br>
      <code>Seconds = Total % 60</code><br>
      • Output the result formatted as <code>hours:minutes:seconds</code> with a newline break <code>\n</code>.<br><br>
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