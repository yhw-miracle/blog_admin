
```c+++
#if _MSC_VER >= 1600
#pragma execution_character_set("utf-8")
#endif

#include "widget3.h"

Widget3::Widget3(QString title, QWidget *parent) : QWidget(parent)
{
    this->setWindowTitle(title);

    this->label1 = new QLabel();
    this->label1->setText("数量");
    this->spinBox1 = new QSpinBox();
    this->spinBox1->setSuffix(" kg");

    this->label2 = new QLabel();
    this->label2->setText("单价");
    this->doubleSpinBox2 = new QDoubleSpinBox();
    this->doubleSpinBox2->setPrefix("￥");

    this->label3 = new QLabel();
    this->label3->setText("总价");
    this->doubleSpinBox3 = new QDoubleSpinBox();
    this->doubleSpinBox3->setPrefix("￥");
    this->doubleSpinBox3->setEnabled(false);

    this->buttonCalc = new QPushButton();
    this->buttonCalc->setText("计算");

    this->gridLayout1 = new QGridLayout();
    this->gridLayout1->addWidget(this->label1, 0, 0);
    this->gridLayout1->addWidget(this->spinBox1, 0, 1);
    this->gridLayout1->addWidget(this->label2, 1, 0);
    this->gridLayout1->addWidget(this->doubleSpinBox2, 1, 1);
    this->gridLayout1->addWidget(this->buttonCalc, 2, 1);
    this->gridLayout1->addWidget(this->label3, 3, 0);
    this->gridLayout1->addWidget(this->doubleSpinBox3, 3, 1);

    this->label4 = new QLabel();
    this->label4->setText("二进制");
    this->spinBox4 = new QSpinBox();
    this->spinBox4->setDisplayIntegerBase(2);
    this->buttonTranform1 = new QPushButton();
    this->buttonTranform1->setText("转换为其他进制");

    this->label5 = new QLabel();
    this->label5->setText("八进制");
    this->spinBox5 = new QSpinBox();
    this->spinBox5->setDisplayIntegerBase(8);
    this->buttonTranform2 = new QPushButton();
    this->buttonTranform2->setText("转换为其他进制");

    this->label6 = new QLabel();
    this->label6->setText("十进制");
    this->spinBox6 = new QSpinBox();
    this->spinBox6->setDisplayIntegerBase(10);
    this->buttonTranform3 = new QPushButton();
    this->buttonTranform3->setText("转换为其他进制");

    this->label7 = new QLabel();
    this->label7->setText("十六进制");
    this->spinBox7 = new QSpinBox();
    this->spinBox7->setDisplayIntegerBase(16);
    this->buttonTranform4 = new QPushButton();
    this->buttonTranform4->setText("转换为其他进制");

    this->gridLayout2 = new QGridLayout();
    this->gridLayout2->addWidget(this->label4, 0, 0);
    this->gridLayout2->addWidget(this->spinBox4, 0, 1);
    this->gridLayout2->addWidget(this->buttonTranform1, 0, 2);
    this->gridLayout2->addWidget(this->label5, 1, 0);
    this->gridLayout2->addWidget(this->spinBox5, 1, 1);
    this->gridLayout2->addWidget(this->buttonTranform2, 1, 2);
    this->gridLayout2->addWidget(this->label6, 2, 0);
    this->gridLayout2->addWidget(this->spinBox6, 2, 1);
    this->gridLayout2->addWidget(this->buttonTranform3, 2, 2);
    this->gridLayout2->addWidget(this->label7, 3, 0);
    this->gridLayout2->addWidget(this->spinBox7, 3, 1);
    this->gridLayout2->addWidget(this->buttonTranform4, 3, 2);

    this->verticalSpacer = new QSpacerItem(10, 100);
    this->layout1 = new QVBoxLayout();
    this->layout1->addLayout(this->gridLayout1);
    this->layout1->addItem(this->verticalSpacer);
    this->layout1->addLayout(this->gridLayout2);
    this->setLayout(layout1);

    this->connect(this->buttonCalc, SIGNAL(clicked()), this, SLOT(buttonCalc_clicked()));
    this->connect(this->buttonTranform1, SIGNAL(clicked()), this, SLOT(buttonTranform_clicked()));
    this->connect(this->buttonTranform2, SIGNAL(clicked()), this, SLOT(buttonTranform_clicked()));
    this->connect(this->buttonTranform3, SIGNAL(clicked()), this, SLOT(buttonTranform_clicked()));
    this->connect(this->buttonTranform4, SIGNAL(clicked()), this, SLOT(buttonTranform_clicked()));
}

void Widget3::buttonCalc_clicked()
{
    int num1 = this->spinBox1->value();
    float num2 = this->doubleSpinBox2->value();
    float num3 = num1 * num2;
    this->doubleSpinBox3->setValue(num3);

}

void Widget3::buttonTranform_clicked()
{
    QPushButton *button = qobject_cast<QPushButton *>(sender());
    if(button == this->buttonTranform1)
    {
        int value = this->spinBox4->value();
        this->spinBox5->setValue(value);
        this->spinBox6->setValue(value);
        this->spinBox7->setValue(value);
    }
    else if(button == this->buttonTranform2)
    {
        int value = this->spinBox5->value();
        this->spinBox4->setValue(value);
        this->spinBox6->setValue(value);
        this->spinBox7->setValue(value);
    }
    else if(button == this->buttonTranform3)
    {
        int value = this->spinBox6->value();
        this->spinBox4->setValue(value);
        this->spinBox5->setValue(value);
        this->spinBox7->setValue(value);
    }
    else if(button == this->buttonTranform4)
    {
        int value = this->spinBox7->value();
        this->spinBox4->setValue(value);
        this->spinBox5->setValue(value);
        this->spinBox6->setValue(value);
    }
}
```