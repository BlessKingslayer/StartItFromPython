1. with ClassA as ObjB
    * 首先通过调用ClassA中的__enter__()方法并返回句柄ObjB用于操作
    * 当with代码块中的代码执行完以后调用ClassA中的__exit__()方法结束
    * 备注: 普通的对象释放后会调用类中的__del__方法

2. functools.update_wrapper(functionA, functionB)
    * 它可以把被封装函数(functionB)的__name__、__module__、__doc__和 __dict__都复制到封装函数(即经装饰器后返回的函数)(functionA)去
    * 或者在装饰器内部 wrapper 函数前加上 @functools.wraps(func) -- func 为被装饰的函数对象

3. Python提供了__future__模块，把下一个新版本的特性导入到当前版本

4. super() 可以显示调用父类中的方法
    ```python
    class C(B):
    def method(self, arg):
        super().method(arg)    
        # This does the same thing as:
        # super(C, self).method(arg)
    ```
    * how to design cooperative classes using super():
    * https://rhettinger.wordpress.com/2011/05/26/super-considered-super/

5. __class__ 类对象实例的类属性储存在这里
    * 类方法用装饰器 @classmethod 修饰
    * @classmethod @staticmethod 区别:
        * 两者都是属于类的方法，但是@classmethod需要传递类对象(cls)作为第一个参数，@staticmethod不需要, 普通函数需要传递类对象实例作为第一个参数(self)
        * 类也可以调用普通函数，但是需要把类的实例作为第一个参数传进去
        * 类对象实例 和 类都能调用@classmethod 或 @staticmethod 修饰的方法
        * 可以使用静态方法作为另一种形式的构造函数
    ```python
    class A(object):
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))
        print('self:', self)
    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))
        print('cls:', cls)
    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)    
    a = A()
    ```

6. lambda 表达式, 匿名函数(lambda argument_list:单方返回值表达式)
    # region 展示lambda表达式的作用
        ```python
        # 不使用lambda
        #!/usr/bin/envpython
        def comp(x):
            return x["age"]
        li=[{"age":20,"name":"def"},{"age":25,"name":"abc"},{"age":10,"name":"ghi"}]
        li=sorted(li, key=comp)
        print(li)

        # 使用lambda
        li=[{"age":20,"name":"def"},{"age":25,"name":"abc"},{"age":10,"name":"ghi"}]
        li=sorted(li, key=lambda x:x['age'])
        print(li)
        ```
    # endregion
    * lambda 参数: 
        * lambda x, y: x*y；函数输入是x和y，输出是它们的积x*y
        * lambda:None；函数没有输入参数，输出是None
        * ambda *args: sum(args); 输入是任意个数的参数，输出是它们的和(隐性要求是输入参数必须能够进行加法运算)
        * lambda **kwargs: 1；输入是任意键值对参数，输出是1

7. Composite Pattern（组合模式）

8. isinstance(object, 需要检测的类型)
    * isinstance((x for x in range(10)), Iterable) => True 判断是不是迭代器

9. 处理windows中print乱码或者gbk报错问题
    * import sys, io
    * sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

10. python -u xxx.py 禁用stdout缓冲

11. redis 

12. django
    * windows下使用cli创建django项目，执行时脚本名不带.py  django-admin
    * path 不支持正则表达式， 需要使用re_path
    * 创建和同步数据库:         
        * python manage.py makemigrations rangoapp  #用来检测数据库变更和生成数据库迁移文件
        * python manage.py migrate          #用来迁移数据库
        * python manage.py sqlmigrate rangoapp 0001 # 用来把数据库迁移文件转换成数据库语言(最后一个参数是migration_name)
        * python manage.py createsuperuser  #创建初始的超级用户
        * python manage.py shell            # 进入shell模式