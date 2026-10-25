import json
import os
from openai import OpenAI

# 1. Настройка API под международный OpenRouter
client = OpenAI(
    api_key="sk-or-v1-xxxxxxxx...",  #  новый ключ от OpenRouter
    base_url="https://openrouter.ai"  # Официальный адрес агрегатора
)


# 2. Имена этих моделей в системе OpenRouter
models_to_test = [
    "openai/gpt-4o",                # Chat GPT (OpenAI)
    "deepseek/deepseek-chat",       # DeepSeek V3
    "yandex/yandexgpt-latest",      # YandexGPT (если доступен в регионе)
    "x-ai/grok-2-1212",             # Grok (xAI)
    "google/gemini-pro-1.5",        # Gemini (Google)
    "anthropic/claude-3-5-sonnet"   # Claude (Anthropic)
]


# 3. База правильных ответов для сравнения
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

# 4. Цикл опроса нейросетей
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
                temperature=0.1
            )
            answer = response.choices.message.content
            
            # Сохраняем ответ и прикрепляем правильный вариант для ручной сверки
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

# 5. Сохранение всех результатов в один файл
with open(output_filename, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print(f"\n🎉 Готово! Все ответы сохранены в файл: {output_filename}")

