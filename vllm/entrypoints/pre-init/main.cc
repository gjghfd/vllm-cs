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
    int pid = fork();
    if (pid > 0) {
        // parent process

        system("python3 -u /vllm-workspace/app.py");
        // never return

        throw runtime_error("python program exited unexpectedly.");
    } else {
        // child process

        touch_model_files();
    }

    return 0;
}