# Kopírovanie excelovských hárkov, kde niektoré bunky su chránene

Možno poznáte situáciu, v MS Excel, že chcete skopírovať jeden hárok do ďaľšich hárkov.
Problém nastane ak v hárku, ktorý má niektoré bunky zapezpečené, nakopírujete do nových hárkov.
ale tie zabezpečené bunky neostanú zabezpečené aj v tých nových hárkch. No dá sa to potom robiť, zasa
manuálne, tak ako v prvom hárku, ale ak to máme robiť pre n-hárkov, tak asi nie.

Najprv si to ale vyskúšajte so zdrojovým súborom (teda jeho kópiou) v MS Excely, že je to naozaj tak.

No urobíme na to pythonovský kód, ktorý vykoná kopírovanie hárku, v ktorom sú zapezpečené bunky sám.