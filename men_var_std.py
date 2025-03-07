from statistics import variance
import numpy as np

def calculate(list):
    """
    This function takes a list of numbers and returns a dictionary containing the following calculations:
    - The sum of all numbers
    - The average of all numbers
    - The maximum number"""

    if len(list) >= 9:
       
        # convertion de la liste en tableau numpy
            List = np.array(list).reshape(3, 3)
            print(List)

            list_flatten=List.flatten()
            print(list_flatten)
           
        # moyenne sur les deux axes
            mean_list_x=np.mean(List, axis=0)
            print(mean_list_x)

            mean_list_y=np.mean(List, axis=1)
            print(mean_list_y)

            mean_list_flatten=np.mean(list_flatten)
            print("flatten",mean_list_flatten)

            #somme sur les deux axes 
            sum_list_x=np.sum(List, axis=0)
            print(sum_list_x)

            sum_list_y=np.sum(List, axis=1)
            print(sum_list_x)

            sum_list_flatten=np.sum(list_flatten)
            print("flatten",sum_list_flatten)

            max_list_x=np.max(List, axis=0)
            print(max_list_x)
            max_list_y=np.max(List, axis=1)
            print(max_list_y)
            max_list_flatten=np.max(list_flatten)
            print("flatten",max_list_flatten)

            min_list_x=np.min(List, axis=0)
            print(min_list_x)
            min_list_y=np.min(List, axis=1)
            print(min_list_y)
            min_list_flatten=np.min(list_flatten)
            print("flatten",min_list_flatten)

            variance_x=np.var(List, axis=0)
            print(variance_x)
            variance_y=np.var(List, axis=1)
            print(variance_y)
            variance_flatten=np.var(list_flatten)
            print("flatten",variance_flatten)

         # standard deviation sur les deux axes

            standard_deviation_x=np.std(List, axis=0)
            print(standard_deviation_x)

            standard_deviation_y=np.std(List, axis=1)
            print(standard_deviation_y)

            standard_deviation_flatten=np.std(list_flatten,dtype=np.float64)
            print("flatten",standard_deviation_flatten)
    else:
            print("Enter at least 9 items")

    mean_calculations = [mean_list_x.tolist(),mean_list_y.tolist(),mean_list_flatten]
    variance_calculations = [variance_x.tolist(),variance_y.tolist(),variance_flatten]
    standard_deviation_calculations = [standard_deviation_x.tolist(),standard_deviation_y.tolist(),standard_deviation_flatten]
    max_calculations = [max_list_x.tolist(),max_list_y.tolist(),max_list_flatten]
    min_calculations = [min_list_x.tolist(),min_list_y.tolist(),min_list_flatten]
    sum_calculations = [sum_list_x.tolist(),sum_list_y.tolist(),sum_list_flatten]
    
    calculations = dict(mean=mean_calculations, variance=variance_calculations, standard_deviation=standard_deviation_calculations, max=max_calculations, min=min_calculations, sum=sum_calculations)
    
    return calculations

list=[0,1,2,3,4,5,6,7,8]
dict=calculate(list)
print(dict)