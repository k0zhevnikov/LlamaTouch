import os

from evaluator.task_trace import DatasetHelper
from gr_vis import plot_single_trace,TaskTrace
from rename_tracedir import proc_single_trace

helper = DatasetHelper(
    epi_metadata_path="./all_app_metadata.tsv",
    gr_dataset_path="./",
)
def rm_input_text(instruct):
    with open(instruct, "r") as f:
        lines = f.readlines()
    with open(instruct, "w") as f:
        for line in lines:
            if "Input" in line:
                f.write("[Input] \n")
                continue
            f.write(line)
# def plot_single_trace(
#     epi: str,
#     category: str,
#     task_description: str,
#     task_trace: TaskTrace,
#     output_file: str,
# ):
    
if __name__ == "__main__":
    trace_folder = "/home/kozhev/Agent/rawCaptureData/Uber"
    instruct = os.path.join(trace_folder, "eventStructs.txt")
    output_dir = "/home/kozhev/Agent/AgentEnv/docs/pics"
    ep = "025"
    
    # 处理顺序问题
    proc_single_trace(trace_folder)
    rm_input_text(instruct)
    trace = helper._load_groundtruth_trace_by_path(trace_folder)
    output_file = os.path.join(output_dir, trace_folder.split("/")[-1]+".png")
    plot_single_trace(ep,"setup",trace_folder.split("/")[-1],trace,output_file)