# Cartography Queries

This is the companion repo for the "[Continuous Visibility into Ephemeral Cloud Environments](https://www.marcolancini.it/continuous-cloud-visibility/)" series.

## Custom Queries

The file `queries/queries.json` contains a set of custom queries specifically created for analysing data collected by Cartography, and is structured as a list of dictionaries, where each dictionary represents an annotated query (enriched with metadata).


## Consumers

### Elasticsearch

The [consumers/elasticsearch](consumers/elasticsearch/) folder contains all the code needed to get you started with integrating Elasticsearch with Cartography data.

For more information, please refer to the [README.md](consumers/elasticsearch/README.md) file in that folder, and the "[Tracking Moving Clouds: How to continuously track cloud assets with Cartography](https://www.marcolancini.it/2020/blog-tracking-moving-clouds-with-cartography)" blog post.

### Jupyter Notebooks

The [consumers/jupyter_notebooks](consumers/jupyter_notebooks/) folder contains all the code needed to get you started with your own Jupyter reports for analysing Cartography data.

For more information, please refer to the [README.md](consumers/jupyter_notebooks/README.md) file in that folder, and the "[Repeatability: Jupyter Notebooks](https://www.marcolancini.it/2020/blog-mapping-moving-clouds-with-cartography/#repeatability-jupyter-notebooks)" section of the "[Mapping Moving Clouds: how to stay on top of your ephemeral environments with Cartography](https://www.marcolancini.it/2020/blog-mapping-moving-clouds-with-cartography)" blog post.


## Deployment on Kubernetes

I've now described an automated process to get Neo4J and Cartography up and running in a Kubernetes cluster at: [Automating Cartography Deployments on Kubernetes](https://www.marcolancini.it/2021/blog-cartography-on-kubernetes/).



## References
* **[CODE]** [Cartography's source code](https://github.com/lyft/cartography)
* **[CODE]** [Cartography Deployment on Kubernetes](https://github.com/marco-lancini/k8s-lab-plz/tree/master/components/cartography)
* **[CODE]** [Terraform AWS Security Reviewer](https://github.com/marco-lancini/utils/tree/main/terraform/aws-security-reviewer)
* **[BLOG]** [Mapping Moving Clouds: How to stay on top of your ephemeral environments with Cartography](https://www.marcolancini.it/2020/blog-mapping-moving-clouds-with-cartography/)
* **[BLOG]** [Tracking Moving Clouds: How to continuously track cloud assets with Cartography](https://www.marcolancini.it/2020/blog-tracking-moving-clouds-with-cartography/)
* **[BLOG]** [Automating Cartography Deployments on Kubernetes](https://www.marcolancini.it/2021/blog-cartography-on-kubernetes/)
* **[BLOG]** [Cross Account Auditing in AWS and GCP](https://www.marcolancini.it/2019/blog-cross-account-auditing/)
* **[BLOG]** [Kubernetes Lab on Baremetal](https://www.marcolancini.it/2021/blog-kubernetes-lab-baremetal/)
* **[TALK]** [Cartography: using graphs to improve and scale security decision-making](https://speakerdeck.com/marcolancini/cartography-using-graphs-to-improve-and-scale-security-decision-making)
