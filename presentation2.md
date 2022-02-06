---
marp: true
theme: uncover
class: invert
paginate: true
backgroundImage: url('https://media.discordapp.net/attachments/654703064279941140/934997629404852234/wp4831645.png')
---

![bg left:40% 80%](https://media.discordapp.net/attachments/654703064279941140/934999099990736896/8-abstract-feather-setsiri-silapasuwanchai-transparent.png)

# **Terrain generation**
Procedural Content Generation

https://github.com/Lerqiu/AI4Games-project

---

# Islands and shapes

---

### Wolrey for mass clusterization
![width:1000px drop-shadow:0,5px,10px,rgba(0,0,0,.4)](https://media.discordapp.net/attachments/891385522063302747/939978440403206194/unknown.png)

---

### Singular cluster
![width:1000px drop-shadow:0,5px,10px,rgba(0,0,0,.4)](https://media.discordapp.net/attachments/891385522063302747/939979068676395028/unknown.png)

---

We can hide marginal islands gracefully with heat-like noise distribution

![bg left:50% 70% drop-shadow:0,5px,10px,rgba(0,0,0,.4)](https://media.discordapp.net/attachments/891385522063302747/939979429948583966/unknown.png)

---

Before             		   | After
:-------------------------:|:-------------------------:
![width:475px](https://media.discordapp.net/attachments/891385522063302747/939980512938819645/unknown.png)  |  ![width:475px](https://media.discordapp.net/attachments/891385522063302747/939980562884595742/unknown.png)

---

# Moisture levels
![bg drop-shadow:0,5px,10px,rgba(0,0,0,.4)](https://media.discordapp.net/attachments/654703064279941140/939983340247851038/unknown.png)

---

Before             		   | After
:-------------------------:|:-------------------------:
![width:475px](https://media.discordapp.net/attachments/654703064279941140/939985555817656360/unknown.png)  |  ![width:475px](https://cdn.discordapp.com/attachments/654703064279941140/939984341235277824/unknown.png)


---

# Biomes

---

Biomes are dependent upon both the terrain height and the moisture level 

![bg left:40% 60% drop-shadow:0,5px,10px,rgba(0,0,0,.4)](https://media.discordapp.net/attachments/654703064279941140/939998616892874792/unknown.png) 

---

##### We apply different gradients to each of the biomes

![width:900px drop-shadow:0,5px,10px,rgba(0,0,0,.4)](https://media.discordapp.net/attachments/654703064279941140/940003881017024522/unknown.png)

---

# Content generators
![bg](https://media.discordapp.net/attachments/654703064279941140/940013246293901342/unknown.png)

---

## Model parameters
- clusters
- beaches
- mountains
- moisture
- land

---

## Clusters

Low             		   | High
:-------------------------:|:-------------------------:
![width:475px](https://media.discordapp.net/attachments/654703064279941140/940016832562229278/unknown.png)  |  ![width:475px](https://media.discordapp.net/attachments/654703064279941140/940016277525766206/unknown.png)

---

## Beaches

Low             		   | High
:-------------------------:|:-------------------------:
![width:475px](https://media.discordapp.net/attachments/654703064279941140/940017697423503370/unknown.png)  |  ![width:475px](https://media.discordapp.net/attachments/654703064279941140/940017859889872908/unknown.png)

---

## Mountains

Low             		   | High
:-------------------------:|:-------------------------:
![width:475px](https://images-ext-2.discordapp.net/external/71zE8cqUF_2riVlq7TX-rABzgQa2PvP566o73HW6WS0/https/media.discordapp.net/attachments/654703064279941140/940017859889872908/unknown.png)  |  ![width:475px](https://media.discordapp.net/attachments/654703064279941140/940018787946749962/unknown.png)

---

## Moisture

Low             		   | High
:-------------------------:|:-------------------------:
![width:475px](https://media.discordapp.net/attachments/654703064279941140/940020348856983572/unknown.png)  |  ![width:475px](https://media.discordapp.net/attachments/654703064279941140/940020903998291968/unknown.png)

---

## Land

Low             		   | High
:-------------------------:|:-------------------------:
![width:475px](https://media.discordapp.net/attachments/654703064279941140/940021546871844874/unknown.png)  |  ![width:475px](https://media.discordapp.net/attachments/654703064279941140/940021480153051186/unknown.png)

