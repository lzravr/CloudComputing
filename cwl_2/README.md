# Zadatak 3
Neka je dat proizvoljan broj fajlova u kojima se nalaze logovi poziva i sms poruka mobilnog operatera u formatu:


broj_telefona, tip_saobracaja, ostvaren_saobracaj,


tip_saobracaja može imati vrednosti "poziv" ili "sms", dok ostvaren_saobracaj predstavlja broj minuta ili broj poslatih sms poruka u zavisnosti od tipa saobraćaja. Primer log fajla je:

065111111,poziv,3.25 
065222222,sms,5 
065111111,sms,3 
.
.
.

Cena jedne sms poruke iznosi 3.26 dinara, dok cena jednog minuta poziva iznosi 5.89 dinara. Potrebno je odrediti broj telefona korisnika koji u ukupnom zbiru troškova saobraćaja ima najveći iznos račun za plaćanje. 

Potrebno je na CWL jeziku napisati odgovarajuća skripta i programe koji će odrediti traženog korisnika paralelnom obradom ulaznih fajlova. Ulaz u ceo proces izvršavanja je lista fajlova sa opisanim logovima, cena sms poruke i cena minuta poziva. Rešenje je potrebno ispisati u fajl resenje.txt.

Napomena: Zadatak je moguće rešiti u proizvoljnom programskom jeziku. Obradu je obavezno uraditi u kontejnerskom okruženju i obavezno je korišćenje scattering radnih tokova.