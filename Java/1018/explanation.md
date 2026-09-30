<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1018">
    <img src="https://skillicons.dev/icons?i=java" width="45" alt="Java Logo" />
  </a>

  <h3>beecrowd 1018 — Cédulas</h3>

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
      A entrada contém um valor inteiro <code>N</code> (<code>0 &lt; N &lt; 1000000</code>).<br><br>
      <b>🧠 Lógica:</b><br>
      • Ler o valor inteiro <code>N</code>.<br>
      • Imprimir o valor lido originalmente.<br>
      • Definir o vetor de cédulas: <code>[100, 50, 20, 10, 5, 2, 1]</code>.<br>
      • Para cada cédula, calcular a quantidade de notas necessárias usando a divisão inteira (<code>/</code>) e atualizar o valor restante com o operador de resto (<code>%</code>).<br>
      • Exibir o resultado formatado no padrão <code>X nota(s) de R$ Y,00</code> com quebra de linha <code>\n</code>.<br><br>
      <b>📤 Saída:</b><br>
      Imprima o valor lido e a quantidade mínima de notas de cada tipo necessárias.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input file contains an integer value <code>N</code> (<code>0 &lt; N &lt; 1000000</code>).<br><br>
      <b>🧠 Logic:</b><br>
      • Read the integer value <code>N</code>.<br>
      • Print the original read value.<br>
      • Define the array of available banknotes: <code>[100, 50, 20, 10, 5, 2, 1]</code>.<br>
      • For each banknote, calculate the required quantity using integer division (<code>/</code>) and update the remaining balance using modulo (<code>%</code>).<br>
      • Output each line formatted as <code>X nota(s) de R$ Y,00</code> with an end-of-line break <code>\n</code>.<br><br>
      <b>📤 Output:</b><br>
      Print the read number and the minimum number of each necessary banknote.
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