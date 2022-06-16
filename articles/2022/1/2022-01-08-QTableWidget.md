
```c++
#if _MSC_VER >= 1600
#pragma execution_character_set("utf-8")
#endif

#include "mainwindow14.h"

#include <QStringList>
#include <QFont>
#include <QColor>
#include <QDate>
#include <QAbstractItemView>
#include <QHeaderView>
#include <QDebug>

MainWindow14::MainWindow14(QString title, QWidget *parent) : QMainWindow(parent)
{
    this->setWindowTitle(title);

    this->button1 = new QPushButton();
    this->button1->setText("设置表头");
    this->button2 = new QPushButton();
    this->button2->setText("设置行数");
    this->spinBox1 = new QSpinBox();
    this->button3 = new QPushButton();
    this->button3->setText("初始化表格数据");
    this->button4 = new QPushButton();
    this->button4->setText("插入行");
    this->button5 = new QPushButton();
    this->button5->setText("添加行");
    this->button6 = new QPushButton();
    this->button6->setText("删除当前行");
    this->button7 = new QPushButton();
    this->button7->setText("自动调节行高");
    this->button8 = new QPushButton();
    this->button8->setText("自动调节列宽");
    this->button9 = new QPushButton();
    this->button9->setText("读取表格内容到文本");
    this->checkBox1 = new QCheckBox();
    this->checkBox1->setText("表格可编辑");
    this->checkBox2 = new QCheckBox();
    this->checkBox2->setText("间隔行底色");
    this->checkBox3 = new QCheckBox();
    this->checkBox3->setText("显示行表头");
    this->checkBox4 = new QCheckBox();
    this->checkBox4->setText("显示列表头");
    this->radioButton1 = new QRadioButton();
    this->radioButton1->setText("行选择");
    this->radioButton2 = new QRadioButton();
    this->radioButton2->setText("单元格选择");

    QGridLayout *gridLayout1 = new QGridLayout();
    gridLayout1->addWidget(this->button1, 0, 0, 1, 2);
    gridLayout1->addWidget(this->button2, 1, 0);
    gridLayout1->addWidget(this->spinBox1, 1, 1);
    gridLayout1->addWidget(this->button3, 2, 0, 1, 2);
    gridLayout1->addWidget(this->button4, 3, 0);
    gridLayout1->addWidget(this->button5, 3, 1);
    gridLayout1->addWidget(this->button6, 4, 0, 1, 2);
    gridLayout1->addWidget(this->button7, 5, 0);
    gridLayout1->addWidget(this->button8, 5, 1);
    gridLayout1->addWidget(this->button9, 6, 0, 1, 2);
    gridLayout1->addWidget(this->checkBox1, 7, 0);
    gridLayout1->addWidget(this->checkBox2, 7, 1);
    gridLayout1->addWidget(this->checkBox3, 8, 0);
    gridLayout1->addWidget(this->checkBox4, 8, 1);
    gridLayout1->addWidget(this->radioButton1, 9, 0);
    gridLayout1->addWidget(this->radioButton2, 9, 1);
    this->groupBox1 = new QGroupBox();
    this->groupBox1->setLayout(gridLayout1);

    this->tableWidget1 = new QTableWidget();
    this->plainTextEdit1 = new QPlainTextEdit();

    this->splitter1 = new QSplitter();
    this->splitter1->setOrientation(Qt::Vertical);
    this->splitter1->addWidget(this->tableWidget1);
    this->splitter1->addWidget(this->plainTextEdit1);

    this->splitter2 = new QSplitter();
    this->splitter2->setOrientation(Qt::Horizontal);
    this->splitter2->addWidget(this->groupBox1);
    this->splitter2->addWidget(this->splitter1);

    this->setCentralWidget(this->splitter2);

    this->label1 = new QLabel();
    this->label2 = new QLabel();
    this->label3 = new QLabel();
    this->statusBar1 = new QStatusBar();
    this->statusBar1->addWidget(this->label1);
    this->statusBar1->addWidget(this->label2);
    this->statusBar1->addWidget(this->label3);
    this->setStatusBar(this->statusBar1);

    this->connect(this->button1, SIGNAL(clicked()), this, SLOT(button1_clicked()));
    this->connect(this->button2, SIGNAL(clicked()), this, SLOT(button2_clicked()));
    this->connect(this->button3, SIGNAL(clicked()), this, SLOT(button3_clicked()));
    this->connect(this->button4, SIGNAL(clicked()), this, SLOT(button4_clicked()));
    this->connect(this->button5, SIGNAL(clicked()), this, SLOT(button5_clicked()));
    this->connect(this->button6, SIGNAL(clicked()), this, SLOT(button6_clicked()));
    this->connect(this->button7, SIGNAL(clicked()), this, SLOT(button7_clicked()));
    this->connect(this->button8, SIGNAL(clicked()), this, SLOT(button8_clicked()));
    this->connect(this->button9, SIGNAL(clicked()), this, SLOT(button9_clicked()));
    this->connect(this->checkBox1, SIGNAL(clicked(bool)), this, SLOT(checkBox1_clicked(bool)));
    this->connect(this->checkBox2, SIGNAL(clicked(bool)), this, SLOT(checkBox2_clicked(bool)));
    this->connect(this->checkBox3, SIGNAL(clicked(bool)), this, SLOT(checkBox3_clicked(bool)));
    this->connect(this->checkBox4, SIGNAL(clicked(bool)), this, SLOT(checkBox4_clicked(bool)));
    this->connect(this->radioButton1, SIGNAL(clicked(bool)), this, SLOT(radioButton1_clicked(bool)));
    this->connect(this->radioButton2, SIGNAL(clicked(bool)), this, SLOT(radioButton2_clicked(bool)));
    this->connect(this->tableWidget1, SIGNAL(currentCellChanged(int, int, int, int)), this, SLOT(tableWidget1_currentCellChanged(int, int, int, int)));
}

void MainWindow14::button1_clicked()
{
    // 设置表头
    QStringList headerText;
    headerText << "姓名" << "性别" << "出生日期" << "民族" << "分数" << "是否党员";
    this->tableWidget1->setHorizontalHeaderLabels(headerText);
    this->tableWidget1->setColumnCount(6);
    this->tableWidget1->setShowGrid(true);
    for(int i=0; i<this->tableWidget1->columnCount(); i++)
    {
        QTableWidgetItem *headerItem = new QTableWidgetItem(headerText.at(i));
        QFont font = headerItem->font();
        font.setBold(true);
        font.setPointSize(12);
        font.setFamily("hack");
        headerItem->setFont(font);
        headerItem->setTextColor(QColor("#800080"));
        this->tableWidget1->setHorizontalHeaderItem(i, headerItem);
    }
}

void MainWindow14::addOneRowToTableWidget1(int row, QString name, QString sex, QDate *birth, QString nation, QString score, bool isParty)
{
    QTableWidgetItem *nameItem = new QTableWidgetItem(name, MainWindow14::nameCellType);
    nameItem->setTextAlignment(Qt::AlignHCenter | Qt::AlignVCenter);
    nameItem->setData(Qt::UserRole, QVariant(name));
    this->tableWidget1->setItem(row, MainWindow14::nameColumnNum, nameItem);

    QTableWidgetItem *sexItem = new QTableWidgetItem(sex, MainWindow14::sexCellType);
    sexItem->setTextAlignment(Qt::AlignHCenter | Qt::AlignVCenter);
    sexItem->setData(Qt::UserRole, QVariant(sex));
    this->tableWidget1->setItem(row, MainWindow14::sexColumnNum, sexItem);

    QTableWidgetItem *birthItem = new QTableWidgetItem(birth->toString("yyyy年MM月dd日"), MainWindow14::birthCellType);
    birthItem->setTextAlignment(Qt::AlignHCenter | Qt::AlignVCenter);
    birthItem->setData(Qt::UserRole, QVariant(birth->toString("yyyy年MM月dd日")));
    this->tableWidget1->setItem(row, MainWindow14::birthColumnNum, birthItem);

    QTableWidgetItem *nationItem = new QTableWidgetItem(nation, MainWindow14::nationCellType);
    nationItem->setTextAlignment(Qt::AlignHCenter | Qt::AlignVCenter);
    nationItem->setData(Qt::UserRole, QVariant(nation));
    this->tableWidget1->setItem(row, MainWindow14::nationColumnNum, nationItem);

    QTableWidgetItem *scoreItem = new QTableWidgetItem(score, MainWindow14::scoreCellType);
    scoreItem->setTextAlignment(Qt::AlignHCenter | Qt::AlignVCenter);
    scoreItem->setData(Qt::UserRole, QVariant(score));
    this->tableWidget1->setItem(row, MainWindow14::scoreColumnNum, scoreItem);

    QTableWidgetItem *partyItem = new QTableWidgetItem("党员", MainWindow14::partyCellType);
    partyItem->setTextAlignment(Qt::AlignHCenter | Qt::AlignVCenter);
    partyItem->setData(Qt::UserRole, QVariant(isParty));
    if(isParty)
    {
        partyItem->setCheckState(Qt::Checked);
    }
    else
    {
        partyItem->setCheckState(Qt::Unchecked);
    }
    this->tableWidget1->setItem(row, MainWindow14::partyColumnNum, partyItem);
}

void MainWindow14::button2_clicked()
{
    // 设置行数
    int count = this->spinBox1->value();
    this->tableWidget1->setRowCount(count);
}

void MainWindow14::button3_clicked()
{
    // 初始化表格数据

    // 清除工作区，不清除表头
    this->tableWidget1->clearContents();
    int row = this->tableWidget1->rowCount();
    if(row == 0)
    {
        row = 10;
    }
    for(int i=0; i<row; i++)
    {
        QString name = QString::asprintf("name_%d", i);

        QString sex;
        if(i % 2 == 0)
        {
            sex = "男";
        }
        else
        {
            sex = "女";
        }

        QDate *birth = new QDate(2000, 1 ,1);

        QString nation = "汉族";

        QString score;
        score.setNum(100);

        bool isParty = false;
        if(i % 2 == 0)
        {
            isParty = true;
        }

        this->addOneRowToTableWidget1(i, name, sex, birth, nation, score, isParty);
    }
}

void MainWindow14::button4_clicked()
{
    // 插入行
    int currentRow = this->tableWidget1->currentRow();
    QString name = QString::asprintf("name_%d", currentRow);

    QString sex = "男";

    QDate *birth = new QDate(2000, 1 ,1);

    QString nation = "汉族";

    QString score;
    score.setNum(100);

    bool isParty = false;
    this->addOneRowToTableWidget1(currentRow, name, sex, birth, nation, score, isParty);
}

void MainWindow14::button5_clicked()
{
    // 添加行
    int row = this->tableWidget1->rowCount();
    QString name = QString::asprintf("name_%d", row);

    QString sex = "男";

    QDate *birth = new QDate(2000, 1 ,1);

    QString nation = "汉族";

    QString score;
    score.setNum(100);

    bool isParty = false;
    this->addOneRowToTableWidget1(row, name, sex, birth, nation, score, isParty);
}

void MainWindow14::button6_clicked()
{
    // 删除当前行
    int currentRow = this->tableWidget1->currentRow();
    this->tableWidget1->removeRow(currentRow);
}

void MainWindow14::button7_clicked()
{
    // 自动调节行高
    this->tableWidget1->resizeRowsToContents();
}

void MainWindow14::button8_clicked()
{
    // 自动调节列宽
    this->tableWidget1->resizeColumnsToContents();
}

void MainWindow14::button9_clicked()
{
    // 读取表格内容到文本
    int row = this->tableWidget1->rowCount();
    int column = this->tableWidget1->columnCount();

    QString str1 = "";

    for(int r=0; r<row; r++)
    {
        str1 = QString::asprintf("第 %d 行", r);
        for(int c=0; c<column; c++)
        {
            if(c == 5)
            {
                if(this->tableWidget1->item(r, c)->checkState() == Qt::Checked)
                {
                    str1 += "党员";
                }
                else
                {
                    str1 += "非党员";
                }
            }
            else
            {
                str1 += this->tableWidget1->item(r, c)->text();
            }
        }
        this->plainTextEdit1->appendPlainText(str1);
    }
}

void MainWindow14::checkBox1_clicked(bool checked)
{
    // 表格可编辑
    if(checked)
    {
        this->tableWidget1->setEditTriggers(QAbstractItemView::DoubleClicked | QAbstractItemView::SelectedClicked);
    }
    else
    {
        this->tableWidget1->setEditTriggers(QAbstractItemView::NoEditTriggers);
    }
}

void MainWindow14::checkBox2_clicked(bool checked)
{
    // 间隔行底色
    this->tableWidget1->setAlternatingRowColors(checked);
}

void MainWindow14::checkBox3_clicked(bool checked)
{
    // 显示行表头
    this->tableWidget1->horizontalHeader()->setVisible(checked);
}

void MainWindow14::checkBox4_clicked(bool checked)
{
    // 显示列表头
    this->tableWidget1->verticalHeader()->setVisible(checked);
}

void MainWindow14::radioButton1_clicked(bool checked)
{
    // 行选择
    Q_UNUSED(checked);
    this->tableWidget1->setSelectionBehavior(QAbstractItemView::SelectRows);
}

void MainWindow14::radioButton2_clicked(bool checked)
{
    // 单元格选择
    Q_UNUSED(checked);
    this->tableWidget1->setSelectionBehavior(QAbstractItemView::SelectItems);
}

void MainWindow14::tableWidget1_currentCellChanged(int currentRow, int currentColumn, int previousRow, int previousColumn)
{
    Q_UNUSED(previousColumn);
    Q_UNUSED(previousRow);
    QTableWidgetItem *item = this->tableWidget1->item(currentRow, currentColumn);
    if(!item)
        return;
    this->label1->setText(QString::asprintf("当前单元格坐标:第 %d 行第 %d 列", currentRow + 1, currentColumn + 1));
    this->label2->setText(QString::asprintf("当前单元格类型:%d", item->type()));
    if(currentColumn == 5)
    {
        if(item->checkState() == Qt::Checked)
        {
            this->label3->setText("当前单元格数据:党员");
        }
        else
        {
            this->label3->setText("当前单元格数据:非党员");
        }
    }
    else
    {
        this->label3->setText("当前单元格数据:" + item->text());
    }
}

```