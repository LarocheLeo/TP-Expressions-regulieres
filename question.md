
# TP - Expressions regulières
## 1 Outils du Shell GNU
### 1 - Une Debian classique fournit deux outils de recherche de texte, grep et egrep, ce dernier utilisant par défaut les Regex "ERE". A l’aide de la commande which, donner la commande qui va donner la localisation de ces deux outils, et le résultat :

```
fi25-laroc@IUTR-25-69a2:~$ which grep egrep

/usr/bin/grep

/usr/bin/egrep

```
### 2 - En utilisant une substitution de commande utilisant la commande file, donner la commande qui va donner la nature de ces deux ﬁchiers, ainsi que le résultat :


```
fi25-laroc@IUTR-25-69a2:~/TP-regex$ file $(which grep egrep)

/usr/bin/grep:  ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=94e89ce001d1bd1b0067229744810d2e56c9b020, for GNU/Linux 3.2.0, stripped

/usr/bin/egrep: POSIX shell script, ASCII text executable

```
### 3 - En utilisant une substitution de commande utilisant du --bytes , donner la commande qui va donner la taille de ces deux fichiers, ainsi que leur taille :
```
fi25-laroc@IUTR-25-69a2:~/TP-regex$ du --bytes  $(which grep egrep)

186824	/usr/bin/grep

41	/usr/bin/egrep

```

### 4 - Pour ce dernier, l’afficher avec cat. Que pouvez-vous dire ?

```
fi25-laroc@IUTR-25-69a2:~/TP-regex$ cat  $(which egrep)
#!/bin/sh
cmd=${0##*/}
exec grep -E "$@"

```

on peut voir donc que egrep est un scrip qui utilise grep avec -E pour extended-regexp.

## 2 Mise en pratique

### 2.1 Noms de fichiers
### Proposer une Regex qui va permettre de détecter des noms de fichiers de type image, à la condition qu’ils respectent les critères habituels : extension séparée du nom par un point, pas de fichier caché (commençant par un point)

img0912.jpg
updated_img0912.png
favicon.gif
documentation.html
.bash_profile
img0912.jpg.tmp
access.lock
workspace.doc
.a.b.jpg
azertyjpg


```
fi25-laroc@IUTR-25-69a2:~/TP-regex$ grep -Px "[^\.].*\.(jpg|gif|png)$" noms_fichiers.txt 

img0912.jpg
updated_img0912.png
favicon.gif
```


### 2.2 Nombres
### Proposer une regex qui va matcher sur les chaines suivantes :

# ok 
3,14529
-255,34
128
1,9e10
2e11
123.340,00
245,433
456


### en évitant de matcher sur les suivantes :

# pas bon
 789
720p
384$
248.22€
5x22
0xF5
3+2=6



```
fi25-laroc@IUTR-25-69a2:~/TP-regex$ grep -Px "[0-9\.e,-]{1,}[^+=xp\$€]" nombres.txt 

3,14529
-255,34
128
1,9e10
2e11
123.340,00
245,433
456

```

### 2.3 Numéros de téléphone (Américains)
### Dans un champ de texte, les utilisateurs doivent saisir des numéros de téléphone américains. Par exemple :


```
fi25-laroc@IUTR-25-69a2:~/TP-regex$ grep -E '^(1(\s|-))?((\([0-9]{3}\)(\s|-)?[0-9]{3}(\s|-)[0-9]{4})|([0-9]{3}(\s|-)?[0-9]{3}(\s|-)[0-9]{4})|([0-9]{10}))$' no_tel_USA.txt
415-555-1234
650-555-2345
(416)555-3456
202 555 4567
4035555678
1 416 555 9292
1-416-555-9292

```

### 2.4 Adresses IPv4
### Matcher une adresse IP n’est pas si simple qu’il n’y parait : Il s’agit de 3 groupes de 3 chiffres, mais qui doivent respecter la contrainte de ne pas dépasser 255.
### Commencer par écrire une Regex qui matche sur une valeur entre 1 et 255 avec un point derrière. Vous utiliserez ce ﬁchier pour la validation :

```
fi25-laroc@IUTR-25-69a2:~/TP-regex$ grep -P '^([1-2][0-4][0-9]?|^25[0-5]|[1-9]\d?|1\d{0,2})\.$' adresses_ipv4_1.txt 
1.
2.
9.
10.
20.
21.
30.
99.
100.
200.
248.
255.
```


```
fi25-laroc@IUTR-25-69a2:~/TP-regex$ a='(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])'
fi25-laroc@IUTR-25-69a2:~/TP-regex$ grep -P "^($a\.){3}$a$" adresses_ipv4_2.txt
1.1.1.1
200.200.200.200
4.4.4.40
4.6.7.8
255.255.255.255
fi25-laroc@IUTR


```

## Analyse d’un fichier système
### Le fichier /etc/services liste les services réseau et le port qui leur est assigné. Examiner ce fichier (sans le modifier ! ! !) et donner les commandes suivantes :
### 1 - Analyser la construction de ce fichier. En particulier, essayer l’outil xxd pour voir le/les caractère(s) utilisé(s) pour séparer les colonnes.
### 2 - Donner le nombre de services utilisant un port TCP :
```
fi25-laroc@IUTR-25-69a2:~/TP-regex$ cat /etc/services | grep /tcp | wc -l
218
```
### 3 - En prenant à la place du fichier réel le fichier ici :

### https://github.com/skramm/but3_rt/blob/main/ressources_TP/regex/services.txt
### Donner le nombre de services utilisant un port UDP et avec un numéro de port inférieur à 1023.

```
fi25-laroc@IUTR-25-69a2:~/TP-regex$ grep -P "\s([0-9]|[0-9]{2}|[0-9]{3}|10[0-2][0-3])/udp" services.txt | wc -l 
54

```
## 4 Validation d’entrée utilisateur






```


