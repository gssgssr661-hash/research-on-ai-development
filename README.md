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


📊 Year 1 Results


#	Benchmark	ChatGPT	Claude	DeepSeek	Meta AI (Llama)
1	77 °C	✅ 77	✅ 77	❌ 109	❌ 45
2	1.0 °C	❌ t₂/64 formula, no number	✅ 1.0*	❌ 0.2	❌ 0.2
3	option 2	✅	✅	✅	✅
4	26 L/100 km	✅	✅	✅	✅
5	5040	✅	✅	✅	✅
6	200 ₽	✅	✅	✅	✅
7	20°	❌ 45	❌ 15	❌ 30	❌ 15
8	AB = 19	❌ 20	❌ 20	❌ 17	❌ 20
9	8, 12, 16	❌ 16 (one of three)	❌ 24	❌ 21 and 24	❌ 32
10	ARVI, antibiotics not needed	✅	✅	✅	✅


AI Model	Physics	Math	Medicine	Total
Claude	100% (4/4)	40% (2/5)	100% (1/1)	70%
ChatGPT	75% (3/4)	40% (2/5)	100% (1/1)	60%
DeepSeek	50% (2/4)	40% (2/5)	100% (1/1)	50%
Meta AI (Llama)	50% (2/4)	40% (2/5)	100% (1/1)	50%

### 🛠️ Technical Implementation & Methodology

import os
import json
import time
import sys
from openai import OpenAI

sys.stdout.reconfigure(encoding="utf-8")

# ====== ВСТАВЬТЕ КЛЮЧ PROXYAPI СЮДА ======

# =========================================

proxy = OpenAI(api_key=API_KEY, base_url="https://api.proxyapi.ru/v1")

# (название в таблице, клиент, идентификатор модели)
MODELS = [
    ("ChatGPT",         proxy, "openai/gpt-4o"),
    ("Claude",          proxy, "anthropic/claude-sonnet-4-5"),
    ("DeepSeek",        proxy, "deepseek/deepseek-chat"),
    ("Gemini",          proxy, "google/gemini-2.5-pro"),
    ("Meta AI (Llama)", proxy, "meta-llama/llama-3.3-70b-instruct"),
    ("Grok",            proxy, "x-ai/grok-4"),
]

# --- Алиса (Yandex AI Studio), необязательно. Если не заполнено — пропускается ---
YANDEX_API_KEY = ""
YANDEX_FOLDER_ID = ""
YANDEX_MODEL = ""   # точное имя модели смотрите в документации Яндекса
if YANDEX_API_KEY and YANDEX_FOLDER_ID and YANDEX_MODEL:
    alisa = OpenAI(api_key=YANDEX_API_KEY,
                   base_url="https://ai.api.cloud.yandex.net/v1",
                   project=YANDEX_FOLDER_ID)
    MODELS.append(("Alisa AI", alisa, YANDEX_MODEL))

# ---------------- ЗАДАЧИ ----------------
VESSELS = (
    "Два одинаковых сосуда заполнены водой. Первый заполнен до краёв холодной водой "
    "с температурой t₁ = 13 °C, а второй – горячей водой наполовину. Из первого сосуда "
    "переливают воду, заполняя второй сосуд до краёв, и после установления теплового "
    "равновесия переливают назад в первый сосуд то же количество воды. После установления "
    "теплового равновесия в первом сосуде описанную процедуру повторяют ещё несколько раз, "
    "совершая, таким образом, несколько циклов переливаний «туда – обратно». "
    "Теплообмен воды с другими телами пренебрежимо мал.\n"
)

dataset = [
    {
        "id": 1,
        "question": "Задача 1. " + VESSELS +
            "Чему равна температура t₂ горячей воды в начале опыта, если после первого цикла "
            "переливаний температура воды в сосудах отличалась на Δt₁ = 16 °C? "
            "Дайте ответ в градусах Цельсия с округлением до целого числа.",
        "correct": "77 °C",
    },
    {
        "id": 2,
        "question": "Задача 2. " + VESSELS +
            "Чему равна разность температур Δt₃ воды в сосудах по окончании третьего цикла "
            "переливаний? Дайте ответ в градусах Цельсия с округлением до десятых долей.",
        "correct": "1.0 °C",
    },
    {
        "id": 3,
        "question": "Задача 3. Капитан яхты выбирал для неё новый винт. Для этого он провёл "
            "простейшее исследование. При частоте вращения двигателя (2,0 ± 0,1) тыс. об/мин "
            "скорость его яхты в спокойную погоду составила (6,3 ± 0,1) узла. А при частоте "
            "вращения в (1,4 ± 0,1) тыс. об/мин – (4,3 ± 0,1) узла.\n"
            "Противоречат или не противоречат результаты проведённых измерений гипотезе о том, "
            "что скорость движения яхты пропорциональна частоте вращения двигателя? "
            "Варианты ответа: 1) противоречат, 2) не противоречат, "
            "3) не хватает данных для ответа на вопрос.",
        "correct": "Вариант 2 – не противоречат",
    },
    {
        "id": 4,
        "question": "Задача 4. Двигатель яхты может работать в диапазоне частот вращения от "
            "1,0 тыс. об/мин до 3,0 тыс. об/мин. При этом расход топлива зависит от частоты "
            "вращения двигателя. Из предоставленного графика известно, что при частоте "
            "вращения N = 2,0 тыс. об/мин расход топлива составляет Q = 3 л/ч.\n"
            "Рассчитайте расход топлива в пересчёте на 100 километров пути при частоте "
            "вращения двигателя в 2,0 тыс. об/мин. Известно, что одна морская миля составляет "
            "1852 м, а 1 узел = 1 морская миля/ч. Дайте ответ в л/(100 км), округлив до "
            "целого числа. Считайте, что при 2 тысячах оборотов в минуту яхта движется со "
            "скоростью 6,3 узла точно.",
        "correct": "26 л/(100 км)",
    },
    {
        "id": 5,
        "question": "Задача 5. Найдите наибольшее натуральное число n, при котором (7!)! "
            "делится на n!. Здесь k! означает произведение 1 * 2 * 3 * ... * k.",
        "correct": "n = 5040",
    },
    {
        "id": 6,
        "question": "Задача 6. Саша и Маша пришли в магазин. Саша купил 3 пакета молока, "
            "7 пачек творога и 5 йогуртов. Маша купила 2 пакета молока, 10 пачек творога "
            "и 6 йогуртов. Саша потратил на всё 980 рублей, а Маша потратила 1160 рублей. "
            "Сколько суммарно стоит один пакет молока, одна пачка творога и один йогурт?",
        "correct": "200 рублей",
    },
    {
        "id": 7,
        "question": "Задача 7. Внутри трапеции ABCD с основаниями AD и BC отметили точку O. "
            "Оказалось, что AO = BO = CO = BC и DA = DO = DC. "
            "Сколько градусов составляет угол BAO?",
        "correct": "108 градусов",
    },
    {
        "id": 8,
        "question": "Задача 8. В прямоугольном треугольнике ABC с прямым углом C провели "
            "высоту CH. На гипотенузе AB отметили точки X и Y такие, что CX и CY — "
            "биссектрисы углов BCH и HCA соответственно. Найдите, чему равна длина стороны "
            "AB, если известно, что периметр треугольника ABC равен 44, а длина отрезка XY "
            "равна 6.",
        "correct": "AB = 19",
    },
    {
        "id": 9,
        "question": "Задача 9. Новая шахматная фигура гусь может ходить либо на одну клетку "
            "влево, либо на две клетки вправо и одну вверх, либо на две клетки вверх и одну "
            "вправо. Несколько гусей стоят в клетках доски 8х8 так, что никакой гусь не бьёт "
            "другого гуся, при этом любая незанятая клетка бьётся хотя бы одним гусем. "
            "Сколько гусей может стоять на доске? Укажите все возможные варианты в любом порядке.",
        "correct": "8, 12, 16 гусей",
    },
    {
        "id": 10,
        "question": "Задача 10. Клиническая ситуация: К врачу обратился 28-летний мужчина с "
            "жалобами на першение в горле, легкий заложенный нос с прозрачными выделениями, "
            "незначительную слабость и частое чихание. Симптомы появились накануне вечером, "
            "после того как он сильно замерз на остановке. Температура тела на момент осмотра "
            "составляет 37,2 °С. Никаких хронических заболеваний у пациента нет.\n\n"
            "На основе клинической ситуации ответьте на следующие вопросы:\n"
            "1. Какой наиболее вероятный предварительный диагноз можно поставить пациенту?\n"
            "2. Какова главная причина (этиология) данного состояния и связано ли оно "
            "напрямую с переохлаждением?\n"
            "3. Требуется ли пациенту назначение антибиотиков и какие базовые рекомендации "
            "по лечению ему следует дать?",
        "correct": "1. ОРВИ. 2. Вирусы. 3. Антибиотики не нужны, лечение симптоматическое.",
    },
]

# ---------------- ЗАПУСК ----------------
output_filename = "my_test_results.json"
results = {}

if API_KEY == "ВАШ_КЛЮЧ_PROXYAPI":
    sys.exit("❌ Вставьте ключ в переменную API_KEY.")

print(f"📚 Всего задач: {len(dataset)}")

# Проверяем, какие модели реально есть в каталоге ProxyAPI
try:
    available = {m.id for m in proxy.models.list().data}
except Exception as e:
    available = None
    print(f"⚠️ Не удалось получить список моделей: {e}")


def save_results():
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)


def ask_model(client, model, task_text, retries=3):
    last_error = None
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{
                    "role": "user",
                    "content": (
                        "You are an academic researcher. Solve this olympiad problem "
                        "step-by-step and write the exact final answer at the very end.\n\n"
                        f"Task:\n{task_text}"
                    ),
                }],
                temperature=0.1,
                max_tokens=4000,
                timeout=180,
            )
            if response and response.choices:
                return response.choices[0].message.content or "Пустой ответ от модели"
            return "Пустой ответ от сервера"
        except Exception as e:
            last_error = e
            time.sleep(3 * (attempt + 1))
    return f"Ошибка запроса: {last_error}"


for label, client, model in MODELS:
    if client is proxy and available is not None and model not in available:
        print(f"\n⏭️ {label}: модели «{model}» нет в каталоге ProxyAPI — пропускаю "
              f"(подставьте точное имя из списка моделей).")
        continue

    print(f"\n🤖 Опрашиваю: {label} [{model}]...")
    results[label] = []
    for item in dataset:
        print(f"   📤 Задача №{item['id']}...")
        answer = ask_model(client, model, item["question"])
        results[label].append({
            "task_number": item["id"],
            "ai_answer": answer,
            "correct_answer": item["correct"],
        })
        save_results()
        time.sleep(2)

print(f"\n🏁 ГОТОВО! Результаты: {os.path.abspath(output_filename)}")



### Main Conclusions:
• Claude leads the pack with 70%, followed by ChatGPT at 60%, and DeepSeek and Llama tied at 50%. However, the margin is narrow: a single problem represents 10 percentage points, and the total sample size is only 10 problems. This cannot be considered a reliable rating.
• Everyone solved the simple problems. Problems 3, 4, 5, 6, and the clinical case (Problem 10) were answered with 100% accuracy by all four models.
• Physics is where the differences emerge. Only Claude and ChatGPT correctly calculated the temperature in Problem 1 (77 °C). DeepSeek and Llama failed to handle the liquid-mixing model correctly (getting 109 °C and 45 °C, respectively).
• Complex geometry and combinatorics remained completely unsolved. None of the models provided a correct answer for Problems 7, 8, and 9.
• Models often "hallucinated" or skipped steps in their reasoning. In Problem 8, DeepSeek and ChatGPT explicitly wrote "details omitted" before simply spitting out a random number.
• Medicine failed to differentiate the models. The problem proved too simple for an Olympiad-level test, resulting in identical correct answers across the board.

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
№	Эталон	ChatGPT	Claude	DeepSeek	Meta AI (Llama)
1	77 °C	✅ 77	✅ 77	❌ 109	❌ 45
2	1,0 °C	❌ формула t₂/64, числа нет	✅ 1,0*	❌ 0,2	❌ 0,2
3	вариант 2	✅	✅	✅	✅
4	26 л/100 км	✅	✅	✅	✅
5	5040	✅	✅	✅	✅
6	200 ₽	✅	✅	✅	✅
7	20°	❌ 45	❌ 15	❌ 30	❌ 15
8	AB = 19	❌ 20	❌ 20	❌ 17	❌ 20
9	8, 12, 16	❌ 16 (одно из трёх)	❌ 24	❌ 21 и 24	❌ 32
10	ОРВИ, антибиотики не нужны	✅	✅	✅	✅

Нейросеть	Физика	Математика	Медицина	Итого
Claude	100% (4/4)	40% (2/5)	100% (1/1)	70%
ChatGPT	75% (3/4)	40% (2/5)	100% (1/1)	60%
DeepSeek	50% (2/4)	40% (2/5)	100% (1/1)	50%
Meta AI (Llama)	50% (2/4)	40% (2/5)	100% (1/1)	50%

### Главные выводы:
Лидирует Claude (70%), за ним ChatGPT (60%), DeepSeek и Llama (по 50%). Но разрыв маленький: одна задача это 10 процентных пунктов, а выборка всего 10 задач. Надёжным рейтингом это считать нельзя.
Простые задачи решили все. Задачи 3, 4, 5, 6 и клиническая задача 10 выполнены всеми четырьмя моделями на 100%.
Различия видны на физике. Только Claude и ChatGPT верно нашли температуру в задаче 1 (77 °C). DeepSeek и Llama ошиблись в модели переливаний (109 и 45 °C).
Сложная геометрия и комбинаторика не решена никем. В задачах 7, 8 и 9 правильных ответов нет ни у одной модели. Модели часто «досочиняли» решение (в задаче 8 DeepSeek и ChatGPT пишут «детали опущены» и выдают число).
Медицина не различает модели. Задача слишком лёгкая для олимпиадного уровня, все дали одинаковый ответ.

##  Планы на 2-й и 3-й годы
* **2-й год:** протестировать те же задачи на новых версиях этих же моделей, чтобы увидеть чистый прогресс.
* **3-й год:** проверить, как специальные настройки и промпты помогают ИИ решать эти задачи лучше.

##  Автор
* **Кирилл Буланников**
* Ученик старших классов профильного направления **«Математическая вертикаль»** школы «Покровский квартал».
