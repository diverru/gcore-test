На выполнение 1.5 часа. Код д.б. на github
Нужно проинициировать git, создать новый пустой проект на django.
В этом проекте необходимо реализовать ендпоинт, который будет выводить следующую информацию в соответствии с созданным репозиторием:
```javascript
{
    "commit": "aad95f46b5ee6abcd99c3a165aa20297642d38ec", // хеш хед-коммита текущей ветки
    "commit_date": "2018-04-12T07:53:19Z", // дата хед-коммита текущей ветки
    "branch": "feature/adding_status_info", // текущая ветка
    "version": "release_v1.16.1", // максимальный тег хед-коммита
    "started": "2018-04-12T09:33:25Z", // дата и время запуска приложения
    "uptime_seconds": 69470 // количество секунд между текущим временем на момент запроса и started
}
```
