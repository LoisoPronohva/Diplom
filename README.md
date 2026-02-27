1-загрузить файлы на компьютер

2-открыть файлы проекта (мною тестировалось в PyCharm, с подключением Ubunta через wsl)

3-запустить Linux

4-синхрониировать проект с Linux

5-активировать виртуально. окружение 
source venv/bin/activate

6-построить докер образ.
docker-compose build

7-запустить контейнеры.
docker-compose up -d

8-выполнить миграци в контейнере.
docker-compose exec web python manage.py migrate

9-создать superuser.
docker-compose exec web python manage.py createsuperuser

10-проверить работоспособность


