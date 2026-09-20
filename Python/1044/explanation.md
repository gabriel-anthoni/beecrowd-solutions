<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1044">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1044 — Múltiplos</h3>

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
      A entrada contém dois valores inteiros A e B em uma única linha.<br><br>
      <b>🧠 Lógica:</b><br>
      • Leia os dois inteiros utilizando <code>map(int, input().split())</code>.<br>
      • Verifique se um é múltiplo do outro avaliando o resto da divisão:<br>
      &nbsp;&nbsp;<code>A % B == 0 or B % A == 0</code><br>
      • Se a condição for verdadeira, imprima <code>Sao Multiplos</code>.<br>
      • Caso contrário, imprima <code>Nao sao Multiplos</code>.<br><br>
      <b>📤 Saída:</b><br>
      Imprima <code>Sao Multiplos</code> ou <code>Nao sao Multiplos</code> de acordo com o resultado.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input contains two integer values, A and B, on a single line.<br><br>
      <b>🧠 Logic:</b><br>
      • Read the two integers using <code>map(int, input().split())</code>.<br>
      • Check whether one is a multiple of the other using the modulo operator:<br>
      &nbsp;&nbsp;<code>A % B == 0 or B % A == 0</code><br>
      • If true, print <code>Sao Multiplos</code>.<br>
      • Otherwise, print <code>Nao sao Multiplos</code>.<br><br>
      <b>📤 Output:</b><br>
      Print <code>Sao Multiplos</code> or <code>Nao sao Multiplos</code> depending on the evaluation result.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
6 24
```

### 📤 Exemplo de Saída / Example Output

```
Sao Multiplos
```