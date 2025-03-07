import numpy as np

def calculate(list):
  

    if len(list) >= 9:

        try:
            def calculer_statistiques(liste, fonction_statistique):
                return [fonction_statistique(liste, axis=0).tolist(), fonction_statistique(liste, axis=1).tolist(), fonction_statistique(liste.flatten())]

            # conversion de la liste en tableau numpy
            List = np.array(list).reshape(3, 3)
            #list_flatten = List.flatten()

            # Calculs des statistiques
            mean_calculations = calculer_statistiques(List, np.mean)
            sum_calculations = calculer_statistiques(List, np.sum)
            max_calculations = calculer_statistiques(List, np.max)
            min_calculations = calculer_statistiques(List, np.min)
            variance_calculations = calculer_statistiques(List, np.var)
            standard_deviation_calculations = calculer_statistiques(List, np.std)
        except Exception as e:
            print("Entrez au moins 9 éléments",e)

    def calculer_statistiques(liste, fonction_statistique):
        return [fonction_statistique(liste, axis=0).tolist(), fonction_statistique(liste, axis=1).tolist(), fonction_statistique(liste.flatten())]

    mean_calculations = calculer_statistiques(List, np.mean)
    variance_calculations = calculer_statistiques(List, np.var)
    standard_deviation_calculations = calculer_statistiques(List, np.std)
    max_calculations = calculer_statistiques(List, np.max)
    min_calculations = calculer_statistiques(List, np.min)
    sum_calculations = calculer_statistiques(List, np.sum)
    calculations = dict(mean=mean_calculations, variance=variance_calculations, standard_eviation=standard_deviation_calculations, max=max_calculations, min=min_calculations, sum=sum_calculations)
    
    return calculations

list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
dict = calculate(list)
print(dict)