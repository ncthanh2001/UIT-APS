# Production Planning — Quick Start Checklist (README)

> **Scope:** Everything needed to RUN the *Production Planning* module only (no MRP / no Scheduling).  
> **Last updated:** 2025-11-09 · **Language:** VI + EN terms.

---

## 0) TL;DR (Tóm tắt nhanh)

**CẦN CÓ (Must-have):**
- ✅ 1. **Master Data**
- ✅ 2. **Input Parameters**
- ✅ 3. **Calculation Logic**
- ✅ 4. **Output DocType**

**KHÔNG CẦN (Not required for this step):**
- ❌ **BOM** *(for MRP)*  
- ❌ **Routing** *(for Scheduling)*  
- ❌ **Work Center / Workstation** *(for Scheduling)*

---

## 1) Master Data (Đã có / Cần có)

### ✅ Already in place
1. **APS Item** — *8 items* *(5 finished goods + 3 raw materials)*  
2. **APS Warehouse** — *6 warehouses*  
3. **APS Bin** — *17 stock records (inventory levels)*  
4. **APS Forecast Result** — *Have forecast (if using forecast source)*  
5. **APS Sales Order History** — *48 records (≈23 months)*  
6. **APS Supplier** — *8 suppliers*  
7. **APS Supplier Item** — *8 supplier–item links*

### 🆕 Need to create now
8. **APS Production Plan (NEW DocType)** — *Stores the output of Production Planning*

**Header fields**
- `plan_name` (Data, required)  
- `planning_date` (Date, default = today)  
- `planning_period_from` (Date, required)  
- `planning_period_to` (Date, required)  
- `demand_source` (Select: Forecast / Sales History / Hybrid, required)  
- `forecast_result` (Link → APS Forecast Result, required if demand_source = Forecast/Hybrid)  
- `warehouse` (Link / Multi / All, optional)  
- `status` (Draft / Submitted / Approved)  
- `total_planned_qty` (Float, computed)

**Child Table: `APS Production Plan Item`**
- `item` (Link Item, required)  
- `item_name` (Data)  
- `forecasted_demand` (Float)  
- `safety_stock` (Float)  
- `current_stock` (Float)  
- `work_in_process` (Float)  
- `ordered_qty` (Float, open POs / in-transit)  
- `projected_stock` (Float)  
- `net_requirement` (Float)  
- `planned_production_qty` (Float)  
- `production_priority` (Int / Select)  
- `start_date` (Date)  
- `due_date` (Date)

> **Note:** This DocType is used only for PP output; MRP & Scheduling will read it later.

---

## 2) Input Parameters (Khi chạy)

**UI Flow (wireframe):**
```
RUN PRODUCTION PLANNING
─────────────────────────────────────────
1) BASIC INFO
   - Plan Name*: [Text]           e.g., "December 2025 Plan"
   - Planning Date: [auto today]

2) PLANNING SCOPE
   - Planning Period*:
       From*: [2025-12-01]
       To*  : [2025-12-31]
   - Items*:
       ○ All Items (default)
       ● Specific: [Multi-select]
   - Warehouse:
       ○ All Warehouses (default)
       ● Specific: [Select]

3) DEMAND SOURCE*
   ○ Forecast
     - Forecast Result: [Link]
   ○ Sales Order (Historical)
     - From: [2024-01-01]
     - To  : [2025-10-31]
     - Method: Average
   ○ Hybrid
     - Forecast: [Link]
     - Orders weight: [70]%
     - Forecast weight: [30]%
     
4) PLANNING PARAMETERS
   - Safety Stock Days: [7]
   - Consider Current Stock: [✓]
   - Consider In-transit:   [✓]
   - Consider WIP:          [ ]
   
[Cancel]   [Validate]   [Run Plan ▶]
```

### Required vs Optional

**REQUIRED**
- Planning Period (`From` / `To`)  
- Demand Source  
- Demand Source details:  
  - If **Forecast** → `forecast_result` ID  
  - If **Historical** → `date_range`  
  - If **Hybrid** → both + weights

**OPTIONAL (with sensible defaults)**
- Items (default **All**)  
- Warehouse (default **All**)  
- Safety Stock Days (default **7**)  
- Stock considerations (default **Yes**, include Current + In-transit)

---

## 3) Calculation Logic (Tóm tắt)

For each **item** in scope and period:

1. **Get demand**
   - If **Forecast**: use quantity from `APS Forecast Result` within period.  
   - If **Sales Historical**: compute method (e.g., period average).  
   - If **Hybrid**: `Demand = Orders * w1 + Forecast * w2` (weights sum = 100%).

2. **Compute Safety Stock**
   - Daily demand ≈ `period_demand / period_days`  
   - `safety_stock = daily_demand × safety_stock_days`

3. **Collect Stocks**
   - `current_stock` from **APS Bin** (by warehouse scope).  
   - `in_transit = openPOs_due_in_period` (if enabled).  
   - `wip` (if enabled).  
   - `projected_stock = current_stock + in_transit + wip`

4. **Net Requirement**
   - `net_requirement = (demand + safety_stock) − projected_stock`

5. **Plan Quantity**
   - If `net_requirement <= 0` → `planned_production_qty = 0` (surplus)  
   - Else → `planned_production_qty = lot_size(net_requirement)`
     - *Lot-sizing method:* simple rounding / EOQ / policy-based (configurable)

6. **Priority & Dates (optional)**
   - Assign `production_priority` by rule (e.g., larger net, earlier due).  
   - Suggest `start_date/due_date` if capacity calendar exists (soft check).

7. **Totals**
   - Sum `planned_production_qty` to `total_planned_qty` on header.

**Validation Rules**
- Date range valid (`from <= to`).  
- Demand source details provided.  
- Items exist and are active.  
- If Hybrid: `orders_weight + forecast_weight = 100`.

---

## 4) Output (DocType records)

- **Header:** One `APS Production Plan` per run.  
- **Child rows:** One `APS Production Plan Item` per item in scope.  
- **Status flow:** `Draft → Submitted → Approved`.  
- **Downstream:**  
  - MRP reads `planned_production_qty` per item + due date.  
  - Scheduling may read the same plus priorities/dates if provided.

**Example row (JSON):**
```json
{
  "item": "CHAI-1L",
  "forecasted_demand": 6000,
  "safety_stock": 1400,
  "current_stock": 3000,
  "work_in_process": 0,
  "ordered_qty": 0,
  "projected_stock": 3000,
  "net_requirement": 4400,
  "planned_production_qty": 5000,
  "production_priority": 2,
  "start_date": null,
  "due_date": "2025-12-31"
}
```

---

## Appendix — Developer Hooks (gợi ý)

- **Server Method:** `run_production_planning(params) -> APS Production Plan name`  
- **Permissions:** Only Planner / Manager roles can Run & Approve.  
- **Indexes:** `APS Bin (item, warehouse)`, `APS Forecast (item, period)`  
- **Extensibility:** plug-in lot-sizing / weights / custom priority rules.

---

## Troubleshooting (nhanh)

- *“No items in scope”* → Check Items filter or item statuses.  
- *“Missing demand source details”* → Provide Forecast ID / date range.  
- *“Negative or zero demand”* → Validate forecast/historical aggregation.  
- *“Duplicate plan name”* → Use unique `plan_name` per month/site.

---

**Ready to run.** After approval, proceed to **MRP** (if production > 0) or skip if all items are surplus.
