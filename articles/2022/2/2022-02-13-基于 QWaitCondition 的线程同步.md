
```c++
#if _MSC_VER >= 1600
#pragma execution_character_set("utf-8")
#endif

#include "mainwindow35.h"
#include <QDebug>

QMutex mutex;
QWaitCondition newDataAvailable;

int count = 0;
int diceValue = 0;

QProducerThread::QProducerThread()
{

}

void QProducerThread::run()
{
    this->isStop = false;
    // 随机数初始化 qsrand 是线程安全的
    qsrand(QTime::currentTime().msec());

    while (!this->isStop) {
        // 信号量和定时器的实现方式
        mutex.lock();
        // QMutexLocker mutexLocker(&this->mutex);
        // 获得随机数
        diceValue = qrand();
        diceValue = (diceValue % 6) + 1;
        count ++;
        mutex.unlock();
        newDataAvailable.wakeAll();

        msleep(1);
    }
    quit();
}

void QProducerThread::stopThread()
{
    this->isStop = true;
}

QConsumerThread::QConsumerThread()
{

}

void QConsumerThread::run()
{
    this->isStop = false;
    while(!this->isStop)
    {
        mutex.lock();
        newDataAvailable.wait(&mutex);
        emit this->newValue(count, diceValue);
        mutex.unlock();
    }
}

void QConsumerThread::stopThread()
{
    this->isStop = true;
}

MainWindow35::MainWindow35(QString title, QWidget *parent) : QMainWindow(parent)
{
    this->setWindowTitle(title);
    QFont font;
    font.setFamily("Hack");
    font.setPixelSize(12);
    this->setFont(font);

    this->groupBox1 = new QGroupBox();
    QHBoxLayout *layout1 = new QHBoxLayout();
    this->startThreadButton = new QPushButton();
    this->startThreadButton->setText("启动线程");
    this->endTheadButton = new QPushButton();
    this->endTheadButton->setText("结束线程");
    this->clearTextButton = new QPushButton();
    this->clearTextButton->setText("清空");
    layout1->addWidget(this->startThreadButton);
    layout1->addWidget(this->endTheadButton);
    layout1->addWidget(this->clearTextButton);

    this->plainTextEdit = new QPlainTextEdit();
    this->chartView = new QChartView();

    QSplitter *splitter = new QSplitter();
    splitter->setOrientation(Qt::Horizontal);
    splitter->addWidget(this->plainTextEdit);
    splitter->addWidget(this->chartView);

    QWidget *w = new QWidget();
    QVBoxLayout *layout3 = new QVBoxLayout();
    layout3->addLayout(layout1);
    layout3->addWidget(splitter);
    w->setLayout(layout3);
    this->setCentralWidget(w);

    this->statusBar1 = new QStatusBar();
    this->label1 = new QLabel();
    this->label2 = new QLabel();
    this->statusBar1->addWidget(this->label1);
    this->statusBar1->addWidget(this->label2);
    this->setStatusBar(this->statusBar1);

    this->connect(&this->producerThread, SIGNAL(started()), this, SLOT(producerThread_started()));
    this->connect(&this->producerThread, SIGNAL(finished()), this, SLOT(producerThread_finished()));
    this->connect(&this->consumerThread, SIGNAL(started()), this, SLOT(consumerThread_started()));
    this->connect(&this->consumerThread, SIGNAL(finished()), this, SLOT(consumerThread_finished()));
    this->connect(&this->consumerThread, SIGNAL(newValue(int, int)), this, SLOT(consumerThread_newValue(int, int)));

    this->connect(this->startThreadButton, SIGNAL(clicked()), this, SLOT(startThreadButton_clicked()));
    this->connect(this->endTheadButton, SIGNAL(clicked()), this, SLOT(endTheadButton_clicked()));
    this->connect(this->clearTextButton, SIGNAL(clicked()), this, SLOT(clearTextButton_clicked()));

    this->historyDiceValue[1] = 0;
    this->historyDiceValue[2] = 0;
    this->historyDiceValue[3] = 0;
    this->historyDiceValue[4] = 0;
    this->historyDiceValue[5] = 0;
    this->historyDiceValue[6] = 0;
}

void MainWindow35::producerThread_started()
{
    this->label1->setText("producer thread start.");
}

void MainWindow35::producerThread_finished()
{
    this->label1->setText("producer thread finished.");
}

void MainWindow35::consumerThread_started()
{
    this->label2->setText("consumer thread start.");
}

void MainWindow35::consumerThread_finished()
{
    this->label2->setText("consumer thread finished.");
}

void MainWindow35::consumerThread_newValue(int count, int diceValue)
{
    this->plainTextEdit->appendPlainText(QString("第 %1 次掷骰子，点数为 %2.").arg(count).arg(diceValue));
    this->historyDiceValue[diceValue] ++;
}

void MainWindow35::buildPieChart()
{
    QChart *chart = this->chartView->chart();
    chart->removeAllSeries();

    QPieSeries *pieSeries = new QPieSeries();
    // 饼图中间空心大小
    pieSeries->setHoleSize(0);
    // 添加分块数据
    pieSeries->append("1", this->historyDiceValue[1]);
    pieSeries->append("2", this->historyDiceValue[2]);
    pieSeries->append("3", this->historyDiceValue[3]);
    pieSeries->append("4", this->historyDiceValue[4]);
    pieSeries->append("5", this->historyDiceValue[5]);
    pieSeries->append("6", this->historyDiceValue[6]);

    QPieSlice *slice;
    // 饼图分块文字
    for(int i=0; i<6; i++)
    {
        slice = pieSeries->slices().at(i);
        slice->setLabel(slice->label() + QString(": %1 次,占 %2%").arg(slice->value()).arg(slice->percentage() * 100));
        this->connect(slice, SIGNAL(hovered(bool)), this, SLOT(pieSlice_hovered(bool)));
    }

    slice->setExploded(true);
    pieSeries->setLabelsVisible(true);
    chart->addSeries(pieSeries);
    chart->setTitle("骰子统计结果");
    chart->legend()->setVisible(false);
//    chart->legend()->setAlignment(Qt::AlignBottom);
}

void MainWindow35::pieSlice_hovered(bool show)
{
    QPieSlice *slice = (QPieSlice*)sender();
    slice->setExploded(show);
}

void MainWindow35::startThreadButton_clicked()
{
    // 注意: 这里先启动生产者线程后启动消费者线程，数据不会丢失
    // 先启动消费者线程后启动生产者线程，会丢失第一次数据
    this->producerThread.start();
    this->consumerThread.start();
    this->startThreadButton->setEnabled(false);
    this->endTheadButton->setEnabled(true);
}

void MainWindow35::endTheadButton_clicked()
{
    this->producerThread.stopThread();
    this->producerThread.wait();
    this->consumerThread.stopThread();
    this->consumerThread.terminate();
    this->startThreadButton->setEnabled(true);
    this->endTheadButton->setEnabled(false);

    this->buildPieChart();
}

void MainWindow35::clearTextButton_clicked()
{
    this->plainTextEdit->clear();
}

void MainWindow35::closeEvent(QCloseEvent *event)
{
    if(this->producerThread.isRunning())
    {
        this->producerThread.stopThread();
        this->producerThread.wait();
    }
    if(this->consumerThread.isRunning())
    {
        this->consumerThread.stopThread();
        this->consumerThread.terminate();
    }
    event->accept();
}

```