# Elasticsearch Consumer

The Elasticsearch Consumer is a cronjob which executes (daily) all the queries defined in the `queries` folder against the Neo4j database, and pushes the results to Elasticsearch.

This folder is composed as follows:

| Subfolder          | Description                                                                                            |
| ------------------ | ------------------------------------------------------------------------------------------------------ |
| `deployment`       | Contains Kubernetes manifests and python code for the custom Elasticsearch Ingestor                    |
| `elastalert_rules` | Contains the source code (as yaml) of the Elastalert rules defined to trigger on occurrences of drift  |
| `kibana`           | Contains an export of all the Kibana visualizations and dashboards used to visualize Cartography data  |
| `transforms`       | Contains the source code (as json) of the Elastic Transforms powering the drift detection capabilities |

For more information, please refer to the "[Tracking Moving Clouds: How to continuously track cloud assets with Cartography](https://www.marcolancini.it/2020/blog-tracking-moving-clouds-with-cartography)" blog post.
