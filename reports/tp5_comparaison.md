# Modele manuel ou modele AutoML ? (TP05)

| Critere                    | Manuel (rf 500/16)       | AutoML (FLAML 90 s)       |
|----------------------------|--------------------------|---------------------------|
| Famille de modele          | foret aleatoire          | [famille du run]          |
| F1 sur le jeu de test      | 0.8669                   | 0.8582                    |
| Temps de recherche machine | [duree_entrainement_s] s | 90.6 s                    |
| Temps humain (estimation)  | ~1 a 2 h (TP2)           | ~10 min                   |
| Latence mediane (ms)       | [mediane 8101]           | 13.4 / 14.3               |
| Latence p95 (ms)           | [p95 8101]               | 29.9 / 28.6               |
| Taille du fichier (Mo)     | [model_manuel.pkl]       | [model_automl.pkl]        |
| Explicabilite              | importance des variables, 500 arbres, profondeur 16 | importance des variables ; ensemble sequentiel (boosting), plus difficile a lire |