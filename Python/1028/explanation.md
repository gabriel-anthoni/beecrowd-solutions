<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1028">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1028 — Figurinhas</h3>

  <p>
    <img src="https://img.shields.io/badge/Linguagem-Python_3.11-3776AB?style=flat-square&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/N%C3%ADvel-3-green?style=flat-square" />
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
      A primeira linha contém um inteiro N (1 ≤ N ≤ 3000) indicando a quantidade de casos de teste. Cada caso subsequente contém dois inteiros F1 e F2 representando a quantidade de figurinhas de cada amigo.<br><br>
      <b>🧠 Lógica:</b><br>
      • O problema pede o tamanho máximo de uma pilha de figurinhas que permita dividir ambas as coleções em partes iguais.<br>
      • Isso equivale matematicamente a encontrar o <b>Máximo Divisor Comum (MDC)</b> entre F1 e F2.<br>
      • Em Python, utilize a função nativa <code>math.gcd(F1, F2)</code> para obter o resultado de forma otimizada.<br><br>
      <b>📤 Saída:</b><br>
      Para cada caso de teste, imprima um único valor inteiro correspondente ao tamanho máximo da pilha de figurinhas trocadas.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The first line contains an integer N (1 ≤ N ≤ 3000) indicating the number of test cases. Each subsequent case contains two integers F1 and F2 representing the number of cards each friend has.<br><br>
      <b>🧠 Logic:</b><br>
      • The problem asks for the maximum size of a stack of cards that allows dividing both collections equally.<br>
      • Mathematically, this is equivalent to finding the <b>Greatest Common Divisor (GCD)</b> between F1 and F2.<br>
      • In Python, use the built-in function <code>math.gcd(F1, F2)</code> to compute the answer efficiently.<br><br>
      <b>📤 Output:</b><br>
      For each test case, print a single integer representing the maximum size of the card stack they can trade.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
3
8 12
9 27
259 111
```

### 📤 Exemplo de Saída / Example Output

```txt
4
9
37
```