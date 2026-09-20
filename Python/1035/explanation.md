<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1035">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1035 — Teste de Seleção 1</h3>

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
      A entrada contém quatro valores inteiros: A, B, C e D.<br><br>
      <b>🧠 Lógica:</b><br>
      • Leia os quatro inteiros na mesma linha utilizando <code>input().split()</code>.<br>
      • Valide simultaneamente com o operador <code>and</code> as cinco condições:<br>
      &nbsp;&nbsp;1. <code>B > C</code><br>
      &nbsp;&nbsp;2. <code>D > A</code><br>
      &nbsp;&nbsp;3. <code>(C + D) > (A + B)</code><br>
      &nbsp;&nbsp;4. <code>C > 0</code> e <code>D > 0</code><br>
      &nbsp;&nbsp;5. <code>A % 2 == 0</code> (A é par)<br>
      • Se todas forem verdadeiras, imprima <code>Valores aceitos</code>; caso contrário, imprima <code>Valores nao aceitos</code>.<br><br>
      <b>📤 Saída:</b><br>
      Imprima <code>Valores aceitos</code> se todas as condições forem satisfeitas, ou <code>Valores nao aceitos</code> caso contrário.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input contains four integer values: A, B, C, and D.<br><br>
      <b>🧠 Logic:</b><br>
      • Read four integer values on a single line using <code>input().split()</code>.<br>
      • Validate all five conditions simultaneously using the <code>and</code> operator:<br>
      &nbsp;&nbsp;1. <code>B > C</code><br>
      &nbsp;&nbsp;2. <code>D > A</code><br>
      &nbsp;&nbsp;3. <code>(C + D) > (A + B)</code><br>
      &nbsp;&nbsp;4. <code>C > 0</code> and <code>D > 0</code><br>
      &nbsp;&nbsp;5. <code>A % 2 == 0</code> (A is even)<br>
      • If all conditions are met, print <code>Valores aceitos</code>; otherwise, print <code>Valores nao aceitos</code>.<br><br>
      <b>📤 Output:</b><br>
      Print <code>Valores aceitos</code> if all conditions are met, or <code>Valores nao aceitos</code> otherwise.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
5 6 7 8
```

### 📤 Exemplo de Saída / Example Output

```txt
Valores nao aceitos
```