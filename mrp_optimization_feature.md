# MRP Optimization Feature — Data Mapping (README)

> **File:** `mrp_optimization_feature.md`  
> **Scope:** Full mapping from APS input DocTypes → MRP optimization → Output DocTypes & dashboard.  
> **Author:** BA · **Updated:** 2025-11-09

---

## 📥 INPUT DOCTYPES — DATA SOURCES

### 1) APS Production Plan ⭐⭐⭐⭐⭐ *(PRIMARY INPUT!)*
> Đây là **DEMAND** cho MRP — “cần sản xuất gì, bao nhiêu, khi nào”.

```javascript
// DocType: APS Production Plan
{
  "name": "PROD-PLAN-2025-00001",
  "planning_period_from": "2025-10-01",
  "planning_period_to": "2025-12-31",
  "status": "Approved",
  "items": [
    {
      "item": "B0ES",
      "planned_production_qty": 8000,
      "start_date": "2025-11-01",
      "due_date": "2025-12-07",
      "priority": "High",
      "warehouse": "WH-MAIN"
    }
  ]
}
```

**Mapping to Output:**
- **Items to produce:** `B0ES, 30ES, A0ES, 14ES, 40ES`
- **Quantities:** `345, 266, 181, ...`
- **Need By Date:** `2025-12-07, ...`

---

### 2) APS BOM ⭐⭐⭐⭐⭐ *(CRITICAL!)*
> Công thức sản xuất — phân rã thành **materials**.

```javascript
// DocType: APS BOM
{
  "item": "B0ES",           // Finished good
  "quantity": 1,
  "is_active": 1,
  "is_default": 1,
  "items": [
    { "item_code": "STEEL-A", "qty": 2.5, "uom": "Kg", "rate": 50000, "bom_no": null }
  ]
}
```

**Process Example:**  
- Input: Produce **345** `B0ES`  
- BOM: `1 B0ES = 2.5 kg STEEL-A`  
- Output: Need **862.5 kg** `STEEL-A`

**Mapping to Output:**  
- `Type = "WIP"` nếu có BOM (sản xuất nội bộ)  
- `Type = "PO"` nếu **không có** BOM (mua ngoài)

---

### 3) APS Item ⭐⭐⭐⭐
> Thông tin item & **lead times** (SX/Mua).

```javascript
// DocType: APS Item
{
  "name": "B0ES",
  "item_name": "B0ES Specification",
  "stock_uom": "Pcs",
  "item_group": "Finished Goods",

  // Finished goods:
  "lead_time_days": 5,
  "safety_stock": 50,
  "valuation_rate": 100000,

  // Raw materials:
  "is_purchase_item": 1,
  "min_order_qty": 1000,
  "lead_time_days": 10
}
```

**Mapping to Output:**
- Release Date = `Need By − Lead Time` (ví dụ: `Dec 7 − 20 days = Nov 17`)  
- Safety Stock → **risk** calculation

---

### 4) APS Bin ⭐⭐⭐⭐
> Tồn kho hiện tại (Actual / Ordered / Reserved / Projected).

```javascript
// DocType: APS Bin
{
  "item": "STEEL-A",
  "warehouse": "WH-MAIN",
  "actual_qty": 5000,
  "ordered_qty": 1000,
  "reserved_qty": 500,
  "projected_qty": 5500,
  "valuation_rate": 45000
}
```

**Calculation:**  
- Gross Req: **862.5 kg** (from BOM)  
- Available: **5,500 kg** (from Bin)  
- Net Requirement: **0** → **No order**

**Mapping to Output:**  
- Chỉ tạo **Planned Order** nếu `Net Requirement > 0`

---

### 5) APS Supplier ⭐⭐⭐
> Danh sách **suppliers** có thể mua.

```javascript
// DocType: APS Supplier
{
  "name": "NCC_A",
  "supplier_name": "Nha Cung Cap A",
  "supplier_type": "Company",
  "country": "Vietnam",
  "payment_terms": "30 days",
  "is_active": 1
}
```

**Mapping to Output:**  
- `supplier_process` column: `"NCC_C"`, `"NCC_B"`, `"NCC_D"`

---

### 6) APS Supplier Item ⭐⭐⭐⭐⭐ *(CRITICAL for Supplier Selection!)*
> Giá, MOQ, **lead time**, năng lực theo **Supplier–Item**.

```javascript
// DocType: APS Supplier Item
{
  "supplier": "NCC_A",
  "item_code": "STEEL-A",
  "item_name": "Steel Grade A",

  // Pricing
  "price": 45000,
  "currency": "VND",

  // Constraints
  "min_order_qty": 1000,
  "max_order_qty": 10000,
  "lead_time_days": 10,

  // Quality / misc
  "supplier_part_no": "SA-001",
  "is_default": 0
}
```

**Optimization uses this to:**  
- So sánh **giá** (Cost Minimization)  
- Chọn **nhanh** hơn (Reduce Lead Time)  
- **Trade-off** cost vs speed (multi-objective)  
- Áp dụng **MOQ/capacity**

**Mapping to Output:**  
- Algorithm chọn supplier tối ưu (ví dụ: `NCC_C` giá/lead tốt)

---

### 7) APS Warehouse ⭐⭐
> Thông tin kho để check stock / nhận hàng.

```javascript
// DocType: APS Warehouse
{
  "name": "WH-MAIN",
  "warehouse_name": "Main Warehouse",
  "warehouse_type": "Finished Goods",
  "is_group": 0
}
```

**Mapping to Output:**  
- Tổng hợp stock từ các warehouse trong **scope**.

---

## 🔄 DATA FLOW — FROM INPUT TO OUTPUT

### Complete Process
```
Step 1: READ PRODUCTION PLAN
  APS Production Plan
  Items to produce:
   - B0ES: 345 units (Dec 7)
   - 30ES: 266 units (Dec 6)
   - ...

Step 2: BOM EXPLOSION
  APS BOM
  For each FG:
   - B0ES (345 units):
      STEEL-A: 862.5 kg
      BOLT-M6: 3,450 pcs
      PAINT:   34.5 L
   - 30ES (...)

Step 3: AGGREGATE MATERIALS
  Total material requirements:
   - STEEL-A: 5,200 kg
   - BOLT-M6: 15,000 pcs
   - PAINT:   150 L

Step 4: CHECK STOCK (APS Bin)
  - STEEL-A: Avail 3,000 kg → Net 2,200 kg ⚠️
  - BOLT-M6: Avail 20,000 pcs → Net 0 ✅
  - PAINT:   Avail 50 L → Net 100 L ⚠️

Step 5: SUPPLIER SELECTION (APS Supplier Item)
  For STEEL-A (need 2,200 kg):
   - NCC_A: 50K/kg, LT 15d, Score 6/10
   - NCC_B: 48K/kg, LT 12d, Score 7/10 ✅ Cost
   - NCC_C: 52K/kg, LT  8d, Score 7/10 ✅ Speed
  Decision:
   - Objective "Cost" → NCC_B
   - Objective "Lead" → NCC_C
   - Objective "Balance" → NCC_B

Step 6: CALCULATE DATES (APS Item lead times)
  STEEL-A from NCC_B:
   - Need By: Dec 7
   - Lead: 12d
   - Release: Nov 25
  PAINT from NCC_D:
   - Need By: Dec 6
   - Lead: 10d
   - Release: Nov 26

Step 7: RISK ASSESSMENT
  STEEL-A:
   - Lead 12d; Buffer 5d; Coverage 57% → Risk: MEDIUM 🟡
  PAINT:
   - Lead 10d; Buffer 1d; Coverage 33% → Risk: HIGH 🔴

Step 8: OPTIMIZATION METRICS
  - Total Optimizations: 41
  - Inventory Reduction: đ2.8M
  - Cost Saving: đ1.8M
  - Service Level: 96.5%

Step 9: GENERATE OUTPUT
  APS MRP Result (header + child planned orders)
```

---

## 🆕 OUTPUT DOCTYPES TO CREATE

### 1) APS MRP Result (Header)
```javascript
{
  "doctype": "APS MRP Result",
  "fields": {
    // Identity
    "name": "MRP-2025-00001",
    "scenario_name": "MRP_Month_10_2025",
    "production_plan": "PROD-PLAN-2025-00001",

    // Run info
    "run_date": "2025-11-09",
    "run_time": "2025-11-09 22:41:17",
    "status": "Completed",
    "algorithm_used": "Genetic Algorithm",

    // Parameters used
    "max_budget": 0,
    "min_service_level": 95,
    "objectives_selected": ["Cost Minimization", "Inventory Optimization"],

    // Metrics
    "total_optimizations": 41,
    "total_purchase_orders": 15,
    "total_work_orders": 5,
    "inventory_reduction": 2800000,
    "cost_saving": 1800000,
    "service_level": 96.5,
    "total_order_value": 156000000,

    // Child table link
    "planned_orders": [] // APS MRP Planned Order
  }
}
```

### 2) APS MRP Planned Order (Child Table)
```javascript
{
  "doctype": "APS MRP Planned Order",
  "fields": {
    // Item info
    "item_code": "B0ES",
    "item_name": "B0ES Specification",
    "item_group": "Finished Goods",

    // Order type
    "order_type": "WIP", // or "PO"

    // Requirements (time-phased)
    "gross_requirement": 345,
    "scheduled_receipts": 0,
    "available_stock": 100,
    "safety_stock": 50,
    "net_requirement": 195,

    // Order details
    "order_quantity": 345,
    "unit_price": 100000,
    "total_value": 34500000,

    // Schedule
    "release_date": "2025-11-17",
    "need_by_date": "2025-12-07",
    "lead_time_days": 20,

    // Supplier/Process
    "supplier_process": "Workshop", // or "NCC_C"

    // Analysis
    "priority": "High",
    "risk_level": "MEDIUM",
    "reason": "Nhu cầu từ BOM cấp 2",

    // Source tracing
    "parent_item": "FINISHED-PROD-001",
    "bom_level": 2
  }
}
```

---

## 📊 DOCTYPES SUMMARY TABLE

| DocType             | Purpose                        | Priority | Fields (Key)                                | Output Impact                          |
|---------------------|--------------------------------|---------:|---------------------------------------------|----------------------------------------|
| APS Production Plan | Demand input                   | ⭐⭐⭐⭐⭐   | items, qty, dates                           | All planned orders                      |
| APS BOM             | Material explosion             | ⭐⭐⭐⭐⭐   | items, qty, rates                           | Material requirements                   |
| APS Item            | Item info, lead times          | ⭐⭐⭐⭐    | lead_time, safety_stock                     | Release dates, risk                     |
| APS Bin             | Current stock                  | ⭐⭐⭐⭐    | actual, ordered, reserved, projected        | Net requirements                        |
| APS Supplier        | Supplier list                  | ⭐⭐⭐     | name, supplier_name                         | Supplier/Process column                 |
| APS Supplier Item   | Pricing & terms                | ⭐⭐⭐⭐⭐   | price, lead_time, MOQ, capacity             | Supplier selection, cost                |
| APS Warehouse       | Warehouse info                 | ⭐⭐      | name                                        | Stock location                          |

---

## ✅ COMPLETE DATA MAPPING — Dashboard ↔ DocTypes

```
DASHBOARD ELEMENT            → DATA SOURCE
Header
- "MRP Run #001"             → APS MRP Result.name
- "Run Time: 22:41:17"       → APS MRP Result.run_time

KPI Cards
- "41"                       → COUNT(APS MRP Planned Order)
- "đ2.800.000"               → APS MRP Result.inventory_reduction
- "đ1.800.000"               → APS MRP Result.cost_saving
- "96.5%"                    → APS MRP Result.service_level

Chart 1 — Nhu cầu ròng
- Aggregate APS MRP Planned Order.net_requirement by period

Chart 2 — Tồn kho dự kiến
- Current: APS Bin.actual_qty
- Projected: APS Bin.projected_qty + MRP orders

Planned Orders Table
- Direct from APS MRP Planned Order child table
```

---

## 🎯 TÓM TẮT

**INPUT (Có sẵn):**
```
✅ APS Production Plan (demand)
✅ APS BOM (công thức)
✅ APS Item (lead times)
✅ APS Bin (stock)
✅ APS Supplier (suppliers)
✅ APS Supplier Item (pricing)
✅ APS Warehouse (locations)
```

**OUTPUT (Cần tạo):**
```
🆕 APS MRP Result (header)
🆕 APS MRP Planned Order (child)
```
