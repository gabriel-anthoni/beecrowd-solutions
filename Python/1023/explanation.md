<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1023">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1023 — Estiagem</h3>

  <p>
    <img src="https://img.shields.io/badge/Linguagem-Python_3.11-3776AB?style=flat-square&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/N%C3%ADvel-10-green?style=flat-square" />
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
      A entrada contém vários casos de teste. A primeira linha de cada caso indica a quantidade N de imóveis (1 ≤ N ≤ 100000). As N linhas seguintes contêm o número de moradores e o consumo em m³. A entrada termina quando N = 0.<br><br>
      <b>🧠 Lógica:</b><br>
      • Utilize <code>sys.stdin.readline</code> para leitura rápida devido ao alto volume de dados.<br>
      • Repita a leitura em um laço até que <code>N = 0</code>.<br>
      • Para cada imóvel, acumule o total de pessoas e o consumo total.<br>
      • Calcule o consumo médio truncado por pessoa usando divisão inteira: <code>ConsumoMédio = Consumo // Moradores</code>.<br>
      • Agrupe a quantidade total de moradores por faixa de consumo médio utilizando um dicionário.<br>
      • Ordene as faixas de consumo de forma crescente para exibição no formato <code>moradores-consumo</code>.<br>
      • Calcule a média geral da cidade truncando estritamente em 2 casas decimais: <code>MédiaGeral = ⌊(TotalConsumo · 100) / TotalPessoas⌋ / 100</code>.<br><br>
      <b>📤 Saída:</b><br>
      Imprima o cabeçalho <code>Cidade# X:</code>, a lista de moradores por consumo e a média truncada em 2 casas decimais seguida por <code>m3.</code>. Insira uma linha em branco estritamente entre casos de teste consecutivos.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input contains several test cases. The first line indicates the number N of properties (1 ≤ N ≤ 100000). The following N lines contain the number of residents and the consumption in m³. Input ends when N = 0.<br><br>
      <b>🧠 Logic:</b><br>
      • Use <code>sys.stdin.readline</code> for fast input reading due to large dataset size.<br>
      • Loop until <code>N = 0</code>.<br>
      • For each property, accumulate the total number of people and total consumption.<br>
      • Calculate the truncated average consumption per person using integer division: <code>AvgConsumption = Consumption // Residents</code>.<br>
      • Group the total number of residents by consumption bracket using a dictionary.<br>
      • Sort the consumption brackets in ascending order to print pairs in the format <code>residents-consumption</code>.<br>
      • Calculate the overall average consumption truncated strictly to 2 decimal places: <code>OverallAverage = ⌊(TotalConsumption · 100) / TotalPeople⌋ / 100</code>.<br><br>
      <b>📤 Output:</b><br>
      Print the header <code>Cidade# X:</code>, the list of residents by consumption, and the truncated average with 2 decimal places followed by <code>m3.</code>. Insert a blank line strictly between consecutive test cases.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
3
3 22
1 11
2 39
0
```

### 📤 Exemplo de Saída / Example Output

```txt
Cidade# 1:
1-11 2-11 3-7
Consumo medio: 12.00 m3.
```