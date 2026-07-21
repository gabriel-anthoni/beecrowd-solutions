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
      <p align="center"><i>beecrowd | 1050</i></p>
      <h3 align="center">DDD</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A entrada consiste em um único valor inteiro representando o número do DDD.

*Exemplo de entrada:*
```
11
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

- Ler a entrada como texto (string) para evitar conversões numéricas desnecessárias.
- Mapear o código DDD digitado para a sua respectiva cidade:
  - `61` $\implies$ **Brasilia**
  - `71` $\implies$ **Salvador**
  - `11` $\implies$ **Sao Paulo**
  - `21` $\implies$ **Rio de Janeiro**
  - `32` $\implies$ **Juiz de Fora**
  - `19` $\implies$ **Campinas**
  - `27` $\implies$ **Vitoria**
  - `31` $\implies$ **Belo Horizonte**
- Caso o DDD informado não conste na tabela, retornar a mensagem `"DDD nao cadastrado"`.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- Imprima o nome da cidade correspondente ao DDD lido ou a mensagem de não cadastrado.

*Exemplo de saída:*
```
Sao Paulo
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
      <p align="center"><i>beecrowd | 1050</i></p>
      <h3 align="center">DDD</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input consists of a single integer number representing an area code (DDD).

*Example Input:*
```
11
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- Read the input directly as a string to bypass unnecessary integer conversions.
- Map the provided DDD area code to its corresponding city:
  - `61` $\implies$ **Brasilia**
  - `71` $\implies$ **Salvador**
  - `11` $\implies$ **Sao Paulo**
  - `21` $\implies$ **Rio de Janeiro**
  - `32` $\implies$ **Juiz de Fora**
  - `19` $\implies$ **Campinas**
  - `27` $\implies$ **Vitoria**
  - `31` $\implies$ **Belo Horizonte**
- If the DDD code is not present in the reference list, output `"DDD nao cadastrado"`.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- Print the city name associated with the given DDD or the "not found" message.

*Example Output:*
```
Sao Paulo
```