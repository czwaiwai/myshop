### 创建项目目录

```bash
mkdir demoproject
```

### 创建虚拟环境

```bash
python3.12 -m venv env
```

### 安装 django

```bash
pip install django
```

### 创建 django 项目

```bash
django-admin startproject translate_xyz
# 在当前目录下创建后面追加点.
django-admin startproject translate_xyz .
```

### 运行项目

```bash

python manage.py runserver
```

### 检查数据变更

```bash
python manage.py makemigrations
```

### 添加后台模块

```bash
python manage.py migrate
```

### 添加系统管理员

```bash
python manage.py createsuperuser
```

### 添加应用

```bash
#创建名叫api的应用
python manage.py startapp api
```

### 创建应用的 models，创建对应的表

```bash
#在应用的admin中添加 admin.site.register(UserGame)
#执行
python manage.py makemigrations
# 让数据库的改动生效
python manage.py migrate
```

### 商城的路由结构

/｜/home 首页
/search 搜索
/cart 购物车
/product/detail/:id 商品详情
/product/categoryId/ 商品大分类
