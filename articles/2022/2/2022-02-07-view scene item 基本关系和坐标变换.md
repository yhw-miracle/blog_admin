
```c++
#if _MSC_VER >= 1600
#pragma execution_character_set("utf-8")
#endif

#include "mainwindow28.h"

MainWindow28::MainWindow28(QString title, QWidget *parent) : QMainWindow(parent)
{
    this->setWindowTitle(title);

    this->statusBar1 = new QStatusBar();
    this->label3 = new QLabel();
    this->label3->setText("View 坐标:");
    this->label4 = new QLabel();
    this->label4->setText("Scene 坐标:");
    this->label5 = new QLabel();
    this->label5->setText("Item 坐标:");
    this->statusBar1->addWidget(this->label3);
    this->statusBar1->addWidget(this->label4);
    this->statusBar1->addWidget(this->label5);
    this->setStatusBar(this->statusBar1);

    this->label1 = new QLabel();
    this->label2 = new QLabel();
    QVBoxLayout *layout1 = new QVBoxLayout();
    layout1->addWidget(this->label1);
    layout1->addWidget(this->label2);
    this->groupBox1 = new QGroupBox();
    this->groupBox1->setLayout(layout1);

    this->graphicsViewWithMouseEvent = new QGraphicsViewWithMouseEvent();
    this->graphicsViewWithMouseEvent->setCursor(Qt::CrossCursor);
    this->graphicsViewWithMouseEvent->setMouseTracking(true);
    this->graphicsViewWithMouseEvent->setDragMode(QGraphicsView::RubberBandDrag);
    this->connect(this->graphicsViewWithMouseEvent, SIGNAL(mouseMovePoint(QPoint)), this, SLOT(mouseMovePoint(QPoint)));
    this->connect(this->graphicsViewWithMouseEvent, SIGNAL(mouseClicked(QPoint)), this, SLOT(mouseClicked(QPoint)));

    QVBoxLayout *layout2 = new QVBoxLayout();
    layout2->addWidget(this->groupBox1);
    layout2->addWidget(this->graphicsViewWithMouseEvent);
    QWidget *widget = new QWidget();
    widget->setLayout(layout2);
    this->setCentralWidget(widget);

    this->initGraphicsSystem();
}

void MainWindow28::mouseMovePoint(QPoint point)
{
    this->label3->setText(QString("View 坐标:%1,%2").arg(point.x()).arg(point.y()));

    QPointF scenePoint = this->graphicsViewWithMouseEvent->mapToScene(point);
    this->label4->setText(QString("scene 坐标:%1,%2").arg(scenePoint.x()).arg(scenePoint.y()));
}

void MainWindow28::mouseClicked(QPoint point)
{
    QPointF scenePoint = this->graphicsViewWithMouseEvent->mapToScene(point);
    QGraphicsItem *item = this->graphicsScene1->itemAt(scenePoint, this->graphicsViewWithMouseEvent->transform());
    if(item != NULL)
    {
        QPointF itemPoint = item->mapFromScene(scenePoint);
        this->label5->setText(QString("item 坐标:%1,%2").arg(itemPoint.x()).arg(itemPoint.y()));
    }
}

void MainWindow28::initGraphicsSystem()
{
    QRectF rectF(-200, -100, 500, 200);
    this->graphicsScene1 = new QGraphicsScene(rectF);
    this->graphicsViewWithMouseEvent->setScene(this->graphicsScene1);

    QGraphicsRectItem *item1 = new QGraphicsRectItem(rectF);
    item1->setFlags(QGraphicsItem::ItemIsSelectable | QGraphicsItem::ItemIsFocusable);
    QPen pen;
    pen.setWidth(1);
    item1->setPen(pen);
    this->graphicsScene1->addItem(item1);

    QGraphicsEllipseItem *item2 = new QGraphicsEllipseItem(-100, -50, 200, 100);
    item2->setPos(0, 0);
    item2->setBrush(QBrush(Qt::green));
    item2->setFlags(QGraphicsItem::ItemIsMovable | QGraphicsItem::ItemIsSelectable | QGraphicsItem::ItemIsFocusable);
    this->graphicsScene1->addItem(item2);

    QGraphicsEllipseItem *item3 = new QGraphicsEllipseItem(-50, -50, 100, 100);
    item3->setPos(rectF.right(), rectF.bottom());
    item3->setBrush(QBrush(Qt::red));
    item3->setFlags(QGraphicsItem::ItemIsMovable | QGraphicsItem::ItemIsSelectable | QGraphicsItem::ItemIsFocusable);
    this->graphicsScene1->addItem(item3);

    this->graphicsScene1->clearSelection();
}

void MainWindow28::resizeEvent(QResizeEvent *event)
{
    Q_UNUSED(event);
    this->label1->setText(QString("Graphics View 坐标: 左上角总是(0,0), 宽度=%1, 高度=%2")
                          .arg(this->graphicsViewWithMouseEvent->width())
                          .arg(this->graphicsViewWithMouseEvent->height()));

    QRectF rectF = this->graphicsViewWithMouseEvent->sceneRect();
    this->label2->setText(QString("QGraphicsView::sceneRect=(left,top,width,height)=%1,%2,%3,%4")
                          .arg(rectF.left())
                          .arg(rectF.top())
                          .arg(rectF.width())
                          .arg(rectF.height()));
}

QGraphicsViewWithMouseEvent::QGraphicsViewWithMouseEvent(QWidget *parent) : QGraphicsView(parent)
{

}

QGraphicsViewWithMouseEvent::~QGraphicsViewWithMouseEvent()
{

}

void QGraphicsViewWithMouseEvent::mouseMoveEvent(QMouseEvent *event)
{
    QPoint point = event->pos();
    emit this->mouseMovePoint(point);
    QGraphicsView::mouseMoveEvent(event);
}

void QGraphicsViewWithMouseEvent::mousePressEvent(QMouseEvent *event)
{
    if(event->button() == Qt::LeftButton)
    {
        QPoint point = event->pos();
        emit this->mouseClicked(point);
    }
    QGraphicsView::mousePressEvent(event);

}

```