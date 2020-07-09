import random
import math
import pandas as pd
import numpy as np

cust = pd.read_csv('data/Cust_Segmentation.csv')

df = cust.drop('Address', axis = 1)

x = df.values[:,1:]
x = np.nan_to_num(x)

def k_means(data, cluster_size, max_iteration):
    batch_size = round(len(data) / cluster_size)
    data_len = len(data)
    column_number = len(data[0])
    clusters = list()

    """Находим начальные координаты кластеров, путем разбиения данных на кол-во кластеров и вычисляем средние координаты по этим точкам"""
    for i in range(cluster_size):
        cluster = list()
        for column_index in range(column_number):
            summ = 0
            size_col = 0
        
            for index_item in range(i * batch_size, (i+1) * batch_size):
                summ += data[index_item][column_index]   
                size_col += 1 

            cluster.append((summ/size_col) * random.random())
        clusters.append(cluster)
    
    """Находим в цикле точки кластеров"""
    for i in range(max_iteration):
        cluster_group = [list() for i in range(cluster_size)]

        for item in data:
            dist_min = False
            cluster_min_index = 0
            
            for cluster_iter in range(len(clusters)):
                dist = euclidean_distance(clusters[cluster_iter], item)

                if dist_min is False:
                    dist_min = dist
                elif dist < dist_min:
                    dist_min = dist
                    cluster_min_index = cluster_iter
            
            cluster_group[cluster_min_index].append(item)
        
        for index_cluster in range(cluster_size):
            new_coords = [0 for i in range(column_number)]
            column_len = [1 for i in range(column_number)]
        
            for index_column in range(column_number):
                for item in cluster_group[index_cluster]:
                    column_len[index_column] += 1
                    new_coords[index_column] += item[index_column]

            for index_column in range(column_number):
                new_coords[index_column] /= column_len[index_column]
        
            clusters[index_cluster] = list(new_coords)

    predict = list();

    """Вычисляем соотношение для каждой точки к кластеру"""
    for item in data:
        dist_min = False
        cluster_min_index = 0
        
        for cluster_iter in range(len(clusters)):
            dist = euclidean_distance(item, clusters[cluster_iter])
            if dist_min is False:
                dist_min = dist
            elif dist < dist_min:
                dist_min = dist
                cluster_min_index = cluster_iter

        predict.append(cluster_min_index)

    return predict
    

def euclidean_distance(vector1, vector2):
    """Евклидово расстояние между двумя точками - векторами"""
    result = 0
    for i in range(len(vector1)):
        result += math.pow(vector1[i] - vector2[i], 2)
    return math.sqrt(result)


data = [[1, 1],[1, 3], [5, 1], [5, 2]]


labels = k_means(x, 3, 12)

df['cluster'] = labels

зкште(df.groupby('cluster').mean())
