# How to Use

## Online (Alibaba FC GPU)

1. Login to Alibaba docker hub.

```
docker login --username=gjghfd_lch@test.aliyunid.com registry.cn-shanghai.aliyuncs.com
```

2. Build image.

```
cd vllm-cs
docker build . --target vllm-openai --tag registry.cn-shanghai.aliyuncs.com/vllm-cs/modelscope-vllm:v1
[For Mac OS] docker buildx build . --platform=linux/amd64 --target vllm-openai --tag registry.cn-shanghai.aliyuncs.com/vllm-cs/modelscope-vllm:v1
docker push registry.cn-shanghai.aliyuncs.com/vllm-cs/modelscope-vllm:v1
```

3. Use serverless devs to deploy the application
```
cd serverlessdevs/start-modelscope-v3
s deploy -y
```

<!-- ## Publish Application Template (Alibaba FC GPU)

1. Push images.

You should have built images in step 2 in the last section.

```
cd my_scripts/registry_script
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
