# Коллекция my_own_namespace.yandex_cloud_elk

Выполнил: **Овсянников Сергей**

## Скриншоты выполнения

### 1. Настройка окружения Ansible
![01-ansible-env](screenshots/01-ansible-env.png)

### 2. Первый запуск модуля (changed=1)
![02-module-test](screenshots/02-module-test.png)

### 3. Повторный запуск модуля (changed=0) – идемпотентность
![03-idempotence](screenshots/03-idempotence.png)

### 4. Сборка коллекции
![04-collection-build](screenshots/04-collection-build.png)

### 5. Установка коллекции из архива
![05-collection-install](screenshots/05-collection-install.png)

### 6. Первый запуск плейбука с ролью (changed=1)
![06-playbook-run](screenshots/06-playbook-run.png)

### 7. Повторный запуск плейбука (changed=0) – идемпотентность
![06b-idempotence](screenshots/06b-idempotence.png)

### 8. Содержимое созданного файла
![07-file-content](screenshots/07-file-content.png)

## Что сделано
- Создан модуль `my_own_module` (создаёт файл по пути `path` с содержимым `content`).
- Создана роль `my_own_role`, использующая этот модуль.
- Роль параметризована через `defaults` (`path`, `content`).
- Коллекция собрана (`ansible-galaxy collection build`).
- Установка из локального архива и запуск плейбука выполнены успешно.
- Идемпотентность подтверждена (повторный запуск – `changed=0`).

## Ссылка на репозиторий
[https://github.com/sergey-281296/my_own_collection](https://github.com/sergey-281296/my_own_collection)
