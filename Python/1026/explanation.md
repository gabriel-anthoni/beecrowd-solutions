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
      <p align="center"><i>beecrowd | 1026</i></p>
      <h3 align="center">Carrega ou não Carrega?</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A entrada contém vários casos de teste e termina com o fim de arquivo (EOF).
- Cada linha contém dois números inteiros não assinados de 32 bits.

*Exemplo de entrada:*
```
4 6
6 9
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

- O problema descreve uma calculadora com um "defeito" no circuito somador: ela soma dois números em binário, mas **esquece de carregar o bit** (o famoso "vai um") para a coluna seguinte.
- Na lógica digital, somar dois bits sem considerar o transporte é exatamente a definição da operação **OU Exclusivo (XOR)**.
  - `0 + 0 = 0`
  - `1 + 0 = 1`
  - `0 + 1 = 1`
  - `1 + 1 = 0` (carregaria 1, mas o "vai um" é descartado)
- Em Python, o operador bitwise XOR é representado pelo símbolo circunflexo (`^`). 
- A leitura contínua até o final do arquivo (EOF) pode ser feita de forma extremamente eficiente iterando diretamente sobre as linhas do buffer de entrada do módulo `sys`.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- Para cada caso de teste, imprima o valor da soma "defeituosa" (o resultado do XOR bit a bit entre os dois inteiros).

*Exemplo de saída:*
```
2
15
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
      <p align="center"><i>beecrowd | 1026</i></p>
      <h3 align="center">To Carry or not to Carry?</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input contains several test cases and ends with the End-of-File (EOF).
- Each line contains two 32-bit unsigned integers.

*Example Input:*
```
4 6
6 9
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- The problem describes a calculator with a "bug" in its addition unit: it adds two numbers in binary format, but it **forgets to carry the bit** to the next column.
- In digital logic, adding two bits while discarding the carry-out is precisely the definition of the **Exclusive OR (XOR)** operation.
  - `0 + 0 = 0`
  - `1 + 0 = 1`
  - `0 + 1 = 1`
  - `1 + 1 = 0` (it would carry 1, but the carry is dropped)
- In Python, the bitwise XOR operator is represented by the caret symbol (`^`).
- Reading continuously until the end of file (EOF) can be handled with high performance by iterating directly through the input buffer from the `sys` module.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- For each test case, print the result of the "buggy" addition (the bitwise XOR result between the two integers).

*Example Output:*
```
2
15
```