# Cartography Queries

This is the companion repo for the [Mapping Moving Clouds: how to stay on top of your ephemeral environments with Cartography](https://www.marcolancini.it/2020/blog-mapping-moving-clouds-with-cartography) blog post.


## Custom Queries
The file `queries/queries.json` contains a set of custom queries specifically created for analyzing data collected by Cartography, and is structured as a list of dictionaries,
where each dictionary represents an annotated query (enriched with metadata).


## Query Manager
The query manager (`queries/query_manager.py`) script is a quick command line option for inspecting/filtering Cartography queries (without actually running them).
For simplicity, you can also directly use the [related Docker image](https://hub.docker.com/r/marcolancini/cartography_queries) created with this `Dockerfile`:

| Command                                                                       | Action                                                               |
| ----------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `docker run --rm marcolancini/cartography_queries:latest --count`             | Count all available queries                                          |
| `docker run --rm marcolancini/cartography_queries:latest --get-all-tags`      | List all available tags                                              |
| `docker run --rm marcolancini/cartography_queries:latest --tags=aws,security` | List queries filtered by tags (`aws` and `security` in this example) |


## Consumers

#### Jupyter Notebooks

The `consumers/jupyter_notebooks` folder contains all the code needed to get you started with your own Jupyter reports for analysing Cartography data.
For detailed instructions on how to set them up, please refer to section "[Repeatability: Jupyter Notebooks](https://www.marcolancini.it/2020/blog-mapping-moving-clouds-with-cartography/#repeatability-jupyter-notebooks)" of the companion blog post.
