# 冷链物流配送管理平台

面向冷藏车调度、温控记录、生鲜配送、冷库管理、运输签收与温控异常处置的一体化冷链物流管理后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 冷藏车辆 | `vehicle` | 冷藏车 | 车牌号、车辆型号、冷机类型 |
| 驾驶员管理 | `driver` | 驾驶员 | 员工编号、驾驶证号、准驾车型 |
| 配送线路 | `route` | 配送线路 | 线路编号、起点站、终点站 |
| 配送任务单 | `task` | 配送任务单 | 任务单号、发车时间、预计到达 |
| 温控记录 | `tempmonitor` | 温控记录 | 记录编号、车辆编号、设定温度 |
| 冷库管理 | `coldroom` | 冷库 | 冷库编号、冷库类型、额定容积 |
| 货品信息 | `goods` | 货品 | 货品编号、货品名称、存储温区 |
| 装车核对 | `loading` | 装车单 | 装车单号、车辆编号、装车时间 |
| 到站签收 | `delivery` | 签收单 | 签收单号、到达时间、签收人 |
| 温控异常 | `anomaly` | 异常报告 | 异常编号、所属任务、车辆编号 |
| 车辆维保 | `maintenance` | 维保单 | 维保单号、车辆编号、维保类型 |
| 油料管理 | `refuel` | 加油记录 | 加油记录号、车辆编号、加油量 |
| 箱体清洁 | `clean` | 清洁记录 | 清洁编号、车辆编号、清洁方式 |
| 排班管理 | `shift` | 排班记录 | 排班编号、驾驶员、车辆编号 |
| 运输合同 | `transport_contract` | 运输合同 | 合同编号、委托方、承运线路 |
| 保险管理 | `insurance` | 保单 | 保单编号、保险类型、被保车辆 |
| 收货方管理 | `customer` | 收货方 | 客户编号、客户名称、收货地址 |
| 运营日报 | `daily_stats` | 运营日报 | 统计日期、出车趟次、配送总吨位 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
