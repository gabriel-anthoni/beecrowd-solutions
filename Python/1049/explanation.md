<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1049">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1049 — Animal</h3>

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
      A entrada contém 3 palavras (strings) em linhas separadas: subfilo, classe e tipo de alimentação.<br><br>
      <b>🧠 Lógica:</b><br>
      • Leia as três palavras utilizando <code>input().strip()</code>.<br>
      • Avalie a <b>árvore de decisão</b> taxonômica usando condicionais aninhadas (<code>if/elif/else</code>) ou um dicionário de tuplas para mapeamento direto:<br>
      &nbsp;&nbsp;- <code>vertebrado → ave → carnivoro</code>: <code>aguia</code><br>
      &nbsp;&nbsp;- <code>vertebrado → ave → onivoro</code>: <code>pomba</code><br>
      &nbsp;&nbsp;- <code>vertebrado → mamifero → onivoro</code>: <code>homem</code><br>
      &nbsp;&nbsp;- <code>vertebrado → mamifero → herbivoro</code>: <code>vaca</code><br>
      &nbsp;&nbsp;- <code>invertebrado → inseto → hematofago</code>: <code>pulga</code><br>
      &nbsp;&nbsp;- <code>invertebrado → inseto → herbivoro</code>: <code>lagarta</code><br>
      &nbsp;&nbsp;- <code>invertebrado → anelideo → hematofago</code>: <code>sanguessuga</code><br>
      &nbsp;&nbsp;- <code>invertebrado → anelideo → onivoro</code>: <code>minhoca</code><br><br>
      <b>📤 Saída:</b><br>
      Imprima o nome do animal correspondente à combinação das três palavras.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input contains 3 words (strings) on separate lines: subphylum, class, and diet type.<br><br>
      <b>🧠 Logic:</b><br>
      • Read the three words using <code>input().strip()</code>.<br>
      • Traverse the taxonomic <b>decision tree</b> using nested conditionals (<code>if/elif/else</code>) or a tuple-keyed dictionary mapping:<br>
      &nbsp;&nbsp;- <code>vertebrado → ave → carnivoro</code>: <code>aguia</code><br>
      &nbsp;&nbsp;- <code>vertebrado → ave → onivoro</code>: <code>pomba</code><br>
      &nbsp;&nbsp;- <code>vertebrado → mamifero → onivoro</code>: <code>homem</code><br>
      &nbsp;&nbsp;- <code>vertebrado → mamifero → herbivoro</code>: <code>vaca</code><br>
      &nbsp;&nbsp;- <code>invertebrado → inseto → hematofago</code>: <code>pulga</code><br>
      &nbsp;&nbsp;- <code>invertebrado → inseto → herbivoro</code>: <code>lagarta</code><br>
      &nbsp;&nbsp;- <code>invertebrado → anelideo → hematofago</code>: <code>sanguessuga</code><br>
      &nbsp;&nbsp;- <code>invertebrado → anelideo → onivoro</code>: <code>minhoca</code><br><br>
      <b>📤 Output:</b><br>
      Print the animal's name corresponding to the combination of the three input words.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
vertebrado
mamifero
onivoro
```

### 📤 Exemplo de Saída / Example Output

```
homem
```