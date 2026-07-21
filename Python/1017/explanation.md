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
      <p align="center"><i>beecrowd | 1017</i></p>
      <h3 align="center">Gasto de Combustível</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A entrada contém dois valores inteiros: o tempo gasto na viagem (em horas) e a velocidade média durante a mesma (em km/h).

*Exemplo de entrada:*
```
10
85
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

- Leia o tempo de viagem (em horas) e a velocidade média (em km/h) usando `int(input())`.
- Calcule a distância total percorrida multiplicando o tempo pela velocidade média:

$$
Distancia = Tempo \\cdot Velocidade
$$

- Calcule a quantidade de combustível consumida dividindo a distância total pelo consumo médio do automóvel (que faz 12 km/L):

$$
Litros = \\frac{Distancia}{12}
$$

- utilize f-string para formatar a saída com 3 casas decimais.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- Imprima a quantidade de litros necessária para realizar a viagem, com três dígitos após o ponto decimal.

*Exemplo de saída:*
```
70.833
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
      <p align="center"><i>beecrowd | 1017</i></p>
      <h3 align="center">Fuel Spent</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input file contains two integers. The first one is the spent time in the trip (in hours) and the second one is the average speed during the trip (in Km/h).

*Example Input:*
```
10
85
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- Read the spent time (in hours) and average speed (in km/h) using `int(input())`.
- Calculate the total distance traveled by multiplying the spent time by the average speed:

$$
Distance = Time \\cdot Speed
$$

- Calculate the spent fuel by dividing the total distance by the average consumption of the car (which does 12 km/L):

$$
Liters = \\frac{Distance}{12}
$$

- Use f-string to format the output to 3 decimal places.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- Print how many liters of fuel would be needed to do this trip, with three digits after the decimal point.

*Example Output:*
```
70.833
```