passwd=$1

while read line
do
    echo "Start pushing to region $line..."

    docker login --username=xiliu@1767215449378635 "registry.$line.aliyuncs.com" --password "$passwd"

    docker tag registry.cn-shenzhen.aliyuncs.com/vllm-cs/modelscope-vllm:v1 "registry.$line.aliyuncs.com/aliyun-fc/fc-modelscope-vllm:v1"
    docker push "registry.$line.aliyuncs.com/aliyun-fc/fc-modelscope-vllm:v1"

    echo "Everything done in region $line!"
done < regions.txt