# python-docker
basic python docker image

## Getting Started

### Setup environment
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

```
python3 -m flask run
curl 127.0.0.1:5000
```

```
docker build --tag cloudacode/python-docker .
docker run --publish 8080:5000 cloudacode/python-docker
```
