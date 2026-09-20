<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1026">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1026 — Carrega ou não Carrega?</h3>

  <p>
    <img src="https://img.shields.io/badge/Linguagem-Python_3.11-3776AB?style=flat-square&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/N%C3%ADvel-5-green?style=flat-square" />
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
      A entrada contém vários casos de teste e termina com fim de arquivo (EOF). Cada linha contém dois números inteiros não assinados de 32 bits.<br><br>
      <b>🧠 Lógica:</b><br>
      • O problema descreve um circuito somador que esquece o transporte ("vai um") ao somar números em binário.<br>
      • Na lógica digital, somar bits sem considerar o transporte é exatamente a definição da operação <b>OU Exclusivo (XOR)</b>.<br>
      • Em Python, utilize o operador bitwise XOR (<code>^</code>) entre os dois inteiros.<br>
      • Trate a leitura contínua até o fim de arquivo (EOF) de forma eficiente iterando sobre as linhas do buffer de <code>sys.stdin</code>.<br><br>
      <b>📤 Saída:</b><br>
      Para cada caso de teste, imprima o resultado do XOR bit a bit entre os dois inteiros.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input contains several test cases and ends with End-of-File (EOF). Each line contains two 32-bit unsigned integers.<br><br>
      <b>🧠 Logic:</b><br>
      • The problem describes an adder circuit that forgets the carry bit when adding numbers in binary.<br>
      • In digital logic, adding bits while discarding the carry is precisely the definition of the <b>Exclusive OR (XOR)</b> operation.<br>
      • In Python, use the bitwise XOR operator (<code>^</code>) between the two integers.<br>
      • Handle continuous reading until End-of-File (EOF) efficiently by iterating through <code>sys.stdin</code> lines.<br><br>
      <b>📤 Output:</b><br>
      For each test case, print the result of the bitwise XOR operation between the two integers.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
4 6
6 9
```

### 📤 Exemplo de Saída / Example Output

```txt
2
15
```