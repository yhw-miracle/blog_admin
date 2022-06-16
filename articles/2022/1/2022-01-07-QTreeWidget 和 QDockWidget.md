
```c++
#if _MSC_VER >= 1600
#pragma execution_character_set("utf-8")
#endif

#include "mainwindow13.h"

#include <QList>
#include <QStringList>
#include <QFileDialog>
#include <QDir>
#include <QFile>
#include <QFileInfoList>
#include <QDebug>
#include <QDateTime>

MainWindow13::MainWindow13(QString title, QWidget *parent) : QMainWindow(parent)
{
    this->setWindowTitle(title);

    this->menuBar1 = new QMenuBar();
    this->menu1 = new QMenu();
    this->menu1->setTitle("目录树");
    this->menu2 = new QMenu();
    this->menu2->setTitle("视图");
    this->menuBar1->addMenu(this->menu1);
    this->menuBar1->addMenu(this->menu2);
    this->setMenuBar(this->menuBar1);

    this->toolBar1 = new QToolBar();
    this->toolBar1->setWindowTitle("QTreeWidget 操作");
    this->action1 = new QAction();
    this->action1->setText("添加目录");
    this->action2 = new QAction();
    this->action2->setText("添加文件");
    this->action3 = new QAction();
    this->action3->setText("删除节点");
    this->action4 = new QAction();
    this->action4->setText("遍历节点");
    this->action5 = new QAction();
    this->action5->setText("放大");
    this->action6 = new QAction();
    this->action6->setText("缩小");
    this->action7 = new QAction();
    this->action7->setText("实际大小");
    this->action8 = new QAction();
    this->action8->setText("适合宽度");
    this->action9 = new QAction();
    this->action9->setText("适合高度");
    this->action10 = new QAction();
    // QAction 是否可选
    this->action10->setCheckable(true);
    this->action10->setText("窗口浮动");
    this->action11 = new QAction();
    this->action11->setCheckable(true);
    this->action11->setText("窗体可见");
    this->action12 = new QAction();
    this->action12->setText("退出");
    this->toolBar1->addAction(this->action1);
    this->toolBar1->addAction(this->action2);
    this->toolBar1->addAction(this->action3);
    this->toolBar1->addAction(this->action4);
    this->toolBar1->addSeparator();
    this->toolBar1->addAction(this->action5);
    this->toolBar1->addAction(this->action6);
    this->toolBar1->addAction(this->action7);
    this->toolBar1->addAction(this->action8);
    this->toolBar1->addSeparator();
    this->toolBar1->addAction(this->action9);
    this->toolBar1->addAction(this->action10);
    this->toolBar1->addAction(this->action11);
    this->toolBar1->addAction(this->action12);
    this->toolBar1->addSeparator();
    this->addToolBar(this->toolBar1);

    this->dockWidge1 = new QDockWidget();
    this->dockWidge1->setWindowTitle("图片目录树");
    this->dockWidge1->setFeatures(QDockWidget::DockWidgetMovable | QDockWidget::DockWidgetFloatable);
    this->treeWidget1 = new QTreeWidget();
    this->dockWidge1->setWidget(this->treeWidget1);
    this->addDockWidget(Qt::LeftDockWidgetArea, this->dockWidge1);

    this->scrollArea1 = new QScrollArea();
    QHBoxLayout *layout1 = new QHBoxLayout();
    this->label1 = new QLabel();
    layout1->addWidget(this->label1);
    this->scrollArea1->setLayout(layout1);
    this->setCentralWidget(this->scrollArea1);

    this->statusBar1 = new QStatusBar();
    this->label2 = new QLabel();
    this->statusBar1->addWidget(this->label2);
    this->setStatusBar(this->statusBar1);

    this->connect(this->action1, SIGNAL(triggered()), this, SLOT(action1_triggered()));
    this->connect(this->action2, SIGNAL(triggered()), this, SLOT(action2_triggered()));
    this->connect(this->action3, SIGNAL(triggered()), this, SLOT(action3_triggered()));
    this->connect(this->action4, SIGNAL(triggered()), this, SLOT(action4_triggered()));
    this->connect(this->action5, SIGNAL(triggered()), this, SLOT(action5_triggered()));
    this->connect(this->action6, SIGNAL(triggered()), this, SLOT(action6_triggered()));
    this->connect(this->action7, SIGNAL(triggered()), this, SLOT(action7_triggered()));
    this->connect(this->action8, SIGNAL(triggered()), this, SLOT(action8_triggered()));
    this->connect(this->action9, SIGNAL(triggered()), this, SLOT(action9_triggered()));
    this->connect(this->action10, SIGNAL(triggered(bool)), this, SLOT(action10_triggered(bool)));
    this->connect(this->action11, SIGNAL(triggered(bool)), this, SLOT(action11_triggered(bool)));
    this->connect(this->action12, SIGNAL(triggered()), this, SLOT(action12_triggered()));
    this->connect(this->treeWidget1, SIGNAL(currentItemChanged(QTreeWidgetItem*, QTreeWidgetItem*)), this, SLOT(treeWidget1_currentItemChanged(QTreeWidgetItem*, QTreeWidgetItem*)));
    this->connect(this->dockWidge1, SIGNAL(visibilityChanged(bool)), this, SLOT(dockWidget1_visibilityChanged(bool)));
    this->connect(this->dockWidge1, SIGNAL(topLevelChanged(bool)), this, SLOT(dockWidget1_topLevelChanged(bool)));

    this->initTreeWidget1();
}

void MainWindow13::action1_triggered()
{
    // 添加目录
    // 添加组节点
    QString dir = QFileDialog::getExistingDirectory();
    if(!dir.isEmpty())
    {
        QTreeWidgetItem *currentItem = this->treeWidget1->currentItem();
        this->addFolderItem(currentItem, dir, MainWindow13::groupItem1);
    }
}

void MainWindow13::action2_triggered()
{
    // 添加文件
    QStringList files = QFileDialog::getOpenFileNames(this, "选择文件", "", "Images(*.jpg)");
    if(files.isEmpty())
    {
        return;
    }
    QTreeWidgetItem *parentItem, *item;
    item = this->treeWidget1->currentItem();
    if(item->type() == MainWindow13::imageItem)
    {
        parentItem = item->parent();
    }
    else if(item->type() == MainWindow13::groupItem1 || item->type() == MainWindow13::groupItem2)
    {
        parentItem = item;
    }
    else
    {
        parentItem = item;
    }

    for(int i=0; i<files.length(); i++)
    {
        QString fileName = files.at(i);
        this->addImageItem(parentItem, fileName);
    }
}

void MainWindow13::action3_triggered()
{
    // 删除节点
    QTreeWidgetItem *item = this->treeWidget1->currentItem();
    QTreeWidgetItem *parentItem = item->parent();
    if(parentItem)
    {
        parentItem->removeChild(item);
        delete item;
    }
}

void MainWindow13::action4_triggered()
{
    // 遍历节点
    for(int i=0; i<this->treeWidget1->topLevelItemCount(); i++)
    {
        QTreeWidgetItem *item = this->treeWidget1->topLevelItem(i);
        this->changeItemCaption(item);
    }
}

void MainWindow13::action5_triggered()
{
    // 放大
    this->pixmapRatio = this->pixmapRatio * 1.2;
    int width = this->pixmapRatio * this->currentPixmap.width();
    int height = this->pixmapRatio * this->currentPixmap.height();
    QPixmap pixmap = this->currentPixmap.scaled(width, height);
    this->label1->setPixmap(pixmap);
}

void MainWindow13::action6_triggered()
{
    // 缩小
    this->pixmapRatio = this->pixmapRatio * 0.8;
    int width = this->pixmapRatio * this->currentPixmap.width();
    int height = this->pixmapRatio * this->currentPixmap.height();
    QPixmap pixmap = this->currentPixmap.scaled(width, height);
    this->label1->setPixmap(pixmap);
}

void MainWindow13::action7_triggered()
{
    // 实际大小
    this->pixmapRatio = 1;
    this->label1->setPixmap(this->currentPixmap);
}

void MainWindow13::action8_triggered()
{
    // 适合宽度
    int width = this->scrollArea1->width();
    int realWidth = this->currentPixmap.width();
    this->pixmapRatio = float(width) / realWidth;
    QPixmap pixmap = this->currentPixmap.scaledToHeight(width - 30);
    this->label1->setPixmap(pixmap);
}

void MainWindow13::action9_triggered()
{
    // 适合高度
    int height = this->scrollArea1->height();
    int realHeight = this->currentPixmap.height();
    this->pixmapRatio = float(height) / realHeight;
    QPixmap pixmap = this->currentPixmap.scaledToWidth(height - 30);
    this->label1->setPixmap(pixmap);
}

void MainWindow13::action10_triggered(bool arg1)
{
    // 窗体浮动
    this->dockWidge1->setFloating(arg1);
}

void MainWindow13::action11_triggered(bool arg1)
{
    // 窗体可见
    this->dockWidge1->setVisible(arg1);
}

void MainWindow13::action12_triggered()
{
    // 退出
    this->close();
}

void MainWindow13::initTreeWidget1()
{
    this->treeWidget1->clear();
    this->treeWidget1->setColumnCount(2);
    QStringList a;
    a.append("名称");
    a.append("类型");
    this->treeWidget1->setHeaderLabels(a);

    QTreeWidgetItem *treeWidgetItem1 = new QTreeWidgetItem(MainWindow13::topItem);
    treeWidgetItem1->setText(0, "图片文件");
    treeWidgetItem1->setText(1, "type=topItem");
    treeWidgetItem1->setFlags(Qt::ItemIsSelectable | Qt::ItemIsUserCheckable | Qt::ItemIsEnabled | Qt::ItemIsAutoTristate);
    treeWidgetItem1->setCheckState(0, Qt::Checked);
    treeWidgetItem1->setData(0, Qt::UserRole, QVariant(""));
    this->treeWidget1->addTopLevelItem(treeWidgetItem1);
    QDir *initDir = new QDir("./images");
    QString initDirName = initDir->absolutePath();
    QDir *initDir1 = new QDir(initDirName);
    QTreeWidgetItem *newItem = this->addFolderItem(treeWidgetItem1, initDirName, MainWindow13::groupItem1);

    QStringList fileFilters;
    fileFilters << "*.jpg";
    initDir1->setNameFilters(fileFilters);
    QFileInfoList fileInfoList = initDir1->entryInfoList();
    for(int i=0; i<fileInfoList.size(); i++)
    {
        this->initImages(newItem, fileInfoList.at(i).absoluteFilePath());
    }
}

void MainWindow13::initImages(QTreeWidgetItem *grandParentItem, QString fileName)
{
    QTreeWidgetItem *parentItem;
    QString finalFileName = this->getFinalFolderName(fileName);
    if(finalFileName.contains('_'))
    {
        finalFileName = finalFileName.left(finalFileName.indexOf('_'));
    }
    else
    {
        finalFileName = finalFileName.left(finalFileName.indexOf('.'));
    }
    QDateTime dateTime = QDateTime::fromString(finalFileName, "yyyyMMdd");
    bool isHasDateTimeItem = false;
    for(int i=0; i<grandParentItem->childCount(); i++)
    {
        if(grandParentItem->child(i)->text(0) == dateTime.toString("yyyy年MM月"))
        {
            isHasDateTimeItem = true;
            parentItem = grandParentItem->child(i);
            break;
        }
    }
    if(!isHasDateTimeItem)
    {
        QTreeWidgetItem *newParentItem = this->addFolderItem(grandParentItem, dateTime.toString("yyyy年MM月"),  MainWindow13::groupItem2);
        this->addImageItem(newParentItem, fileName);
    }
    else
    {
        this->addImageItem(parentItem, fileName);
    }
}

QTreeWidgetItem* MainWindow13::addFolderItem(QTreeWidgetItem *item, QString name, treeItemType typeVariable)
{
    if(name.contains('/'))
    {
        name = this->getFinalFolderName(name);
    }

    QTreeWidgetItem *newItem = new QTreeWidgetItem(typeVariable);
    newItem->setText(0, name);
    newItem->setText(1, "type=groupItem1");
    newItem->setFlags(Qt::ItemIsSelectable | Qt::ItemIsUserCheckable | Qt::ItemIsEnabled | Qt::ItemIsAutoTristate);
    newItem->setCheckState(0, Qt::Checked);
    newItem->setData(0, Qt::UserRole, QVariant("dirName"));
    item->addChild(newItem);
    return newItem;
}

QString MainWindow13::getFinalFolderName(const QString &fullPathName)
{
    int length = fullPathName.length();
    int i = fullPathName.lastIndexOf("/");
    QString str = fullPathName.right(length - i - 1);
    return str;
}

QString MainWindow13::getFolderName(const QString &fullPathName)
{
    int length = fullPathName.length();
    int i = fullPathName.lastIndexOf("/");
    QString str = fullPathName.left(length - i - 1);
    return str;
}

void MainWindow13::addImageItem(QTreeWidgetItem *item, QString fileName)
{
    QString finalFileName = this->getFinalFolderName(fileName);

    QTreeWidgetItem *newItem = new QTreeWidgetItem(MainWindow13::imageItem);
    newItem->setText(0, finalFileName);
    newItem->setText(1, "type=imageItem");
    newItem->setFlags(Qt::ItemIsSelectable | Qt::ItemIsUserCheckable | Qt::ItemIsEnabled | Qt::ItemIsAutoTristate);
    newItem->setCheckState(0, Qt::Checked);
    newItem->setData(0, Qt::UserRole, QVariant(fileName));
    item->addChild(newItem);
}

void MainWindow13::displayImage(QTreeWidgetItem *item)
{
    QString fileName = item->data(0, Qt::UserRole).toString();
    this->label2->setText(fileName);
    this->currentPixmap.load(fileName);
    this->action8_triggered();
}

void MainWindow13::changeItemCaption(QTreeWidgetItem *item)
{
    QString str = "*" + item->text(0);
    item->setText(0, str);
    for(int i=0; i<item->childCount(); i++)
    {
        this->changeItemCaption(item->child(i));
    }
}

void MainWindow13::treeWidget1_currentItemChanged(QTreeWidgetItem *current, QTreeWidgetItem *previous)
{
    Q_UNUSED(previous);

    if(!current)
        return;

    int typeVariable = current->type();
    if(typeVariable == MainWindow13::topItem)
    {
        this->action1->setEnabled(true);
        this->action2->setEnabled(true);
        this->action3->setEnabled(false);
    }
    else if(typeVariable == MainWindow13::groupItem1 || typeVariable == MainWindow13::groupItem2)
    {
        this->action1->setEnabled(true);
        this->action2->setEnabled(true);
        this->action3->setEnabled(true);
    }
    else if(typeVariable == MainWindow13::imageItem)
    {
        this->action1->setEnabled(false);
        this->action2->setEnabled(true);
        this->action3->setEnabled(true);
        this->displayImage(current);
    }
}
void MainWindow13::dockWidget1_visibilityChanged(bool arg1)
{
    this->action11->setChecked(arg1);
}

void MainWindow13::dockWidget1_topLevelChanged(bool arg1)
{
    this->action10->setChecked(arg1);
}

```