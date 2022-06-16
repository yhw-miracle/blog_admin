
```c+++
#if _MSC_VER >= 1600
#pragma execution_character_set("utf-8")
#endif

#include "widget6.h"

Widget6::Widget6(QString title, QWidget *parent) : QWidget(parent)
{
    this->setWindowTitle(title);

    QVBoxLayout *layout1 = new QVBoxLayout();

    this->processBar1 = new QProgressBar();
    layout1->addWidget(this->processBar1);

    this->setLayout(layout1);
}
```