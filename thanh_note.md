    🔄 FULL WORKFLOW - APS SYSTEM
    Overview - 5 Modules:
    ┌─────────────────────────────────────────────────────────┐
    │                  APS WORKFLOW                           │
    ├─────────────────────────────────────────────────────────┤
    │                                                         │
    │  1. DEMAND FORECAST    → Dự báo nhu cầu               │
    │           ↓                                             │
    │  2. PRODUCTION PLANNING → Kế hoạch sản xuất            │
    │           ↓                                             │
    │  3. MRP                → Tính nguyên vật liệu           │
    │           ↓                                             │
    │  4. SUPPLY PLANNING    → Kế hoạch mua hàng             │
    │           ↓                                             │
    │  5. SCHEDULE OPTIMIZATION → Tối ưu lịch sản xuất       │
    │                                                         │
    └─────────────────────────────────────────────────────────┘

    📊 MODULE 1: DEMAND FORECASTING
    🎯 TÍNH NĂNG:
    Purpose:
    "DỰ BÁO NHU CẦU TƯƠNG LAI"

    Làm gì:
    ├─ Phân tích lịch sử bán hàng
    ├─ Phát hiện xu hướng (trend)
    ├─ Phát hiện mùa vụ (seasonality)
    ├─ Dự báo 12 tháng tiếp theo
    └─ Tính độ chính xác (accuracy)

    Input:
    ├─ Sales Order History (48 tháng)
    │   ├─ Transaction date
    │   ├─ Item code
    │   └─ Quantity sold
    └─ Items cần forecast

    Output:
    └─ APS Forecast Result
        ├─ 12 months forecast
        ├─ Upper bound (optimistic)
        ├─ Lower bound (pessimistic)
        └─ Accuracy metrics (MAPE, RMSE)

    🔄 WORKFLOW:
    Step 1: User inputs
    ┌─────────────────────────────────────┐
    │  CREATE FORECAST                    │
    ├─────────────────────────────────────┤
    │  Items: [CHAI-500ML, CHAI-1L, ...]│
    │  Historical period: 48 months       │
    │  Forecast horizon: 12 months        │
    │  Model: ARIMA/SARIMA               │
    └─────────────────────────────────────┘
            ↓
    Step 2: System processes
    ┌─────────────────────────────────────┐
    │  PROCESSING                         │
    ├─────────────────────────────────────┤
    │  ✓ Lấy data từ Sales Order History │
    │  ✓ Clean data (outliers, nulls)   │
    │  ✓ Train ARIMA model               │
    │  ✓ Generate forecast               │
    │  ✓ Calculate accuracy              │
    └─────────────────────────────────────┘
            ↓
    Step 3: Output
    ┌─────────────────────────────────────┐
    │  FORECAST RESULT                    │
    ├─────────────────────────────────────┤
    │  CHAI-500ML:                        │
    │  ├─ Dec 2025: 10,000 ± 500         │
    │  ├─ Jan 2026: 10,200 ± 520         │
    │  ├─ Feb 2026: 9,800 ± 480          │
    │  └─ ... (12 months)                │
    │                                     │
    │  Accuracy: 91.5% MAPE              │
    │  Status: Completed                 │
    └─────────────────────────────────────┘

    📋 EXAMPLE:
    User: "Forecast demand cho 5 sản phẩm"

    Input:
    ├─ Items: CHAI-500ML, CHAI-1L, TUI-20X30, TUI-30X40, HOP-NHUA-1KG
    ├─ Historical: 2022-01 to 2025-10 (48 months)
    └─ Forecast: 2025-11 to 2026-10 (12 months)

    Processing:
    [System trains ARIMA model for each item...]

    Output: FORECAST-2025-00123
    ┌──────────────┬────────┬────────┬────────┬─────────┐
    │    Item      │  Nov   │  Dec   │  Jan   │   ...   │
    ├──────────────┼────────┼────────┼────────┼─────────┤
    │ CHAI-500ML   │ 9,800  │10,000  │10,200  │   ...   │
    │ CHAI-1L      │ 5,900  │ 6,000  │ 6,100  │   ...   │
    │ TUI-20X30    │24,500  │25,000  │25,200  │   ...   │
    │ TUI-30X40    │14,800  │15,000  │15,100  │   ...   │
    │ HOP-NHUA-1KG │ 4,900  │ 5,000  │ 5,100  │   ...   │
    └──────────────┴────────┴────────┴────────┴─────────┘

    → Save to database ✅
    → Dùng cho Production Planning

    📊 MODULE 2: PRODUCTION PLANNING
    🎯 TÍNH NĂNG:
    Purpose:
    "QUYẾT ĐỊNH SẢN XUẤT BAO NHIÊU"

    Làm gì:
    ├─ Nhận demand (từ forecast hoặc sales orders)
    ├─ Kiểm tra tồn kho hiện tại
    ├─ Tính nhu cầu ròng
    ├─ Xét safety stock
    ├─ Apply lot sizing algorithm
    └─ Tạo production plan

    Input:
    ├─ Demand source:
    │   ├─ Forecast Result (từ Module 1)
    │   ├─ Sales Order History (average)
    │   └─ Hybrid (orders + forecast)
    ├─ Current stock (từ APS Bin)
    ├─ Planning parameters:
    │   ├─ Planning period
    │   ├─ Safety stock days
    │   └─ Lot sizing method

    Output:
    └─ APS Production Plan
        ├─ Recommended production quantity
        ├─ Production priority
        ├─ Material requirements (preview)
        └─ Capacity check

    🔄 WORKFLOW:
    Step 1: User inputs
    ┌─────────────────────────────────────┐
    │  CREATE PRODUCTION PLAN             │
    ├─────────────────────────────────────┤
    │  Demand Source: Forecast ✓          │
    │  Forecast: FORECAST-2025-00123      │
    │  Items: All items                   │
    │  Planning Period: Dec 2025          │
    │  Warehouse: All                     │
    │  Safety Stock: 7 days               │
    └─────────────────────────────────────┘
            ↓
    Step 2: System calculates
    ┌─────────────────────────────────────┐
    │  CALCULATION                        │
    ├─────────────────────────────────────┤
    │  FOR EACH ITEM:                     │
    │                                     │
    │  1. Get demand from forecast        │
    │     CHAI-500ML: 10,000             │
    │                                     │
    │  2. Calculate safety stock          │
    │     Daily demand: 10,000/30 = 333   │
    │     Safety: 333 × 7 = 2,333        │
    │                                     │
    │  3. Get current stock from bins     │
    │     WO-00001: 4,500                │
    │     WO-00005: 15,000               │
    │     WO-00006: 8,000                │
    │     Total: 27,500                  │
    │                                     │
    │  4. Calculate net requirement       │
    │     Need: 10,000 + 2,333 = 12,333  │
    │     Have: 27,500                   │
    │     Net: 12,333 - 27,500 = -15,167 │
    │                                     │
    │  5. Production decision             │
    │     → NO NEED to produce           │
    │     (Stock is sufficient)          │
    └─────────────────────────────────────┘
            ↓
    Step 3: Output
    ┌─────────────────────────────────────┐
    │  PRODUCTION PLAN                    │
    ├─────────────────────────────────────┤
    │  CHAI-500ML:                        │
    │  ├─ Demand: 10,000                 │
    │  ├─ Safety Stock: 2,333            │
    │  ├─ Current Stock: 27,500          │
    │  ├─ Net Requirement: -15,167       │
    │  └─ Production: 0 ✓ (Surplus)      │
    │                                     │
    │  CHAI-1L:                           │
    │  ├─ Demand: 6,000                  │
    │  ├─ Safety Stock: 1,400            │
    │  ├─ Current Stock: 3,000           │
    │  ├─ Net Requirement: 4,400         │
    │  └─ Production: 5,000 ✓ (Rounded)  │
    │                                     │
    │  Status: Ready for approval        │
    └─────────────────────────────────────┘

    📋 EXAMPLE:
    Scenario: Manager muốn plan tháng 12

    Input:
    ├─ Forecast: FORECAST-2025-00123 (from Module 1)
    ├─ Items: 5 items (all)
    ├─ Period: 2025-12-01 to 2025-12-31
    └─ Warehouse: All

    Processing:
    [Tính toán cho từng item...]

    Output: PROD-PLAN-2025-00001
    ┌──────────────┬─────────┬─────────┬──────────┬──────────┐
    │    Item      │ Demand  │  Stock  │   Net    │ Produce  │
    ├──────────────┼─────────┼─────────┼──────────┼──────────┤
    │ CHAI-500ML   │ 12,333  │ 27,500  │ -15,167  │    0     │
    │ CHAI-1L      │  7,400  │ 13,000  │  -5,600  │    0     │
    │ TUI-20X30    │ 27,000  │ 57,000  │ -30,000  │    0     │
    │ TUI-30X40    │ 16,500  │ 26,000  │  -9,500  │    0     │
    │ HOP-NHUA-1KG │  6,200  │  7,500  │  -1,300  │    0     │
    └──────────────┴─────────┴─────────┴──────────┴──────────┘

    Conclusion: Không cần sản xuất tháng 12!
    Lý do: Tồn kho đủ cho cả tháng ✅

    → Manager review và approve
    → Input cho MRP (Module 3)

    📊 MODULE 3: MRP (MATERIAL REQUIREMENTS PLANNING)
    🎯 TÍNH NĂNG:
    Purpose:
    "TÍNH NGUYÊN VẬT LIỆU CẦN THIẾT"

    Làm gì:
    ├─ Nhận production plan (từ Module 2)
    ├─ Đọc BOM (Bill of Materials)
    ├─ Phân rá thành phẩm → nguyên liệu
    ├─ Kiểm tra tồn kho NVL
    ├─ Tính net requirements cho NVL
    └─ Offset theo lead time

    Input:
    ├─ Production Plan (từ Module 2)
    │   └─ Produce: 8,000 CHAI-500ML
    ├─ BOM structure
    │   └─ 1 CHAI-500ML needs:
    │       ├─ 0.5 kg PVC-R01
    │       ├─ 1 pc CAP-500ML
    │       └─ 1 pc LABEL-500ML
    └─ Current NVL stock

    Output:
    └─ APS MRP Result
        ├─ Material requirements by item
        ├─ Time-phased requirements
        ├─ Net requirements (gross - stock)
        └─ Planned orders (offset by lead time)

    🔄 WORKFLOW:
    Step 1: Input
    ┌─────────────────────────────────────┐
    │  MRP INPUT                          │
    ├─────────────────────────────────────┤
    │  Production Plan:                   │
    │  └─ PROD-PLAN-2025-00001           │
    │                                     │
    │  Items to produce:                  │
    │  └─ CHAI-500ML: 8,000              │
    │      (Due: Dec 31, 2025)           │
    └─────────────────────────────────────┘
            ↓
    Step 2: BOM Explosion
    ┌─────────────────────────────────────┐
    │  BOM EXPLOSION                      │
    ├─────────────────────────────────────┤
    │  CHAI-500ML (8,000 units)          │
    │  ↓                                  │
    │  Components needed:                 │
    │  ├─ PVC-R01: 8,000 × 0.5 = 4,000 kg│
    │  ├─ CAP-500: 8,000 × 1 = 8,000 pcs │
    │  └─ LABEL-500: 8,000 × 1 = 8,000   │
    └─────────────────────────────────────┘
            ↓
    Step 3: Check stock
    ┌─────────────────────────────────────┐
    │  STOCK CHECK                        │
    ├─────────────────────────────────────┤
    │  PVC-R01:                           │
    │  ├─ Gross requirement: 4,000 kg     │
    │  ├─ Current stock: 5,000 kg        │
    │  ├─ Allocated: 1,000 kg            │
    │  ├─ Available: 4,000 kg            │
    │  └─ Net requirement: 0 ✓           │
    │                                     │
    │  CAP-500:                           │
    │  ├─ Gross requirement: 8,000       │
    │  ├─ Current stock: 3,000           │
    │  ├─ Allocated: 500                 │
    │  ├─ Available: 2,500               │
    │  └─ Net requirement: 5,500 ⚠️       │
    └─────────────────────────────────────┘
            ↓
    Step 4: Time phasing
    ┌─────────────────────────────────────┐
    │  TIME-PHASED REQUIREMENTS           │
    ├─────────────────────────────────────┤
    │  CAP-500 (lead time: 10 days)      │
    │                                     │
    │  Need by: Dec 31                    │
    │  Order by: Dec 21 (31 - 10)        │
    │                                     │
    │  Planned Order:                     │
    │  ├─ Item: CAP-500                  │
    │  ├─ Quantity: 5,500                │
    │  ├─ Order date: Dec 21             │
    │  └─ Due date: Dec 31               │
    └─────────────────────────────────────┘
            ↓
    Step 5: Output
    ┌─────────────────────────────────────┐
    │  MRP RESULT                         │
    ├─────────────────────────────────────┤
    │  Material Requirements:             │
    │                                     │
    │  PVC-R01:                           │
    │  └─ No order needed (sufficient)   │
    │                                     │
    │  CAP-500:                           │
    │  ├─ Order quantity: 5,500          │
    │  ├─ Order by: Dec 21               │
    │  └─ Receive by: Dec 31             │
    │                                     │
    │  LABEL-500:                         │
    │  ├─ Order quantity: 6,000          │
    │  ├─ Order by: Dec 18               │
    │  └─ Receive by: Dec 28             │
    │                                     │
    │  → Forward to Supply Planning      │
    └─────────────────────────────────────┘

    📋 EXAMPLE:
    Scenario: Cần sản xuất 8,000 CHAI-500ML

    BOM:
    CHAI-500ML (1 unit)
    ├─ PVC-R01: 0.5 kg (lead time: 7 days)
    ├─ CAP-500: 1 pc (lead time: 10 days)
    └─ LABEL-500: 1 pc (lead time: 14 days)

    Calculation:
    Gross Requirements:
    ├─ PVC-R01: 4,000 kg
    ├─ CAP-500: 8,000 pcs
    └─ LABEL-500: 8,000 pcs

    Stock:
    ├─ PVC-R01: 5,000 kg → Enough ✅
    ├─ CAP-500: 2,500 pcs → Short 5,500 ⚠️
    └─ LABEL-500: 2,000 pcs → Short 6,000 ⚠️

    Output:
    Planned Orders:
    ├─ CAP-500: 5,500 pcs (Order Dec 21)
    └─ LABEL-500: 6,000 pcs (Order Dec 18)

    → Input cho Supply Planning (Module 4)

    📊 MODULE 4: SUPPLY PLANNING
    🎯 TÍNH NĂNG:
    Purpose:
    "QUYẾT ĐỊNH MUA GÌ, TỪ ĐÂU, BAO NHIÊU"

    Làm gì:
    ├─ Nhận material requirements (từ MRP)
    ├─ So sánh suppliers (price, lead time, quality)
    ├─ Chọn supplier tốt nhất
    ├─ Apply MOQ (minimum order quantity)
    ├─ Tính total cost
    └─ Tạo purchase recommendations

    Input:
    ├─ MRP requirements
    │   └─ Need: 5,500 CAP-500
    ├─ Supplier items (APS Supplier Item)
    │   ├─ Supplier A: 500 VND/pc, 10 days, MOQ 1000
    │   ├─ Supplier B: 480 VND/pc, 14 days, MOQ 2000
    │   └─ Supplier C: 520 VND/pc, 7 days, MOQ 500
    └─ Current stock & orders

    Output:
    └─ APS Supply Plan
        ├─ Purchase recommendations
        ├─ Supplier selection
        ├─ Order quantities
        ├─ Delivery dates
        └─ Total costs

    🔄 WORKFLOW:
    Step 1: Input
    ┌─────────────────────────────────────┐
    │  SUPPLY PLANNING INPUT              │
    ├─────────────────────────────────────┤
    │  MRP Requirements:                  │
    │  ├─ CAP-500: 5,500 pcs             │
    │  │   Need by: Dec 31               │
    │  └─ LABEL-500: 6,000 pcs           │
    │      Need by: Dec 28               │
    └─────────────────────────────────────┘
            ↓
    Step 2: Supplier analysis
    ┌─────────────────────────────────────┐
    │  SUPPLIER COMPARISON                │
    ├─────────────────────────────────────┤
    │  CAP-500:                           │
    │                                     │
    │  Supplier A:                        │
    │  ├─ Price: 500 VND/pc              │
    │  ├─ Lead time: 10 days ✅          │
    │  ├─ MOQ: 1,000                     │
    │  ├─ Order qty: 6,000 (5,500→6K)   │
    │  └─ Total: 3,000,000 VND           │
    │                                     │
    │  Supplier B:                        │
    │  ├─ Price: 480 VND/pc ✅ Cheapest  │
    │  ├─ Lead time: 14 days ⚠️ Too long │
    │  ├─ MOQ: 2,000                     │
    │  ├─ Order qty: 6,000               │
    │  └─ Total: 2,880,000 VND           │
    │                                     │
    │  Supplier C:                        │
    │  ├─ Price: 520 VND/pc              │
    │  ├─ Lead time: 7 days ✅ Fastest   │
    │  ├─ MOQ: 500                       │
    │  ├─ Order qty: 5,500               │
    │  └─ Total: 2,860,000 VND ✅ Best   │
    │                                     │
    │  Selected: Supplier C ✓            │
    │  Reason: Meets deadline + good cost│
    └─────────────────────────────────────┘
            ↓
    Step 3: Generate recommendations
    ┌─────────────────────────────────────┐
    │  PURCHASE RECOMMENDATIONS           │
    ├─────────────────────────────────────┤
    │  Item: CAP-500                      │
    │  ├─ Supplier: Supplier C            │
    │  ├─ Quantity: 5,500 pcs            │
    │  ├─ Unit price: 520 VND            │
    │  ├─ Total cost: 2,860,000 VND      │
    │  ├─ Order by: Dec 24               │
    │  └─ Expected: Dec 31               │
    │                                     │
    │  Item: LABEL-500                    │
    │  ├─ Supplier: Supplier X            │
    │  ├─ Quantity: 6,000 pcs            │
    │  ├─ Unit price: 300 VND            │
    │  ├─ Total cost: 1,800,000 VND      │
    │  ├─ Order by: Dec 14               │
    │  └─ Expected: Dec 28               │
    │                                     │
    │  Grand Total: 4,660,000 VND        │
    │  Status: Ready for approval        │
    └─────────────────────────────────────┘

    📋 EXAMPLE:
    Scenario: Cần mua materials cho production

    MRP Requirements:
    ├─ CAP-500: 5,500 pcs (by Dec 31)
    └─ LABEL-500: 6,000 pcs (by Dec 28)

    Supplier Selection:
    CAP-500:
    ├─ Evaluated 3 suppliers
    ├─ Selected: Supplier C
    └─ Reason: Good price + meets deadline

    LABEL-500:
    ├─ Evaluated 2 suppliers
    ├─ Selected: Supplier X
    └─ Reason: Cheapest + reliable

    Output: SUPPLY-PLAN-2025-00001
    ┌──────────────┬───────────┬──────────┬──────────┬────────────┐
    │    Item      │ Supplier  │   Qty    │  Price   │   Total    │
    ├──────────────┼───────────┼──────────┼──────────┼────────────┤
    │ CAP-500      │ SUP-C     │  5,500   │   520    │ 2,860,000  │
    │ LABEL-500    │ SUP-X     │  6,000   │   300    │ 1,800,000  │
    ├──────────────┼───────────┼──────────┼──────────┼────────────┤
    │ TOTAL        │           │          │          │ 4,660,000  │
    └──────────────┴───────────┴──────────┴──────────┴────────────┘

    → Manager approve
    → Generate Purchase Orders

    📊 MODULE 5: SCHEDULE OPTIMIZATION
    🎯 TÍNH NĂNG:
    Purpose:
    "TỐI ƯU LỊCH TRÌNH SẢN XUẤT"

    Làm gì:
    ├─ Nhận production plan (từ Module 2)
    ├─ Xét production capacity
    ├─ Xét machine availability
    ├─ Xét labor availability
    ├─ Minimize setup time
    ├─ Optimize sequence
    └─ Generate detailed schedule

    Input:
    ├─ Production Plan
    │   └─ CHAI-500ML: 8,000 (Dec)
    │       CHAI-1L: 5,000 (Dec)
    ├─ Resources:
    │   ├─ Production lines
    │   ├─ Machine capacity
    │   └─ Labor hours
    └─ Constraints:
        ├─ Due dates
        ├─ Setup times
        └─ Material availability

    Output:
    └─ APS Production Schedule
        ├─ Daily/weekly schedule
        ├─ Machine assignments
        ├─ Start/end times
        ├─ Resource utilization
        └─ Gantt chart

    🔄 WORKFLOW:
    Step 1: Input
    ┌─────────────────────────────────────┐
    │  SCHEDULING INPUT                   │
    ├─────────────────────────────────────┤
    │  Production Plan:                   │
    │  ├─ CHAI-500ML: 8,000 units        │
    │  │   Due: Dec 31                   │
    │  └─ CHAI-1L: 5,000 units           │
    │      Due: Dec 31                   │
    │                                     │
    │  Resources:                         │
    │  ├─ Line A: 2,000 units/day        │
    │  └─ Line B: 1,500 units/day        │
    │                                     │
    │  Constraints:                       │
    │  ├─ Setup CHAI→CHAI: 4 hours       │
    │  └─ Available days: 28 days        │
    └─────────────────────────────────────┘
            ↓
    Step 2: Optimization
    ┌─────────────────────────────────────┐
    │  OPTIMIZATION                       │
    ├─────────────────────────────────────┤
    │  Objective: Minimize makespan       │
    │                                     │
    │  Consider:                          │
    │  ├─ Due dates                      │
    │  ├─ Capacity                       │
    │  ├─ Setup times                    │
    │  └─ Material availability          │
    │                                     │
    │  Algorithm:                         │
    │  └─ Genetic Algorithm /            │
    │      Constraint Programming        │
    └─────────────────────────────────────┘
            ↓
    Step 3: Generate schedule
    ┌─────────────────────────────────────┐
    │  PRODUCTION SCHEDULE - December     │
    ├─────────────────────────────────────┤
    │  Week 1 (Dec 1-7):                 │
    │  ├─ Line A: CHAI-500ML - 2,000    │
    │  └─ Line B: CHAI-1L - 1,500       │
    │                                     │
    │  Week 2 (Dec 8-14):                │
    │  ├─ Line A: CHAI-500ML - 2,500    │
    │  └─ Line B: CHAI-1L - 1,500       │
    │                                     │
    │  Week 3 (Dec 15-21):               │
    │  ├─ Line A: CHAI-500ML - 2,500    │
    │  └─ Line B: CHAI-1L - 1,500       │
    │                                     │
    │  Week 4 (Dec 22-31):               │
    │  ├─ Line A: CHAI-500ML - 1,000    │
    │  └─ Line B: CHAI-1L - 500         │
    │                                     │
    │  Utilization:                       │
    │  ├─ Line A: 85%                    │
    │  └─ Line B: 72%                    │
    └─────────────────────────────────────┘

    📋 EXAMPLE:
    Scenario: Schedule production cho tháng 12

    Input:
    ├─ CHAI-500ML: 8,000 units
    ├─ CHAI-1L: 5,000 units
    ├─ TUI-20X30: 5,000 units
    └─ Machines: 2 lines

    Optimization:
    ├─ Minimize total time
    ├─ Balance load
    └─ Meet due dates

    Output: SCHEDULE-2025-00001

    Gantt Chart:
    Line A: ████████████████████████████
            CHAI-500ML (4 weeks)

    Line B: ██████████░░░░██████████████
            CHAI-1L    TUI-20X30

    Utilization:
    ├─ Line A: 85% (good)
    └─ Line B: 78% (good)

    → Production dept executes

    🎯 FULL FLOW VISUALIZATION
    End-to-end Example:
    THÁNG 11 - PLANNING CYCLE
    ═════════════════════════════════════════

    Week 1: FORECASTING
    ├─ BA chạy Demand Forecast
    ├─ Input: 48 months history
    ├─ Output: FORECAST-2025-00123
    └─ Result: Dec demand = 10,000 CHAI

    Week 2: PRODUCTION PLANNING
    ├─ Manager chạy Production Planning
    ├─ Input: FORECAST-2025-00123
    ├─ Check: Stock = 27,500 (đủ!)
    ├─ Output: PROD-PLAN-2025-00001
    └─ Decision: Không cần sản xuất ✅

    [IF cần sản xuất:]

    Week 3: MRP + SUPPLY PLANNING
    ├─ System chạy MRP
    ├─ BOM explosion: Need materials
    ├─ Output: MRP-2025-00001
    ├─ Supply Planning: Select suppliers
    └─ Output: SUPPLY-PLAN-2025-00001

    Week 4: SCHEDULING
    ├─ Production chạy Schedule Optimization
    ├─ Input: Production Plan
    ├─ Optimize: Machine assignment
    └─ Output: SCHEDULE-2025-00001


    THÁNG 12 - EXECUTION
    ═════════════════════════════════════════

    ├─ Follow production schedule
    ├─ Receive materials from suppliers
    ├─ Manufacture products
    └─ Deliver to customers

    📋 SUMMARY TABLE
    Module comparison:
    ModuleInputProcessOutputFrequency1. ForecastSales historyARIMA/ML12-month forecastMonthly2. Production PlanningForecast + StockNet requirementsProduction qtyMonthly3. MRPProduction plan + BOMExplosionMaterial requirementsAfter planning4. Supply PlanningMRP + SuppliersOptimizationPurchase ordersAfter MRP5. SchedulingProduction plan + CapacityOptimizationDetailed scheduleAfter planning

    🎯 DEPENDENCIES
    ┌─────────────────────┐
    │  Demand Forecast    │ ← Độc lập (chạy trước)
    └──────────┬──────────┘
            ↓
    ┌──────────┴──────────┐
    │ Production Planning │ ← Phụ thuộc Forecast
    └──────────┬──────────┘
            ├───────────────────────┐
            ↓                       ↓
    ┌──────────┴──────────┐ ┌─────────┴────────────┐
    │       MRP           │ │ Schedule Optimization│
    └──────────┬──────────┘ └──────────────────────┘
            ↓
    ┌──────────┴──────────┐
    │  Supply Planning    │
    └─────────────────────┘

    Linear dependencies: 1 → 2 → 3 → 4
    Parallel possible: 2 → {3, 5}