
```c++
#if _MSC_VER >= 1600
#pragma execution_character_set("utf-8")
#endif

#include "mainwindow29.h"

#include <QDebug>

MainWindow29::MainWindow29(QString title, QWidget *parent) : QMainWindow(parent)
{
    this->setWindowTitle(title);

    this->toolBar1 = new QToolBar();
    this->action1 = new QAction();
    this->action1->setText("放大");
    this->action2 = new QAction();
    this->action2->setText("缩小");
    this->action3 = new QAction();
    this->action3->setText("恢复");
    this->action4 = new QAction();
    this->action4->setText("左旋转");
    this->action5 = new QAction();
    this->action5->setText("右旋转");
    this->action6 = new QAction();
    this->action6->setText("前置");
    this->action7 = new QAction();
    this->action7->setText("后置");
    this->action8 = new QAction();
    this->action8->setText("组合");
    this->action9 = new QAction();
    this->action9->setText("打散");
    this->action10 = new QAction();
    this->action10->setText("删除");
    this->action11 = new QAction();
    this->action11->setText("退出");
    this->toolBar1->addAction(this->action1);
    this->toolBar1->addAction(this->action2);
    this->toolBar1->addAction(this->action3);
    this->toolBar1->addAction(this->action4);
    this->toolBar1->addAction(this->action5);
    this->toolBar1->addAction(this->action6);
    this->toolBar1->addAction(this->action7);
    this->toolBar1->addAction(this->action8);
    this->toolBar1->addAction(this->action9);
    this->toolBar1->addAction(this->action10);
    this->toolBar1->addAction(this->action11);

    this->toolBar2 = new QToolBar();
    this->action12 = new QAction();
    this->action12->setText("矩形");
    this->action13 = new QAction();
    this->action13->setText("椭圆形");
    this->action14 = new QAction();
    this->action14->setText("圆形");
    this->action15 = new QAction();
    this->action15->setText("三角形");
    this->action16 = new QAction();
    this->action16->setText("梯形");
    this->action17 = new QAction();
    this->action17->setText("直线");
    this->action18 = new QAction();
    this->action18->setText("文字");
    this->toolBar2->addAction(this->action12);
    this->toolBar2->addAction(this->action13);
    this->toolBar2->addAction(this->action14);
    this->toolBar2->addAction(this->action15);
    this->toolBar2->addAction(this->action16);
    this->toolBar2->addAction(this->action17);
    this->toolBar2->addAction(this->action18);

    this->addToolBar(Qt::TopToolBarArea, this->toolBar1);
    this->addToolBar(Qt::LeftToolBarArea, this->toolBar2);

    this->connect(this->action1, SIGNAL(triggered()), this, SLOT(action1_triggered()));
    this->connect(this->action2, SIGNAL(triggered()), this, SLOT(action2_triggered()));
    this->connect(this->action3, SIGNAL(triggered()), this, SLOT(action3_triggered()));
    this->connect(this->action4, SIGNAL(triggered()), this, SLOT(action4_triggered()));
    this->connect(this->action5, SIGNAL(triggered()), this, SLOT(action5_triggered()));
    this->connect(this->action6, SIGNAL(triggered()), this, SLOT(action6_triggered()));
    this->connect(this->action7, SIGNAL(triggered()), this, SLOT(action7_triggered()));
    this->connect(this->action8, SIGNAL(triggered()), this, SLOT(action8_triggered()));
    this->connect(this->action9, SIGNAL(triggered()), this, SLOT(action9_triggered()));
    this->connect(this->action10, SIGNAL(triggered()), this, SLOT(action10_triggered()));
    this->connect(this->action11, SIGNAL(triggered()), this, SLOT(action11_triggered()));
    this->connect(this->action12, SIGNAL(triggered()), this, SLOT(action12_triggered()));
    this->connect(this->action13, SIGNAL(triggered()), this, SLOT(action13_triggered()));
    this->connect(this->action14, SIGNAL(triggered()), this, SLOT(action14_triggered()));
    this->connect(this->action15, SIGNAL(triggered()), this, SLOT(action15_triggered()));
    this->connect(this->action16, SIGNAL(triggered()), this, SLOT(action16_triggered()));
    this->connect(this->action17, SIGNAL(triggered()), this, SLOT(action17_triggered()));
    this->connect(this->action18, SIGNAL(triggered()), this, SLOT(action18_triggered()));

    this->label1 = new QLabel();
    this->label2 = new QLabel();
    this->label3 = new QLabel();
    this->label4 = new QLabel();
    this->statusBar = new QStatusBar();
    this->statusBar->addWidget(this->label1);
    this->statusBar->addWidget(this->label2);
    this->statusBar->addWidget(this->label3);
    this->statusBar->addWidget(this->label4);
    this->setStatusBar(this->statusBar);

    this->mainWindow29GraphicsView1 = new MainWindow29GraphicsView();
    this->graphicsScene1 = new QGraphicsScene(-300, -200, 600, 200);
    this->mainWindow29GraphicsView1->setScene(this->graphicsScene1);
    this->mainWindow29GraphicsView1->setCursor(Qt::CrossCursor);
    this->mainWindow29GraphicsView1->setMouseTracking(true);
    this->mainWindow29GraphicsView1->setDragMode(QGraphicsView::RubberBandDrag);
    this->setCentralWidget(this->mainWindow29GraphicsView1);

    this->connect(this->mainWindow29GraphicsView1, SIGNAL(mouseMovePoint(QPoint)), this, SLOT(mouseMovePoint(QPoint)));
    this->connect(this->mainWindow29GraphicsView1, SIGNAL(mouseClicked(QPoint)), this, SLOT(mouseClicked(QPoint)));
    this->connect(this->mainWindow29GraphicsView1, SIGNAL(mouseDoubleClicked(QPoint)), this, SLOT(mouseDoubleClicked(QPoint)));
    this->connect(this->mainWindow29GraphicsView1, SIGNAL(keyPress(QKeyEvent*)), this, SLOT(keyPress(QKeyEvent*)));

    qsrand(QTime::currentTime().second());
}

void MainWindow29::mouseMovePoint(QPoint point)
{
    this->label1->setText(QString("View 坐标:%1,%2")
                          .arg(point.x())
                          .arg(point.y()));

    QPointF scenePoint = this->mainWindow29GraphicsView1->mapToScene(point);
    this->label2->setText(QString("Scene 坐标:%1,%2")
                          .arg(scenePoint.x())
                          .arg(scenePoint.y()));
}

void MainWindow29::mouseClicked(QPoint point)
{
    QPointF scenePoint = this->mainWindow29GraphicsView1->mapToScene(point);
    QGraphicsItem *item = this->graphicsScene1->itemAt(scenePoint, this->mainWindow29GraphicsView1->transform());
    if(item != NULL)
    {
        QPointF itemPoint = item->mapFromScene(scenePoint);
        this->label3->setText(QString("Item 坐标:%1,%2")
                              .arg(itemPoint.x())
                              .arg(itemPoint.y()));
        this->label4->setText(QString("%1,%2")
                              .arg(item->data(this->itemId).toString())
                              .arg(item->data(this->itemDesciption).toString()));
    }
}

template<class T> void setBrushColor(T *item)
{
    QColor color = item->brush().color();
    color = QColorDialog::getColor(color, nullptr, "选择填充颜色");
    if(color.isValid())
    {
        item->setBrush(QBrush(color));
    }
}

void MainWindow29::mouseDoubleClicked(QPoint point)
{
    QPointF scenePoint = this->mainWindow29GraphicsView1->mapToScene(point);
    QGraphicsItem *item = this->graphicsScene1->itemAt(scenePoint, this->mainWindow29GraphicsView1->transform());
    if(item != NULL)
    {
        if(item->type() == QGraphicsRectItem::Type)
        {
            QGraphicsRectItem *item1 = qgraphicsitem_cast<QGraphicsRectItem*>(item);
            setBrushColor(item1);
        }
        else if(item->type() == QGraphicsEllipseItem::Type)
        {
            QGraphicsEllipseItem *item1 = qgraphicsitem_cast<QGraphicsEllipseItem*>(item);
            setBrushColor(item1);
        }
        else if(item->type() == QGraphicsPolygonItem::Type)
        {
            QGraphicsPolygonItem *item1 = qgraphicsitem_cast<QGraphicsPolygonItem*>(item);
            setBrushColor(item1);
        }
        else if(item->type() == QGraphicsLineItem::Type)
        {
            QGraphicsLineItem *item1 = qgraphicsitem_cast<QGraphicsLineItem*>(item);
            QPen pen = item1->pen();
            QColor color = pen.color();
            color = QColorDialog::getColor(color, this, "选择线条颜色");
            if(color.isValid())
            {
                pen.setColor(color);
                item1->setPen(pen);
            }
        }
        else if(item->type() == QGraphicsTextItem::Type)
        {
            QGraphicsTextItem *item1 = qgraphicsitem_cast<QGraphicsTextItem*>(item);
            QFont font = item1->font();
            bool ok = false;
            font = QFontDialog::getFont(&ok, font, this, "设置字体");
            if(ok)
            {
                item1->setFont(font);
            }
        }
    }
}

void MainWindow29::keyPress(QKeyEvent *event)
{
    if(this->graphicsScene1->selectedItems().count() == 1)
    {
        QGraphicsItem *item = this->graphicsScene1->selectedItems().at(0);
        if(event->key() == Qt::Key_Delete)
        {
            this->graphicsScene1->removeItem(item);
        }
        else if(event->key() == Qt::Key_Space)
        {
            item->setRotation(90 + item->rotation());
        }
        else if(event->key() == Qt::Key_PageUp)
        {
            item->setScale(0.1 + item->scale());
        }
        else if(event->key() == Qt::Key_PageDown)
        {
            item->setScale(-0.1 + item->scale());
        }
        else if(event->key() == Qt::Key_Left)
        {
            item->setX(-1 + item->x());
        }
        else if(event->key() == Qt::Key_Right)
        {
            item->setX(1 + item->x());
        }
        else if(event->key() == Qt::Key_Up)
        {
            item->setY(-1 + item->y());
        }
        else if(event->key() == Qt::Key_Down)
        {
            item->setY(1 + item->y());
        }
    }
}

void MainWindow29::action1_triggered()
{
    // 放大
    int count = this->graphicsScene1->selectedItems().count();
    if(count == 1)
    {
        QGraphicsItem *item = this->graphicsScene1->selectedItems().at(0);
        item->setScale(0.1 + item->scale());
    }
    else
    {
        this->mainWindow29GraphicsView1->scale(1.1, 1.1);
    }
}

void MainWindow29::action2_triggered()
{
    // 缩小
    int count = this->graphicsScene1->selectedItems().count();
    if(count == 1)
    {
        QGraphicsItem *item = this->graphicsScene1->selectedItems().at(0);
        item->setScale(item->scale() - 0.1);
    }
    else
    {
        this->mainWindow29GraphicsView1->scale(0.9, 0.9);
    }
}

void MainWindow29::action3_triggered()
{
    // 恢复
    int count = this->graphicsScene1->selectedItems().count();
    if(count == 1)
    {
        QGraphicsItem *item = this->graphicsScene1->selectedItems().at(0);
        item->resetTransform();
    }
    else
    {
        this->mainWindow29GraphicsView1->resetTransform();
    }
}

void MainWindow29::action4_triggered()
{
    // 左旋转
    int count = this->graphicsScene1->selectedItems().count();
    if(count == 1)
    {
        QGraphicsItem *item = this->graphicsScene1->selectedItems().at(0);
        item->setRotation(-30 + item->rotation());
    }
    else
    {
        this->mainWindow29GraphicsView1->rotate(-30);
    }
}

void MainWindow29::action5_triggered()
{
    // 右旋转
    int count = this->graphicsScene1->selectedItems().count();
    if(count == 1)
    {
        QGraphicsItem *item = this->graphicsScene1->selectedItems().at(0);
        item->setRotation(30 + item->rotation());
    }
    else
    {
        this->mainWindow29GraphicsView1->rotate(30);
    }
}

void MainWindow29::action6_triggered()
{
    // 前置
    int count = this->graphicsScene1->selectedItems().count();
    if(count > 1)
    {
        QGraphicsItem *item = this->graphicsScene1->selectedItems().at(0);
        item->setZValue(--this->backZ);
    }
}

void MainWindow29::action7_triggered()
{
    // 后置
    int count = this->graphicsScene1->selectedItems().count();
    if(count > 1)
    {
        QGraphicsItem *item = this->graphicsScene1->selectedItems().at(0);
        item->setZValue(++this->frontZ);
    }
}

void MainWindow29::action8_triggered()
{
    // 组合
    QGraphicsItemGroup *group = new QGraphicsItemGroup();
    this->graphicsScene1->addItem(group);
    int count = this->graphicsScene1->selectedItems().count();
    if(count > 0)
    {
        for(int i=0; i<count; i++)
        {
            QGraphicsItem *item = this->graphicsScene1->selectedItems().at(0);
            item->setSelected(false);
            item->clearFocus();
            group->addToGroup(item);
        }
        group->setFlags(QGraphicsItem::ItemIsMovable | QGraphicsItem::ItemIsSelectable | QGraphicsItem::ItemIsFocusable);
        group->setZValue(++this->frontZ);
        this->graphicsScene1->clearSelection();
        group->setSelected(true);
    }
}

void MainWindow29::action9_triggered()
{
    // 打散
    int count = this->graphicsScene1->selectedItems().count();
    if(count == 1)
    {
        QGraphicsItemGroup *group = (QGraphicsItemGroup*)this->graphicsScene1->selectedItems().at(0);
        this->graphicsScene1->destroyItemGroup(group);
    }
}

void MainWindow29::action10_triggered()
{
    // 删除
    int count = this->graphicsScene1->selectedItems().count();
    for(int i=0; i<count; i++)
    {
        QGraphicsItem *item = this->graphicsScene1->selectedItems().at(i);
        this->graphicsScene1->removeItem(item);

    }
}

void MainWindow29::action11_triggered()
{
    // 退出
    this->close();
}

void MainWindow29::action12_triggered()
{
    // 矩形
}

void MainWindow29::action13_triggered()
{
    // 椭圆
    QGraphicsEllipseItem *item = new QGraphicsEllipseItem(-50, -30, 100, 60);
    item->setFlags(QGraphicsItem::ItemIsMovable | QGraphicsItem::ItemIsSelectable | QGraphicsItem::ItemIsFocusable);
    item->setBrush(QBrush(Qt::green));
    item->setZValue(++this->frontZ);
    item->setPos(-50 + (qrand() % 100), -50 + (qrand() % 100));
    item->setData(this->itemId, ++this->itemNum);
    item->setData(this->itemDesciption, "椭圆");

    this->graphicsScene1->addItem(item);
    this->graphicsScene1->clearSelection();
    item->setSelected(true);
}

void MainWindow29::action14_triggered()
{
    // 圆形
    QGraphicsEllipseItem *item = new QGraphicsEllipseItem(-20, -20, 50, 50);
    item->setFlags(QGraphicsItem::ItemIsMovable | QGraphicsItem::ItemIsSelectable | QGraphicsItem::ItemIsFocusable);
    item->setBrush(QBrush(Qt::yellow));
    item->setZValue(++this->frontZ);
    item->setPos(-50 + (qrand() % 100), -50 + (qrand() % 100));
    item->setData(this->itemId, ++this->itemNum);
    item->setData(this->itemDesciption, "圆");

    this->graphicsScene1->addItem(item);
    this->graphicsScene1->clearSelection();
    item->setSelected(true);
}

void MainWindow29::action15_triggered()
{
    // 三角形
}
void MainWindow29::action16_triggered()
{
    // 梯形
}
void MainWindow29::action17_triggered()
{
    // 直线
}
void MainWindow29::action18_triggered()
{
    // 文字
}

MainWindow29GraphicsView::MainWindow29GraphicsView(QWidget *parent) : QGraphicsView(parent)
{

}

MainWindow29GraphicsView::~MainWindow29GraphicsView()
{

}

void MainWindow29GraphicsView::mouseMoveEvent(QMouseEvent *event)
{
    QPoint point = event->pos();
    emit this->mouseMovePoint(point);
    QGraphicsView::mouseMoveEvent(event);
}

void MainWindow29GraphicsView::mousePressEvent(QMouseEvent *event)
{
    if(event->button() == Qt::LeftButton)
    {
        QPoint point = event->pos();
        emit this->mouseClicked(point);
    }
    QGraphicsView::mousePressEvent(event);
}

void MainWindow29GraphicsView::mouseDoubleClickEvent(QMouseEvent *event)
{
    if(event->button() == Qt::LeftButton)
    {
        QPoint point = event->pos();
        emit this->mouseDoubleClicked(point);
    }
    QGraphicsView::mouseDoubleClickEvent(event);
}

void MainWindow29GraphicsView::keyPressEvent(QKeyEvent *event)
{
    emit this->keyPress(event);
    QGraphicsView::keyPressEvent(event);
}

```