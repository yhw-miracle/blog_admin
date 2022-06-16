
```c++
#if _MSC_VER >= 1600
#pragma execution_character_set("utf-8")
#endif

#include "widget7.h"

Widget7::Widget7(QString title, QWidget *parent) : QWidget(parent)
{
    this->setWindowTitle(title);

    this->dial1 = new QDial();
    this->dial1->setNotchesVisible(true);
    this->dial1->setNotchTarget(1);
    this->lcdNumber1 = new QLCDNumber();

    QVBoxLayout *layout2 = new QVBoxLayout();
    this->radioButton1 = new QRadioButton();
    this->radioButton1->setText("二进制");
    this->radioButton2 = new QRadioButton();
    this->radioButton2->setText("八进制");
    this->radioButton3 = new QRadioButton();
    this->radioButton3->setText("十进制");
    this->radioButton4 = new QRadioButton();
    this->radioButton4->setText("十六进制");
    layout2->addWidget(this->radioButton1);
    layout2->addWidget(this->radioButton2);
    layout2->addWidget(this->radioButton3);
    layout2->addWidget(this->radioButton4);

    this->groupBox1 = new QGroupBox();
    this->groupBox1->setTitle("LCD 显示进制");
    this->groupBox1->setLayout(layout2);

    QHBoxLayout *layout1 = new QHBoxLayout();
    layout1->addWidget(this->dial1);
    layout1->addWidget(this->lcdNumber1);
    layout1->addWidget(this->groupBox1);
    this->setLayout(layout1);

    this->connect(this->dial1, SIGNAL(valueChanged(int)), this, SLOT(dial1_valueChanged(int)));
    this->connect(this->radioButton1, SIGNAL(clicked(bool)), this, SLOT(radioButton_clicked(bool)));
    this->connect(this->radioButton2, SIGNAL(clicked(bool)), this, SLOT(radioButton_clicked(bool)));
    this->connect(this->radioButton3, SIGNAL(clicked(bool)), this, SLOT(radioButton_clicked(bool)));
    this->connect(this->radioButton4, SIGNAL(clicked(bool)), this, SLOT(radioButton_clicked(bool)));
}

void Widget7::dial1_valueChanged(int value)
{
    this->lcdNumber1->display(value);
}

void Widget7::radioButton_clicked(bool checked)
{
    QRadioButton *currentRadioButton = qobject_cast<QRadioButton *>(sender());
    if(currentRadioButton == this->radioButton1)
    {
        if(checked)
        {
            this->lcdNumber1->setDigitCount(8);
            this->lcdNumber1->setBinMode();
        }
    }
    else if(currentRadioButton == this->radioButton2)
    {
        if(checked)
        {
            this->lcdNumber1->setDigitCount(4);
            this->lcdNumber1->setOctMode();
        }
    }
    else if(currentRadioButton == this->radioButton3)
    {
        if(checked)
        {
            this->lcdNumber1->setDigitCount(3);
            this->lcdNumber1->setDecMode();
        }
    }
    else if(currentRadioButton == this->radioButton4)
    {
        if(checked)
        {
            this->lcdNumber1->setDigitCount(3);
            this->lcdNumber1->setHexMode();
        }
    }
}

```