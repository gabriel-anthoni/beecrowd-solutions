<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1021">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1021 — Notas e Moedas</h3>

  <p>
    <img src="https://img.shields.io/badge/Linguagem-Python_3.11-3776AB?style=flat-square&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/N%C3%ADvel-6-green?style=flat-square" />
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
      A entrada contém um valor de ponto flutuante com duas casas decimais, representando o valor monetário.<br><br>
      <b>🧠 Lógica:</b><br>
      • Leia o valor de ponto flutuante e multiplique-o por 100, arredondando para inteiro: <code>int(round(float(input()) * 100))</code> para evitar erros de precisão.<br>
      • Crie listas para os valores das notas e moedas em centavos:<br>
      &nbsp;&nbsp;- Notas: <code>[10000, 5000, 2000, 1000, 500, 200]</code><br>
      &nbsp;&nbsp;- Moedas: <code>[100, 50, 25, 10, 5, 1]</code><br>
      • Itere sobre as listas utilizando divisão inteira (<code>//</code>) para obter a quantidade e o operador de resto (<code>%</code>) para atualizar o valor restante.<br>
      • Utilize f-string dividindo a nota/moeda por 100 para voltar ao formato decimal com duas casas.<br><br>
      <b>📤 Saída:</b><br>
      Imprima a quantidade mínima de notas e moedas necessárias no formato solicitado, indicando "NOTAS:" e "MOEDAS:" como cabeçalhos.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input file contains a floating-point value with two decimal places, representing the monetary value.<br><br>
      <b>🧠 Logic:</b><br>
      • Read the floating-point value and multiply it by 100, rounding to integer: <code>int(round(float(input()) * 100))</code> to avoid floating-point precision issues.<br>
      • Create lists representing banknotes and coins in cents:<br>
      &nbsp;&nbsp;- Banknotes: <code>[10000, 5000, 2000, 1000, 500, 200]</code><br>
      &nbsp;&nbsp;- Coins: <code>[100, 50, 25, 10, 5, 1]</code><br>
      • Iterate through the lists using integer division (<code>//</code>) for quantity and the modulo operator (<code>%</code>) to update the remaining value.<br>
      • Use f-string dividing banknote/coin by 100 to convert back to decimal format with two decimal places.<br><br>
      <b>📤 Output:</b><br>
      Print the minimum quantity of banknotes and coins necessary in the requested format, showing "NOTAS:" and "MOEDAS:" as headers.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
576.73
```

### 📤 Exemplo de Saída / Example Output

```
NOTAS:
5 nota(s) de R$ 100.00
1 nota(s) de R$ 50.00
1 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
1 nota(s) de R$ 5.00
0 nota(s) de R$ 2.00
MOEDAS:
1 moeda(s) de R$ 1.00
1 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
2 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
3 moeda(s) de R$ 0.01
```