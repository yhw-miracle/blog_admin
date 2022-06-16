
```c++
#if _MSC_VER >= 1600
#pragma execution_character_set("utf-8")
#endif

#include "mainwindow16.h"

MainWindow16::MainWindow16(QString title, QWidget *parent) : QMainWindow(parent)
{
    this->setWindowTitle(title);

    this->button1 = new QPushButton();
    this->button1->setText("恢复列表");
    this->button2 = new QPushButton();
    this->button2->setText("添加项");
    this->button3 = new QPushButton();
    this->button3->setText("插入项");
    this->button4 = new QPushButton();
    this->button4->setText("删除当前项");
    this->button5 = new QPushButton();
    this->button5->setText("清除列表");
    this->button6 = new QPushButton();
    this->button6->setText("清空文本");
    this->button7 = new QPushButton();
    this->button7->setText("显示 QStringList 数据");
    this->listView1 = new QListView();
    this->plainTextEdit1 = new QPlainTextEdit();

    this->groupBox1 = new QGroupBox();
    QVBoxLayout *layout1 = new QVBoxLayout();
    layout1->addWidget(this->button1);
    layout1->addWidget(this->button2);
    layout1->addWidget(this->button3);
    layout1->addWidget(this->button4);
    layout1->addWidget(this->button5);
    layout1->addWidget(this->listView1);
    this->groupBox1->setLayout(layout1);

    this->groupBox2 = new QGroupBox();
    QVBoxLayout *layout2 = new QVBoxLayout();
    layout2->addWidget(this->button6);
    layout2->addWidget(this->button7);
    layout2->addWidget(this->plainTextEdit1);
    this->groupBox2->setLayout(layout2);

    QWidget *widget1 = new QWidget();
    QHBoxLayout *layout3 = new QHBoxLayout();
    layout3->addWidget(this->groupBox1);
    layout3->addWidget(this->groupBox2);
    widget1->setLayout(layout3);
    this->setCentralWidget(widget1);

    this->label1 = new QLabel();
    this->statusBar1 = new QStatusBar();
    this->statusBar1->addWidget(this->label1);
    this->setStatusBar(this->statusBar1);

    this->connect(this->button1, SIGNAL(clicked()), this, SLOT(button1_clicked()));
    this->connect(this->button2, SIGNAL(clicked()), this, SLOT(button2_clicked()));
    this->connect(this->button3, SIGNAL(clicked()), this, SLOT(button3_clicked()));
    this->connect(this->button4, SIGNAL(clicked()), this, SLOT(button4_clicked()));
    this->connect(this->button5, SIGNAL(clicked()), this, SLOT(button5_clicked()));
    this->connect(this->button6, SIGNAL(clicked()), this, SLOT(button6_clicked()));
    this->connect(this->button7, SIGNAL(clicked()), this, SLOT(button7_clicked()));
    this->connect(this->listView1, SIGNAL(clicked(const QModelIndex&)), this, SLOT(listView1_clicked(const QModelIndex&)));

    this->strList1 << "111" << "222" << "333" << "444" << "555";
    this->stringListModel1 = new QStringListModel();
    this->stringListModel1->setStringList(this->strList1);
    this->listView1->setModel(this->stringListModel1);
}

void MainWindow16::button1_clicked()
{
    // 恢复列表
    this->listView1->setModel(this->stringListModel1);
}

void MainWindow16::button2_clicked()
{
    // 添加项
    this->stringListModel1->insertRow(this->stringListModel1->rowCount());
    QModelIndex index = this->stringListModel1->index(this->stringListModel1->rowCount() - 1, 0, QModelIndex());
    this->stringListModel1->setData(index, "new item", Qt::DisplayRole);
    this->listView1->setCurrentIndex(index);
}

void MainWindow16::button3_clicked()
{
    // 插入项;
    QModelIndex index = this->listView1->currentIndex();
    this->stringListModel1->setData(index, "new item", Qt::DisplayRole);
    this->listView1->setCurrentIndex(index);
}

void MainWindow16::button4_clicked()
{
    // 删除当前项
    QModelIndex index = this->listView1->currentIndex();
    this->stringListModel1->removeRow(index.row());
}

void MainWindow16::button5_clicked()
{
    // 清空列表
    this->stringListModel1->removeRows(0, this->stringListModel1->rowCount());
}

void MainWindow16::button6_clicked()
{
    // 清空文本
    this->plainTextEdit1->clear();
}

void MainWindow16::button7_clicked()
{
    // 显示 QStringList 数据
    this->plainTextEdit1->clear();
    foreach(QString str1, this->stringListModel1->stringList())
    {
        this->plainTextEdit1->appendPlainText(str1);
    }
}

void MainWindow16::listView1_clicked(const QModelIndex &index)
{
    this->label1->setText(QString("行:%1,列:%2").arg(index.row()).arg(index.column()));
}

```