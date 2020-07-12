
# twisted
scrapy---twisted异步IO框架(实现数据的异步写入)
数据库pymysql的commit()和execute()在提交数据时，都是同步提交至数据库，由于scrapy框架数据的解析和异步是多线程的，所以scrapy的数据解析速度，要远高于数据写入数据库的速度。如果数据写入过慢，会造成数据库写入的阻塞，影响数据库写入的效率。

- 通过多线程异步的形式对数据进行写入，可以提高数据的写入速度。
- 使用twisted异步IO框架，可以实现数据的异步写入。

Our code -》Twisted code -》Reactor Loop -》Callback

# 异步 多任务 多进程
## 多进程
父进程和子进程
多线程、多线程、协程的目的都是希望尽可能多处理任务

### 产生新的进程可以使用一下方式：
- os.fork()
- multiprocessing.Process()

多进程的问题：进程的父子关系

#### os.fork()
```
res = os.fork()
# res = os.fork()
print(f'res == {res}')

if res == 0:
    print(f'我是子进程，我的pid是：{os.getpid()} 我的父进程id是：{os.getppid()}')
else:
    print(f'我是父进程，我的pid是:{os.getpid()}')
```

-  fork()运行时，会有2个返回值，返回值为大于0时，此进程为父进程，且返回的数字为子进程的PID；当返回值为0时，此进程为子进程。
- 注意：父进程结束时，子进程并不会随父进程立刻结束。同样，父进程不会等待子进程执行完。
- 注意：os.fork()无法在windows上运行。

#### multiprocessing.Process()


```
multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={})

# - group：分组，实际上很少使用
# - target：表示调用对象，你可以传入方法的名字
# - name：别名，相当于给这个进程取一个名字
# - args：表示被调用对象的位置参数元组，比如target是函数a，他有两个参数m，n，那么args就传入(m, n)即可
# - kwargs：表示调用对象的字典
```

