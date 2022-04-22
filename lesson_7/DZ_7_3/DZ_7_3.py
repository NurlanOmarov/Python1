# Задание 7.3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача, которая решена, например, во фреймворке django.

#Создаем структуру папок и файлов
import os
import shutil

# dirs = ['my_project/settings', 'my_project/adminapp',
#         'my_project/mainapp/templates/mainapp', 'my_project/authapp/templates/authapp']
# for dir in dirs:
#     os.makedirs(dir)
#
# files = {'my_project/settings': ['--__init__.py', 'dev.py', 'prod.py'],
#          'my_project/mainapp': ['__init__.py', 'models.py', 'views.py'],
#          'my_project/mainapp/templates/mainapp': ['base.html', 'index.html'],
#          'my_project/authapp': ['__init__.py', 'models.py', 'views.py'],
#          'my_project/authapp/templates/authapp': ['base.html', 'index.html']}

# for dir, files in files.items():
#     for file in files:
#         file_path = os.path.join(dir, file)
#         open(file_path, 'w').close()

my_dir = 'templates'
if not os.path.exists(my_dir):
    os.mkdir(my_dir)

folder = r'my_project'
files = []

for r, d, f in os.walk(folder):
    for file in f:
        if '.html' in file:
            files.append(os.path.join(r, file))
for path in files:
    folder_new = os.path.join(my_dir, os.path.basename(os.path.dirname(path)))
    if not os.path.exists(folder_new):
        os.mkdir(folder_new)
    save_path = os.path.join(folder_new, os.path.basename(path))
    shutil.copy(path, save_path)