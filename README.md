# Коллекция my_own_namespace.yandex_cloud_elk

Выполнил: **Овсянников Сергей**

## Что сделано
- Создан модуль `my_own_module` (создаёт файл по пути `path` с содержимым `content`).
- Создана роль `my_own_role`, использующая этот модуль.
- Роль параметризована через `defaults` (`path`, `content`).
- Коллекция собрана (`ansible-galaxy collection build`).
- Установка из локального архива и запуск плейбука выполнены успешно.
- Идемпотентность подтверждена (повторный запуск – `changed=0`).

## Скриншоты
Все скриншоты лежат в папке `screenshots/` этого репозитория.

1. `01-ansible-env.png` – настройка окружения Ansible  
2. `02-module-test.png` – первый запуск модуля  
3. `03-idempotence.png` – повторный запуск (changed=0)  
4. `04-collection-build.png` – сборка коллекции  
5. `05-collection-install.png` – установка из архива  
6. `06-playbook-run.png` – первый запуск плейбука с ролью  
7. `06b-idempotence.png` – повторный запуск плейбука (changed=0)  
8. `07-file-content.png` – содержимое созданного файла

## Ссылка на репозиторий
[https://github.com/sergey-281296/my_own_collection](https://github.com/sergey-281296/my_own_collection)
