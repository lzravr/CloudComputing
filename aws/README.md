# Zadatak 5
Potrebno je napraviti web aplikaciju koja radi CRUD nad najmanje jednom tabelom podataka koja je smeštena u proizvoljnoj bazi podataka. 


Serverski deo aplikacije je potrebno hostovati na dve virtuelne mašine na AWS platformi. Na jednoj mašini je potrebno pokrenuti Eureka server i Zuul servis, a na drugoj mašini servise koji će raditi READ, UPDATE i DELETE. Za svaku od operacija je potrebno kreirati po jedan servis.  


Klijentski deo aplikacije implementirati u proizvoljnoj tehnologiji, a sve zahteve prema serveru je potrebno izvršavati preko Zuul servisa.

## Kako koristiti

**NAPOMENA**: Aplikacija koja je koriscena u ovom primeru je ista ona koju smo koristili u primeru [**docker-compose**](https://github.com/lzravr/CloudComputing/tree/master/docker-compose) .

### Local

Za pokretanje na lokalu, koriste se **.jar** fajlovi iz foldera **local**. Naziv MySql baze je *library* a kredencijali su:

**username**: **phpmyadmin**

**password**: **kiske**

Portovi na kojima rade servisi su navedeni u nastavku.

### AWS

U folderima **vm1** (masina 1) i **vm2** (masina 2) se nalaze **.jar** fajlovi koji se pokrecu na AWS EC2 servisu, na prvoj i drugoj virtuelnoj masini.

Konfiguracija **.jar** fajlova iz navedenih foldera je takva da odgovara konfiguraciji masina na EC2 servisu (njihovih IP adresa, otvorenih portova i konfiguraciji MySql servera). U slucaju koriscenja na drugim masinama potrebno je rekonfigurisati **.jar** fajlove (**application.properties**).

Na prvoj virutelnoj masini se nalaze:
1. nginx (na kome se nalazi klijent)
2. Java 8
3. eureka.jar
4. zuul.jar

Na drugoj virutelnoj masini se nalaze:
1. MySql Server
2. Java 8
3. read.jar
4. write.jar
5. delete.jar

Masinama su dodeljene staticke javne IP adrese (Elastic IPs). Aplikaciji se pristupa putem IP adrese masine na kojoj su webserver (nginx) i zuul, prve masine.

## Portovi

- 8090 - eureka
- 9079 - zuul
- 8082 - read
- 8083 - write
- 8084 - delete
