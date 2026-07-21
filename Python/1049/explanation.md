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
      <p align="center"><i>beecrowd | 1049</i></p>
      <h3 align="center">Animal</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A entrada contém 3 palavras de texto (strings), em linhas separadas e com letras minúsculas, representando as características do animal:
  1. Subfilo (`vertebrado` ou `invertebrado`)
  2. Classe (`ave`, `mamifero`, `inseto` ou `anelideo`)
  3. Alimentação (`carnivoro`, `onivoro`, `herbivoro` ou `hematofago`)

*Exemplo de entrada:*
```
vertebrado
mamifero
onivoro
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

- O problema consiste na navegação por uma **árvore de decisão** binária baseada em três níveis de classificação biológica.
- Para cada combinação única de 3 palavras, existe exatamente um animal correspondente:
  - `vertebrado` $\rightarrow$ `ave` $\rightarrow$ `carnivoro` $\implies$ **aguia**
  - `vertebrado` $\rightarrow$ `ave` $\rightarrow$ `onivoro` $\implies$ **pomba**
  - `vertebrado` $\rightarrow$ `mamifero` $\rightarrow$ `onivoro` $\implies$ **homem**
  - `vertebrado` $\rightarrow$ `mamifero` $\rightarrow$ `herbivoro` $\implies$ **vaca**
  - `invertebrado` $\rightarrow$ `inseto` $\rightarrow$ `hematofago` $\implies$ **pulga**
  - `invertebrado` $\rightarrow$ `inseto` $\rightarrow$ `herbivoro` $\implies$ **lagarta**
  - `invertebrado` $\rightarrow$ `anelideo` $\rightarrow$ `hematofago` $\implies$ **sanguessuga**
  - `invertebrado` $\rightarrow$ `anelideo` $\rightarrow$ `onivoro` $\implies$ **minhoca**

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- Imprima o nome do animal correspondente às três características lidas.

*Exemplo de saída:*
```
homem
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
      <p align="center"><i>beecrowd | 1049</i></p>
      <h3 align="center">Animal</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input contains 3 words (strings), on separate lines and in lowercase, defining the animal's biological traits:
  1. Subphylum (`vertebrado` or `invertebrado`)
  2. Class (`ave`, `mamifero`, `inseto`, or `anelideo`)
  3. Diet (`carnivoro`, `onivoro`, `herbivoro`, or `hematofago`)

*Example Input:*
```
invertebrado
anelideo
hematofago
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- The task requires evaluating a binary **decision tree** based on three hierarchy levels.
- Each unique triplet maps directly to one specific animal target:
  - `vertebrado` $\rightarrow$ `ave` $\rightarrow$ `carnivoro` $\implies$ **aguia**
  - `vertebrado` $\rightarrow$ `ave` $\rightarrow$ `onivoro` $\implies$ **pomba**
  - `vertebrado` $\rightarrow$ `mamifero` $\rightarrow$ `onivoro` $\implies$ **homem**
  - `vertebrado` $\rightarrow$ `mamifero` $\rightarrow$ `herbivoro` $\implies$ **vaca**
  - `invertebrado` $\rightarrow$ `inseto` $\rightarrow$ `hematofago` $\implies$ **pulga**
  - `invertebrado` $\rightarrow$ `inseto` $\rightarrow$ `herbivoro` $\implies$ **lagarta**
  - `invertebrado` $\rightarrow$ `anelideo` $\rightarrow$ `hematofago` $\implies$ **sanguessuga**
  - `invertebrado` $\rightarrow$ `anelideo` $\rightarrow$ `onivoro` $\implies$ **minhoca**

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- Print the animal's name corresponding to the input characteristics.

*Example Output:*
```
sanguessuga
```