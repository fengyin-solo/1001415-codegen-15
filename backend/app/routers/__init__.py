"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import vehicle as router_vehicle
from app.routers import driver as router_driver
from app.routers import route as router_route
from app.routers import task as router_task
from app.routers import tempmonitor as router_tempmonitor
from app.routers import coldroom as router_coldroom
from app.routers import goods as router_goods
from app.routers import loading as router_loading
from app.routers import delivery as router_delivery
from app.routers import anomaly as router_anomaly
from app.routers import maintenance as router_maintenance
from app.routers import refuel as router_refuel
from app.routers import clean as router_clean
from app.routers import shift as router_shift
from app.routers import transport_contract as router_transport_contract
from app.routers import insurance as router_insurance
from app.routers import customer as router_customer
from app.routers import daily_stats as router_daily_stats

ROUTERS = [router_vehicle, router_driver, router_route, router_task, router_tempmonitor, router_coldroom, router_goods, router_loading, router_delivery, router_anomaly, router_maintenance, router_refuel, router_clean, router_shift, router_transport_contract, router_insurance, router_customer, router_daily_stats]
