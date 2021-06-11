## Install
(scripts assume python `v3`, which can be either `python` or `python3` on your machine)

#### Create and activate virtual environment
```sh
python3 -m venv venv # create virtual environment at ./venv
source ./bin/venv/active # activate virtual environment
```

#### Install dependencies
```sh
pip install -r requirements.txt
```

#### Configure environment variables
```sh
cp ./.env.example ./.env
```
Fill necessary values in `.env` file


## Run locally

```sh
uvicorn app.main:app --reload
```

## Deploy

```sh
export $(cat .env | xargs) && ./deploy.sh
```
