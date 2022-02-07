# Visibility Graph Using the Rotational Plane Sweep Algorithm

The present code is an implementation of the rotational Plane Sweep (RPS) algorithm for building a visibility graph from polygon obstacles. the main constratins for this implementation is that the obstacles **must** be represented as polygons. Each vertex that defines the polygon or polygons is defined in an `env_X.csv` file where **X** is the environment number.

The code implementation has a CLI to execute it as follows.

`python main.py environments/env_X.csv`  where X is the environment number. Some execution examples are using the following commands. The code shows the environment displayed where the blue lines represent the visibility. The code prints the list of non-repeated edges that represent the visbility graph and how many of them are. Finally, the implementation writes a `.csv` file that stores all the visibility edges for further use in the A* path planning algorithm.


### Simple Three Vertices Polygon Obstacle

`python main.py environments/env_0.csv`

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=18E03g6sD7lafWBBzx8l-4Ye4WhxfeQAU" width="300" height="300" />
</p>

```
Printing  8  visibility edges...
[(0, 1), (0, 3), (1, 3), (1, 2), (1, 4), (2, 3), (2, 4), (3, 4)]
```



### Environment With Multiple Polygon Obstacles

`python main.py environments/env_10.csv`

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1lyCQ1rlZ2GkbGrtmWQQWSLGjtTBKPsx9" width="400" height="300" />
</p>

```
Printing  93  visibility edges...
[(0, 16), (0, 6), (0, 7), (0, 8), (0, 4), (0, 3), (0, 1), (0, 19), (0, 14), (0, 9), (0, 10), (0, 15), (1, 4), (1, 3), (1, 2), (1, 19), (1, 13), (1, 14), (1, 9), (1, 10), (1, 15), (1, 16), (1, 6), (1, 8), (2, 4), (2, 19), (2, 3), (3, 4), (3, 19), (3, 13), (3, 14), (3, 9), (3, 10), (3, 15), (3, 16), (3, 6), (3, 8), (4, 19), (4, 13), (4, 14), (4, 9), (4, 10), (4, 8), (4, 5), (5, 6), (5, 16), (6, 7), (6, 8), (6, 19), (6, 14), (6, 9), (6, 10), (6, 12), (6, 15), (6, 16), (7, 8), (7, 19), (7, 14), (7, 9), (7, 10), (7, 15), (8, 19), (8, 14), (8, 9), (8, 10), (8, 15), (8, 16), (9, 16), (9, 19), (9, 14), (9, 10), (9, 18), (9, 15), (10, 15), (10, 16), (10, 11), (10, 12), (10, 18), (11, 18), (11, 15), (11, 16), (11, 12), (12, 18), (12, 15), (12, 13), (12, 19), (13, 14), (13, 19), (14, 19), (15, 16), (15, 18), (16, 17), (17, 18)]
```


