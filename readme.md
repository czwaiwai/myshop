### 创建项目目录

```bash
mkdir demoproject
```

### 创建虚拟环境

```bash
# 一般创建.venv作为虚拟环境
python3.12 -m venv .venv
```

### 激活虚拟环境

```bash
source venv/bin/activate
```

### 使用 uv 创建虚拟环境

```bash
# 创建指定python版本的虚拟环境
uv venv --python 3.12
# 初始化项目
uv init
# 添加包
uv add django==5.2.3 --index https://mirrors.aliyun.com/pypi/simple/
```

### 项目中配置国内源

```bash
# 在pyproject.toml中添加以下内容， 清华源为主力，阿里云为备胎
[[tool.uv.index]]
# name其实可以不写
name = "tsinghua"
url = "https://pypi.tuna.tsinghua.edu.cn/simple"
default = true

[[tool.uv.index]]
name = "aliyun"
url = "https://mirrors.aliyun.com/pypi/simple/"
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

### 管理项目依赖

安装完所需依赖后执行，将项目依赖导入到 requirements.txt

```bash
pip freeze > requirements.txt
```

导入所需依赖，引入项目后执行

```bash
pip install -r requirements.txt
```

### 当数据库同步出现问题时
```bash
# 清除迁移历史记录
python manage.py migrate --fake app_name zero

# 查看当前的migration进度，此时文件前的 [x] 变成了[ ]
python manage.py showmigrations app_name

#删除app-migrations下除__init__.py的其他文件

#执行makemigrations，程序会再次为这个app 生成 0001_initial.py 文件

python manage.py makemigrations app_name

# 把当前数据库的状态作为初始状态
python manage.py migrate --fake-initial app_name
```

### 商城的路由结构

/｜/home 首页
/search 搜索
/cart 购物车
/product/detail/:id 商品详情
/product/categoryId/ 商品大分类

需要完成的内容
后台部分

    商品的添加    
    sku商品添加同时添加相关的属性值，优化管理关联属性的方式
    地址表关联省市区
    订单表的管理
    用户购物车物品列表查看
    用户头像关联显示
    头像上传路径优化
    订单对接对应的支付方式

前端部分完成一个标准的商城c端

    商城首页
    商城分类查询
    商城商品总览
    用户购物车
    购买流程
    个人中心
    个人订单显示
    发货地址填写
    支付方式对接

扩展部分 

    国际化支持
    用户积分逻辑
    会员等级
    商品秒杀
    活动券发放


    
    
    






### 配合 Django 的前端框架

Alpine.js htmx tailwind css

### 数据库使用偏好

PostgreSQL， redis
