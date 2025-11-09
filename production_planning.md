✅ CHECKLIST - ĐỂ CHẠY PRODUCTION PLANNINGTÓM TẮT NHANH:CẦN CÓ:
├─ 1. Master Data ✅
├─ 2. Input Parameters ✅
├─ 3. Calculation Logic ✅
└─ 4. Output DocType ✅

KHÔNG CẦN:
├─ ❌ BOM (dành cho MRP)
├─ ❌ Routing (dành cho Scheduling)
└─ ❌ Work Center (dành cho Scheduling)📊 1. MASTER DATA (Đã có/Cần có)✅ CÓ RỒI (Already have):1. APS Item ✅
   └─ 8 items (5 finished goods + 3 raw materials)
   
2. APS Warehouse ✅
   └─ 6 warehouses
   
3. APS Bin ✅
   └─ 17 stock records (inventory levels)
   
4. APS Forecast Result ✅
   └─ Đã có forecast (nếu dùng forecast source)
   
5. APS Sales Order History ✅
   └─ 48 records (23 months data)
   
6. APS Supplier ✅
   └─ 8 suppliers
   
7. APS Supplier Item ✅
   └─ 8 supplier-item links🆕 CẦN TẠO (Need to create):8. APS Production Plan (DocType mới)
   Purpose: Lưu output của Production Planning
   
   Structure:
   ├─ Header:
   │   ├─ plan_name
   │   ├─ planning_date
   │   ├─ planning_period_from
   │   ├─ planning_period_to
   │   ├─ demand_source
   │   ├─ forecast_result (nếu dùng forecast)
   │   ├─ warehouse
   │   ├─ status
   │   └─ total_planned_qty
   │
   └─ Child Table (APS Production Plan Item):
       ├─ item
       ├─ item_name
       ├─ forecasted_demand
       ├─ safety_stock
       ├─ current_stock
       ├─ work_in_process
       ├─ ordered_qty
       ├─ projected_stock
       ├─ net_requirement
       ├─ planned_production_qty
       ├─ production_priority
       ├─ start_date
       └─ due_date📝 2. INPUT PARAMETERS (Khi chạy)User cần nhập:┌─────────────────────────────────────────┐
│  RUN PRODUCTION PLANNING                │
├─────────────────────────────────────────┤
│                                         │
│  1. BASIC INFO                          │
│  ├─ Plan Name: [Text] *                │
│  │   Example: "December 2025 Plan"     │
│  └─ Planning Date: [Date] (auto today) │
│                                         │
│  2. PLANNING SCOPE                      │
│  ├─ Planning Period: *                 │
│  │   ├─ From: [2025-12-01]            │
│  │   └─ To: [2025-12-31]              │
│  │                                     │
│  ├─ Items: *                           │
│  │   ○ All Items (default)            │
│  │   ● Specific: [Multi-select]       │
│  │                                     │
│  └─ Warehouse:                         │
│      ○ All Warehouses (default)       │
│      ● Specific: [Select]             │
│                                         │
│  3. DEMAND SOURCE *                    │
│  ├─ ○ Forecast                         │
│  │   └─ Forecast Result: [Link]       │
│  │                                     │
│  ├─ ○ Sales Order (Historical)        │
│  │   ├─ From: [2024-01-01]           │
│  │   ├─ To: [2025-10-31]             │
│  │   └─ Method: Average               │
│  │                                     │
│  └─ ○ Hybrid                           │
│      ├─ Forecast: [Link]              │
│      ├─ Orders weight: [70]%          │
│      └─ Forecast weight: [30]%        │
│                                         │
│  4. PLANNING PARAMETERS                │
│  ├─ Safety Stock Days: [7]            │
│  ├─ Consider Current Stock: ☑         │
│  ├─ Consider In-transit: ☑            │
│  └─ Consider WIP: ☐                   │
│                                         │
│  [Cancel]  [Validate]  [Run Plan ▶]   │
│                                         │
└─────────────────────────────────────────┘Required vs Optional:REQUIRED (Bắt buộc):
├─ Planning Period (From/To dates) ✅
├─ Demand Source ✅
└─ Demand Source details:
    ├─ IF Forecast → Forecast Result ID
    ├─ IF Historical → Date range
    └─ IF Hybrid → Both + weights

OPTIONAL (Tùy chọn):
├─ Items (default: All)
├─ Warehouse (default: All)
├─ Safety Stock Days (default: 7)
└─ Stock considerations (default: Yes)