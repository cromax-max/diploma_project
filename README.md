//![visitor badge](https://visitor-badge-reloaded.herokuapp.com/badge?page_id=cromax-max/diploma-project&color=55acb7&style=flat&logo=Github&text=Welcome!)
### Дипломное задание представляет собой автоматизацию тестирования мобильного приложения(Android)

### Задачи
1. Провести ручное тестирование мобильного приложения "Мобильный хоспис";
2. Составить чек-лист для проверки приложения;
3. Составить тест-кейсы для проверки приложения;
4. Автоматизировать проверку тест-кейсов по чек-листу;
5. Составить отчеты о тестировании;

__Описание приложения__  
Приложение предоставляет функционал по работе с претензиями хосписа и включает в себя:

- Информацию о претензиях и функционал для работы с ними;
- Новостную сводку хосписа;
- Тематические цитаты;

### Запуск тестов
__Установка__  
- appium v2.x.x `npm i -g appium@next`
- driver uiautomator2 `appium driver install uiautomator2`

__Запуск__  
- Клонировать репо
- Установить зависимости `pip install -r requirements.txt`
- Подключить устройство или запустить эмулятор (Android)
- Запуск тестов `python -m pytest --alluredir=./tmp/allure_report ./tests`

__Отчет__
- Просмотр отчёта `allure serve ./tmp/allure_report`  
  [как установить allure](https://docs.qameta.io/allure-report/#_installing_a_commandline)
