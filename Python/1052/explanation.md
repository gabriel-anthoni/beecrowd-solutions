<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1052">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1052 — Mês</h3>

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
      A entrada contém um único valor inteiro entre 1 e 12.<br><br>
      <b>🧠 Lógica:</b><br>
      • Leia o número inteiro representando o mês usando <code>int(input())</code>.<br>
      • Defina uma lista contendo os meses do ano em inglês: <code>meses = ["January", "February", ...]</code>.<br>
      • Acesse o mês correspondente usando o índice ajustado <code>meses[mes - 1]</code> (devido à indexação base zero do Python).<br>
      • Exiba o nome do mês com a primeira letra maiúscula.<br><br>
      <b>📤 Saída:</b><br>
      Imprima o nome do mês correspondente em inglês com a primeira letra maiúscula.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input contains a single integer value between 1 and 12.<br><br>
      <b>🧠 Logic:</b><br>
      • Read the integer number representing the month using <code>int(input())</code>.<br>
      • Define a list containing the months of the year in English: <code>months = ["January", "February", ...]</code>.<br>
      • Retrieve the corresponding month name using 0-based index adjustment <code>months[month - 1]</code>.<br>
      • Output the capitalized month name.<br><br>
      <b>📤 Output:</b><br>
      Print the name of the month corresponding to the input number, in English, with the first letter capitalized.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
4
```

### 📤 Exemplo de Saída / Example Output

```
April
```