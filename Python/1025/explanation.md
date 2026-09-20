<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1025">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1025 — Onde estão os Mármores?</h3>

  <p>
    <img src="https://img.shields.io/badge/Linguagem-Python_3.11-3776AB?style=flat-square&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/N%C3%ADvel-8-green?style=flat-square" />
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
      A entrada contém vários casos de teste. Cada caso começa com N (número de mármores) e Q (número de consultas). Seguem N linhas com os valores dos mármores e Q linhas com as consultas. A entrada termina quando N = 0 e Q = 0.<br><br>
      <b>🧠 Lógica:</b><br>
      • Leia N e Q. Para cada caso de teste, armazene os N números em uma lista.<br>
      • Ordene a lista em ordem crescente, pois a Busca Binária exige um conjunto de dados ordenado.<br>
      • Para cada consulta, busque a primeira ocorrência do elemento utilizando <code>bisect.bisect_left</code> (ideal para tratar elementos duplicados).<br>
      • Verifique se o índice retornado está dentro dos limites e se o valor no índice é igual ao valor procurado:<br>
      &nbsp;&nbsp;- Se coincidir, exiba a posição somando 1 (indexação iniciando em 1).<br>
      &nbsp;&nbsp;- Caso contrário, informe que o elemento não foi encontrado.<br><br>
      <b>📤 Saída:</b><br>
      Para cada caso de teste, imprima o cabeçalho <code>CASE# X:</code>. Para cada consulta, imprima se o número foi encontrado e sua posição (1-based), ou se não foi encontrado.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input contains several test cases. Each case starts with N (number of marbles) and Q (number of queries). Followed by N lines with marble values and Q lines with query values. The input ends when N = 0 and Q = 0.<br><br>
      <b>🧠 Logic:</b><br>
      • Read N and Q. For each test case, collect the N marble values in a list.<br>
      • Sort the list in ascending order, as Binary Search relies on an ordered dataset.<br>
      • For each query, search for the first occurrence of the element using <code>bisect.bisect_left</code> (ideal for handling duplicate values).<br>
      • Check if the returned index is within bounds and matches the searched value:<br>
      &nbsp;&nbsp;- If it matches, print the 1-based position (<code>index + 1</code>).<br>
      &nbsp;&nbsp;- Otherwise, state that the element was not found.<br><br>
      <b>📤 Output:</b><br>
      For each test case, print the header <code>CASE# X:</code>. For each query, print whether the number was found and its 1-based position, or that it was not found.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
4 1
2
3
5
1
5
5 2
1
3
3
3
1
2
3
0 0
```

### 📤 Exemplo de Saída / Example Output

```txt
CASE# 1:
5 found at 4
CASE# 2:
2 not found
3 found at 3
```