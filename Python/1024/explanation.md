<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1024">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1024 — Criptografia</h3>

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
      A primeira linha contém a quantidade N de casos de teste. As N linhas seguintes contêm frases com caracteres variados (letras, números, espaços, símbolos).<br><br>
      <b>🧠 Lógica:</b><br>
      A criptografia é executada em três passadas consecutivas:<br>
      • <b>1ª Passada:</b> Desloque todas as letras maiúsculas e minúsculas 3 posições à direita na tabela ASCII. Caracteres não alfabéticos permanecem inalterados.<br>
      • <b>2ª Passada:</b> Inverta a ordem dos caracteres da string resultante.<br>
      • <b>3ª Passada:</b> A partir da metade da string (índice <code>len(texto) // 2</code>), desloque todos os caracteres 1 posição à esquerda na tabela ASCII.<br><br>
      <b>📤 Saída:</b><br>
      Imprima a string completamente criptografada após a aplicação das três etapas para cada caso de teste.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The first line contains an integer N indicating the number of test cases. Each of the following N lines contains a string with various characters (letters, digits, spaces, symbols).<br><br>
      <b>🧠 Logic:</b><br>
      Encryption is performed in three consecutive passes:<br>
      • <b>1st Pass:</b> Shift all uppercase and lowercase letters 3 positions to the right in the ASCII table. Non-alphabetical characters remain unchanged.<br>
      • <b>2nd Pass:</b> Reverse the order of the resulting string.<br>
      • <b>3rd Pass:</b> From the middle of the string onwards (starting at index <code>len(text) // 2</code>), shift all characters 1 position to the left in the ASCII table.<br><br>
      <b>📤 Output:</b><br>
      Print the fully encrypted string after applying all three steps for each test case.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
4
Texto #3
abcABC1
vxvx xvxv
vvv
```

### 📤 Exemplo de Saída / Example Output

```txt
3#xTeTo
1CBcbda
wuwu uwuw
uuu
```