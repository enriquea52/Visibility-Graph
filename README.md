# Visibility Graph Using the Rotational Plane Sweep Algorithm

The present code is an implementation of the rotational Plane Sweep (RPS) algorithm for building a visibility graph from polygon obstacles. the main constratins for this implementation is that the obstacles **must** be represented as polygons. Each vertex that defines the polygon or polygons is defined in an `env_X.csv` file where **X** is the environment number.

The code implementation has a CLI to execute it as follows.

`python main.py environments/env_X.csv`  where X is the environment number. Some execution examples are using the following commands. The code shows the environment displayed where the blue lines represent the visibility. It also prints the list of non-repeated edges that represent the visbility graph.


### Simple Three Vertices Polygon Obstacle

`python main.py environments/env_0.csv`

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=18E03g6sD7lafWBBzx8l-4Ye4WhxfeQAU" width="300" height="300" />
</p>



### Environment With Multiple Polygon Obstacles

`python main.py environments/env_10.csv`

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1lyCQ1rlZ2GkbGrtmWQQWSLGjtTBKPsx9" width="400" height="300" />
</p>



