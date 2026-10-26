# research-on-ai-development
A Three-Year Study of AI Development and its Comparative Performance in Solving Olympiad Problems in Physics, Mathematics, and Medicine
# AI Development Study: Year 1 / Исследование развития ИИ: Год 1
## Comparing ChatGPT, Alisa AI, Gemini, Meta AI, DeepSeek, Claude, and Grok 
## Сравнение ChatGPT, Алисы, Gemini, Meta, DeepSeek, Claude и Grok

---

# 🇺🇸 English Version

##  About the Project
This is a student research project. 
I test and compare how well different AI models solve difficult olympiad problems. 
The project runs for 3 years to track the speed of AI development.

Right now, this repository contains the results for **Year 1**. I tested the models in three main areas: **Physics, Mathematics, and Medicine**.

##  Tested AI Models
* **ChatGPT** (OpenAI)
* **Claude** (Anthropic)
* **Gemini** (Google)
* **DeepSeek**
* **Meta AI**
* **Grok** (xAI)
* **Alisa AI** (Yandex)

##  How I Tested Them
I gave all AI models the same difficult tasks from real high school competitions:
*  **Math:** Logic, geometry, and number theory problems.
*  **Physics:** Tasks that require hard formulas and deep understanding of physical laws.
*  **Medicine:** Complex medical case studies and diagnostic questions.

## 📊 Year 1 Results
This table shows the percentage of correct answers for each model in the first year:

| AI Model | Math Accuracy | Physics Accuracy | Medicine Accuracy |
| :--- | :---: | :---: | :---: |
| **Claude** | -% | -% | -% |
| **ChatGPT** | -% | -% | -% |
| **DeepSeek** | -% | -% | -% |
| **Gemini** | -% | -% | -% |
| **Meta AI** | -% | -% | -% |
| **Grok** | -% | -% | -% |
| **Alisa AI** | -% | -% | -% |

### 🛠️ Technical Implementation & Methodology

The evaluation process is fully automated using a structured Python pipeline. To ensure fair and identical testing conditions across all large language models (LLMs), the project utilizes the unified **OpenRouter API** architecture.

#### Key Features of the Pipeline:
* **Strict Reproducibility:** The `temperature` parameter is hardcoded to `0.1` to reduce stochastic variance and ensure deterministic reasoning.
* **Unified Interface:** Allows seamless evaluation of heterogeneous models (`GPT-4o`, `Claude 3.5 Sonnet`, `DeepSeek V3`, `Grok 2`, `Gemini Pro`) within a single loop.
* **Input Isolation:** Tasks are decoupled from the codebase and dynamically parsed from an external `tasks.txt` source payload using structured delimiters (`===`).

#### Core Evaluation Script (`src/benchmark_runner.py`)

```python
import os
import json
from openai import OpenAI

# Initialize the client leveraging OpenRouter infrastructure via Environment Variables
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai"
)

# Benchmark Suite: Multi-provider model configuration
models_to_test = [
    "openai/gpt-4o",
    "deepseek/deepseek-chat",
    "x-ai/grok-2-1212",
    "google/gemini-pro-1.5",
    "anthropic/claude-3-5-sonnet"
]

def run_benchmark(tasks, correct_answers):
    results = {}
    
    for model in models_to_test:
        results[model] = []
        for idx, task in enumerate(tasks, 1):
            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {
                            "role": "system", 
                            "content": "You are an elite expert in STEM and Medicine. "
                                       "Solve the problem step-by-step, outline your logic, "
                                       "and provide the exact final answer at the end."
                        },
                        {"role": "user", "content": task}
                    ],
                    temperature=0.1  # Enforces maximum deterministic response behavior
                )
                
                results[model].append({
                    "task_number": idx,
                    "ai_answer": response.choices.message.content,
                    "correct_answer": correct_answers.get(idx)
                })
            except Exception as e:
                print(f"API Execution Error for {model} on Task {idx}: {e}")
                
    return results
```

#### How to Reproduce

1. Clone the repository and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set your API credentials:
   ```bash
   export OPENROUTER_API_KEY="your_openrouter_api_key_here"
   ```
3. Populate `data/tasks.txt` with your evaluation targets separated by `===` and execute the core runner script.

### Main Conclusions:


##  Plans for Year 2 & 3
* **Year 2:** Test the same problems on the new versions of these AI models to see the progress.
* **Year 3:** Test how special prompts and settings can help AI solve these tasks better.

## Author
* **Kirill Bulannikov**
* High school student in the **Advanced Math Track** (Math Vertical) at Pokrovsky Kvartal School.

---

# 🇷🇺 Русская версия

##  О проекте
Это школьный исследовательский проект. 
В нем я тестирую и сравниваю, насколько хорошо разные модели ИИ решают сложные олимпиадные задачи. 
Проект рассчитан на 3 года для отслеживания скорости развития ИИ.

Сейчас в этом репозитории собраны результаты за **1-й год**. Я протестировал нейросети в трех главных направлениях: **физика, математика и медицина**.

##  Протестированные модели ИИ
* **ChatGPT** (OpenAI)
* **Claude** (Anthropic)
* **Gemini** (Google)
* **DeepSeek**
* **Meta AI**
* **Grok** (xAI)
* **Alisa AI** (Яндекс)

##  Как проходило тестирование
Я давал всем моделям ИИ одинаковые сложные задания из реальных олимпиад для старших классов:
*  **Математика:** задачи на логику, геометрию и теорию чисел.
*  **Физика:** задания, требующие сложных формул и глубокого понимания физических законов.
*  **Медицина:** комплексные медицинские кейсы и вопросы по диагностике.

## 📊 Результаты 1-го года
В этой таблице показан процент правильных ответов каждой модели за первый год:

| AI Model | Math Accuracy | Physics Accuracy | Medicine Accuracy |
| :--- | :---: | :---: | :---: |
| **Claude** | -% | -% | -% |
| **ChatGPT** | -% | -% | -% |
| **DeepSeek** | -% | -% | -% |
| **Gemini** | -% | -% | -% |
| **Meta AI** | -% | -% | -% |
| **Grok** | -% | -% | -% |
| **Alisa AI** | -% | -% | -% |

### Главные выводы:


##  Планы на 2-й и 3-й годы
* **2-й год:** протестировать те же задачи на новых версиях этих же моделей, чтобы увидеть чистый прогресс.
* **3-й год:** проверить, как специальные настройки и промпты помогают ИИ решать эти задачи лучше.

##  Автор
* **Кирилл Буланников**
* Ученик старших классов профильного направления **«Математическая вертикаль»** школы «Покровский квартал».
