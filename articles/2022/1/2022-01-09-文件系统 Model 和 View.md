
```c++
#if _MSC_VER >= 1600
#pragma execution_character_set("utf-8")
#endif

#include "mainwindow15.h"

MainWindow15::MainWindow15(QString title, QWidget *parent) : QMainWindow(parent)
{
    this->setWindowTitle(title);

    this->treeView1 = new QTreeView();
    QVBoxLayout *layout1 = new QVBoxLayout();
    layout1->addWidget(this->treeView1);
    this->groupBox1 = new QGroupBox();
    this->groupBox1->setLayout(layout1);

    this->listView1 = new QListView();
    QVBoxLayout *layout2 = new QVBoxLayout();
    layout2->addWidget(this->listView1);
    this->groupBox2 = new QGroupBox();
    this->groupBox2->setLayout(layout2);

    this->tableView1 = new QTableView();
    QVBoxLayout *layout3 = new QVBoxLayout();
    layout3->addWidget(this->tableView1);
    this->groupBox3 = new QGroupBox();
    this->groupBox3->setLayout(layout3);

    this->splitter1 = new QSplitter();
    this->splitter1->setOrientation(Qt::Vertical);
    this->splitter1->addWidget(this->groupBox2);
    this->splitter1->addWidget(this->groupBox3);
    this->splitter2 = new QSplitter();
    this->splitter2->setOrientation(Qt::Horizontal);
    this->splitter2->addWidget(this->groupBox1);
    this->splitter2->addWidget(this->splitter1);
    this->setCentralWidget(this->splitter2);

    this->connect(this->treeView1, SIGNAL(clicked(QModelIndex)), this, SLOT(treeView1_clicked_setRootIndex(QModelIndex)));

    this->fileSystemModel1 = new QFileSystemModel();
    this->fileSystemModel1->setRootPath(QDir::currentPath());
    this->treeView1->setModel(this->fileSystemModel1);
    this->listView1->setModel(this->fileSystemModel1);
    this->tableView1->setModel(this->fileSystemModel1);
}

void MainWindow15::treeView1_clicked_setRootIndex(const QModelIndex &index)
{
    this->listView1->setRootIndex(index);
    this->tableView1->setRootIndex(index);

    QString str1 = "";
    this->fileSystemModel1->isDir(index);
    str1 += QString("是否为目录:%1\n").arg(this->fileSystemModel1->isDir(index));
    str1 += "文件路径:" + this->fileSystemModel1->filePath(index) + "\n";
    str1 += "文件类型:" + this->fileSystemModel1->type(index) + "\n";
    str1 += "文件名称:" + this->fileSystemModel1->fileName(index) + "\n";
    int s = this->fileSystemModel1->size(index);
    if(s/1024 < 1024)
    {
        str1 += "文件大小:" + QString("%1 KB ").arg(s/1024);
    }
    else
    {
        str1 += "文件大小:" + QString("%1 MB").arg(s/1024/1024);
    }

    this->messageBox1->information(this, "提示", str1, QMessageBox::Ok);
}

```