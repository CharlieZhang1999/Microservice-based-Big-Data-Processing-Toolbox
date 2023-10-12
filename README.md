[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/gmvPxYB2)


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

## Run app on Docker


```bash
docker build -t yaokangw/data-app .
docker run --name data-app -p 5000:5000 -d yaokangw/data-app
```