from cmath import cos, sqrt
import random
import math
import numpy as np
import matplotlib.pyplot as plt

def dibujarCentroides(numCentroides, radio, limite, puntosPorCentroide):
    centroides = []
    puntosCentroides = []

    while len(centroides) != numCentroides:
        x = random.randint(0, limite)
        y = random.randint(0, limite)
        tupla = ()
        if len(centroides) != 0:
            tupla = centroides[len(centroides)-1]
            distancia = math.dist(tupla, (x,y))
            if distancia < radio:
                asd = 55
        
        if len(centroides) == 0 and x > radio and y > radio and x < limite-radio and y < limite-radio:
            centroides.append((x, y))            
        elif len(centroides) != 0 and math.dist(tupla, (x,y)) > radio and x > radio and y > radio and x < limite-radio and y < limite-radio:
            centroides.append((x, y))
        else:
            continue

    area = math.pi * radio**2
    for i in range(numCentroides):
        for j in range(puntosPorCentroide):
            anguloRandom = random.uniform(0, 2*math.pi)
            radioRandom = sqrt(random.uniform(0, area/math.pi))
            x_ = centroides[i-1][0] + radioRandom * math.cos(anguloRandom)
            y_ = centroides[i-1][1] + radioRandom * math.sin(anguloRandom)
            puntosCentroides.append((x_,y_))


    x_val = [x[0] for x in puntosCentroides]
    y_val = [x[1] for x in puntosCentroides]

    plt.scatter(x_val,y_val)
    plt.show()

    return puntosCentroides

def KMedias(chart, numCentroides):
        # initialize cluster centroids
    centroids = random.sample(chart, numCentroides)
    totalCentroids = []
    totalCentroids.append(centroids)

    # initialize cluster assignments
    clusters = [0] * len(chart)

    while True:
        # calculate distances to centroids
        for i, point in enumerate(chart):
            distances = [((point[0] - centroid[0]) ** 2 + (point[1] - centroid[1]) ** 2)**0.5 for centroid in centroids]
            real_parts=[ complex(x).real for x in distances]
            clusters[i] = real_parts.index(min(real_parts))

        # calculate new centroids
        new_centroids = [[0, 0] for _ in range(numCentroides)]
        counts = [0] * numCentroides
        for i, point in enumerate(chart):
            cluster = clusters[i]
            new_centroids[cluster][0] += point[0]
            new_centroids[cluster][1] += point[1]
            counts[cluster] += 1

        for i in range(numCentroides):
            new_centroids[i][0] /= counts[i]
            new_centroids[i][1] /= counts[i]

        # check if convergence has been reached
        totalCentroids.append(new_centroids)
        if new_centroids == centroids:
            break
        else:
            centroids = new_centroids


    # plot the clusters
    colors = ["r", "g", "b", "y", "c", "m"]
    for i, point in enumerate(chart):
        plt.scatter(point[0], point[1], c=colors[clusters[i]])

    # plot the centroids
    for i, Centroids_ in enumerate(totalCentroids):
        for centroid in Centroids_:
            plt.scatter(centroid[0], centroid[1], c="c")

    # plot the centroids
    for centroid in centroids:
        plt.scatter(centroid[0], centroid[1], c="black", marker="x")

    plt.show()  
    #plot_centroid(2, 100, 100)

chart = dibujarCentroides(3, 60, 500, 20)
KMedias(chart, 3)
