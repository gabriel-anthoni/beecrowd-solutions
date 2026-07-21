### <img src="https://static.wikia.nocookie.net/duolingo/images/1/17/Brazil_bandera.png/revision/latest?cb=20230710181600&path-prefix=es" width="20"> PT-BR

<!----------------------------------------------------------------------------------------->

<table>
  <tr>
    <th width="300">Linguagem</th>
    <th width="1000">Questão</th>
  </tr>
  <tr>
    <td>
      <p align="center"><img src="https://skillicons.dev/icons?i=python"></p>
      <p align="center"><code>Python 3.11</code></p>
    </td>
    <td>
      <p align="center"><i>beecrowd | 1024</i></p>
      <h3 align="center">Criptografia</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A entrada contém vários casos de teste. A primeira linha de cada caso de teste contém um inteiro N que indica a quantidade de casos de teste.
- Cada uma das N linhas seguintes contém uma string com diversos caracteres (letras, números, espaços, pontuações, etc.).

*Exemplo de entrada:*
```
4
Texto #3
abcABC1
vxvx xvxv
vvv
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

Este problema é composto por três etapas consecutivas de criptografia:

1. **Primeira Passada:** Desloque todas as letras maiúsculas e minúsculas 3 posições para a direita na tabela ASCII.
   - *Exemplo:* 'a' se torna 'd', 'Z' se torna ']'. Caracteres não alfabéticos (números, espaços, pontuações) permanecem inalterados.
2. **Segunda Passada:** Inverta a ordem dos caracteres da string (do fim para o começo).
3. **Terceira Passada:** A partir da metade da string (truncada/divisão inteira), todos os caracteres devem ser deslocados 1 posição para a esquerda na tabela ASCII.
   - O índice de início da segunda metade é definido por `metade = len(texto) // 2`.
   - *Exemplo:* se a string invertida tem tamanho 6, os caracteres nos índices 3, 4 e 5 serão deslocados; se tem tamanho 5, os caracteres nos índices 2, 3 e 4 serão deslocados.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- Para cada caso de teste, imprima a string completamente criptografada de acordo com as três regras descritas.

*Exemplo de saída:*
```
3#xTeTo
1CBcbda
wuwu uwuw
uuu
```

---

<!----------------------------------------------------------------------------------------->

### <img src="https://static.wikia.nocookie.net/duolingo/images/7/79/Ingles.png/revision/latest?cb=20230710181050&path-prefix=es" width="20"> EN

<!----------------------------------------------------------------------------------------->

<table>
  <tr>
    <th width="300">Language</th>
    <th width="1000">Problem</th>
  </tr>
  <tr>
    <td>
      <p align="center"><img src="https://skillicons.dev/icons?i=python"></p>
      <p align="center"><code>Python 3.11</code></p>
    </td>
    <td>
      <p align="center"><i>beecrowd | 1024</i></p>
      <h3 align="center">Encryption</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input contains several test cases. The first line of each testcase contains an integer N indicating the number of test cases.
- Each of the following N lines contains a string with various types of characters (letters, numbers, spaces, punctuation, etc.).

*Example Input:*
```
4
Texto #3
abcABC1
vxvx xvxv
vvv
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

This problem consists of three consecutive encryption steps:

1. **First Pass:** Shift all uppercase and lowercase letters 3 positions to the right in the ASCII table.
   - *Example:* 'a' becomes 'd', 'Z' becomes ']'. Non-alphabetical characters (digits, spaces, symbols) remain unchanged.
2. **Second Pass:** Reverse the string (from end to beginning).
3. **Third Pass:** Starting from the half of the string (integer division/truncated), all characters must be shifted 1 position to the left in the ASCII table.
   - The starting index for the second half is defined by `half = len(text) // 2`.
   - *Example:* if the reversed string has length 6, characters at indices 3, 4, and 5 are shifted; if it has length 5, characters at indices 2, 3, and 4 are shifted.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- For each testcase, print the fully encrypted string according to the three rules.

*Example Output:*
```
3#xTeTo
1CBcbda
wuwu uwuw
uuu
```