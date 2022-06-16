
```c++
#if _MSC_VER >= 1600
#pragma execution_character_set("utf-8")
#endif

#include "mainwindow37.h"

MainWindow37::MainWindow37(QString title, QWidget *parent) : QMainWindow(parent)
{
    this->toolBox1 = new QToolBox();
    QWidget *w1 = new QWidget();
    this->toolBox1->addItem(w1, "QHostInfo");
    QWidget *w2 = new QWidget();
    this->toolBox1->addItem(w2, "QNetworkInterface");

    this->plainTextEdit1 = new QPlainTextEdit();

    QSplitter *splitter = new QSplitter();
    splitter->addWidget(this->toolBox1);
    splitter->addWidget(this->plainTextEdit1);

    this->setCentralWidget(splitter);

    QPushButton *button1 = new QPushButton();
    button1->setText("localHostName");
    QPushButton *button2 = new QPushButton();
    button2->setText("localDomainName");
    QPushButton *button3 = new QPushButton();
    button3->setText("addresses");
    QPushButton *button4 = new QPushButton();
    button4->setText("查询IP地址");

    this->connect(button1, SIGNAL(clicked()), this,SLOT(button1_clicked()));
    this->connect(button2, SIGNAL(clicked()), this,SLOT(button2_clicked()));
    this->connect(button3, SIGNAL(clicked()), this,SLOT(button3_clicked()));
    this->connect(button4, SIGNAL(clicked()), this,SLOT(button4_clicked()));

    QGridLayout *layout1 = new QGridLayout();
    layout1->addWidget(button1, 0, 0);
    layout1->addWidget(button2, 0, 1);
    layout1->addWidget(button3, 1, 0);
    layout1->addWidget(button4, 1, 1);
    w1->setLayout(layout1);

    QPushButton *button5= new QPushButton();
    button5->setText("allAddresses");
    QPushButton *button6= new QPushButton();
    button6->setText("allInterfaces");

    QGridLayout *layout2 = new QGridLayout();
    layout2->addWidget(button5, 0, 0);
    layout2->addWidget(button6, 0, 1);
    w2->setLayout(layout2);

    this->connect(button5, SIGNAL(clicked()), this,SLOT(button5_clicked()));
    this->connect(button6, SIGNAL(clicked()), this,SLOT(button6_clicked()));
}

void MainWindow37::button1_clicked()
{
    this->plainTextEdit1->appendPlainText("本机主机名:" + QHostInfo::localHostName());
}

void MainWindow37::button2_clicked()
{
    this->plainTextEdit1->appendPlainText("本机DNS域名:" + QHostInfo::localDomainName());
}

void MainWindow37::button3_clicked()
{
    QHostInfo hostInfo = QHostInfo::fromName(QHostInfo::localHostName());
    QList<QHostAddress> addresses = hostInfo.addresses();
    if(!addresses.empty())
    {
        foreach(QHostAddress address, addresses)
        {
            if(address.protocol() == QAbstractSocket::IPv4Protocol)
            {
                this->plainTextEdit1->appendPlainText("协议: IPv4Protocol");
            }
            else if(address.protocol() == QAbstractSocket::IPv6Protocol)
            {
                this->plainTextEdit1->appendPlainText("协议: IPv6Protocol");
            }
            else if(address.protocol() == QAbstractSocket::AnyIPProtocol)
            {
                this->plainTextEdit1->appendPlainText("协议: AnyIPProtocol");
            }
            else
            {
                this->plainTextEdit1->appendPlainText("协议: unknown");
            }

            this->plainTextEdit1->appendPlainText("本机IP地址:" + address.toString());
        }
    }
}

void MainWindow37::button4_clicked()
{
    this->plainTextEdit1->appendPlainText("正在查询 www.aliyun.com 的 IP地址:");
    QHostInfo::lookupHost("www.aliyun.com", this, SLOT(lookupHostInfo(const QHostInfo&)));
}

void MainWindow37::lookupHostInfo(const QHostInfo &host)
{
    QList<QHostAddress> addresses = host.addresses();
    if(!addresses.empty())
    {
        foreach(QHostAddress address, addresses)
        {
            if(address.protocol() == QAbstractSocket::IPv4Protocol)
            {
                this->plainTextEdit1->appendPlainText("协议: IPv4Protocol");
            }
            else if(address.protocol() == QAbstractSocket::IPv6Protocol)
            {
                this->plainTextEdit1->appendPlainText("协议: IPv6Protocol");
            }
            else if(address.protocol() == QAbstractSocket::AnyIPProtocol)
            {
                this->plainTextEdit1->appendPlainText("协议: AnyIPProtocol");
            }
            else
            {
                this->plainTextEdit1->appendPlainText("协议: unknown");
            }

            this->plainTextEdit1->appendPlainText("本机IP地址:" + address.toString());
        }
    }
}

void MainWindow37::button5_clicked()
{
    QList<QHostAddress> addresses = QNetworkInterface::allAddresses();
    if(!addresses.empty())
    {
        foreach(QHostAddress address, addresses)
        {
            if(address.protocol() == QAbstractSocket::IPv4Protocol)
            {
                this->plainTextEdit1->appendPlainText("协议: IPv4Protocol");
            }
            else if(address.protocol() == QAbstractSocket::IPv6Protocol)
            {
                this->plainTextEdit1->appendPlainText("协议: IPv6Protocol");
            }
            else if(address.protocol() == QAbstractSocket::AnyIPProtocol)
            {
                this->plainTextEdit1->appendPlainText("协议: AnyIPProtocol");
            }
            else
            {
                this->plainTextEdit1->appendPlainText("协议: unknown");
            }

            this->plainTextEdit1->appendPlainText("本机IP地址:" + address.toString());
        }
    }
}

void MainWindow37::button6_clicked()
{
    QList<QNetworkInterface> interfaces = QNetworkInterface::allInterfaces();
    foreach(QNetworkInterface interface, interfaces)
    {
        if(interface.isValid())
        {
            this->plainTextEdit1->appendPlainText("设备名称:" + interface.humanReadableName());
            this->plainTextEdit1->appendPlainText("硬件地址:" + interface.hardwareAddress());

            QList<QNetworkAddressEntry> entryList = interface.addressEntries();
            foreach(QNetworkAddressEntry entery, entryList)
            {
                this->plainTextEdit1->appendPlainText("IP 地址:" + entery.ip().toString());
                this->plainTextEdit1->appendPlainText("子网掩码:" + entery.netmask().toString());
                this->plainTextEdit1->appendPlainText("广播地址:" + entery.broadcast().toString());
            }
        }
    }
}

```