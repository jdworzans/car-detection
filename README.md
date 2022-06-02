# Run locally
It requires `docker-compose`. To install `docker` and `docker-compose` see https://docs.docker.com/get-docker/.

Prepare `web/.env` file (according to `web/.env.example`).
Run using
```
docker-compose up
```

Upload to `torchseve` model with name matching `$PREDICTION_ADRESS`.
As an example, you can use pretrained FastRCNN
```
curl -X POST  "http://localhost:8081/models?url=https://torchserve.pytorch.org/mar_files/fastrcnn.mar&initial_workers=1"
```
You can explore pretrained models from [TorchServe Model ZOO](https://pytorch.org/serve/model_zoo.html)
or export `.mar` file from selected model according to
[TorchServe docs](https://pytorch.org/serve/index.html).

# Run on Kubernetes
`deployment.yml` and `service.yml` files are prepared
for development within GKE (Google Kubernetes Engine).
Created pods need secrets, which you can add using `.env` file based on `.env.example`.
Remember to set `$DJANGO_ALLOWED_HOST`.

Continue as in local run by adding model for object detection.
