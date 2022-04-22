# Задание 7.1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?


# import os
# dirs = ['my_project/settings', 'my_project/mainapp', 'my_project/adminapp', 'my_project/authapp']
# for dir in dirs:
#     os.makedirs(dir)

import os
dirs = ['my_project/settings', 'my_project/mainapp', 'my_project/adminapp', 'my_project/authapp']
for dir in dirs:
    if os.path.exists(dir):
        print(dir, 'директория существует')
    else:
        os.makedirs(dir)