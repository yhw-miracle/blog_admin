本篇文章介绍在`linux`系统（以 CentOS 7 系统和 Ubuntu16.04 系统为例）中源码编译安装`Python3.6.9`，并配置虚拟环境，其他系统和`Python`版本可以类似参考。

### 源码安装 python3.6.9

* 1.下载`Python 3.6.9`源码包；
	```bash
	wget https://www.python.org/ftp/python/3.6.9/Python-3.6.9.tgz
	```

* 2.解压`Python-3.6.9.tgz`；
	```bash
	tar zxvf Python-3.6.9.tgz
	```

* 3.准备编译环境；
	* CentOS 7 系统：
	```bash
	yum groupinstall 'Development Tools'
	yum install zlib-devel bzip2-devel  openssl-devel ncurses-devel
	```

	* Ubuntu16.04 Server 系统：
    ```bash
    sudo apt-get install build-essential libssl-dev libffi-dev libxml2 libxml2-dev libxslt1-dev zlib1g-dev libcurl4-openssl-dev libsqlite3-dev 
    ```

* 4.解压完，进入文件夹，编译安装，该过程耗时较长，大约耗时`20`到`30`分钟，可以泡杯茶等待；
	```bash
	cd Python-3.6.9/
	./configure --prefix=/usr/local/python3 --enable-optimizations # 据说 --enable-optimizations 配置项用于提高 Python 安装后的性能，但是会导致安装慢
	make
	make install
	```

![CentOS 7 系统中成功安装](images/2019/Jul/39.png)

> Ubuntu 16.04 Server 系统使用 `--enable-optimizations` 参数可能会出错，可以不加该参数。

* 5.创建`python3`和`pip3`命令；
	```bash
	ln -s /usr/local/python3/bin/python3.6 /usr/bin/python3
	ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
	```

* 6.更新`pip3`；
	```bash
	pip3 install --upgrade pip
	```

> 若在 ubuntu 16.04 server 系统中使用 pip 命令出现 lsb_release 报错，如图所示，解决方法如下。
> ```bash
> sudo rm /usr/bin/lsb_release
> ```

![lsb_release_error](images/2019/Jul/40.png)

### 配置虚拟环境

> **Q**: 为啥要配置虚拟环境，直接用`Python`解析器也可以开发呀？
> 
> **A**: 虚拟环境的作用可以配置多个开发环境，并且彼此不受影响，避免依赖包之间的冲突；另外，虚拟环境也便于管理开发环境，可以随意创建开发环境，方便开发。

* 1.安装`virtualenv`和`virtualenvwrapper`包；
	```bash
	pip3 install virtualenvwrapper
	```

* 2.配置`virtualenv`环境变量；
	```bash
	vi ~/.bashrc
	export WORKON_HOME=~/.virtualenvs #指定virtualenvwrapper环境的目录
	export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3 #指定virtualenvwrapper通过哪个python版本来创建虚拟环境
	source /usr/local/python3/bin/virtualenvwrapper.sh
	```

* 3.创建`virtualenv`命令；
	```bash
	ln -s /usr/local/python3/bin/virtualenv /usr/bin/virtualenv
	```

* 4.创建虚拟环境；
	```bash
	mkvirtualenv demo -p python3
	```

* 5.查看虚拟环境；
	```bash
	workon
	```

* 6.进入虚拟环境；
	```bash
	workon demo
	```

* 7.退出虚拟环境；
    ```bash
    deactivate
    ```

<hr />

* 文内资源
	* [python3.6.9 源码包](https://www.python.org/ftp/python/3.6.9/Python-3.6.9.tgz)

* 参考资源
	* [CentOS 系统安装 Python3](https://mp.weixin.qq.com/s/h5eb1nVZCdY6BrsD0hnQnA)
	* [Centos7 安装配置 python3 虚拟环境 virtualenvwrapper](https://www.jianshu.com/p/562ce3c2f3b8)
	* [Pipenv & 虚拟环境](https://pythonguidecn.readthedocs.io/zh/latest/dev/virtualenvs.html)
