[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/gmvPxYB2)

# Big Data Processing

## Team

Yaokang Wu - yaokangw@andrew.cmu.edu

Qiuyang Zhang - qiuyangz@andrew.cmu.edu


## Deployment

1. Add Google Cloud Platform credentials json file in `terraform.json`.

2. Execute the following command:

    ```bash
    $ terraform init
    $ terraform apply
    ```

3. After the terraform finished, navigate to the frontend ip address with corresponding port and you are good to go.

    For the Jenkins application, after Sonarqube server is started,

    ![imgs/sonarqube_starting.jpg](imgs/sonarqube_starting.jpg)

    go to the dashboard and run the pre-configured [DummyProject](https://github.com/Hallimede/dummy-project) job.

    ![imgs/jenkins_dashboard.jpg](imgs/jenkins_dashboard.jpg)

    ![imgs/jenkins_build.jpg](imgs/jenkins_build.jpg)

    Then you can see both the successful build in Jenkins and result report in Sonarqube. 


# Microservices

The architecture for this application is like the following diagram:

![imgs/diagram.jpg](imgs/diagram.jpg)

1. Frontend App

   - Docker hub image: https://hub.docker.com/repository/docker/yaokangw/data-app

   - Dockerfile: [app/Dockerfile](app/Dockerfile)

   - Command to run it:
        ```bash
        $ docker run --name data-app -d -p 5000:5000 yaokangw/data-app
        ```

   - Kubernetes Deployment file: [scripts/frontend-deployment.yaml](scripts/frontend-deployment.yaml)

   - Kubernetes Service file: [scripts/frontend-lb.yaml](scripts/frontend-lb.yaml)

   - Screenshot:

        ![Web App Screenshot](imgs/webapp.jpg)

2. Jupyter Notebook

   - Docker hub image: https://hub.docker.com/repository/docker/yaokangw/jupyter

   - Dockerfile: [jupyter/Dockerfile](jupyter/Dockerfile)

   - Command to run it:
        ```bash
        $ docker run --name jupyter -d -p 8888:8888 yaokangw/jupyter-notebook
        ```

   - Kubernetes Deployment file: [scripts/jupyter-deployment.yaml](scripts/jupyter-deployment.yaml)

   - Kubernetes Service file: [scripts/jupyter-lb.yaml](scripts/jupyter-lb.yaml)

   - Screenshot:

        ![imgs/jupyter_notebook.jpg](imgs/jupyter_notebook.jpg)


3. SonarQube

   - Docker hub image: https://hub.docker.com/r/yaokangw/sonarqube

   - Dockerfile: [sonarqube/Dockerfile](sonarqube/Dockerfile)

   - Command to run it:
        ```bash
        $ docker run -d --name sonarqube -e SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true -p 9000:9000 sonarqube:latest
        ```

   - Kubernetes Deployment file: [scripts/sonarqube-deployment.yaml](scripts/sonarqube-deployment.yaml)

   - Kubernetes Service file: [scripts/sonarqube-deployment.yaml](scripts/sonarqube-deployment.yaml)

   - Screenshot:

        ![imgs/sonarqube.jpg](imgs/sonarqube.jpg)

4. Jenkins

   - Docker hub image: https://hub.docker.com/r/yaokangw/jenkins

   - Dockerfile: [jenkins/Dockerfile](jenkins/Dockerfile)

   - Command to run it:
        ```bash
        $ docker run -d -p 8080:8080 -p 50000:50000 yaokangw/jenkins:sonar /usr/local/bin/jenkins.sh
        ```

   - Kubernetes Deployment file: [scripts/jenkins-deployment.yaml](scripts/jenkins-deployment.yaml)

   - Kubernetes Service file: [scripts/jenkins-lb.yaml](scripts/jenkins-lb.yaml)

   - Screenshot:

        ![Jenkins Screenshot](imgs/jenkins.jpg)


To be modified

5. Hadoop

    [Hadoop base image](https://hub.docker.com/layers/apache/hadoop/3/images/sha256-af361b20bec0dfb13f03279328572ba764926e918c4fe716e197b8be2b08e37f?context=explore)

    [Hadoop custom image](https://hub.docker.com/layers/qiuyangz/myhadoop/latest/images/sha256-af361b20bec0dfb13f03279328572ba764926e918c4fe716e197b8be2b08e37f?context=repo)
    
    - Kubernetes hadoop namenode Deployment file: [scripts/namenode-deployment.yaml](scripts/namenode-deployment.yaml)

    - Kubernetes hadoop datanode1 Deployment file: [scripts/datanode1-deployment.yaml](scripts/datanode1-deployment.yaml)

    - Kubernetes hadoop datanode2 Deployment file: [scripts/datanode2-deployment.yaml](scripts/datanode2-deployment.yaml)

    - Kubernetes hadoop resourcemanager Deployment file: [scripts/resourcemanager-deployment.yaml](scripts/resourcemanager-deployment.yaml)

    - Kubernetes hadoop namenode Service file: [scripts/namenode-service.yaml](scripts/namenode-service.yaml)

    - Screenshot: 
        ![Hadoop Screenshot](imgs/hadoop.jpg)

6. Spark

    [Spark base image](https://hub.docker.com/layers/apache/spark/latest/images/sha256-a4a48089219912a8a87d7928541d576df00fc8d95f18a1509624e32b0e5c97d7?context=explore)


    [Spark custom image](https://hub.docker.com/layers/qiuyangz/spark/latest/images/sha256-3809b9a329db6b13278661155941c7aad31e7d94abd39692d9cd1f562ded3043?context=repo)

    - Kubernetes spark master Deployment file: [scripts/spark-deployment.yaml](scripts/spark-deployment.yaml)

    - Kubernetes spark worker Deployment file: [scripts/spark-worker-deployment.yaml](scripts/spark-worker-deployment.yaml)

    - Kubernetes spark Service file: [scripts/spark-service.yaml](scripts/spark-service.yaml)

    - Screenshot:
        ![Spark Screenshot](imgs/spark.jpg)




# Reference


- Jenkins

    - Jenkins Configuration as Code Plugin Documentation [(Link)](https://github.com/jenkinsci/configuration-as-code-plugin/tree/master)

    - Configure sonar plugin in jenkins - Github [(Link)](https://github.com/jenkinsci/configuration-as-code-plugin/blob/master/demos/sonarqube/README.md)

    - Setting up Dockerized Jenkins and SonarQube in Linux Environment - Medium [(Link)](https://faun.pub/setting-up-dockerized-jenkins-and-sonarqube-in-linux-environment-155ce52b884a)

    - Disable Access Control - Jenkins [(Link)](https://www.jenkins.io/doc/book/security/access-control/disable/)

    - Option 1 Sample Solution Jenkins Dockerfile - Sankalp, Kishan [(Link)](https://github.com/Cloud-Infrastructure-Fall-2023/option-1-sample-solution/blob/main/jenkins-sonarqube-sonarscanner/Dockerfile)

- Sonarqube

    - Installing SonarQube from the Docker image - SonarQube [(Link)](https://docs.sonarsource.com/sonarqube/latest/setup-and-upgrade/install-the-server/)

    - Allow anonymous authentication on SonarQube 8.6 - StackOverflow [(Link)](https://stackoverflow.com/questions/65270209/allow-anonymous-authentication-on-sonarqube-8-6)

    - SonarQube with Jenkins Setup using Docker Images - FunnelGarden [(Link)](https://funnelgarden.com/sonarqube-jenkins-docker/)


- Hadoop
    - Namenode format issue - StackOverflow [(Link)](https://stackoverflow.com/questions/61694471/hdfs-namenode-format-issue-with-aws-ebs-in-eks-cluster)

    - Multi-attach error for pvc volume - StackOverflow [(Link)](https://stackoverflow.com/questions/70945223/kubernetes-multi-attach-error-for-volume-pvc-volume-is-already-exclusively-att)

    - How to create a storageclass that allows ReadWriteMany -- nfs filestore - StackOverflow [(Link)](https://stackoverflow.com/questions/54796639/how-do-i-create-a-persistent-volume-claim-with-readwritemany-in-gke)

    - Persistent Volume - Kubernetes [(Link)](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)


- Spark
    