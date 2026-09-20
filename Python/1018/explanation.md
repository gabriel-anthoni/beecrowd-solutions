<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1018">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1018 — Cédulas</h3>

  <p>
    <img src="https://img.shields.io/badge/Linguagem-Python_3.11-3776AB?style=flat-square&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/N%C3%ADvel-4-green?style=flat-square" />
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
      A entrada contém um valor inteiro N (0 < N < 1000000).<br><br>
      <b>🧠 Lógica:</b><br>
      • Leia o valor inteiro usando <code>int(input())</code>.<br>
      • Defina uma lista com os valores das cédulas possíveis: <code>[100, 50, 20, 10, 5, 2, 1]</code>.<br>
      • Imprima o valor lido originalmente.<br>
      • Itere sobre a lista de cédulas. Para cada cédula:<br>
      &nbsp;&nbsp;- Calcule a quantidade de notas necessárias utilizando a divisão inteira <code>//</code>.<br>
      &nbsp;&nbsp;- Atualize o valor restante utilizando o operador de resto <code>%</code>.<br>
      • Utilize f-string para exibir a quantidade de cada nota no formato exigido.<br><br>
      <b>📤 Saída:</b><br>
      Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada valor necessárias.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input file contains an integer value N (0 < N < 1000000).<br><br>
      <b>🧠 Logic:</b><br>
      • Read the integer value using <code>int(input())</code>.<br>
      • Define a list containing the possible banknote values: <code>[100, 50, 20, 10, 5, 2, 1]</code>.<br>
      • Print the originally read value.<br>
      • Iterate through the list of banknotes. For each banknote:<br>
      &nbsp;&nbsp;- Calculate the quantity of notes needed using integer division <code>//</code>.<br>
      &nbsp;&nbsp;- Update the remaining amount using the modulo operator <code>%</code>.<br>
      • Use f-string to display the quantity of each banknote in the required format.<br><br>
      <b>📤 Output:</b><br>
      Print the read number and the minimum quantity of each necessary banknotes.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
576
```

### 📤 Exemplo de Saída / Example Output

```
576
5 nota(s) de R$ 100,00
1 nota(s) de R$ 50,00
1 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
1 nota(s) de R$ 5,00
0 nota(s) de R$ 2,00
1 nota(s) de R$ 1,00
```