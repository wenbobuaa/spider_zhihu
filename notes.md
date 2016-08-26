### Python3 的bytes
-bytes个str类型明显的区分开

## 与Python2 的不同
-bytes + str 的运算不被允许
-str全部使用Unicode编码
-bytes.decode('')->str
-str.encode('')->bytes

### django的分组查询
-values
    services = Service.objects.filter().values().annotate()
-sql
    services = Service.objects.raw('Select * from api_service group by ')
    
### 一个错误
-Models aren't loaded yet.
    Service.objects.all().values('doctor')
    Django 测试依赖于 DJANGO_SETTINGS_MODULE 环境变量. 如果我们想要使用单独的 PY 脚本来测试 Django,那么应该在我们的程序开始初始化Django环境.否则就会报出 AppRegistryNotReady 异常.
    可以使用
    import django
    django.setup()
    原因是我在ipython下直接做的，后来却是manage.py shell，没法复现。