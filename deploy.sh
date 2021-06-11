# This script can be run as
# `export $(cat .env | xargs) && ./deploy.sh`
# to activate environment variables from .env file

docker build -t $DOCKER_IMAGE_NAME .

docker push $DOCKER_IMAGE_NAME

gcloud --project $GCLOUD_PROJECT_NAME \
  run deploy $GCLOUD_SERVICE_NAME \
  --image $DOCKER_IMAGE_NAME \
  --allow-unauthenticated \
  --platform managed \
  --quiet \
  --region us-east1 \
  --port 80 \
  --format "value(status.url)"



