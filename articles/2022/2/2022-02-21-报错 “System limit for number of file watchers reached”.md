
* 报错描述
```text
ENOSPC: System limit for number of file watchers reached, watch '/data/react_workspace/demo01/public/index.html'
```

报错内容是：文件监视程序的系统产生了限制，达到了默认的上限，需要增加限额。

* 解决

```bash
cat /proc/sys/fs/inotify/max_user_watch
sysctl fs.inotify.max_user_watches = 50000
sysctl -p
echo fs.inotify.max_user_watches = 50000 | tee -a /etc/sysctl.conf
sysctl -p
```