# 计算前处理模块
* 计算前处理的菜单包括：计算参数、特殊构件定义、多塔定义、楼层属性查看修改、风荷载查看修改柱计算长度查看修改、温度荷载设置、活荷载折减、生成结构计算数据、数据检查报告、计算简图。
## 计算参数
### 地下室层数。
* 指与上部结构同时进行内力分析发地下室部分的层数，该数据对结构整体分析与设计有重要影响，如：地下室侧向约束的施加；地下室外墙平面外设计；风荷载计算时，起算位置为地下室顶板；剪力墙底部加强区起算位置为地下室顶板；人防荷载必须加载在地下室楼层；框架结构底层地震组合下设计内力调整；各项楼层指标判断及调整对地下室楼层的过滤等内容。
### 施工模拟加载层步长
* 软件自动生成的各楼层施工次序时属于同一个施工工段的连续楼层数，比如一个4层结构，如果参数填2，表示1，2层属于同一施工工段，3、4层属于同一施工工段。

## 计算控制信息
### 连梁按墙元计算控制跨高比

### 弹性板荷载计算方式
* 控制指定为弹性板属性的楼板，其上的导荷方式有两种：平面导荷和有限元计算