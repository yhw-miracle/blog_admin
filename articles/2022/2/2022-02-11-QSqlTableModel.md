
```c++
#if _MSC_VER >= 1600
#pragma execution_character_set("utf-8")
#endif

#include "mainwindow32.h"
#include <QDebug>

MainWindow32::MainWindow32(QString title, QWidget *parent) : QMainWindow(parent)
{
    this->setWindowTitle(title);

    this->tableView1 = new QTableView();
    this->tableView1->setSelectionBehavior(QAbstractItemView::SelectRows);
    this->tableView1->setSelectionMode(QAbstractItemView::SingleSelection);
    this->tableView1->setEditTriggers(QAbstractItemView::NoEditTriggers);
    this->tableView1->setContextMenuPolicy(Qt::CustomContextMenu);
    this->tableView1->setAlternatingRowColors(true);
    this->setCentralWidget(this->tableView1);

    this->db = QSqlDatabase::addDatabase("QMYSQL", "MainWindow32");
    this->db.setHostName("127.0.0.1");
    this->db.setPort(3306);
    this->db.setUserName("root");
    this->db.setPassword("root");
    this->db.setDatabaseName("test01");
    if(this->db.open())
    {
        this->openTable();
    }
}

void MainWindow32::openTable()
{
    this->tableModel = new QSqlTableModel(this, this->db);
    this->tableModel->setTable("station_monitor");
    this->tableModel->setSort(this->tableModel->fieldIndex("id"), Qt::AscendingOrder);
    this->tableModel->setEditStrategy(QSqlTableModel::OnManualSubmit);
    this->tableModel->setFilter("is_show = 1 and is_del = 0");
    if(this->tableModel->select())
    {
        this->tableModel->setHeaderData(this->tableModel->fieldIndex("id"), Qt::Horizontal, "id");
        this->tableModel->setHeaderData(this->tableModel->fieldIndex("area_id"), Qt::Horizontal, "area_id");
        this->tableModel->setHeaderData(this->tableModel->fieldIndex("area_name"), Qt::Horizontal, "area_name");
        this->tableModel->setHeaderData(this->tableModel->fieldIndex("station_name"), Qt::Horizontal, "station_name");
        this->tableModel->setHeaderData(this->tableModel->fieldIndex("company_name"), Qt::Horizontal, "company_name");
        this->tableModel->setHeaderData(this->tableModel->fieldIndex("address"), Qt::Horizontal, "address");
        this->tableModel->setHeaderData(this->tableModel->fieldIndex("state_flag"), Qt::Horizontal, "high/low");
        this->tableModel->setHeaderData(this->tableModel->fieldIndex("graphfile_id"), Qt::Horizontal, "graphfile_id");

        this->itemSelectionModel = new QItemSelectionModel(this->tableModel);
        this->tableView1->setModel(this->tableModel);
        this->tableView1->setSelectionModel(this->itemSelectionModel);
        this->tableView1->setColumnHidden(this->tableModel->fieldIndex("id"), true);
        this->tableView1->setColumnHidden(this->tableModel->fieldIndex("region_id"), true);
        this->tableView1->setColumnHidden(this->tableModel->fieldIndex("is_show"), true);
        this->tableView1->setColumnHidden(this->tableModel->fieldIndex("is_del"), true);
        this->tableView1->resizeRowsToContents();
        this->tableView1->resizeColumnsToContents();
        this->connect(this->tableView1, SIGNAL(customContextMenuRequested(const QPoint&)), this, SLOT(tableView1_customContextMenuRequested(const QPoint&)));

        QStringList isHighOrLowStation;
        isHighOrLowStation << "low" << "high";
        int row = this->tableModel->rowCount();
        for(int r=0; r<row; r++)
        {
            QModelIndex currentModelIndex = this->tableModel->index(r, this->tableModel->fieldIndex("state_flag"));
            int currentValue = this->tableModel->data(currentModelIndex).toInt();
            this->tableModel->setData(currentModelIndex, isHighOrLowStation.at(currentValue), Qt::DisplayRole | Qt::EditRole);
        }
        this->tableView1->setModel(this->tableModel);
        this->tableView1->setItemDelegateForColumn(this->tableModel->fieldIndex("state_flag"), &this->isHighOrLowStationDelegate);
        this->isHighOrLowStationDelegate.setItems(isHighOrLowStation, false);
        this->connect(this->itemSelectionModel, SIGNAL(currentChanged(const QModelIndex&, const QModelIndex&)), this, SLOT(itemSelectionModel_currentChanged(const QModelIndex&, const QModelIndex&)));
        this->connect(this->itemSelectionModel, SIGNAL(currentRowChanged(const QModelIndex&, const QModelIndex&)), this, SLOT(itemSelectionModel_currentRowChanged(const QModelIndex&, const QModelIndex&)));

        this->dataMapper = new QDataWidgetMapper();
        this->dataMapper->setModel(this->tableModel);
        this->dataMapper->setSubmitPolicy(QDataWidgetMapper::AutoSubmit);
//        this->dataMapper->addMapping()
    }
}

void MainWindow32::itemSelectionModel_currentChanged(const QModelIndex &current, const QModelIndex &previous)
{
    qDebug() << current.row() << current.column();
}

void MainWindow32::itemSelectionModel_currentRowChanged(const QModelIndex &current, const QModelIndex &previous)
{
    qDebug() << current.row() << current.column();
}

void MainWindow32::tableView1_customContextMenuRequested(const QPoint &pos)
{
    qDebug() << "custom menu";
    Q_UNUSED(pos);
    QMenu *menu = new QMenu(this);
    this->actionAdd = new QAction();
    this->actionAdd->setText("新增");
    this->actionModify = new QAction();
    this->actionModify->setText("修改");
    this->actionDelete = new QAction();
    this->actionDelete->setText("删除");
    menu->addAction(this->actionAdd);
    menu->addAction(this->actionModify);
    menu->addAction(this->actionDelete);
    this->connect(this->actionAdd, SIGNAL(triggered()), this, SLOT(actionAdd_triggered()));
    this->connect(this->actionModify, SIGNAL(triggered()), this, SLOT(actionModify_triggered()));
    this->connect(this->actionDelete, SIGNAL(triggered()), this, SLOT(actionDelete_triggered()));
    menu->exec(QCursor::pos());
    delete menu;
}

void MainWindow32::actionAdd_triggered()
{

}

void MainWindow32::actionModify_triggered()
{

}

void MainWindow32::actionDelete_triggered()
{
    QModelIndex isShowModelIndex= this->tableModel->index(this->itemSelectionModel->currentIndex().row(), this->tableModel->fieldIndex("is_show"));
    QModelIndex isDelModelIndex= this->tableModel->index(this->itemSelectionModel->currentIndex().row(), this->tableModel->fieldIndex("is_del"));
    this->tableModel->setData(isShowModelIndex, 0, Qt::EditRole);
    this->tableModel->setData(isDelModelIndex, 0, Qt::EditRole);
    this->tableModel->submitAll();
}


```