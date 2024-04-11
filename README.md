<div align="center">
    <h1>LlamaTouch: A Faithful and Scalable Testbed for Mobile UI Automation Task Evaluation</h1>
</div>

<p align="center">
  <a href="https://example.com">Website</a> •
  <a href="#dataset">Dataset</a> •
  <a href="#agentenv">AgentEnv</a> •
  <a href="#llamatouch-evaluator">LlamaTouch Evaluator</a> •
  <a href="https://arxiv.org/">Paper</a> •
  <a href="#citation">Citation</a>
</p>

LlamaTouch is a testbed for evaluating mobile UI automation agents in real-world mobile environments.
It compares agent execution traces on mobile devices with our annotated essential states in the ground-truth datasets, rather than directly comparing two concrete action sequences on static datasets.

Key features of LlamaTouch:

1. **Task execution in real-world mobile environments.**
<!-- : Mobile UI automation agents execute tasks on real mobile devices with dynamic contents to reveal their real capabilities. -->

2. **Faithful and scalable task evaluation powered by essential application states.**
<!-- : Powered by the annotated application states in the ground-truth task interaction sequences, LlamaTouch accurately records and compares application states with pre-defined counterparts. -->

3. **Easy task set annotation and expansion with a rich set of UI state annotation primitives.**

## Dataset

> [!TIP]
> [llamatouch_task_metadata.tsv](dataset/llamatouch_task_metadata.tsv) contains the metadata of the dataset.
>
> See [docs](dataset/README.md) to explore and use the dataset.

LlamaTouch comprises 495 mobile UI automation tasks, with 102 tasks sampled from [AITW](https://arxiv.org/abs/2307.10088) and 393 self-constructed tasks in 46 popular Android applications.

Each UI automation task in the dataset contains:

- **A task description**: e.g., "Reserve a rental car in Los Angeles from June 1st-7th, with a budget of up to $60 per day on Expedia"
- **A sequence of UI representations and actions** to complete the task
    - UI representations: pixel-level screenshots and textual view hierarchies
    - Actions: concrete actions recorded on a UI representation
- **Annotated essential states**: e.g., a textbox in the screen with the text "Your cart is empty"

A visualized example in shown in the following figure.

<div align="center">
    <img src="src/example_task.png">
</div>

## AgentEnv

> [!TIP]
> See [docs](https://github.com) to use AgentEnv.

[AgentEnv](https://github.com/) acts as the bridge between a mobile agent and a mobile device (e.g., a real smartphone or an Android emulator) for real-world task execution.

AgentEnv provides basic APIs for completing a mobile UI automation task, including (1) retrieve the UI representations from mobile devices, and (2) forward agent decisions (predicted actions) to the mobile devices.
All device states will be recorded during task execution, which will be used in LlamaTouch Evaluator.

See [docs](https://github.com) to use AgentEnv.

## LlamaTouch Evaluator

> [!TIP]
> See [docs](https://github.com) to use LlamaTouch Evaluator.

LlamaTouch Evaluator takes the essential state-powered dataset and agent execution traces in real-world environments as the input.
For each task, it iterates the agent execution trace to detect whether it traverses all annotated essential states to complete the task.

## Citation

```
```