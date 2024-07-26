
> 注：当前项目为 Serverless Devs 应用，由于应用中会存在需要初始化才可运行的变量（例如应用部署地区、服务名、函数名等等），所以**不推荐**直接 Clone 本仓库到本地进行部署或直接复制 s.yaml 使用，**强烈推荐**通过 `s init ` 的方法或应用中心进行初始化，详情可参考[部署 & 体验](#部署--体验) 。

# modelscope-vllm 帮助文档

<description>

ModelScope大模型 + vLLM的快速启动版本(fc3.0)

</description>

## 前期准备

使用该项目，您需要有开通以下服务：

<service>

| 服务 |  备注  |
| --- |  --- |
| 函数计算 FC |  下载并加载模型 |
| 文件存储 NAS |  存储模型，加快模型启动速度 |

</service>

推荐您拥有以下的产品权限 / 策略：
<auth>


| 服务/业务 |  权限 |  备注  |
| --- |  --- |   --- |
| 函数计算 | AliyunFCFullAccess |  需要创建函数资源，通过函数下载及加载模型 |
| NAS | AliyunNASFullAccess |  先将模型从公网下载到NAS，应用启动时加载NAS上的模型使用 |
| VPC | AliyunVPCFullAccess |  使用NAS需要同时使用VPC |

</auth>

<remark>



</remark>

<disclaimers>

免责声明：   
本项目会自动创建若干NAS实例并将模型下载到NAS，然后使用函数计算的GPU实例，模型的大小会影响文件存储占用以及函数执行时间，需根据情况具验证模型下载及加载所产生的费用。

</disclaimers>

## 部署 & 体验


<deploy>
    
- 通过 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署：
  - [安装 Serverless Devs Cli 开发者工具](https://www.serverless-devs.com/serverless-devs/install) ，并进行[授权信息配置](https://docs.serverless-devs.com/fc/config) ；
  - 初始化项目：`s init modelscope-vllm -d modelscope-vllm `
  - 进入项目，并进行项目部署：`cd modelscope-vllm && s deploy - y`
  - 初次部署时函数会将模型从公网下载至NAS，需要等待约 10 分钟
   
</deploy>

## 应用特点

本应用为魔搭ModelScope应用的大模型推理版本，使用冷启动优化后的 vLLM 执行模型的推理，相比普通ModelScope应用具有以下两个优势：

- 更快的冷启动时间：使用本应用可以将大模型的冷启动时间降低至多 20 秒
- 更先进的推理框架：本应用使用 [vLLM 推理框架](https://docs.vllm.ai/en/stable/) 进行模型推理，相比 huggingface/transformers 库增加了多种优化。

## 案例介绍

<appdetail id="flushContent">

将魔搭模型部署至函数计算Serverless GPU具有以下优势：

* a). 成本效益： Serverless 架构使得资源利用更加灵活，可以根据需求动态分配和释放资源，从而降低成本。利用 Serverless GPU，开发者可以根据实际需要分配 GPU 资源，而不必一直支付固定的 GPU 租用费用。

* b). 弹性扩展： 在需求量增加时，Serverless GPU 能够自动扩展以满足更高的负载，而不会因为硬件限制导致性能瓶颈。这种弹性扩展使得系统能够更好地应对突发流量和高负载情况。

* c). 简化管理： 使用 Serverless GPU，开发者无需关心底层硬件和软件的管理维护工作，如服务器配置、操作系统更新等。平台提供商负责管理基础设施，开发者只需专注于模型开发和部署。

* d). 高可用性： Serverless GPU 架构通常具有高可用性，因为服务商会自动处理故障转移和容错机制。这样可以确保模型服务的持续可用性，提高系统稳定性和可靠性。

* e). 灵活部署： Serverless GPU 可以根据应用程序的需求部署到不同的地理位置，以降低延迟和提高性能。同时，也可以轻松地跨多个云平台进行部署，提高了系统的灵活性和可移植性。

综上所述，将魔搭模型部署至 函数计算 GPU 上具有降低成本、弹性扩展、简化管理、高可用性和灵活部署等必要性，可以帮助开发者更高效地部署和管理模型服务。

</appdetail>

## 使用流程

<usedetail id="flushContent">

[ModelScope一键部署模型：新手村实操FAQ篇](https://developer.aliyun.com/article/1307460?spm=5176.28261954.J_7341193060.1.43f42fdewvfTyq&scm=20140722.S_community@@%E6%96%87%E7%AB%A0@@1307460._.ID_1307460-RL_%E9%AD%94%E6%90%AD%20%E4%B8%80%E9%94%AE%E9%83%A8%E7%BD%B2-LOC_search~UND~community~UND~item-OR_ser-V_3-P0_0)

注意，您选择的模型必须是 [vLLM 支持的大模型](https://docs.vllm.ai/en/stable/models/supported_models.html)

</usedetail>

## 开发者社区

您如果有关于错误的反馈或者未来的期待，您可以在 [Serverless Devs repo Issues](https://github.com/serverless-devs/serverless-devs/issues) 中进行反馈和交流。如果您想要加入我们的讨论组或者了解 FC 组件的最新动态，您可以通过以下渠道进行：

<p align="center">  

| <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407298906_20211028074819117230.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407044136_20211028074404326599.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407252200_20211028074732517533.png" width="130px" > |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <center>微信公众号：`serverless`</center>                                                                                         | <center>微信小助手：`xiaojiangwh`</center>                                                                                        | <center>钉钉交流群：`33947367`</center>                                                                                           |
</p>
</devgroup>
