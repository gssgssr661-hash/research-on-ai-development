import json
import os
from openai import OpenAI

# 1. Настройка API 
client = OpenAI(
    api_key="_API_КЛЮЧ",
    base_url="https://proxyapi.ru"  # Заменить URL
)

# 2. Полный список моделей для  исследования
models_to_test = [
    "gpt-4o",               # Chat GPT (OpenAI)
    "deepseek-chat",        # DeepSeek
    "yandexgpt/latest",     # YandexGPT 
    "grok-beta",            # Grok (xAI)
    "gemini-1.5-pro",       # Gemini (Google)
    "claude-3-5-sonnet"     # Claude (Anthropic)
]

input_filename = "tasks.txt"
output_filename = "olympiad_results.json"

# 3. Чтение задач из файла Задачи.txt
if not os.path.exists(Задачи.txt):
    print(f {Задачи.txt} )
    exit()

with open(input_filename, "r", encoding="utf-8") as f:
    content = f.read()
    tasks = [task.strip() for task in content.split("===") if task.strip()]

print(f" Успешно загружено задач из файла: {len(tasks)}")
results = {}

# 4. Цикл опроса всех нейросетей
for model in models_to_test:
    print(f"\n Запуск тестирования модели: [{model}]...")
    results[model] = []
    
    for idx, task in enumerate(tasks, 1):
        print(f"    Отправка задачи №{idx}...")
        
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "system", 
                        "content": "Ты — выдающийся физик и член жюри Всероссийской олимпиады школьников. "
                                   "Реши задачу по физике пошагово, выведи формулы, распиши ход мысли и укажи финальный ответ."
                    },
                    {"role": "user", "content": task}
                ],
                temperature=0.1  # Низкая температура для минимизации выдуманных фактов
            )
            answer = response.choices.message.content
            results[model].append({
                "task_number": idx,
                "task_text": task,
                "ai_answer": answer
            })
        except Exception as e:
            print(f"    Ошибка у модели {model} на задаче №{idx}: {e}")
            results[model].append({
                "task_number": idx,
                "task_text": task,
                "ai_answer": f"Ошибка запроса к API: {e}"
            })

# 5. Сохранение всех ответов в один большой JSON файл
with open(output_filename, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print(f"\n Исследование завершено! Все ответы сохранены в: {output_filename}")
