"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class VehicleEntry(BaseModel):
    """冷藏车明细结构。"""

    field_0: str | None = None  # 车牌号
    field_1: str | None = None  # 车辆型号
    field_2: str | None = None  # 冷机类型
    field_3: str | None = None  # 运载吨位
    field_4: str | None = None  # 所属车队
    field_5: str | None = None  # 年检日期
    field_6: str | None = None  # 车厢容积
    field_7: str | None = None  # 车辆状态

class DriverEntry(BaseModel):
    """驾驶员明细结构。"""

    field_0: str | None = None  # 员工编号
    field_1: str | None = None  # 驾驶证号
    field_2: str | None = None  # 准驾车型
    field_3: str | None = None  # 从业资格证
    field_4: str | None = None  # 联系电话
    field_5: str | None = None  # 当前排班
    field_6: str | None = None  # 驾龄
    field_7: str | None = None  # 驾驶员状态

class RouteEntry(BaseModel):
    """配送线路明细结构。"""

    field_0: str | None = None  # 线路编号
    field_1: str | None = None  # 起点站
    field_2: str | None = None  # 终点站
    field_3: str | None = None  # 途经站点
    field_4: str | None = None  # 预计里程
    field_5: str | None = None  # 标准时长
    field_6: str | None = None  # 温区要求
    field_7: str | None = None  # 线路状态

class TaskEntry(BaseModel):
    """配送任务单明细结构。"""

    field_0: str | None = None  # 任务单号
    field_1: str | None = None  # 发车时间
    field_2: str | None = None  # 预计到达
    field_3: str | None = None  # 配送车辆
    field_4: str | None = None  # 主驾司机
    field_5: str | None = None  # 副驾司机
    field_6: str | None = None  # 品项数量
    field_7: str | None = None  # 任务状态

class TempmonitorEntry(BaseModel):
    """温控记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 车辆编号
    field_2: str | None = None  # 设定温度
    field_3: str | None = None  # 实时温度
    field_4: str | None = None  # 记录时间
    field_5: str | None = None  # 温区类型
    field_6: str | None = None  # 偏差幅度
    field_7: str | None = None  # 记录状态

class ColdroomEntry(BaseModel):
    """冷库明细结构。"""

    field_0: str | None = None  # 冷库编号
    field_1: str | None = None  # 冷库类型
    field_2: str | None = None  # 额定容积
    field_3: str | None = None  # 设定温度
    field_4: str | None = None  # 制冷机组
    field_5: str | None = None  # 除霜周期
    field_6: str | None = None  # 负责人
    field_7: str | None = None  # 冷库状态

class GoodsEntry(BaseModel):
    """货品明细结构。"""

    field_0: str | None = None  # 货品编号
    field_1: str | None = None  # 货品名称
    field_2: str | None = None  # 存储温区
    field_3: str | None = None  # 保质期限
    field_4: str | None = None  # 规格单位
    field_5: str | None = None  # 供货商
    field_6: str | None = None  # 包装方式
    field_7: str | None = None  # 货品状态

class LoadingEntry(BaseModel):
    """装车单明细结构。"""

    field_0: str | None = None  # 装车单号
    field_1: str | None = None  # 车辆编号
    field_2: str | None = None  # 装车时间
    field_3: str | None = None  # 装车人员
    field_4: str | None = None  # 核验人员
    field_5: str | None = None  # 铅封编号
    field_6: str | None = None  # 品项数量
    field_7: str | None = None  # 核对结果

class DeliveryEntry(BaseModel):
    """签收单明细结构。"""

    field_0: str | None = None  # 签收单号
    field_1: str | None = None  # 到达时间
    field_2: str | None = None  # 签收人
    field_3: str | None = None  # 签收人电话
    field_4: str | None = None  # 温控达标
    field_5: str | None = None  # 货品完好
    field_6: str | None = None  # 异常说明
    field_7: str | None = None  # 签收状态

class AnomalyEntry(BaseModel):
    """异常报告明细结构。"""

    field_0: str | None = None  # 异常编号
    field_1: str | None = None  # 所属任务
    field_2: str | None = None  # 车辆编号
    field_3: str | None = None  # 异常时段
    field_4: str | None = None  # 超温最高值
    field_5: str | None = None  # 影响品项
    field_6: str | None = None  # 原因分析
    field_7: str | None = None  # 处置措施

class MaintenanceEntry(BaseModel):
    """维保单明细结构。"""

    field_0: str | None = None  # 维保单号
    field_1: str | None = None  # 车辆编号
    field_2: str | None = None  # 维保类型
    field_3: str | None = None  # 维保厂站
    field_4: str | None = None  # 计划日期
    field_5: str | None = None  # 实际工时
    field_6: str | None = None  # 维保费用
    field_7: str | None = None  # 维保状态

class RefuelEntry(BaseModel):
    """加油记录明细结构。"""

    field_0: str | None = None  # 加油记录号
    field_1: str | None = None  # 车辆编号
    field_2: str | None = None  # 加油量
    field_3: str | None = None  # 油料单价
    field_4: str | None = None  # 加油费用
    field_5: str | None = None  # 加油站
    field_6: str | None = None  # 里程读数
    field_7: str | None = None  # 记录日期

class CleanEntry(BaseModel):
    """清洁记录明细结构。"""

    field_0: str | None = None  # 清洁编号
    field_1: str | None = None  # 车辆编号
    field_2: str | None = None  # 清洁方式
    field_3: str | None = None  # 消毒剂类型
    field_4: str | None = None  # 清洁人员
    field_5: str | None = None  # 清洁日期
    field_6: str | None = None  # 下次清洁日
    field_7: str | None = None  # 清洁状态

class ShiftEntry(BaseModel):
    """排班记录明细结构。"""

    field_0: str | None = None  # 排班编号
    field_1: str | None = None  # 驾驶员
    field_2: str | None = None  # 车辆编号
    field_3: str | None = None  # 排班日期
    field_4: str | None = None  # 班次类型
    field_5: str | None = None  # 计划线路
    field_6: str | None = None  # 调班原因
    field_7: str | None = None  # 排班状态

class TransportContractEntry(BaseModel):
    """运输合同明细结构。"""

    field_0: str | None = None  # 合同编号
    field_1: str | None = None  # 委托方
    field_2: str | None = None  # 承运线路
    field_3: str | None = None  # 合同金额
    field_4: str | None = None  # 起止日期
    field_5: str | None = None  # 结算周期
    field_6: str | None = None  # 服务等级
    field_7: str | None = None  # 合同状态

class InsuranceEntry(BaseModel):
    """保单明细结构。"""

    field_0: str | None = None  # 保单编号
    field_1: str | None = None  # 保险类型
    field_2: str | None = None  # 被保车辆
    field_3: str | None = None  # 保险起止日
    field_4: str | None = None  # 保费金额
    field_5: str | None = None  # 保额上限
    field_6: str | None = None  # 理赔记录
    field_7: str | None = None  # 保单状态

class CustomerEntry(BaseModel):
    """收货方明细结构。"""

    field_0: str | None = None  # 客户编号
    field_1: str | None = None  # 客户名称
    field_2: str | None = None  # 收货地址
    field_3: str | None = None  # 联系人
    field_4: str | None = None  # 联系电话
    field_5: str | None = None  # 常配温区
    field_6: str | None = None  # 结算方式
    field_7: str | None = None  # 客户状态

class DailyStatsEntry(BaseModel):
    """运营日报明细结构。"""

    field_0: str | None = None  # 统计日期
    field_1: str | None = None  # 出车趟次
    field_2: str | None = None  # 配送总吨位
    field_3: str | None = None  # 温控达标率
    field_4: str | None = None  # 异常趟次
    field_5: str | None = None  # 在途车辆
    field_6: str | None = None  # 签收完成率
    field_7: str | None = None  # 填表人
