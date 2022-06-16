
```c++
#if _MSC_VER >= 1600
#pragma execution_character_set("utf-8")
#endif

#include "mainwindow24.h"

#include <QDebug>

MainWindow24::MainWindow24(QString title, QWidget *parent) : QMainWindow(parent)
{
    this->setWindowTitle(title);

    this->toolBar1 = new QToolBar();
    this->action1 = new QAction();
    this->action1->setText("表格复位");
    this->action2 = new QAction();
    this->action2->setText("打开 stm 文件");
    this->action3 = new QAction();
    this->action3->setText("保存 stm 文件");
    this->action4 = new QAction();
    this->action4->setText("打开 dat 文件");
    this->action5 = new QAction();
    this->action5->setText("保存 dat 文件");
    this->action6 = new QAction();
    this->action6->setText("添加行");
    this->action7 = new QAction();
    this->action7->setText("插入行");
    this->action8 = new QAction();
    this->action8->setText("删除行");
    this->action9 = new QAction();
    this->action9->setText("退出");
    this->toolBar1->addAction(this->action1);
    this->toolBar1->addAction(this->action2);
    this->toolBar1->addAction(this->action3);
    this->toolBar1->addAction(this->action4);
    this->toolBar1->addAction(this->action5);
    this->toolBar1->addAction(this->action6);
    this->toolBar1->addAction(this->action7);
    this->toolBar1->addAction(this->action8);
    this->toolBar1->addAction(this->action9);
    this->addToolBar(this->toolBar1);

    this->connect(this->action1, SIGNAL(triggered()), this, SLOT(action1_triggered()));
    this->connect(this->action2, SIGNAL(triggered()), this, SLOT(action2_triggered()));
    this->connect(this->action3, SIGNAL(triggered()), this, SLOT(action3_triggered()));
    this->connect(this->action4, SIGNAL(triggered()), this, SLOT(action4_triggered()));
    this->connect(this->action5, SIGNAL(triggered()), this, SLOT(action5_triggered()));
    this->connect(this->action6, SIGNAL(triggered()), this, SLOT(action6_triggered()));
    this->connect(this->action7, SIGNAL(triggered()), this, SLOT(action7_triggered()));
    this->connect(this->action8, SIGNAL(triggered()), this, SLOT(action8_triggered()));
    this->connect(this->action9, SIGNAL(triggered()), this, SLOT(action9_triggered()));

    this->tableView1 = new QTableView();
    this->standardItemModel1 = new QStandardItemModel();
    this->standardItemModel1->setColumnCount(6);
    QStringList header;
    header << "测深" << "垂深" << "方位" << "位移" << "固井质量" << "测井取样";
    this->standardItemModel1->setHorizontalHeaderLabels(header);
    this->itemSelectionModel1 = new QItemSelectionModel(this->standardItemModel1);
    this->tableView1->setModel(this->standardItemModel1);
    this->tableView1->setSelectionModel(this->itemSelectionModel1);
    this->tableView1->setSelectionMode(QAbstractItemView::ExtendedSelection);
    this->tableView1->setSelectionBehavior(QAbstractItemView::SelectItems);

    this->tableView1->setItemDelegateForColumn(0, &this->spinBoxDelegate);
    this->tableView1->setItemDelegateForColumn(1, &this->doubleSpinBoxDelegate);
    this->tableView1->setItemDelegateForColumn(2, &this->doubleSpinBoxDelegate);
    this->tableView1->setItemDelegateForColumn(3, &this->doubleSpinBoxDelegate);
    this->tableView1->setItemDelegateForColumn(4, &this->comboBoxDelegate);
    this->setCentralWidget(this->tableView1);

    this->statusBar1 = new QStatusBar();
    this->label1 = new QLabel();
    this->label2 = new QLabel();
    this->statusBar1->addWidget(this->label1);
    this->statusBar1->addWidget(this->label2);
    this->setStatusBar(this->statusBar1);
}

void MainWindow24::paintEvent(QPaintEvent *event)
{
    // 绘制窗口背景图片
    Q_UNUSED(event);
    QString currentPath = QDir::currentPath();
    QPainter painter(this);
    painter.drawPixmap(0,
                       this->toolBar1->height(),
                       this->width(),
                       this->height() - this->toolBar1->height() - this->statusBar1->height(),
                       QPixmap(currentPath + "/images/" + "20210925_47ff6192976c0e3394e4db2f2507efce.jpg"));
}

void MainWindow24::resetTable(int row)
{
    this->standardItemModel1->removeRows(0, this->standardItemModel1->rowCount());

    this->standardItemModel1->setRowCount(row);

    QString str = this->standardItemModel1->headerData(this->standardItemModel1->columnCount() - 1,
                                                       Qt::Horizontal,
                                                       Qt::DisplayRole).toString();
    for(int i=0; i<row; i++)
    {
        this->standardItemModel1->setData(this->standardItemModel1->index(i, 0), 0, Qt::DisplayRole);
        this->standardItemModel1->setData(this->standardItemModel1->index(i, 1), 0.0, Qt::DisplayRole);
        this->standardItemModel1->setData(this->standardItemModel1->index(i, 2), 0.0, Qt::DisplayRole);
        this->standardItemModel1->setData(this->standardItemModel1->index(i, 3), 0.0, Qt::DisplayRole);
        this->standardItemModel1->setData(this->standardItemModel1->index(i, 4), "111", Qt::DisplayRole);
        this->standardItemModel1->itemFromIndex(this->standardItemModel1->index(i, 5))->setText(str);
        this->standardItemModel1->itemFromIndex(this->standardItemModel1->index(i, 5))->setCheckable(true);
        this->standardItemModel1->itemFromIndex(this->standardItemModel1->index(i, 5))->setCheckState(Qt::Checked);
    }
}


void MainWindow24::action1_triggered()
{
    // 表格复位
    this->resetTable(10);
}

void MainWindow24::action2_triggered()
{
    // 打开 stm 文件
    QString currentPath = QDir::currentPath();
    QString fileName = QFileDialog::getOpenFileName(this, "打开文件", currentPath, "Qt预定义编码数据文件(*.stm)");
    if(fileName.isEmpty())
        return;

    QFile file(fileName);
    if(file.open(QIODevice::ReadOnly))
    {
        QDataStream dataSteam(&file);
        // 写入和读取的版本一致,或者读取版本高于写入版本
        dataSteam.setVersion(QDataStream::Qt_5_12);
        qint16 row, column;
        dataSteam >> row;
        dataSteam >> column;
        this->resetTable(row);

        QString str;
        for(int i=0; i<column; i++)
        {
            dataSteam >> str;
        }

        for(int i=0; i<row; i++)
        {
            qint16 a;
            qreal b, c, d;
            QString e;
            bool f;
            dataSteam >> a >> b >> c >> d >> e >> f;

            qDebug() << a << b << c << d << e << f;

            QModelIndex index1 = this->standardItemModel1->index(i, 0);
            QStandardItem *item1 = this->standardItemModel1->itemFromIndex(index1);
            item1->setData(a, Qt::DisplayRole);

            QModelIndex index2 = this->standardItemModel1->index(i, 1);
            QStandardItem *item2 = this->standardItemModel1->itemFromIndex(index2);
            item2->setData(b, Qt::DisplayRole);

            QModelIndex index3 = this->standardItemModel1->index(i, 2);
            QStandardItem *item3 = this->standardItemModel1->itemFromIndex(index3);
            item3->setData(c, Qt::DisplayRole);

            QModelIndex index4 = this->standardItemModel1->index(i, 3);
            QStandardItem *item4 = this->standardItemModel1->itemFromIndex(index4);
            item4->setData(d, Qt::DisplayRole);

            QModelIndex index5 = this->standardItemModel1->index(i, 4);
            QStandardItem *item5 = this->standardItemModel1->itemFromIndex(index5);
            item5->setData(e, Qt::DisplayRole);

            QModelIndex index6 = this->standardItemModel1->index(i, 5);
            QStandardItem *item6 = this->standardItemModel1->itemFromIndex(index6);
            if(f)
            {
                item6->setCheckState(Qt::Checked);
            }
            else
            {
                item6->setCheckState(Qt::Unchecked);
            }
        }
    }
}

void MainWindow24::action3_triggered()
{
    // 保存 stm 文件
    QString currentPath = QDir::currentPath();
    QString fileName = QFileDialog::getSaveFileName(this, "打开文件", currentPath, "Qt预定义编码数据文件(*.stm)");
    if(fileName.isEmpty())
        return;

    QFile file(fileName);
    if(file.open(QIODevice::WriteOnly | QIODevice::Truncate))
    {
        QDataStream dataStream(&file);
        // 写入和读取的版本一致
        dataStream.setVersion(QDataStream::Qt_5_12);
        qint16 row = this->standardItemModel1->rowCount();
        qint16 column = this->standardItemModel1->columnCount();
        dataStream << row;
        dataStream << column;
        // 表头
        for(int i=0; i<column;i++)
        {
            dataStream << this->standardItemModel1->horizontalHeaderItem(i)->text();
        }
        // 数据
        for(int r=0; r<row; r++)
        {
            qint16 a = this->standardItemModel1->item(r, 0)->data(Qt::DisplayRole).toInt();
            qreal b = this->standardItemModel1->item(r, 1)->data(Qt::DisplayRole).toReal();
            qreal c = this->standardItemModel1->item(r, 2)->data(Qt::DisplayRole).toReal();
            qreal d = this->standardItemModel1->item(r, 3)->data(Qt::DisplayRole).toReal();
            QString e = this->standardItemModel1->item(r, 4)->data(Qt::DisplayRole).toString();
            bool f = (this->standardItemModel1->item(r, 5)->checkState() == Qt::Checked);

            qDebug() << a << b << c << d << e << f;
            dataStream << a << b << c << d << e << f;
        }
        file.close();
    }
}

void MainWindow24::action4_triggered()
{
    // 打开 dat 文件
//    QDataStream::readBytes();QDataStream::writeBytes();
//    QDataStream::readBytes();QDataStream::writeBytes();
    QString currentPath = QDir::currentPath();
    QString fileName = QFileDialog::getOpenFileName(this, "打开文件", currentPath, "标准编码数据文件(*.dat)");
    if(fileName.isEmpty())
        return;

    QFile file(fileName);
    if(file.open(QIODevice::ReadOnly))
    {
        QDataStream dataStream(&file);
        dataStream.setByteOrder(QDataStream::LittleEndian);

        qint16 row, column;
        dataStream.readRawData((char*)&row, sizeof(qint16));
        dataStream.readRawData((char*)&column, sizeof(qint16));
        this->resetTable(row);

        char *buffer;
        uint bufferLength;
        for(int i=0; i<column; i++)
        {
            dataStream.readBytes(buffer, bufferLength);
            QString str = QString::fromLocal8Bit(buffer, bufferLength);
        }

        for(int i=0; i<row; i++)
        {
            qint16 a;
            qreal b, c, d;
            char *eChar;
            uint eLength;
            QString e;
            bool f;
            dataStream.readRawData((char*)&a, sizeof(qint16));
            dataStream.readRawData((char*)&b, sizeof(qreal));
            dataStream.readRawData((char*)&c, sizeof(qreal));
            dataStream.readRawData((char*)&d, sizeof(qreal));
            dataStream.readBytes(eChar, eLength);
            e = QString::fromLocal8Bit(eChar, eLength);
            dataStream.readRawData((char*)&f, sizeof(bool));

            qDebug() << a << b << c << d << e << f;

            this->standardItemModel1->itemFromIndex(this->standardItemModel1->index(i, 0))->setData(a, Qt::DisplayRole);
            this->standardItemModel1->itemFromIndex(this->standardItemModel1->index(i, 1))->setData(b, Qt::DisplayRole);
            this->standardItemModel1->itemFromIndex(this->standardItemModel1->index(i, 2))->setData(c, Qt::DisplayRole);
            this->standardItemModel1->itemFromIndex(this->standardItemModel1->index(i, 3))->setData(d, Qt::DisplayRole);
            this->standardItemModel1->itemFromIndex(this->standardItemModel1->index(i, 4))->setData(e, Qt::DisplayRole);
            if(f)
            {
                this->standardItemModel1->itemFromIndex(this->standardItemModel1->index(i, 5))->setCheckState(Qt::Checked);
            }
            else
            {
                this->standardItemModel1->itemFromIndex(this->standardItemModel1->index(i, 5))->setCheckState(Qt::Unchecked);
            }
        }
        file.close();
    }
}

void MainWindow24::action5_triggered()
{
    // 保存 dat 文件
    QString currentPath = QDir::currentPath();
    QString fileName = QFileDialog::getSaveFileName(this, "打开文件", currentPath, "标准编码数据文件(*.dat)");
    if(fileName.isEmpty())
        return;

    QFile file(fileName);
    if(file.open(QIODevice::WriteOnly | QIODevice::Truncate))
    {
        QDataStream dataSteam(&file);
        // 小端字节序
        dataSteam.setByteOrder(QDataStream::LittleEndian);
        // 大端字节序
//        dataSteam.setByteOrder(QDataStream::BigEndian);

        qint16 row = this->standardItemModel1->rowCount();
        qint16 column = this->standardItemModel1->columnCount();
        dataSteam.writeRawData((char *)&row, sizeof (qint16));
        dataSteam.writeRawData((char *)&column, sizeof (qint16));
        // 表头
        QByteArray byteArray;
        for(int i=0; i<column; i++)
        {
            QString str = this->standardItemModel1->horizontalHeaderItem(i)->text();
            QByteArray byteArray = str.toUtf8();
            dataSteam.writeBytes(byteArray, byteArray.length());
        }
        // 数据
        for(int i=0; i<row; i++)
        {
            qint16 a = this->standardItemModel1->item(i, 0)->data(Qt::DisplayRole).toInt();
            dataSteam.writeRawData((char *)&a, sizeof(qint16));

            qreal b = this->standardItemModel1->item(i, 1)->data(Qt::DisplayRole).toReal();
            dataSteam.writeRawData((char *)&b, sizeof(qreal));

            qreal c = this->standardItemModel1->item(i, 2)->data(Qt::DisplayRole).toReal();
            dataSteam.writeRawData((char *)&c, sizeof(qreal));

            qreal d = this->standardItemModel1->item(i, 3)->data(Qt::DisplayRole).toReal();
            dataSteam.writeRawData((char *)&d, sizeof(qreal));

            QString e = this->standardItemModel1->item(i, 4)->data(Qt::DisplayRole).toString();
            QByteArray byteArray = e.toUtf8();
            dataSteam.writeBytes(byteArray, byteArray.length());

            bool f = (this->standardItemModel1->item(i, 5)->checkState() == Qt::Checked);
            dataSteam.writeRawData((char *)&f, sizeof(bool));

            qDebug() << a << b << c << d << e << f;
        }
        file.close();
    }
}

void MainWindow24::action6_triggered()
{
    // 添加行
    qDebug() << this->standardItemModel1->rowCount();
    if(this->standardItemModel1->rowCount() > 1)
    {
        int columnCount = this->standardItemModel1->columnCount();
        QString str = this->standardItemModel1->headerData(columnCount - 1,
                                                           Qt::Horizontal,
                                                           Qt::DisplayRole).toString();

        int rowCount = this->standardItemModel1->rowCount();
        this->standardItemModel1->insertRow(rowCount);
        this->itemSelectionModel1->clearSelection();
        this->itemSelectionModel1->setCurrentIndex(this->standardItemModel1->index(rowCount, 0),
                                                   QItemSelectionModel::Select);

        this->standardItemModel1->setData(this->standardItemModel1->index(rowCount, 0), 0, Qt::DisplayRole);
        this->standardItemModel1->setData(this->standardItemModel1->index(rowCount, 1), 0.0, Qt::DisplayRole);
        this->standardItemModel1->setData(this->standardItemModel1->index(rowCount, 2), 0.0, Qt::DisplayRole);
        this->standardItemModel1->setData(this->standardItemModel1->index(rowCount, 3), 0.0, Qt::DisplayRole);
        this->standardItemModel1->setData(this->standardItemModel1->index(rowCount, 4), "111", Qt::DisplayRole);
        this->standardItemModel1->itemFromIndex(this->standardItemModel1->index(rowCount, 5))->setText(str);
        this->standardItemModel1->itemFromIndex(this->standardItemModel1->index(rowCount, 5))->setCheckable(true);
        this->standardItemModel1->itemFromIndex(this->standardItemModel1->index(rowCount, 5))->setCheckState(Qt::Checked);
    }
}

void MainWindow24::action7_triggered()
{
    // 插入行
    if(this->standardItemModel1->rowCount() > 1)
    {
        int columnCount = this->standardItemModel1->columnCount();
        QString str = this->standardItemModel1->headerData(columnCount - 1, Qt::Horizontal, Qt::DisplayRole).toString();
        QModelIndex currentIndex = this->itemSelectionModel1->currentIndex();

        this->standardItemModel1->insertRow(currentIndex.row());
        this->standardItemModel1->setData(this->standardItemModel1->index(currentIndex.row(), 0), 0, Qt::DisplayRole);
        this->standardItemModel1->setData(this->standardItemModel1->index(currentIndex.row(), 1), 0.0, Qt::DisplayRole);
        this->standardItemModel1->setData(this->standardItemModel1->index(currentIndex.row(), 2), 0.0, Qt::DisplayRole);
        this->standardItemModel1->setData(this->standardItemModel1->index(currentIndex.row(), 3), 0.0, Qt::DisplayRole);
        this->standardItemModel1->setData(this->standardItemModel1->index(currentIndex.row(), 4), "111", Qt::DisplayRole);
        this->standardItemModel1->itemFromIndex(this->standardItemModel1->index(currentIndex.row(), 5))->setText(str);
        this->standardItemModel1->itemFromIndex(this->standardItemModel1->index(currentIndex.row(), 5))->setCheckable(true);
        this->standardItemModel1->itemFromIndex(this->standardItemModel1->index(currentIndex.row(), 5))->setCheckState(Qt::Checked);
    }
}

void MainWindow24::action8_triggered()
{
    // 删除行
    QModelIndex currentIndex = this->itemSelectionModel1->currentIndex();
    if(currentIndex.row() == this->standardItemModel1->rowCount() - 1)
    {
        this->standardItemModel1->removeRow(currentIndex.row());
    }
    else
    {
        this->standardItemModel1->removeRow(currentIndex.row());
        this->itemSelectionModel1->setCurrentIndex(currentIndex, QItemSelectionModel::Select);
    }
}

void MainWindow24::action9_triggered()
{
    // 退出
    this->close();
}

```