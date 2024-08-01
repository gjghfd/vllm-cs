# How to Use

## Online (Alibaba FC GPU)

1. Login to Alibaba docker hub.

```
docker login --username=gjghfd_lch@test.aliyunid.com registry.cn-shenzhen.aliyuncs.com
```

2. Build image.

```
cd vllm-cs
DOCKER_BUILDKIT=1 docker build . --target vllm-openai --tag registry.cn-shenzhen.aliyuncs.com/vllm-cs/modelscope-vllm:v1
[For Mac OS] DOCKER_BUILDKIT=1 docker buildx build . --platform=linux/amd64 --target vllm-openai --tag registry.cn-shenzhen.aliyuncs.com/vllm-cs/modelscope-vllm:v1
docker push registry.cn-shenzhen.aliyuncs.com/vllm-cs/modelscope-vllm:v1
```

Or you can choose to build image incrementally in case that you only updated python codes or main.cc.

```
cd vllm-cs
docker build . --tag registry.cn-shenzhen.aliyuncs.com/vllm-cs/modelscope-vllm:v1 -f Dockerfile_inc
[For Mac OS] docker buildx build . --platform=linux/amd64 --tag registry.cn-shenzhen.aliyuncs.com/vllm-cs/modelscope-vllm:v1 -f Dockerfile_inc
docker push registry.cn-shenzhen.aliyuncs.com/vllm-cs/modelscope-vllm:v1
```

1. Use serverless devs to deploy the application
```
cd serverlessdevs/start-modelscope-v3
s deploy -y
```

<!-- ## Publish Application Template (Alibaba FC GPU)

1. Push images.

You should have built images in step 2 in the last section.

```
cd vllm-cs/serverless-devs/registry_script
bash run.sh [password for aliyun dockerhub registry]
```

2. Publish template.

```
cd serverlessdevs/modelscope-app
s registry login
s registry publish
# In another directory
s init modelscope-coldstart
``` -->
