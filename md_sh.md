![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![coverage](coverage.svg)
![pipeline status](https://gitlab.com/ORG/REPO/badges/main/pipeline.svg)



### Other

1. To generate a secure random secret key use the command: `openssl rand -hex 256`
2. add execute permission to a file: `sudo chmod +x ./file.sh`
3. encode .env secrets file: `base64 -w 0 .env > .env.b64`
4. decode .env secrets file: `echo ${CD_SECRETS} | base64 -d > .env`


#### black
```shell
black .
```

#### requirements
```shell
pip install -U pip setuptools wheel pip-tools --timeout 60
pip-compile --upgrade requirements.in -o requirements.txt
pip-compile --upgrade requirements_dev.in -o requirements_dev.txt -c requirements.txt
pip-sync requirements.txt requirements_dev.txt --pip-args "--retries 10 --timeout 60"
```

#### generate random key
```shell
openssl rand -hex 32
```

#### 
```shell

```
