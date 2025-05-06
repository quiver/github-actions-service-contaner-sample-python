# github-actions-service-contaner-sample-python

This repository demonstrates how to use PostgreSQL as a service container in GitHub Actions workflows and connect to it from Python code. It includes examples of two different approaches:

1. [Running jobs directly on the runner machine](.github/workflows/job-on-runner.yml) and connecting to PostgreSQL via port mapping
2. [Running jobs inside a container](.github/workflows/job-on-container.yml) and connecting to PostgreSQL through Docker's internal networking

The sample code shows how to set up service containers, configure network connections, and execute simple Python scripts to verify the PostgreSQL connection.

For detailed explanation, [check out the blog post](https://dev.classmethod.jp/articles/github-actions-service-contaner-postgres-from-python/).
