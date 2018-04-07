# Redis数据库 - REmote DIctionary Server

- 日志型、Key-Value数据库

## 支持的存储方式

- 基于网络 - 分布式
- 基于内存 - 快速存取
- 基于硬盘 - 持久化

## 支持的数据结构

- string
- hashMap
- list
- sets
- sorted sets

## 安装、启动、关闭(Ubuntu)

- 安装

        $ sudo apt-get update
        $ sudo apt-get install redis-server

- 启动服务

        $ redis-server

    ![redis-server.png](images/redis-server.png)
- 启动客户端

        $ redis-cli
        $ redis-cli -h host -p post -a password

    ![redis-cli.png](images/redis-cli.png)
- 后台启动服务

    nohup命令: 不挂起

    命令后加 &: 后台运行

        $ nohup redis-server &

    jobs命令: 查看后台运行的进程

    -l 参数: 显示其进程号PID

        $ jobs
        $ jobs -l

    ![nohup-jobs.png](images/nohup-jobs.png)

    后台进程的输出会重定向到nohup.out文件

        $ cat nohup.out

    ![nohup-out.png](images/nohup-out.png)

- 通过 service 启动和关闭

    启动服务

        $ sudo service redis-server start

    使用客户端

        $ redis-cli

    关闭服务

        $ sudo service redis-server stop

## 配置

- 启动时使用配置文件

        $ redis-server /etc/redis/redis.conf

- 通过修改配置文件 /etc/redis/redis.conf 内容配置
- 通过客户端命令进行配置

        $ redis-cli
        127.0.0.1:6379> config get [config-name]
        1) "[config-name]"
        2) "[value]"
        127.0.0.1:6379> config set [config-name] [new-value]
        OK

    ![redis-config.png](images/redis-config.png)

- 常用配置

    ![redis-prop1](images/redis-prop1.png)
    ![redis-prop2](images/redis-prop2.png)
    ![redis-prop3](images/redis-prop3.png)
    ![redis-prop4](images/redis-prop4.png)
    ![redis-prop5](images/redis-prop5.png)

## 数据结构

### string

    127.0.0.1:6379> set foo bar
    OK
    127.0.0.1:6379> get foo
    "bar"

![redis-datastruc-string](images/redis-datastruc-string.png)

### list

    127.0.0.1:6379> lpush ldb foo
    (integer) 1
    127.0.0.1:6379> lrange ldb 0 10
    1) "foo"

![redis-datastruc-list](images/redis-datastruc-list.png)

### hash

    127.0.0.1:6379> hmset hdb key1 hello key2 world
    OK
    127.0.0.1:6379> hget hdb key1
    "hello"
    127.0.0.1:6379> hget hdb key2
    "world"
    127.0.0.1:6379> hgetall hdb
    1) "key1"
    2) "hello"
    3) "key2"
    4) "world"

![redis-datastruc-hash.png](images/redis-datastruc-hash.png)

### set

    127.0.0.1:6379> sadd sdb foo bar
    (integer) 2
    127.0.0.1:6379> smenbers sdb
    1) "bar"
    2) "foo"

![redis-datastruc-set.png](images/redis-datastruc-set.png)

### sorted set

    127.0.0.1:6379> zadd zdb 0 foo 0 bar 1 foo
    (integer) 2
    127.0.0.1:6379> zrangebyscore zdb 0 10
    1) "bar"
    2) "foo"
    127.0.0.1:6379> zrangebyscore zdb 1 10
    1) "foo"

![redis-datastruc-zset.png](images/redis-datastruc-zset.png)

## KEY 管理

    127.0.0.1:6379> keys *

![redis-key-list.png](images/redis-key-list.png)

    127.0.0.1:6379> del key-name

![redis-key-del.png](images/redis-key-del.png)
