from PIL import Image
import gradio as gr
import io
import os
import requests
import base64
import random
import time
import threading

import sys
sys.path.append('/code/python')
from openai import OpenAI

## global variables inherited from env
demo = None
model_id = os.getenv('MODEL_ID', '')
model_revision = os.getenv('MODEL_VERSION', '')
model_task = os.getenv('TASK', '')
api_url = os.getenv('API_URL')
title = "魔搭社区x函数计算 : 一键部署模型"
description = "本页面提供图形化方式调用部署后的魔搭模型，更多FAQ请见 [ModelScope一键部署模型：新手村实操FAQ篇](https://developer.aliyun.com/article/1307460?spm=5176.28261954.J_7341193060.1.43f42fdewvfTyq&scm=20140722.S_community@@%E6%96%87%E7%AB%A0@@1307460._.ID_1307460-RL_%E9%AD%94%E6%90%AD%20%E4%B8%80%E9%94%AE%E9%83%A8%E7%BD%B2-LOC_search~UND~community~UND~item-OR_ser-V_3-P0_0)"
article = '''
- 模型ID: [{}](https://www.modelscope.cn/models/{})
- 模型版本: {}
- 模型任务类型: {}
- 模型推理URL: {}/invoke'''.format(model_id, model_id, model_revision, model_task, api_url)

print("[debug] model_id=", model_id)
print("[debug] model_revision=", model_revision)
print("[debug] model_task=", model_task)
print("[debug] api_url=", api_url)

if model_task == None or len(model_task) == 0:
    gr.Warning("Missing necessary model task")
if api_url == None or len(api_url) == 0:
    gr.Warning("Missing necessary api url")
else:
    api_url += "/v1"

client = OpenAI(
    base_url=api_url,
    api_key="token"
)

def chat_setup():
    def stream_handler(message, history):
        if message == None or len(message) == 0:
            raise gr.Error("Missing necessary input message, please retry.")

        history_openai_format = []
        for human, assistant in history:
            history_openai_format.append({"role": "user", "content": human })
            history_openai_format.append({"role": "assistant", "content":assistant})
        history_openai_format.append({"role": "user", "content": message})

        start_time = time.time()
        chat = client.chat.completions.create(
            model=model_id,
            messages=history_openai_format,
            stream=True
        )
        partial_response = ""
        for stream_response in chat:
            if stream_response.choices[0].delta.content is not None:
                partial_response = partial_response + stream_response.choices[0].delta.content
                yield partial_response
        
        reply = partial_response
        elpased = time.time() - start_time
        print(f"reply = {reply}")
        print(f"generation finished, time cost = {elpased} seconds")

    with gr.Blocks() as demo:
        gr.ChatInterface(fn=stream_handler,
                         examples=["hello", "您好", "你能做什么"],
                         title=title,
                         description=description)
        gr.Markdown(article)

    return demo

def default_setup():
    def default_callback():
        return "invalid model task"

    return gr.Interface(fn=default_callback, inputs=None, outputs="text", title="404", description="invalid model task")

## initiailzie
model_task_handlers = {
    "chat" : chat_setup,
    "default" : default_setup,
}

if model_task_handlers.get(model_task) == None:
    demo = model_task_handlers["default"]()
else:
    demo = model_task_handlers[model_task]()
    
demo.queue(concurrency_count=16).launch(server_name="0.0.0.0")
