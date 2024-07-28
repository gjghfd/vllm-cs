// download the model weights
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <errno.h>
#include <unistd.h>
#include <fstream>
#include <thread>
using namespace std;

void touch_model_files() {
    // Get path to model weights
    string FC_MODEL_CACHE_DIR = getenv("MODELSCOPE_CACHE");
    string model_id = getenv("MODEL_ID");

    string model_path = FC_MODEL_CACHE_DIR + '/' + model_id;

    // use vmtouch to store files in page cache
    string command = "vmtouch -t " + model_path;
    system(command.c_str());
}

int main() {
    thread init_model_thread(touch_model_files);
    init_model_thread.join();
    system("python3 -m vllm.entrypoints.openai.api_server");
    // never return

    throw runtime_error("vllm.entrypoints.openai.api_server exited unexpectedly.");
    return 0;
}