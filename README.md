# Моделирование Аэропортов

Этот проект демонстрирует объектно-ориентированное моделирование работы аэропортов, самолётов и вертолётов. Основная цель — симуляция отправки воздушного транспорта между аэропортами с учётом различных условий посадки.

## Функционал

1.  **Загрузка данных**: Информация об аэропортах и транспорте считывается из JSON-файла (`airports.json`).
2.  **Моделирование объектов**:
    *   **Аэропорт (`Airports`)**: Имеет название, максимальную вместимость, длину взлётно-посадочной полосы и список транспортных средств.
    *   **Транспорт (`Transport`)**: Базовый класс для самолётов и вертолётов.
    *   **Самолёт (`Planes`)**: Имеет минимальную требуемую длину ВПП для посадки.
    *   **Вертолёт (`Helicopter`)**: Может быть военным или гражданским. Военные вертолёты могут приземляться только если в аэропорту занято менее половины мест.
3.  **Симуляция отправки**: Случайным образом выбирается тип транспорта (самолёт или вертолёт) из исходного аэропорта и отправляется в целевой аэропорт.
4.  **Проверка условий**: Перед отправкой проверяются все необходимые условия для посадки в целевом аэропорту (наличие места, длина ВПП для самолётов, лимит на военные вертолёты).
5.  **Вывод**: Отправляющий и принимающий аэропорт до посадки, если возможна посдака самолета в принимающем аэропорту, то затем выведется два аэропорта после посадки, иначе выведет, что невозможен полёт.

## Структура проекта

*   `airports.py` — основной скрипт с классами и логикой симуляции.
*   `airports.json` — файл с данными об аэропортах, самолётах и вертолётах.

## Как запустить

1.  Убедитесь, что у вас установлен Python (версия 3.7+).
2.  Поместите файлы `airports.py` и `airports.json` в одну директорию.
3.  Запустите скрипт из терминала:
    ```bash
    python airports.py
    ```
4.  Скрипт выведет информацию об аэропортах до и после попытки отправки транспорта.

## Ограничения

*   Проект является учебным примером и не претендует на реалистичную симуляцию.
*   Логика отправки реализована в виде однократной попытки между двумя случайными аэропортами.

## Пример вывода
name: Sheremetyevo, max_aircrafts: 15, line_length: 3500, transports: {'planes': [number: SU123; max_distance: 8000; max_cargo_weight: 25000; min_line_lenth: 2800, number: A320-456; max_distance: 6000; max_cargo_weight: 18000; min_line_lenth: 2400], 'helicopters': [number: MI-8-001; max_distance: 800; max_cargo_weight: 4000; if_military: False, number: KA-52-007; max_distance: 1200; max_cargo_weight: 2000; if_military: True]}
name: Vnukovo, max_aircrafts: 12, line_length: 3000, transports: {'planes': [number: TU154-789; max_distance: 5000; max_cargo_weight: 20000; min_line_lenth: 2600], 'helicopters': [number: AN-2-111; max_distance: 600; max_cargo_weight: 1500; if_military: False]}

ОТПРАВКА A320-456 (самолёт) из Sheremetyevo в Vnukovo
name: Sheremetyevo, max_aircrafts: 15, line_length: 3500, transports: {'planes': [number: SU123; max_distance: 8000; max_cargo_weight: 25000; min_line_lenth: 2800], 'helicopters': [number: MI-8-001; max_distance: 800; max_cargo_weight: 4000; if_military: False, number: KA-52-007; max_distance: 1200; max_cargo_weight: 2000; if_military: True]}
name: Vnukovo, max_aircrafts: 12, line_length: 3000, transports: {'planes': [number: TU154-789; max_distance: 5000; max_cargo_weight: 20000; min_line_lenth: 2600, number: A320-456; max_distance: 6000; max_cargo_weight: 18000; min_line_lenth: 2400], 'helicopters': [number: AN-2-111; max_distance: 600; max_cargo_weight: 1500; if_military: False]}
