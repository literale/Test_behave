# Created by Literal at 15.10.2018
Feature: Проверка ВК

  Scenario: Проверка логина
      When Зашли на сайт "https://vk.com/"
      And Кликаем на кнопку Логина
      And Прверяем, что не залогинились
      Then Вводим логин "Testssa@yandex.ru"
        And Кликаем на кнопку Логина
        And Прверяем, что не залогинились
        Then Вводим пароль "1234567T"
          And Кликаем на кнопку Логина
          Then Приверяем страницу
          And Сделаем скриншот "new_page_sc" и отправим на почту "Literallle@yandex.ru"
          And Нажимаем кнопку регистрации
          And Опять проверяем страницу

