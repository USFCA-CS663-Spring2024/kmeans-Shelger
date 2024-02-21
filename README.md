# KMeans

Assignment 2 - CS 663 - Machine Learning

In addition to this README.md file, this repository contains two (2) files:
* `Assignment 2 - Clustering.ipynb`: which is a notebook for you to start your implementation of this assignment
* `cluster.py`: which can be the superclass for your implementation of KMeans

You may make any changes you like to the notebook. Find assignment details as well as links to the required data on Canvas.

I didn't do the optional part, so the KMeans.py file only contains the code of first question.
I posted the answers of question 2 below:


For Taxi Dataset:


Choose and run clustering algorithms:<br>
Taxi Dataset:<br>
1. The reason why you chose the clustering algorithm(s)<br>
    The dataset of pickup and dropoff haven't many outliers. The scatter plot shows the dataset is suitable for kmeans.
2. Any pre-processing of the data or any hyperparameter settings<br>
    Considering pickup and dropoff position can be used for different situations, I separated them into pickup_data and dropoff_data, and removed rows with NaN values.
    I used Elbow method to get the k, which was 5.
3. Output from the algorithm(s) -- show what clusters were generated<br>
    The visulization graph is below.
4. The metrics you used to evaluate the output. What kind of performance did you get from
that algorithm? Is that what you expected?<br>
    I used Silhouette Score, which should be between -1 to 1. The result of pickup_data is 0.70, and 0.61 for dropoff_data. They are not perfectly ideal result, but good enough for a well defined clusters.


For Route Dataset:<br>
Choose and run clustering algorithms:<br>
Mopsi Dataset:<br>
1. The reason why you chose the clustering algorithm(s)<br>
    The outliers seems influencing the performance of kmeans, so I decide to use DBSCAN at first.
    The elbow method seems not working, so I changed the algorithm to kmeans.
2. Any pre-processing of the data or any hyperparameter settings<br>
    Using elbow method to calculate k.
3. Output from the algorithm(s) -- show what clusters were generated<br>
    The visulization graph is below.
4. The metrics you used to evaluate the output. What kind of performance did you get from
that algorithm? Is that what you expected?<br>
    I used Silhouette Score, which should be between -1 to 1. The result of data is 0.8, much better than pickup_data. It is a good sign for the performance of kmeans. There exists outliers, but they didn't influence the performance of Kmeans very much, perhaps the density of outliers were not high.

