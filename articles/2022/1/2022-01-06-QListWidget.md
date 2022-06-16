
```c++
#if _MSC_VER >= 1600
#pragma execution_character_set("utf-8")
#endif

#include "mainwindow12.h"
#include <QList>

MainWindow12::MainWindow12(QString title, QWidget *parent) : QMainWindow(parent)
{
    this->setWindowTitle(title);

    this->action1 = new QAction();
    this->action1->setText("初始化列表");
    this->toolButton1 = new QToolButton();
    this->toolButton1->setText(this->action1->text());
    this->toolButton1->setDefaultAction(this->action1);

    this->action2 = new QAction();
    this->action2->setText("清除列表");
    this->toolButton2 = new QToolButton();
    this->toolButton2->setText(this->action2->text());
    this->toolButton2->setDefaultAction(this->action2);

    this->action3 = new QAction();
    this->action3->setText("插入项");
    this->toolButton3 = new QToolButton();
    this->toolButton3->setText(this->action3->text());
    this->toolButton3->setDefaultAction(this->action3);

    this->action4 = new QAction();
    this->action4->setText("添加项");
    this->toolButton4 = new QToolButton();
    this->toolButton4->setText(this->action4->text());
    this->toolButton4->setDefaultAction(this->action4);

    this->action5 = new QAction();
    this->action5->setText("删除当前项");
    this->toolButton5 = new QToolButton();
    this->toolButton5->setText(this->action5->text());
    this->toolButton5->setDefaultAction(this->action5);

    this->setToolButton6();

    this->action7 = new QAction();
    this->action7->setText("退出");

    this->toolBar1 = new QToolBar();
    this->toolBar1->setWindowTitle("QListWidget 操作");
    QList<QAction* > actions;
    actions.append(this->action1);
    actions.append(this->action2);
    actions.append(this->action3);
    actions.append(this->action4);
    actions.append(this->action5);
    actions.append(this->action6);
    actions.append(this->action7);
    this->toolBar1->addActions(actions);
    this->addToolBar(this->toolBar1);
    // 取消工具栏的右键菜单
    this->setContextMenuPolicy(Qt::NoContextMenu);

    this->toolBox1 = new QToolBox();
    this->toolBox1->addItem(this->setToolBox1ItemWidget1(), "QListWidget 操作");
    this->toolBox1->addItem(this->setToolBox1ItemWidget2(), "QTreeWidget 操作");
    this->toolBox1->addItem(this->setToolBox1ItemWidget3(), "QTableWidget 操作");

    this->tabWidget1 = new QTabWidget();
    this->tabWidget1->addTab(this->setTabWidget1ItemWidget1(), "QListWidget");
    // 设置右键菜单策略
    this->listWidget1->setContextMenuPolicy(Qt::CustomContextMenu);
    this->tabWidget1->addTab(this->setTabWidget1ItemWidget2(), "QTreeWidget");
    this->tabWidget1->addTab(this->setTabWidget1ItemWidget3(), "QTableWidget");

    this->splitter1 = new QSplitter();
    this->splitter1->setOrientation(Qt::Horizontal);
    this->splitter1->addWidget(this->toolBox1);
    this->splitter1->addWidget(this->tabWidget1);
    this->splitter1->show();

//    QHBoxLayout *layout1 = new QHBoxLayout();
////    layout1->addWidget(this->toolBox1);
//    layout1->addWidget(this->splitter1);
////    layout1->addWidget(this->tabWidget1);
//    QVBoxLayout *layout2 = new QVBoxLayout();
////    layout2->addWidget(this->toolBar1);
//    layout2->addLayout(layout1);
//    QWidget* mainWindowWidget = new QWidget();
//    mainWindowWidget->setLayout(layout2);
    this->setCentralWidget(this->splitter1);

    this->connect(this->action1, SIGNAL(triggered()), this, SLOT(action1_triggered()));
    this->connect(this->action2, SIGNAL(triggered()), this, SLOT(action2_triggered()));
    this->connect(this->action3, SIGNAL(triggered()), this, SLOT(action3_triggered()));
    this->connect(this->action4, SIGNAL(triggered()), this, SLOT(action4_triggered()));
    this->connect(this->action5, SIGNAL(triggered()), this, SLOT(action5_triggered()));
    this->connect(this->action6, SIGNAL(triggered()), this, SLOT(action6_triggered()));
    this->connect(this->action7, SIGNAL(triggered()), this, SLOT(action7_triggered()));
    this->connect(this->selectAllAction, SIGNAL(triggered()), this, SLOT(selectAllAction_triggered()));
    this->connect(this->selectNoneAction, SIGNAL(triggered()), this, SLOT(selectNoneAction_triggered()));
    this->connect(this->selectReverseAction, SIGNAL(triggered()), this, SLOT(selectReverseAction_triggered()));
    this->connect(this->checkBox1, SIGNAL(clicked(bool)), this, SLOT(checkBox1_clicked(bool)));
    this->connect(this->listWidget1, SIGNAL(currentItemChanged(QListWidgetItem*, QListWidgetItem*)), this, SLOT(listWidget1_currentItemChanged(QListWidgetItem*, QListWidgetItem*)));
    this->connect(this->listWidget1, SIGNAL(customContextMenuRequested(const QPoint)), this, SLOT(listWidget1_customContextMenuRequested(const QPoint)));

}

void MainWindow12::setToolButton6()
{
    this->action6 = new QAction();
    this->action6->setText("项选择");
    this->toolButton6 = new QToolButton();
    this->toolButton6->setText(this->action6->text());
    this->toolButton6->setDefaultAction(this->action6);
    QMenu *menu1 = new QMenu();

    this->selectAllAction = new QAction();
    this->selectAllAction->setText("全选");
    this->selectAllToolButton = new QToolButton();
    this->selectAllToolButton->setText(this->selectAllAction->text());
    this->selectAllToolButton->setDefaultAction(this->selectAllAction);
    menu1->addAction(this->selectAllAction);

    this->selectNoneAction = new QAction();
    this->selectNoneAction->setText("全不选");
    this->selectNoneToolButton = new QToolButton();
    this->selectNoneToolButton->setText(this->selectNoneAction->text());
    this->selectNoneToolButton->setDefaultAction(this->selectNoneAction);
    menu1->addAction(this->selectNoneAction);

    this->selectReverseAction = new QAction();
    this->selectReverseAction->setText("反选");
    this->selectReverseToolButton = new QToolButton();
    this->selectReverseToolButton->setText(this->selectReverseAction->text());
    this->selectReverseToolButton->setDefaultAction(this->selectReverseAction);
    menu1->addAction(this->selectReverseAction);
    this->action6->setMenu(menu1);
//    this->toolButton6->setMenu(menu1);
    // QToolButton::DelayedPopup 不会弹出菜单
//    this->toolButton6->setPopupMode(QToolButton::DelayedPopup);
    this->toolButton6->setPopupMode(QToolButton::MenuButtonPopup);
//    this->toolButton6->setPopupMode(QToolButton::InstantPopup);
}

QWidget* MainWindow12::setToolBox1ItemWidget1()
{
    QWidget *toolBox1ItemWidget1 = new QWidget(this->toolBox1);
    QGridLayout *layout1 = new QGridLayout();
    layout1->addWidget(this->toolButton1, 0, 0);
    layout1->addWidget(this->toolButton2, 1, 0);
    layout1->addWidget(this->toolButton3, 2, 0);
    layout1->addWidget(this->toolButton4, 4, 0);
    layout1->addWidget(this->toolButton5, 5, 0);
    toolBox1ItemWidget1->setLayout(layout1);
    return toolBox1ItemWidget1;
}

QWidget* MainWindow12::setToolBox1ItemWidget2()
{
    QWidget *toolBox1ItemWidget2 = new QWidget(this->toolBox1);
    return toolBox1ItemWidget2;
}

QWidget* MainWindow12::setToolBox1ItemWidget3()
{
    QWidget *toolBox1ItemWidget3 = new QWidget(this->toolBox1);
    return toolBox1ItemWidget3;
}

QWidget* MainWindow12::setTabWidget1ItemWidget1()
{
    QWidget *tabWidget1ItemWidget1 = new QWidget(this->tabWidget1);

    this->label1 = new QLabel();
    this->label1->setText("当前项变化");
    this->lineEdit1 = new QLineEdit();
    this->checkBox1 = new QCheckBox();
    this->checkBox1->setText("可编辑");
    QHBoxLayout *layout1 = new QHBoxLayout();
    layout1->addWidget(this->label1);
    layout1->addWidget(this->lineEdit1);
    layout1->addWidget(this->checkBox1);

    QHBoxLayout *layout2 = new QHBoxLayout();
    layout2->addWidget(this->toolButton6);
    layout2->addWidget(this->selectAllToolButton);
    layout2->addWidget(this->selectNoneToolButton);
    layout2->addWidget(this->selectReverseToolButton);

    this->listWidget1 = new QListWidget();
    this->initListWidget1();

    QVBoxLayout *layout3 = new QVBoxLayout();
    layout3->addLayout(layout1);
    layout3->addLayout(layout2);
    layout3->addWidget(this->listWidget1);

    tabWidget1ItemWidget1->setLayout(layout3);
    return tabWidget1ItemWidget1;
}

QWidget* MainWindow12::setTabWidget1ItemWidget2()
{
    QWidget *tabWidget1ItemWidget2 = new QWidget(this->tabWidget1);
    return tabWidget1ItemWidget2;
}

QWidget* MainWindow12::setTabWidget1ItemWidget3()
{
    QWidget *tabWidget1ItemWidget3 = new QWidget(this->tabWidget1);
    return tabWidget1ItemWidget3;
}

void MainWindow12::initListWidget1()
{
    this->listWidget1->clear();
    bool check1 = this->checkBox1->isChecked();
    for(int i=0; i<10; i++)
    {
        QListWidgetItem *item = new QListWidgetItem();
        item->setText(QString::asprintf("Item_%d", i));
        item->setCheckState(Qt::Checked);
        if(check1)
        {
            item->setFlags(Qt::ItemIsSelectable | Qt::ItemIsEditable | Qt::ItemIsUserCheckable | Qt::ItemIsEnabled);
            this->listWidget1->addItem(item);
        }
    }
}

void MainWindow12::action1_triggered()
{
    this->initListWidget1();
}

void MainWindow12::action2_triggered()
{
    this->listWidget1->clear();
}

void MainWindow12::action3_triggered()
{
    bool check = this->checkBox1->isChecked();
    if(check)
    {
        QListWidgetItem *item = new QListWidgetItem();
        item->setFlags(Qt::ItemIsSelectable | Qt::ItemIsEditable | Qt::ItemIsUserCheckable | Qt::ItemIsEnabled);
        item->setText("new inserted item");
        item->setCheckState(Qt::Checked);
        this->listWidget1->insertItem(this->listWidget1->currentRow(), item);
    }
}

void MainWindow12::action4_triggered()
{
    bool check = this->checkBox1->isChecked();
    if(check && this->listWidget1->currentRow())
    {
        QListWidgetItem *item = new QListWidgetItem();
        item->setFlags(Qt::ItemIsSelectable | Qt::ItemIsEditable | Qt::ItemIsUserCheckable | Qt::ItemIsEnabled);
        item->setText("new inserted item");
        item->setCheckState(Qt::Checked);
        this->listWidget1->insertItem(this->listWidget1->count(), item);
    }
}

void MainWindow12::action5_triggered()
{
    QListWidgetItem* item = this->listWidget1->currentItem();
    this->listWidget1->removeItemWidget(item);
    delete item;

//    int row = this->listWidget1->currentRow();
//    QListWidgetItem* item = this->listWidget1->takeItem(row);
//    delete item;
}

void MainWindow12::action6_triggered()
{

}

void MainWindow12::action7_triggered()
{
    this->close();
}

void MainWindow12::selectAllAction_triggered()
{
    int count = this->listWidget1->count();
    for(int i=0; i<count; i++)
    {
        this->listWidget1->item(i)->setCheckState(Qt::Checked);
    }
}

void MainWindow12::selectNoneAction_triggered()
{
    int count = this->listWidget1->count();
    for(int i=0; i<count; i++)
    {
        this->listWidget1->item(i)->setCheckState(Qt::Unchecked);
    }
}

void MainWindow12::selectReverseAction_triggered()
{
    int count = this->listWidget1->count();
    for(int i=0; i<count; i++)
    {
        bool check = this->listWidget1->item(i)->checkState();
        if(check)
        {
            this->listWidget1->item(i)->setCheckState(Qt::Unchecked);
        }
        else
        {
            this->listWidget1->item(i)->setCheckState(Qt::Checked);
        }
    }
}

void MainWindow12::checkBox1_clicked(bool checked)
{
    if(checked)
    {
        this->initListWidget1();
    }
}

void MainWindow12::listWidget1_currentItemChanged(QListWidgetItem* current, QListWidgetItem* previous)
{
    this->lineEdit1->clear();
    if(current)
    {
        if(previous)
        {
            this->lineEdit1->setText("前一项:" + previous->text() + "当前项:" + current->text());
        }
        else
        {
            this->lineEdit1->setText("当前项:" + current->text());
        }
    }
}

void MainWindow12::listWidget1_customContextMenuRequested(const QPoint &pos)
{
    Q_UNUSED(pos);
    QMenu* menu1 = new QMenu(this);
    menu1->addAction(this->action1);
    menu1->addAction(this->action2);
    menu1->addAction(this->action3);
    menu1->addAction(this->action4);
    menu1->addAction(this->action5);
    menu1->addAction(this->selectAllAction);
    menu1->addAction(this->selectNoneAction);
    menu1->addAction(this->selectReverseAction);
    // 在鼠标光标位置显示右键快捷菜单
    menu1->exec(QCursor::pos());
    delete menu1;

}

```