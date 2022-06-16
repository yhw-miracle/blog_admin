
```c++
#if _MSC_VER >= 1600
#pragma execution_character_set("utf-8")
#endif

#include "widget5.h"

Widget5::Widget5(QString title, QWidget *parent) : QWidget(parent)
{
    this->setWindowTitle(title);
    this->setGeometry(100, 100, 500, 300);

    QVBoxLayout *layout1 = new QVBoxLayout();

    this->scrollBar1 = new QScrollBar();
    this->scrollBar1->setOrientation(Qt::Horizontal);
    layout1->addWidget(this->scrollBar1);

    this->scrollBar2 = new QScrollBar();
    this->scrollBar2->setOrientation(Qt::Vertical);
    layout1->addWidget(this->scrollBar2);

    this->setLayout(layout1);
}
```