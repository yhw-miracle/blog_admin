
```c++
#if _MSC_VER >= 1600
#pragma execution_character_set("utf-8")
#endif

#include "widget11.h"

#include <QMap>
#include <QTextDocument>
#include <QTextBlock>

Widget11::Widget11(QString title, QWidget *parent) : QWidget(parent)
{
    this->setWindowTitle(title);

    this->initSimpleComboBoxButton = new QPushButton();
    this->initSimpleComboBoxButton->setText("初始化列表");
    this->clearSimpleComboBoxButton = new QPushButton();
    this->clearSimpleComboBoxButton->setText("清空列表");
    this->simpleComboBox = new QComboBox();

    QHBoxLayout *layout1 = new QHBoxLayout();
    layout1->addWidget(this->initSimpleComboBoxButton);
    layout1->addWidget(this->clearSimpleComboBoxButton);
    QVBoxLayout *layout2 = new QVBoxLayout();
    layout2->addLayout(layout1);
    layout2->addWidget(this->simpleComboBox);
    this->groupBox1 = new QGroupBox();
    this->groupBox1->setTitle("simple combobox");
    this->groupBox1->setLayout(layout2);

    this->initWithUserDataComboBoxButton = new QPushButton();
    this->initWithUserDataComboBoxButton->setText("初始化城市+区号");
    this->withUserDataComboBox = new QComboBox();
    QVBoxLayout *layout3 = new QVBoxLayout();
    layout3->addWidget(this->initWithUserDataComboBoxButton);
    layout3->addWidget(this->withUserDataComboBox);
    this->groupBox2 = new QGroupBox();
    this->groupBox2->setTitle("with userdata combobox");
    this->groupBox2->setLayout(layout3);

    this->addContentToComboBoxButton = new QPushButton();
    this->addContentToComboBoxButton->setText("文本框内容添加到 combobox");
    this->clearPLainTextEditButton = new QPushButton();
    this->clearPLainTextEditButton->setText("清空文本内容");
    this->comboBox1 = new QComboBox();
    this->plainTextEdit1 = new QPlainTextEdit();

    QHBoxLayout *layout4 = new QHBoxLayout();
    layout4->addWidget(this->addContentToComboBoxButton);
    layout4->addWidget(this->clearPLainTextEditButton);
    QVBoxLayout *layout5 = new QVBoxLayout();
    layout5->addLayout(layout4);
    layout5->addWidget(this->comboBox1);
    layout5->addWidget(this->plainTextEdit1);
    this->groupBox3 = new QGroupBox();
    this->groupBox3->setTitle("QPlainTextEdit(具有标准快捷菜单)");
    this->groupBox3->setLayout(layout5);

    QHBoxLayout *layout6 = new QHBoxLayout();
    layout6->addWidget(this->groupBox1);
    layout6->addWidget(this->groupBox2);
    QVBoxLayout *layout7 = new QVBoxLayout();
    layout7->addLayout(layout6);
    layout7->addWidget(this->groupBox3);
    this->setLayout(layout7);

    this->connect(this->initSimpleComboBoxButton, SIGNAL(clicked()), this, SLOT(initSimpleComboBoxButton_clicked()));
    this->connect(this->clearSimpleComboBoxButton, SIGNAL(clicked()), this, SLOT(clearSimpleComboBoxButton_clicked()));
    this->connect(this->initWithUserDataComboBoxButton, SIGNAL(clicked()), this, SLOT(initWithUserDataComboBoxButton_clicked()));
    this->connect(this->addContentToComboBoxButton, SIGNAL(clicked()), this, SLOT(addContentToComboBoxButton_clicked()));
    this->connect(this->clearPLainTextEditButton, SIGNAL(clicked()), this, SLOT(clearPLainTextEditButton_clicked()));

    this->connect(this->simpleComboBox, SIGNAL(currentIndexChanged(const QString)), this, SLOT(simpleComboBox_currentIndexChanged(const QString)));
    this->connect(this->withUserDataComboBox, SIGNAL(currentIndexChanged(const QString)), this, SLOT(withUserDataComboBox_currentIndexChanged(const QString)));
    this->connect(this->plainTextEdit1, SIGNAL(customContextMenuRequested(const QPoint)), this, SLOT(plainTextEdit1_customContextMenuRequested(const QPoint)));
}

void Widget11::initSimpleComboBoxButton_clicked()
{
    this->simpleComboBox->clear();
    for(int i=0; i<10; i++)
    {
        this->simpleComboBox->addItem(QString::asprintf("Item %d", i));
    }
}

void Widget11::clearSimpleComboBoxButton_clicked()
{
    this->simpleComboBox->clear();
}

void Widget11::initWithUserDataComboBoxButton_clicked()
{
    QMap<int, QString> cityZone;
    cityZone.insert(1, "北京");
    cityZone.insert(2, "上海");
    cityZone.insert(3, "广州");
    cityZone.insert(4, "深圳");
    cityZone.insert(5, "南京");
    cityZone.insert(6, "合肥");

    foreach(const int cityZontKey, cityZone.keys())
    {
        this->withUserDataComboBox->addItem(cityZone.value(cityZontKey), cityZontKey);
    }
}

void Widget11::simpleComboBox_currentIndexChanged(const QString &arg1)
{
    this->plainTextEdit1->appendPlainText(arg1);
}

void Widget11::withUserDataComboBox_currentIndexChanged(const QString &arg1)
{
    // 获取 combobox 项的 userdata
    QString str1 = this->withUserDataComboBox->currentData().toString();
    this->plainTextEdit1->appendPlainText(str1 + ":" +arg1);
}

void Widget11::addContentToComboBoxButton_clicked()
{
    // 文本对象
    QTextDocument *doc = this->plainTextEdit1->document();
    // 回车符是一个 block
    int count = doc->blockCount();

    for(int i=0; i<count; i++)
    {
        QTextBlock textLine = doc->findBlockByNumber(i);
        QString str1 = textLine.text();
        this->comboBox1->addItem(str1);
    }
}

void Widget11::clearPLainTextEditButton_clicked()
{
    this->plainTextEdit1->clear();
}

void Widget11::plainTextEdit1_customContextMenuRequested(const QPoint &pos)
{
    QMenu *menu1 = this->plainTextEdit1->createStandardContextMenu();
    menu1->exec(pos);
}

```