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
      <p align="center"><i>beecrowd | 1023</i></p>
      <h3 align="center">Estiagem</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A entrada contém vários casos de teste. A primeira linha de cada caso de teste contém um inteiro N (1 <= N <= 100000) que indica a quantidade de imóveis.
- Cada uma das N linhas seguintes contém dois inteiros: o número de moradores de cada imóvel e o respectivo consumo desse imóvel (em m³).
- A entrada termina quando N = 0.

*Exemplo de entrada:*
```
3
3 22
1 11
2 39
0
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

- Use `sys.stdin.readline` para uma leitura extremamente rápida de dados, pois este problema possui um volume massivo de entradas e limites de tempo rigorosos.
- Continue lendo os casos até que $N = 0$.
- Para cada imóvel, acumule o total de pessoas (`total_people`) e o consumo total (`total_consumption`).
- Calcule o consumo médio truncado (divisão inteira `//`) por pessoa de cada imóvel:

$$
ConsumoMédio = Consumo // Moradores
$$

- Agrupe a quantidade total de moradores por cada faixa de consumo médio em um dicionário (`consumptions`).
- Ordene as faixas de consumo de forma crescente e imprima os pares no formato `moradores-consumo`.
- Calcule a média geral de consumo da cidade com truncamento exato de duas casas decimais (sem arredondar para cima):

$$
MédiaGeral = \frac{\lfloor (TotalConsumo \cdot 100) / TotalPessoas \rfloor}{100}
$$

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- Para cada caso de teste, imprima o cabeçalho `Cidade# X:`.
- Apresente os moradores agrupados por consumo médio em ordem crescente, separados por um espaço em branco (sem espaço extra no final da linha).
- Imprima a média de consumo com duas casas decimais, truncada, seguida por `m3.`.
- Deve haver uma linha em branco estritamente *entre* dois casos de teste consecutivos (não deve haver linha em branco após o último caso).

*Exemplo de saída:*
```
Cidade# 1:
1-11 2-11 3-7
Consumo medio: 12.00 m3.
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
      <p align="center"><i>beecrowd | 1023</i></p>
      <h3 align="center">Drought</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input contains several test cases. The first line of each testcase contains an integer N (1 <= N <= 100000) indicating the number of properties.
- Each of the following N lines contains two integers: the number of residents in each property and their respective consumption (in m³).
- The input ends when N = 0.

*Example Input:*
```
3
3 22
1 11
2 39
0
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- Use `sys.stdin.readline` for high-speed input reading, as this problem features massive input datasets and tight execution time limits.
- Loop until $N = 0$.
- For each property, accumulate the total number of people (`total_people`) and total consumption (`total_consumption`).
- Calculate the truncated average consumption (integer division `//`) per person for each property:

$$
AvgConsumption = Consumption // Residents
$$

- Group the total number of residents by their average consumption bracket using a dictionary (`consumptions`).
- Sort the consumption brackets in ascending order and print the pairs in the format `residents-consumption`.
- Calculate the overall average consumption for the city, truncated strictly to two decimal places (without rounding up):

$$
OverallAverage = \frac{\lfloor (TotalConsumption \cdot 100) / TotalPeople \rfloor}{100}
$$

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- For each testcase, print the header `Cidade# X:`.
- Print the residents grouped by consumption in ascending order, separated by a single space (no trailing space at the end of the line).
- Print the average consumption with two decimal places, truncated, followed by `m3.`.
- There must be a blank line strictly *between* consecutive test cases (no trailing blank line after the final case).

*Example Output:*
```
Cidade# 1:
1-11 2-11 3-7
Consumo medio: 12.00 m3.
```