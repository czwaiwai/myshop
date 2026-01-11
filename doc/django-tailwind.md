# django 关联 tailwind
1、 安装 django-tailwind
```bash
pip install django-tailwind
```
2、添加配置到setting.py
```python
INSTALLED_APPS = [
    # ...
    "tailwind",
]
```
3、创建Tailwind app
```bash
python manage.py tailwind init
```
4、添加生成的app到INSTALLED_APPS
```python
INSTALLED_APPS = [
    # ...
    "tailwind",
    "theme",  # 你自己定义的名称
]
```
5、配置
```python
TAILWIND_APP_NAME = "theme"
```
6、安装Tailwind CSS依赖
```bash
python manage.py tailwind install
```
7、启动开发
```bash
python manage.py tailwind dev
```
8、在模板中使用Tailwind类
```html
{% load tailwind_tags %}
{% tailwind_css %}

<h1 class="text-4xl font-bold text-blue-600">Hello Tailwind!</h1>
```
