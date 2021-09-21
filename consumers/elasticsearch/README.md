# Consumer: Elasticsearch

The Elasticsearch Consumer is a cronjob which executes
all the queries defined in the `queries` folder against the Neo4j database,
and pushes the results to Elasticsearch.

This folder is composed as follows:

| Subfolder                            | Description                                                                                            |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| [deployment](deployment)             | Contains Kubernetes manifests for the CronJob                                                          |
| [docker](docker)                     | Contains Dockerfile and python code for the custom Elasticsearch Ingestor                              |
| [elastalert_rules](elastalert_rules) | Contains the source code (as yaml) of the Elastalert rules defined to trigger on occurrences of drift  |
| [kibana](kibana)                     | Contains an export of all the Kibana visualizations and dashboards used to visualize Cartography data  |
| [transforms](transforms)             | Contains the source code (as json) of the Elastic Transforms powering the drift detection capabilities |

For more information, please refer to the "[Tracking Moving Clouds: How to continuously track cloud assets with Cartography](https://www.marcolancini.it/2020/blog-tracking-moving-clouds-with-cartography)" blog post.

A sample automated deployment of the Elasticsearch Consumer is
also available as part of [k8s-lab-plz](https://github.com/marco-lancini/k8s-lab-plz): [Elasticsearch Ingestor](https://github.com/marco-lancini/k8s-lab-plz/tree/main/components/cartography#elasticsearch-ingestor).
