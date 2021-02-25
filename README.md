# Cartography Queries

This is the companion repo for the "[Continuous Visibility into Ephemeral Cloud Environments](https://www.marcolancini.it/continuous-cloud-visibility/)" series.

## Custom Queries

The file `queries/queries.json` contains a set of custom queries specifically created for analyzing data collected by Cartography, and is structured as a list of dictionaries,
where each dictionary represents an annotated query (enriched with metadata).

```json
[
    {
        "name": "ec2_list",
        "tags": [
            "inventory",
            "cloud",
            "aws",
            "list"
        ],
        "description": "List of EC2 instances by AWSAccount",
        "query": "MATCH (a:AWSAccount)-[:RESOURCE]->(instance:EC2Instance) RETURN ",
        "return": "a.name, a.id, instance.instanceid, instance.state, instance.exposed_internet, instance.launchtime, instance.region ORDER BY a.name, instance.state, instance.exposed_internet",
        "result_headers": [
            "account_name",
            "account_id",
            "instance_id",
            "state",
            "internet_exposed",
            "launchtime",
            "region"
        ]
    },
    ...
]
```

As shown in the snippet above, each query has the following fields:

- `name`: the short name for the query
- `tags`: for ease of filtering. Usually it contains:
  - the source to target (e.g., `aws`, `gcp`, `k8s`)
  - any kind of query (e.g., `security`, `inventory`, `networking`)
  - any subtype (`misconfig`, `anomaly`, `drift`, `list`) that can assist in further filtering the queries
- `description`: a human readable description of the query
- `query`: the actual Cypher query that is going to be run against Neo4j
  - ⚠️ it is important that both AWSAccounts and GCPProjects are assigned to a variable called `a`
- `return`: the fields to select from the query
- `result_headers`: human readable list of the fields that are going to be returned by `query`

## Query Manager

The query manager (`queries/query_manager.py`) script is a quick command line option for inspecting/filtering Cartography queries (without actually running them).
For simplicity, you can also directly use the [related Docker image](https://github.com/users/marco-lancini/packages/container/package/cartography_queries) created with this `Dockerfile`:

| Command                                                                                | Action                                                               |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `docker run --rm ghcr.io/marco-lancini/cartography_queries:latest --count`             | Count all available queries                                          |
| `docker run --rm ghcr.io/marco-lancini/cartography_queries:latest --get-all-tags`      | List all available tags                                              |
| `docker run --rm ghcr.io/marco-lancini/cartography_queries:latest --tags=aws,security` | List queries filtered by tags (`aws` and `security` in this example) |

## Consumers

#### Elasticsearch

The `consumers/elasticsearch` folder contains all the code needed to get you started with integrating Elasticsearch with Cartography data.

For more information, please refer to the [README.md](https://github.com/marco-lancini/cartography-queries/blob/master/consumers/elasticsearch/README.md) file in that folder, and the "[Tracking Moving Clouds: How to continuously track cloud assets with Cartography](https://www.marcolancini.it/2020/blog-tracking-moving-clouds-with-cartography)" blog post.

#### Jupyter Notebooks

The `consumers/jupyter_notebooks` folder contains all the code needed to get you started with your own Jupyter reports for analysing Cartography data.

See the [README.md](https://github.com/marco-lancini/cartography-queries/blob/master/consumers/jupyter_notebooks/README.md) file in that folder for more information on the available notebooks.

For detailed instructions on how to set them up, please refer to section "[Repeatability: Jupyter Notebooks](https://www.marcolancini.it/2020/blog-mapping-moving-clouds-with-cartography/#repeatability-jupyter-notebooks)" of the "[Mapping Moving Clouds: how to stay on top of your ephemeral environments with Cartography](https://www.marcolancini.it/2020/blog-mapping-moving-clouds-with-cartography)" blog post.
