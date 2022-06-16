* QSlider/QScrollBar/Qdial 的基类是 QAbstractSlider

### QAbstractSlider 的属性
* minimum
* maximum
* singleStep
* pageStep
* value
* sliderPosition
* racking
* orientation
	* Qt::Horizontal
	* Qt::Vertical
* invertedApperance
* invertedControls

### QSlider 的属性
* tickPosition
	* QSlider::NoTicks
	* QSlider::TicksBothSides
	* QSlider::TicksAbove
	* QSlider::TickBelow
	* QSlider::TickLeft
	* QSlider::TIckRight
* tickInterval

### Qdial 的属性
* notchesVisible
* notchTarget

### QProcessBar 的属性
* minimum
* maximum
* value
* textVisible
* orientation
* format
	* "%p%" ===> 百分比
	* "%v" ===> 当前值
	* "%m" ===> 总步数

### QLCDNumber 的属性
* digitCount
* smallDecimalPoint
* mode
	* setBinMode
	* setOctMode
	* setDecMode
	* setHexMode
* value
* intValue