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

import os
import json
import time
from openai import OpenAI

# 1. НАСТРОЙКА API ПОД PROXYAPI (Ключ встроен прямо в код)
# Вставьте ваш секретный токен вместо proxyapi-xxxxxxxxxxxx...
client = OpenAI(
    api_key="proxyapi-xxxxxxxxxxxx...", 
    base_url="https://proxyapi.ru"
)

# 2. АКТУАЛЬНЫЕ ИМЕНА МОДЕЛЕЙ В СИСТЕМЕ PROXYAPI
models_to_test = [
    "gpt-4o",               # ChatGPT (OpenAI)
    "claude-3-5-sonnet",    # Claude (Anthropic)
    "deepseek-chat",        # DeepSeek V3
    "gemini-1.5-pro"        # Gemini (Google)
]

# 3. БАЗА ПРАВИЛЬНЫХ ОТВЕТОВ ДЛЯ СРАВНЕНИЯ
correct_answers = {
    1: "45 °C",
    2: "2.0 °C",
    3: "Вариант 2 — не противоречат",
    4: "26 л/(100 км)",
    5: "n = 5040",
    6: "210 рублей",
    7: "108 градусов",
    8: "AB = 20",
    9: "8, 12, 16 гусей",
    10: "1. ОРВИ. 2. Вирусы. 3. Антибиотики НЕ нужны, лечение симптоматическое."
}

input_filename = "tasks.txt"
output_filename = "my_test_results.json"

# Чтение задач из файла tasks.txt
if not os.path.exists(input_filename):
    print(f"Ошибка! Создайте текстовый файл {input_filename} рядом со скриптом.")
    exit()

with open(input_filename, "r", encoding="utf-8") as f:
    content = f.read()
    tasks = [task.strip() for task in content.split("===") if task.strip()]

print(f"📚 Загружено задач из файла: {len(tasks)}")
results = {}

# 4. ЦИКЛ ОПРОСА НЕЙРОСЕТЕЙ
for model in models_to_test:
    print(f"\n🤖 Опрашиваю модель: [{model}]...")
    results[model] = []
    
    for idx, task in enumerate(tasks, 1):
        print(f"   👉 Отправка задачи №{idx}...")
        
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "system", 
                        "content": "Ты — сильный эксперт в точных науках и медицине. "
                                   "Реши задачу пошагово, выведи формулы или логику рассуждений, "
                                   "распиши понятный ход мысли и в конце укажи точный финальный ответ."
                    },
                    {"role": "user", "content": task}
                ],
                temperature=0.1  # Низкая температура для минимизации случайных ошибок
            )
            answer = response.choices.message.content
            
            # Сохраняем ответ модели
            results[model].append({
                "task_number": idx,
                "task_text": task,
                "ai_answer": answer,
                "correct_answer": correct_answers.get(idx, "Нет данных")
            })
        except Exception as e:
            print(f"   ❌ Ошибка у модели {model} на задаче №{idx}: {e}")
            results[model].append({
                "task_number": idx,
                "task_text": task,
                "ai_answer": f"Ошибка запроса к API: {e}",
                "correct_answer": correct_answers.get(idx, "Нет данных")
            })
        
        # Небольшая пауза между запросами, чтобы не превышать лимиты (Rate Limits)
        time.sleep(1)

# 5. СОХРАНЕНИЕ ВСЕХ РЕЗУЛЬТАТОВ В JSON
with open(output_filename, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print(f"\n🎉 Готово! Все ответы сохранены в файл: {output_filename}")



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
