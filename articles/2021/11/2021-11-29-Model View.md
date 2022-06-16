### Model/View 结构

* 数据

* 数据模型
	* QAbstracttemModel
	* QAbstractListModel
		* QStringListModel
	* QAbstractProxy
		* QSortFilterProxyModel
	* QAbstractTableModel
		* QSqlQueryModel
		* QSqlTableModel
		* QSqlRelationalTableModel
	* QStandardItemModel
	* QFileSystemModel

* 视图组件
	* QListView
	* QTreeView
	* QTableView
	* QColumnView
	* QHeaderView

* 代理
	* 模型、视图和代理之间使用信号和糙通信。
	* 当源数据发生变化时，数据模型发射信号通知视图组件。
	* 当用户在界面上操作数据时，视图组件发射信号通知这个操作信息。
	* 当编辑数据时，代理发射信号告知数据模型和视图组件编辑器的状态。
	* QAbstracrItemDelegate
		* QStyledItemDelegate