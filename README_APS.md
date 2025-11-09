# APS System — Full Workflow (README)

> **Version:** 1.0 · **Last updated:** 2025-11-09  
> **Scope:** End-to-end Advanced Planning & Scheduling (APS) workflow with 5 modules: Demand Forecasting → Production Planning → MRP → Supply Planning → Schedule Optimization.  
> **Language:** VI + EN terms for clarity.

---

## Table of Contents
- [1) Overview](#1-overview)
- [2) Module 1 — Demand Forecasting](#2-module-1—demand-forecasting)
- [3) Module 2 — Production Planning](#3-module-2—production-planning)
- [4) Module 3 — MRP (Material Requirements Planning)](#4-module-3—mrp-material-requirements-planning)
- [5) Module 4 — Supply Planning](#5-module-4—supply-planning)
- [6) Module 5 — Schedule Optimization](#6-module-5—schedule-optimization)
- [7) End-to-End Planning Cycle](#7-end-to-end-planning-cycle)
- [8) Summary & Comparison](#8-summary--comparison)
- [9) Dependencies](#9-dependencies)
- [10) Example IDs & Conventions](#10-example-ids--conventions)

---

## 1) Overview

```
┌─────────────────────────────────────────────────────────┐
│                  APS WORKFLOW                           │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  1. DEMAND FORECAST    → Dự báo nhu cầu                 │
│           ↓                                             │
│  2. PRODUCTION PLANNING → Kế hoạch sản xuất            │
│           ↓                                             │
│  3. MRP                → Tính nguyên vật liệu          │
│           ↓                                             │
│  4. SUPPLY PLANNING    → Kế hoạch mua hàng             │
│           ↓                                             │
│  5. SCHEDULE OPTIMIZATION → Tối ưu lịch sản xuất       │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

- **Objective (Mục tiêu):** Cung cấp luồng quy hoạch tổng thể từ dự báo → quyết định sản xuất → tính NVL → kế hoạch mua → tối ưu lịch.
- **Frequency (Tần suất):** Lập theo chu kỳ tháng (planning cycle) và cập nhật theo sự kiện (đơn hàng mới, thay đổi năng lực, v.v.).

---

## 2) Module 1—Demand Forecasting

**Purpose (Mục tiêu):** *Dự báo nhu cầu tương lai.*  
**Làm gì:**  
- Phân tích lịch sử bán hàng  
- Phát hiện xu hướng (trend)  
- Phát hiện mùa vụ (seasonality)  
- Dự báo 12 tháng tiếp theo  
- Tính độ chính xác (MAPE, RMSE)

**Input:**  
- **Sales Order History** (48 tháng): `transaction_date`, `item_code`, `qty_sold`  
- **Danh sách Items cần forecast**

**Output:** `APS Forecast Result`  
- 12-month forecast  
- Upper / Lower bounds (optimistic / pessimistic)  
- Accuracy metrics (MAPE, RMSE)

**Workflow:**

**Step 1 — User inputs**

```
CREATE FORECAST
Items: [CHAI-500ML, CHAI-1L, ...]
Historical period: 48 months
Forecast horizon: 12 months
Model: ARIMA / SARIMA
```

**Step 2 — System processing**
- Lấy dữ liệu lịch sử bán hàng
- Làm sạch dữ liệu (outliers, nulls)
- Train ARIMA/SARIMA theo từng item
- Generate forecast + confidence bounds
- Tính độ chính xác (MAPE, RMSE)

**Step 3 — Output**
- Ví dụ (CHAI-500ML):  
  - Dec 2025: `10,000 ± 500`  
  - Jan 2026: `10,200 ± 520`  
  - Feb 2026: `9,800 ± 480`  
- Accuracy: `91.5% MAPE`  
- Status: `Completed`

**Example:**

- **Input:**  
  Items: `CHAI-500ML, CHAI-1L, TUI-20X30, TUI-30X40, HOP-NHUA-1KG`  
  Historical: `2022-01 → 2025-10` (48 months)  
  Forecast: `2025-11 → 2026-10` (12 months)

- **Output ID:** `FORECAST-2025-00123`

| Item          | Nov   | Dec   | Jan   | ... |
|---------------|-------|-------|-------|-----|
| CHAI-500ML    | 9,800 | 10,000| 10,200| ... |
| CHAI-1L       | 5,900 | 6,000 | 6,100 | ... |
| TUI-20X30     |24,500 |25,000 |25,200 | ... |
| TUI-30X40     |14,800 |15,000 |15,100 | ... |
| HOP-NHUA-1KG  | 4,900 | 5,000 | 5,100 | ... |

> **Next:** Lưu DB → dùng cho Production Planning (Module 2).

---

## 3) Module 2—Production Planning

**Purpose (Mục tiêu):** *Quyết định sản xuất bao nhiêu.*  
**Làm gì:**  
- Nhận demand (từ forecast hoặc sales orders)  
- Kiểm tra tồn kho hiện tại  
- Tính nhu cầu ròng (net requirements)  
- Xét safety stock  
- Áp dụng lot-sizing  
- Tạo production plan

**Input:**  
- **Demand source:** Forecast Result / Sales average / Hybrid  
- **Current stock** (APS Bin)  
- **Planning parameters:** Planning period, Safety stock (days), Lot sizing

**Output:** `APS Production Plan`  
- Recommended production quantity  
- Production priority  
- Material requirements (preview)  
- Capacity check

**Workflow:**

**Step 1 — User inputs**

```
CREATE PRODUCTION PLAN
Demand Source: Forecast (FORECAST-2025-00123)
Items: All
Planning Period: Dec 2025
Warehouse: All
Safety Stock: 7 days
```

**Step 2 — System calculation (per item):**  
1) Lấy demand từ forecast  
2) Tính safety stock (vd: daily = 10,000/30 = 333; safety = 333 × 7 = 2,333)  
3) Lấy tồn kho từ bins  
4) Tính net requirement = (Demand + Safety) − Stock  
5) Quyết định sản xuất (nếu `Net > 0` mới cần sản xuất)

**Step 3 — Output (ví dụ):**

```
PRODUCTION PLAN
CHAI-500ML
- Demand: 10,000
- Safety Stock: 2,333
- Current Stock: 27,500
- Net Requirement: -15,167 → Produce: 0 (Surplus)

CHAI-1L
- Demand: 6,000
- Safety: 1,400
- Stock: 3,000
- Net: 4,400 → Produce: 5,000 (rounded)
Status: Ready for approval
```

**Example:**

- **Input:** Forecast `FORECAST-2025-00123`, Period `2025-12-01 → 2025-12-31`, Items `5 items`  
- **Output ID:** `PROD-PLAN-2025-00001`

| Item          | Demand | Stock | Net     | Produce |
|---------------|--------|-------|---------|---------|
| CHAI-500ML    | 12,333 | 27,500| -15,167 | 0       |
| CHAI-1L       | 7,400  | 13,000| -5,600  | 0       |
| TUI-20X30     | 27,000 | 57,000| -30,000 | 0       |
| TUI-30X40     | 16,500 | 26,000| -9,500  | 0       |
| HOP-NHUA-1KG  | 6,200  | 7,500 | -1,300  | 0       |

> **Conclusion:** Không cần sản xuất tháng 12 (tồn kho đủ).  
> **Next:** Manager review/approve → Input cho MRP (Module 3).

---

## 4) Module 3—MRP (Material Requirements Planning)

**Purpose (Mục tiêu):** *Tính nguyên vật liệu cần thiết.*  
**Làm gì:**  
- Nhận production plan  
- Đọc BOM (Bill of Materials)  
- Explosion: TP → NVL  
- Kiểm tra tồn kho NVL  
- Tính net requirements cho NVL  
- Offset theo lead time

**Input:**  
- **Production Plan** (vd: `CHAI-500ML: 8,000`)  
- **BOM structure** (1 CHAI-500ML → 0.5 kg PVC-R01, 1 CAP-500ML, 1 LABEL-500ML)  
- **Current NVL stock**

**Output:** `APS MRP Result`  
- Material requirements by item  
- Time-phased requirements  
- Net requirements (gross - stock)  
- Planned orders (offset by lead time)

**Workflow (rút gọn):**
1) **MRP Input**: `PROD-PLAN-2025-00001`, items to produce + due date  
2) **BOM Explosion**: tính gross requirement theo định mức  
3) **Stock Check**: xác định net requirement (sau khi trừ tồn khả dụng)  
4) **Time Phasing**: lùi đơn mua theo lead time  
5) **Output**: Planned Orders theo từng NVL

**Example:**

- **BOM** (per 1 unit `CHAI-500ML`):  
  - PVC-R01: 0.5 kg (LT 7d)  
  - CAP-500: 1 pc (LT 10d)  
  - LABEL-500: 1 pc (LT 14d)

- **Gross Requirements** (for 8,000 units):  
  - PVC-R01: 4,000 kg  
  - CAP-500: 8,000 pcs  
  - LABEL-500: 8,000 pcs

- **Stock Snapshot:**  
  - PVC-R01: 5,000 kg → Enough  
  - CAP-500: 2,500 pcs → Short 5,500  
  - LABEL-500: 2,000 pcs → Short 6,000

- **Planned Orders:**  
  - CAP-500: 5,500 pcs (Order **Dec 21**, Need **Dec 31**)  
  - LABEL-500: 6,000 pcs (Order **Dec 18**, Need **Dec 28**)

> **Next:** Forward to Supply Planning (Module 4).

---

## 5) Module 4—Supply Planning

**Purpose (Mục tiêu):** *Quyết định mua gì, từ đâu, bao nhiêu.*  
**Làm gì:**  
- Nhận yêu cầu NVL từ MRP  
- So sánh nhà cung cấp (giá, LT, chất lượng)  
- Chọn supplier tối ưu  
- Áp dụng MOQ  
- Tính total cost  
- Tạo purchase recommendations

**Input:**  
- **MRP Requirements** (vd: CAP-500: 5,500)  
- **Supplier Items** (giá/LT/MOQ)  
- **Current stock & open POs**

**Output:** `APS Supply Plan`  
- Purchase recommendations  
- Supplier selection & order qty  
- Delivery dates & total cost

**Supplier Comparison (ví dụ CAP-500):**

- **Supplier A**: 500 VND/pc, LT 10d, MOQ 1,000 → Order 6,000 → Total 3,000,000  
- **Supplier B**: 480 VND/pc, LT 14d, MOQ 2,000 → Order 6,000 → Total 2,880,000  
- **Supplier C**: 520 VND/pc, LT 7d, MOQ 500 → Order 5,500 → **Total 2,860,000 (Selected)**

**Purchase Recommendations:**

- **CAP-500** → Supplier C, Qty 5,500, Unit 520 → **2,860,000 VND**  
  Order by **Dec 24**, Expected **Dec 31**  
- **LABEL-500** → Supplier X, Qty 6,000, Unit 300 → **1,800,000 VND**  
  Order by **Dec 14**, Expected **Dec 28**

**Output ID:** `SUPPLY-PLAN-2025-00001`

| Item       | Supplier | Qty   | Price | Total     |
|------------|----------|-------|-------|-----------|
| CAP-500    | SUP-C    | 5,500 | 520   | 2,860,000 |
| LABEL-500  | SUP-X    | 6,000 | 300   | 1,800,000 |
| **TOTAL**  |          |       |       | **4,660,000** |

> **Next:** Manager approve → Generate Purchase Orders.

---

## 6) Module 5—Schedule Optimization

**Purpose (Mục tiêu):** *Tối ưu lịch trình sản xuất.*  
**Làm gì:**  
- Nhận production plan  
- Xét capacity, máy, nhân công  
- Minimize setup time & tối ưu thứ tự  
- Sinh lịch chi tiết (Gantt, daily/weekly, assignment)

**Input:**  
- Production Plan (vd: CHAI-500ML: 8,000; CHAI-1L: 5,000)  
- Resources (line, machine capacity, labor hours)  
- Constraints (due dates, setup, vật tư)

**Output:** `APS Production Schedule`  
- Daily/weekly schedule  
- Machine/line assignments  
- Start/end times & utilization

**Optimization:**  
- **Objective:** Minimize makespan, meet due dates  
- **Algorithm:** Genetic Algorithm / Constraint Programming (hoặc heuristic nâng cao)

**Example — December:**

- **Lines:** Line A (2,000 u/day), Line B (1,500 u/day)  
- **Setup:** CHAI→CHAI = 4h, Available = 28 ngày

```
Week 1 (Dec 1–7)
- Line A: CHAI-500ML — 2,000
- Line B: CHAI-1L     — 1,500

Week 2 (Dec 8–14)
- Line A: CHAI-500ML — 2,500
- Line B: CHAI-1L     — 1,500

Week 3 (Dec 15–21)
- Line A: CHAI-500ML — 2,500
- Line B: CHAI-1L     — 1,500

Week 4 (Dec 22–31)
- Line A: CHAI-500ML — 1,000
- Line B: CHAI-1L     —   500

Utilization
- Line A: 85%
- Line B: 72%
```

---

## 7) End-to-End Planning Cycle

**THÁNG 11 — PLANNING CYCLE**

- **Week 1: Forecasting**
  - BA chạy Demand Forecast (48 tháng lịch sử) → `FORECAST-2025-00123`
  - Kết quả: Dec demand = 10,000 CHAI
- **Week 2: Production Planning**
  - Manager chạy Production Planning với Forecast trên
  - Check stock = 27,500 (đủ) → `PROD-PLAN-2025-00001`
  - Quyết định: Không sản xuất ✅
- **[IF cần sản xuất] Week 3: MRP + Supply Planning**
  - System chạy MRP → `MRP-2025-00001`
  - Supply Planning: chọn NCC → `SUPPLY-PLAN-2025-00001`
- **Week 4: Scheduling**
  - Production chạy Schedule Optimization → `SCHEDULE-2025-00001`

**THÁNG 12 — EXECUTION**
- Thực thi lịch sản xuất
- Nhận NVL từ nhà cung cấp
- Sản xuất & giao hàng

---

## 8) Summary & Comparison

| Module | Input                          | Process                   | Output               | Frequency          |
|-------:|--------------------------------|---------------------------|----------------------|--------------------|
| 1. Forecast | Sales history (48m)      | ARIMA/ML                  | 12-month forecast    | Monthly            |
| 2. Prod. Planning | Forecast + Stock  | Net requirements, lot-size| Production qty       | Monthly            |
| 3. MRP  | Production plan + BOM         | Explosion, net calc       | Material requirements| After planning     |
| 4. Supply | MRP + Suppliers            | Optimization               | Purchase orders      | After MRP          |
| 5. Scheduling | Plan + Capacity        | Optimization               | Detailed schedule    | After planning     |

---

## 9) Dependencies

```
┌─────────────────────┐
│  Demand Forecast    │ ← Độc lập (chạy trước)
└──────────┬──────────┘
           ↓
┌──────────┴──────────┐
│ Production Planning │ ← Phụ thuộc Forecast
└──────────┬──────────┘
           ├───────────────────────┐
           ↓                       ↓
┌──────────┴──────────┐   ┌────────┴────────────┐
│       MRP           │   │ Schedule Optimization│
└──────────┬──────────┘   └──────────────────────┘
           ↓
┌──────────┴──────────┐
│  Supply Planning    │
└─────────────────────┘
```
- **Linear:** `1 → 2 → 3 → 4`  
- **Parallel possible:** `2 → {3, 5}`

---

## 10) Example IDs & Conventions

- Forecast: `FORECAST-YYYY-#####` (vd: `FORECAST-2025-00123`)  
- Production Plan: `PROD-PLAN-YYYY-#####`  
- MRP: `MRP-YYYY-#####`  
- Supply Plan: `SUPPLY-PLAN-YYYY-#####`  
- Schedule: `SCHEDULE-YYYY-#####`

**Notes**
- Tất cả ví dụ số liệu (demand/stock/price/dates) chỉ minh hoạ.  
- Tích hợp thực tế có thể nối ERPNext (SO, BIN, BOM, PO) và module APS tuỳ biến.
