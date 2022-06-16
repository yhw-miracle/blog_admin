* 软件下载
下载地址为：[https://downloads.mysql.com/archives/community/](https://downloads.mysql.com/archives/community/)，我选择的是社区服务版本5.7.17，且是解压版到的。

* 配置环境变量
将 mysql 的 bin 目录（如：D:\MySQL\mysql-5.7.17-winx64\bin）放到 Path 里。操作：我的电脑—>属性—>高级系统设置—>环境变量—>系统变量—>Path。

* 配置 my-default.ini 文件
在 my-default.ini 文件里添加如下代码：

```text
[mysqld]
basedir = D:\MySQL\mysql-5.7.17-winx64（mysql 的目录）
datadir = D:\MySQL\mysql-5.7.17-winx64\data（mysql 的目录\data）
```

如果 mysql 目录下没有 data 目录，自行在在 mysql 目录下新建 data 文件夹。

![](images/2017/qt0SrHtVggeA0ncYHTYoISs6.png)

![](images/2017/sSfgZ0WAahadPJaDTflA0TPy.png)

* 初始化 mysql 服务
在 Windows PowerShell 或 CMD 里切换到 mysql 目录下的 bin 目录，执行下面的命令。

```bash
mysqld --initialize-insecure --user=mysql
```

* 注册 mysql 服务
在 Windows PowerShell 或 CMD 里切换到 mysql 目录下的 bin 目录，执行下面的命令。

```bash
mysqld --install mysql --defaults-file=d:\MySQL\mysql-5.7.17-winx64\my-default.ini
```

记得将路径切换成自己的。

* 启动 mysql 服务
在 Windows PowerShell 或 CMD 里切换到 mysql 目录下的 bin 目录，执行下面的命令。

```bash
net start mysql
```

![](images/2017/C3OfsPgYjHKQUqBv_78wTtGX.png)

* 修改 root 登录密码
解压版安装时，初始情况 mysql 登录是没有密码，需要先登录数据库，再修改 root 登录密码。登录 mysql 数据库的命令是：

```bash
mysql -u root -p
```

修改 root 密码的命令是：

```bash
update mysql.user set authentication_string=password('123') where user='root';
```

修改完 root 登录密码需要重启 mysql 数据库，密码才生效。

* 说明
若从第四步开始出错，可以以管理员方式打开 Windows PowerShell 或 CMD 软件，再依次执行命令。若在安装 myql 数据库时出错了，可以将安装错的服务删除，并清空 data 目录。删除服务的命令如下。

```bash
mysqld --remove mysql
```

* 开始使用 mysql 数据库吧。
操作 mysql 数据库可以是终端加上脚本，也可以是 GUI 软件。
