[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/gmvPxYB2)


Yaokang Wu - yaokangw@andrew.cmu.edu

Qiuyang Zhang - qiuyangz@andrew.cmu.edu

# Web Application

## Run app locally

```bash
cd app
python -m venv venv
source venv/bin/activate
pip install -r requirements.tx
```

```bash
python app.py
```

[Web App image](https://hub.docker.com/r/yaokangw/data-app)

![Web App Screenshot](imgs/webapp.jpg)

## Run app on Docker


```bash
docker build -t yaokangw/data-app .
docker run --name data-app -p 5000:5000 -d yaokangw/data-app
```

# Images

## SonarQube

[SonarQube image](https://hub.docker.com/_/sonarqube)

[SonarQube documentation](https://docs.sonarsource.com/sonarqube/latest/setup-and-upgrade/install-the-server/)

```bash
docker run -d --name sonarqube -e SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true -p 9000:9000 sonarqube:latest
```

## SonarScanner

[SonarScanner image](https://hub.docker.com/r/sonarsource/sonar-scanner-cli)

[SonarScanner documentation](https://docs.sonarsource.com/sonarqube/latest/analyzing-source-code/scanners/sonarscanner/)

```bash
docker run  --rm --network=host -e SONAR_HOST_URL="http://127.0.0.1:9000" -e SONAR_SCANNER_OPTS="-Dsonar.projectKey=dummy" -e SONAR_TOKEN="squ_3d972dd73f4e3a7abf386ae9eda5c70ee05b683a" -v "https://github.com/Hallimede/dummy-project" sonarsource/sonar-scanner-cli
```

![SonarQube Screenshot](imgs/sonarqube.jpg)

## Jupyter

[Jupyter base image](https://hub.docker.com/r/jupyter/base-notebook)

[Jupyter custom image](https://hub.docker.com/repository/docker/yaokangw/jupyter-notebook/general)

[Jupyter documentation](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html)

```
docker run --name jupyter -d -p 8888:8888 yaokangw/jupyter-notebook
```

![Jupyter Notebook Screenshot](imgs/jupyternotebook.jpg)