# GeoPlan Benchmark

GeoPlan-bench is a benchmark platform for evaluating agent architectures in remote sensing task planning. The platform provides a complete workflow for task generation, filtering, and evaluation, supporting multiple agent architectures and evaluation metrics.

## Features

### Supported Agent Architectures

GeoPlan-bench implements the following 6 agent architectures:

- **ReAct**: Reasoning-Acting loop agent that solves problems by alternating between reasoning and acting
- **Plan-and-Execute**: Planning-execution separation agent that plans first and then executes
- **CoT (Chain of Thought)**: Zero-shot chain-of-thought agent
- **Debate**: Multi-agent debate architecture that improves solutions through discussion among multiple agents
- **AFlow**: Adaptive flow agent that can dynamically adjust tool calling sequences
- **EarthAgent**: Hierarchical expert agent with multi-layer architecture optimized for remote sensing tasks

### Evaluation Metrics

The platform provides 3 evaluation metrics:

1. **Correctness**: Evaluates the correctness of agent tool calls
   - Key Step Recall
   - Key Tool Precision
   - F1 Score

2. **Structural**: Evaluates structural similarity of tool calling sequences
   - Tool Flow Similarity
   - Enhanced Edit Distance

3. **Holistic**: Evaluates solution completeness
   - Elo ranking-based completeness score

### Core Functions

1. **Task Generation**: Automatically generates diverse remote sensing tasks with DAG templates, tool flows, and real-world questions
2. **Task Filtering**: Intelligent filtering and deduplication to ensure task quality and diversity
3. **Task Evaluation**: Automated evaluation pipeline supporting batch evaluation and result analysis

## Installation

### Prerequisites

- Python >= 3.8
- pip

### Installation Steps

1. Clone the repository:

```bash
git clone https://github.com/earth-insights/geoplan-bench.git
cd geoplan-bench
```

2. Create a virtual environment (venv or conda):

```bash
# Using venv (Python 3.8+)
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Install package (optional, for command-line tools):

```bash
pip install -e .
```

5. Configure environment variables:

```bash
cp env.example .env
# Edit .env and add your API keys
```

Required environment variables:

- `OPENAI_API_KEY`: OpenAI API key
- `OPENAI_API_BASE`: OpenAI API base URL (optional)
- `GEMINI_API_KEY`: Google Gemini API key

## Quick Start

### 1. Generate Tasks

Generate tasks using the command-line tool:

```bash
geoplan-generate --num-dags 1 --output-dir data/tasks/raw
```

Or use Python script:

```bash
python scripts/generate_tasks.py --num-dags 1 --output-dir data/tasks/raw
```

### 2. Filter Tasks

Filter and deduplicate generated tasks:

```bash
geoplan-filter --input-dir data/tasks/raw --output-dir data/tasks/filtered
```

Or use Python script:

```bash
python scripts/filter_tasks.py --input-dir data/tasks/raw --output-dir data/tasks/filtered
```

### 3. Evaluate Agents

Evaluate agent performance on tasks:

```bash
geoplan-evaluate --start-index 0 --end-index 3
```

Or use Python script:

```bash
python scripts/evaluate.py --start-index 0 --end-index 3
```

## Project Structure

```
geoplan_bench/
├── agents/             # Agent implementations
│   ├── base.py         # Base agent interface
│   ├── ReAct.py        # ReAct agent
│   ├── Plan_and_Execute.py  # Plan-and-Execute agent
│   ├── CoT.py          # CoT agent
│   ├── Debate.py       # Debate agent
│   ├── AFlow.py        # AFlow agent
│   └── EarthAgent.py   # EarthAgent agent
├── evaluation/          # Evaluation modules
│   └── metrics/        # Evaluation metrics
│       ├── correctness.py  # Correctness evaluation
│       ├── holistic.py     # Holistic evaluation
│       └── structural.py   # Structural evaluation
├── tools/              # Tool implementations
│   └── tools.py        # Remote sensing toolset
├── pipeline/           # Pipelines
│   ├── task_generation.py    # Task generation pipeline
│   ├── task_evaluation.py    # Task evaluation pipeline
│   └── task_validation.py    # Task filtering logic
├── data/               # Data management
│   └── schemas.py      # Data schema definitions
├── utils/              # Utility functions
│   ├── arena.py        # Agent creation utilities
│   └── importance.py   # Tool importance analysis
└── config/             # Configuration
    ├── constants.py    # Constant definitions
    └── prompts.py      # Prompt templates

scripts/                # Executable scripts
├── generate_tasks.py   # Task generation script
├── filter_tasks.py     # Task filtering script
└── evaluate.py         # Evaluation script

examples/               # Example code and data

docs/                   # Documentation

data/                   # Our data files
├── aflow_train_tasks/  # Training set for AFlow
└── test_tasks/         # Test set
```

## Usage Guide

For detailed usage instructions, please refer to:

- [Usage Guide](docs/usage.md) - Detailed feature usage instructions
- [Architecture Documentation](docs/architecture.md) - System architecture description
- [Example Code and Data](examples/) - Code and Data examples

## Task Domains

GeoPlan Benchmark supports the following 7 remote sensing task domains:

1. **Agriculture & Forestry**
2. **Urban & Regional Planning**
3. **Environmental Monitoring & Climate Change**
4. **Disaster Emergency & Management**
5. **Earth Science & Resource Exploration**
6. **Marine & Water Resources**
7. **Defense & Security**

Each domain supports three complexity levels: Simple, Medium, and Complex.

## Contributing

Contributions are welcome! Please check our contributing guidelines.

## License

See LICENSE file for details.

## Citation

If you use GeoPlan Benchmark, please cite:

```bibtex
@article{li2025designing,
  title={Designing Domain-Specific Agents via Hierarchical Task Abstraction Mechanism},
  author={Li, Kaiyu and Wang, Jiayu and Wang, Zhi and Qiao, Hui and Zhang, Weizhan and Meng, Deyu and Cao, Xiangyong},
  journal={arXiv preprint arXiv:2511.17198},
  year={2025}
}
```
