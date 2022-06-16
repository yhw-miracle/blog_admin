
```c++
#if _MSC_VER >= 1600
#pragma execution_character_set("utf-8")
#endif

#include "mainwindow17.h"

#include <QDebug>

MainWindow17::MainWindow17(QString title, QWidget *parent) : QMainWindow(parent)
{
    this->setWindowTitle(title);

    this->toolBar1 = new QToolBar();
    this->toolBar1->setWindowTitle("QTableView 操作");
    this->action1 = new QAction();
    this->action1->setText("打开文件");
    this->action2 = new QAction();
    this->action2->setText("另存文件");
    this->action3 = new QAction();
    this->action3->setText("模型数据预览");
    this->action4 = new QAction();
    this->action4->setText("添加行");
    this->action5 = new QAction();
    this->action5->setText("插入行");
    this->action6 = new QAction();
    this->action6->setText("删除行");
    this->action7 = new QAction();
    this->action7->setCheckable(true);
    this->action7->setText("居左");
    this->action8 = new QAction();
    this->action8->setCheckable(true);
    this->action8->setText("居中");
    this->action9 = new QAction();
    this->action9->setCheckable(true);
    this->action9->setText("居右");
    this->action10 = new QAction();
    this->action10->setCheckable(true);
    this->action10->setText("粗体");
    this->action11 = new QAction();
    this->action11->setText("退出");

    this->toolBar1->addAction(this->action1);
    this->toolBar1->addAction(this->action2);
    this->toolBar1->addAction(this->action3);
    this->toolBar1->addSeparator();
    this->toolBar1->addAction(this->action4);
    this->toolBar1->addAction(this->action5);
    this->toolBar1->addAction(this->action6);
    this->toolBar1->addSeparator();
    this->toolBar1->addAction(this->action7);
    this->toolBar1->addAction(this->action8);
    this->toolBar1->addAction(this->action9);
    this->toolBar1->addAction(this->action10);
    this->toolBar1->addSeparator();
    this->toolBar1->addAction(this->action11);
    this->addToolBar(this->toolBar1);

    this->tableView1 = new QTableView();
    this->plainTextEdit1 = new QPlainTextEdit();
    this->splitter1 = new QSplitter();
    this->splitter1->setOrientation(Qt::Horizontal);
    this->splitter1->addWidget(this->tableView1);
    this->splitter1->addWidget(this->plainTextEdit1);
    this->setCentralWidget(this->splitter1);

    this->label1 = new QLabel();
    this->label2 = new QLabel();
    this->label3 = new QLabel();
    this->statusBar1 = new QStatusBar();
    this->statusBar1->addWidget(this->label1);
    this->statusBar1->addWidget(this->label2);
    this->statusBar1->addWidget(this->label3);
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
    this->connect(this->action11, SIGNAL(triggered()), this, SLOT(action11_triggered()));

    this->standardItemModel1 = new QStandardItemModel(2, 6);
    this->itemSelectionModel1 = new QItemSelectionModel(this->standardItemModel1);
    this->connect(this->itemSelectionModel1, SIGNAL(currentChanged(QModelIndex, QModelIndex)), this, SLOT(itemSelectionModel1_currentChanged(QModelIndex, QModelIndex)));

    this->tableView1->setModel(this->standardItemModel1);
    this->tableView1->setSelectionModel(this->itemSelectionModel1);
    this->tableView1->setSelectionMode(QAbstractItemView::ExtendedSelection);
    this->tableView1->setSelectionBehavior(QAbstractItemView::SelectItems);

    this->tableView1->setItemDelegateForColumn(0, &this->spinBoxDelegate);
    this->tableView1->setItemDelegateForColumn(1, &this->doubleSpinBoxDelegate);
    this->tableView1->setItemDelegateForColumn(2, &this->doubleSpinBoxDelegate);
    this->tableView1->setItemDelegateForColumn(3, &this->doubleSpinBoxDelegate);
    this->tableView1->setItemDelegateForColumn(4, &this->comboBoxDelegate);
}

void MainWindow17::action1_triggered()
{
    // 打开文件
    QString cuurentPath = QCoreApplication::applicationDirPath();
    QString fileName = QFileDialog::getOpenFileName(this, "打开文件", cuurentPath, "文本文件(*.txt);;所有文件(*.*)");
    if(fileName.isEmpty())
        return;

    QStringList fileContent;
    QFile file(fileName);
    if(file.open(QIODevice::ReadOnly | QIODevice::Text))
    {
        this->plainTextEdit1->clear();
        QTextStream textStream(&file);
        while(!textStream.atEnd())
        {
            QString str = textStream.readLine();
            this->plainTextEdit1->appendPlainText(str);
            fileContent.append(str);
        }
        file.close();
        this->label1->setText(QString("当前文件:%1").arg(fileName));
        this->initOneLineData(fileContent);
    }
}

void MainWindow17::initOneLineData(QStringList &fileContent)
{
    // 处理文本内容
    int rowRount = fileContent.count();
    this->standardItemModel1->setRowCount(rowRount - 1);

    QString header = fileContent.at(0);
    QStringList headerList = header.split(QRegExp("\\s+"), QString::SkipEmptyParts);
    this->standardItemModel1->setHorizontalHeaderLabels(headerList);

    for(int i=1; i<rowRount; i++)
    {
        QString lineText = fileContent.at(i);
        QStringList lineTextList = lineText.split(QRegExp("\\s+"), QString::SkipEmptyParts);
        int columnCount = lineTextList.count();
        for(int j=0; j<columnCount - 1; j++)
        {
            QStandardItem *item = new QStandardItem(lineTextList.at(j));
            this->standardItemModel1->setItem(i - 1, j, item);
        }
        // 最后一列用可选框显示
        QStandardItem *item = new QStandardItem(headerList.at(columnCount - 1));
        item->setCheckable(true);
        if(lineTextList.at(columnCount - 1) == "0")
        {
            item->setCheckState(Qt::Unchecked);
        }
        else
        {
            item->setCheckState(Qt::Checked);
        }
        this->standardItemModel1->setItem(i - 1, columnCount - 1, item);
    }
}

void MainWindow17::action2_triggered()
{
    // 另存文件
    QString currentPath = QCoreApplication::applicationDirPath();
    QString fileName = QFileDialog::getSaveFileName(this, "选择文件", currentPath, "文本文件(*.txt);;所有文件(*.*)");
    if(fileName.isEmpty())
        return;

    QFile file(fileName);
    QTextStream textStream(&file);
    if(file.open(QIODevice::ReadWrite | QIODevice::Text | QIODevice::Truncate))
    {
        int rowCount = this->standardItemModel1->rowCount();
        int columnCount = this->standardItemModel1->columnCount();


        for(int i=0; i<columnCount; i++)
        {
            QStandardItem *item = this->standardItemModel1->horizontalHeaderItem(i);
            textStream << item->text() + "\t";
        }
        textStream << "\n";

        for(int r=0; r<rowCount; r++)
        {
            for(int c=0; c<columnCount - 1; c++)
            {
                QStandardItem *item = this->standardItemModel1->item(r, c);
                textStream << item->text() + "\t";
            }
            QStandardItem *item = this->standardItemModel1->item(r, columnCount - 1);
            if(item->checkState() == Qt::Checked)
            {
                textStream << "1";
            }
            else
            {
                textStream << "0";
            }
            textStream << "\n";
        }
    }
}

void MainWindow17::action3_triggered()
{
    // 模型数据预览
    this->plainTextEdit1->clear();
    QString str = "";
    int rowCount = this->standardItemModel1->rowCount();
    int columnCount = this->standardItemModel1->columnCount();


    for(int i=0; i<columnCount; i++)
    {
        QStandardItem *item = this->standardItemModel1->horizontalHeaderItem(i);
        str += item->text() + "\t";
    }
    this->plainTextEdit1->appendPlainText(str);

    for(int r=0; r<rowCount; r++)
    {
        str = "";
        for(int c=0; c<columnCount - 1; c++)
        {
            QStandardItem *item = this->standardItemModel1->item(r, c);
            str += item->text() + "\t";
        }
        QStandardItem *item = this->standardItemModel1->item(r, columnCount - 1);
        if(item->checkState() == Qt::Checked)
        {
            str += "1";
        }
        else
        {
            str += "0";
        }
        this->plainTextEdit1->appendPlainText(str);
    }
}

void MainWindow17::action4_triggered()
{
    // 添加行
    QList<QStandardItem*> itemList;
    int columnCount = this->standardItemModel1->columnCount();
    for(int c=0; c<columnCount - 1; c++)
    {
        QStandardItem *item = new QStandardItem(" ");
        itemList << item;
    }
    QString str = this->standardItemModel1->headerData(columnCount - 1, Qt::Horizontal, Qt::DisplayRole).toString();
    QStandardItem *item = new QStandardItem(str);
    item->setCheckable(true);
    itemList << item;

    this->standardItemModel1->insertRow(this->standardItemModel1->rowCount(), itemList);
    QModelIndex currentIndex = this->standardItemModel1->index(this->standardItemModel1->rowCount() - 1, 0);
    this->itemSelectionModel1->clearSelection();
    this->itemSelectionModel1->setCurrentIndex(currentIndex, QItemSelectionModel::Select);
}

void MainWindow17::action5_triggered()
{
    // 插入行
    QList<QStandardItem*> itemList;
    int columnCount = this->standardItemModel1->columnCount();
    for(int c=0; c<columnCount - 1; c++)
    {
        QStandardItem *item = new QStandardItem(" ");
        itemList << item;
    }
    QString str = this->standardItemModel1->headerData(columnCount - 1, Qt::Horizontal, Qt::DisplayRole).toString();
    QStandardItem *item = new QStandardItem(str);
    item->setCheckable(true);
    itemList << item;

    QModelIndex currentIdnex = this->itemSelectionModel1->currentIndex();
    this->standardItemModel1->insertRow(currentIdnex.row(), itemList);
}

void MainWindow17::action6_triggered()
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

void MainWindow17::action7_triggered()
{
    // 居左
    if(!this->itemSelectionModel1->hasSelection())
        return;

    QModelIndexList selectedIndexs = this->itemSelectionModel1->selectedIndexes();
    for(int i=0; i<selectedIndexs.count(); i++)
    {
        QModelIndex index = selectedIndexs.at(i);
        QStandardItem *item = this->standardItemModel1->itemFromIndex(index);
        item->setTextAlignment(Qt::AlignLeft);
    }
}

void MainWindow17::action8_triggered()
{
    // 居中
    if(!this->itemSelectionModel1->hasSelection())
        return;

    QModelIndexList selectedIndexs = this->itemSelectionModel1->selectedIndexes();
    for(int i=0; i<selectedIndexs.count(); i++)
    {
        QModelIndex index = selectedIndexs.at(i);
        QStandardItem *item = this->standardItemModel1->itemFromIndex(index);
        item->setTextAlignment(Qt::AlignCenter);
    }
}

void MainWindow17::action9_triggered()
{
    // 居右
    if(!this->itemSelectionModel1->hasSelection())
        return;

    QModelIndexList selectedIndexs = this->itemSelectionModel1->selectedIndexes();
    for(int i=0; i<selectedIndexs.count(); i++)
    {
        QModelIndex index = selectedIndexs.at(i);
        QStandardItem *item = this->standardItemModel1->itemFromIndex(index);
        item->setTextAlignment(Qt::AlignRight);
    }
}

void MainWindow17::action10_triggered(bool checked)
{
    // 粗体
    if(!this->itemSelectionModel1->hasSelection())
        return;

    QModelIndexList selectedIndexs = this->itemSelectionModel1->selectedIndexes();
    for(int i=0; i<selectedIndexs.count(); i++)
    {
        QModelIndex index = selectedIndexs.at(i);
        QStandardItem *item = this->standardItemModel1->itemFromIndex(index);
        QFont font = item->font();
        font.setBold(checked);
        item->setFont(font);
    }
}

void MainWindow17::action11_triggered()
{
    // 退出
    this->close();
}

void MainWindow17::itemSelectionModel1_currentChanged(const QModelIndex &current, const QModelIndex &previous)
{
    if(current.isValid())
    {
        this->label2->setText(QString("行:%1,列:%2").arg(current.row()).arg(current.column()));
        QStandardItem *item = this->standardItemModel1->itemFromIndex(current);
        this->label3->setText(QString("单元格内容:%1").arg(item->text()));
        QFont font = item->font();
        this->action10->setChecked(font.bold());
    }
}

QSpinBoxDelegate::QSpinBoxDelegate(QObject *parent) : QStyledItemDelegate(parent)
{

}

QWidget* QSpinBoxDelegate::createEditor(QWidget *parent, const QStyleOptionViewItem &option, const QModelIndex &index) const
{
    QSpinBox *spinBox = new QSpinBox(parent);
    spinBox->setFrame(false);
    spinBox->setMinimum(0);
    spinBox->setMaximum(100);
    return spinBox;
}

void QSpinBoxDelegate::setEditorData(QWidget *editor, const QModelIndex &index) const
{
    int value = index.model()->data(index, Qt::EditRole).toInt();
    QSpinBox *spinBox = static_cast<QSpinBox*>(editor);
    spinBox->setValue(value);
}

void QSpinBoxDelegate::setModelData(QWidget *editor, QAbstractItemModel *model, const QModelIndex &index) const
{
    QSpinBox *spinBox = static_cast<QSpinBox*>(editor);
    spinBox->interpretText();
    int value = spinBox->value();
    model->setData(index, value, Qt::EditRole);
}

void QSpinBoxDelegate::updateEditorGeometry(QWidget *editor, const QStyleOptionViewItem &option, const QModelIndex &index) const
{
    editor->setGeometry(option.rect);
}

QDoubleSpinBoxDelegate::QDoubleSpinBoxDelegate(QObject *parent) : QStyledItemDelegate(parent)
{

}

QWidget* QDoubleSpinBoxDelegate::createEditor(QWidget *parent, const QStyleOptionViewItem &option, const QModelIndex &index) const
{
    QDoubleSpinBox *doubleSpinBox = new QDoubleSpinBox(parent);
    doubleSpinBox->setFrame(false);
    doubleSpinBox->setMinimum(0);
    doubleSpinBox->setMaximum(100);
    return doubleSpinBox;
}

void QDoubleSpinBoxDelegate::setEditorData(QWidget *editor, const QModelIndex &index) const
{
    int value = index.model()->data(index, Qt::EditRole).toInt();
    QDoubleSpinBox *doubleSpinBox = static_cast<QDoubleSpinBox*>(editor);
    doubleSpinBox->setValue(value);
}

void QDoubleSpinBoxDelegate::setModelData(QWidget *editor, QAbstractItemModel *model, const QModelIndex &index) const
{
    QDoubleSpinBox *doubleSpinBox = static_cast<QDoubleSpinBox*>(editor);
    doubleSpinBox->interpretText();
    int value = doubleSpinBox->value();
    model->setData(index, value, Qt::EditRole);
}

void QDoubleSpinBoxDelegate::updateEditorGeometry(QWidget *editor, const QStyleOptionViewItem &option, const QModelIndex &index) const
{
    editor->setGeometry(option.rect);
}

QComboBoxDelegate::QComboBoxDelegate(QObject *parent) : QStyledItemDelegate(parent)
{

}

QWidget* QComboBoxDelegate::createEditor(QWidget *parent, const QStyleOptionViewItem &option, const QModelIndex &index) const
{
    QComboBox *comboBox = new QComboBox(parent);
    comboBox->setFrame(false);
//    QStringList strList;
//    strList << "111" << "222" << "333";
//    comboBox->insertItems(0, strList);
    comboBox->addItems(this->data);
    comboBox->setEditable(this->isEditable);
    return comboBox;
}

void QComboBoxDelegate::setEditorData(QWidget *editor, const QModelIndex &index) const
{
    QString value = index.model()->data(index, Qt::EditRole).toString();
    QComboBox *comboBox = static_cast<QComboBox*>(editor);
    comboBox->setCurrentText(value);
}

void QComboBoxDelegate::setModelData(QWidget *editor, QAbstractItemModel *model, const QModelIndex &index) const
{
    QComboBox *comboBox = static_cast<QComboBox*>(editor);
    QString value = comboBox->currentText();
    model->setData(index, value, Qt::EditRole);
}

void QComboBoxDelegate::updateEditorGeometry(QWidget *editor, const QStyleOptionViewItem &option, const QModelIndex &index) const
{
    editor->setGeometry(option.rect);
}

void QComboBoxDelegate::setItems(QStringList data, bool isEditable)
{
    this->data = data;
    this->isEditable = isEditable;
}

```