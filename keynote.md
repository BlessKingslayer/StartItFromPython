1. with ClassA as ObjB
    * 首先通过调用ClassA中的__enter__()方法并返回句柄ObjB用于操作
    * 当with代码块中的代码执行完以后调用ClassA中的__exit__()方法结束
    * 备注: 普通的对象释放后会调用类中的__del__方法

2. functools.update_wrapper(functionA, functionB)
    * 它可以把被封装函数(functionB)的__name__、__module__、__doc__和 __dict__都复制到封装函数(即经装饰器后返回的函数)(functionA)去

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

5. __class__ 对象的类属性储存在这里
    * 类方法用装饰器 @classmethod 修饰