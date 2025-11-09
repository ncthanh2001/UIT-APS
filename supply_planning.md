🎯 OUTPUT CỦA SUPPLY PLANNING FUNCTION
PRIMARY OUTPUT: APS Purchase Plan (Kế hoạch mua hàng)
Đây là kết quả CHÍNH - một document/report chi tiết:
┌─────────────────────────────────────────────────────────┐
│         APS PURCHASE PLAN - THÁNG 12/2025              │
│         Planning Date: 09/11/2025                       │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  SUMMARY:                                               │
│  - Total Items: 5                                       │
│  - Total Quantity: 45,000 units                         │
│  - Total Value: 185,500,000 VND                         │
│  - Suppliers: 4                                         │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  ITEM DETAILS:                                          │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  1. CHAI-500ML                                          │
│     ├─ Forecasted Demand: 10,000                        │
│     ├─ Current Stock: 15,000 (WO-00005)                │
│     ├─ Reserved: 3,000                                  │
│     ├─ Projected Qty: 17,000                           │
│     ├─ Safety Stock: 2,000                              │
│     ├─ Reorder Level: 5,000                            │
│     ├─ Net Requirement: -5,000 (NO NEED TO ORDER)      │
│     └─ Status: ✅ SUFFICIENT                            │
│                                                         │
│  2. CHAI-1L                                             │
│     ├─ Forecasted Demand: 8,000                         │
│     ├─ Current Stock: 6,000 (WO-00005)                 │
│     ├─ Reserved: 1,000                                  │
│     ├─ Projected Qty: 7,000                            │
│     ├─ Safety Stock: 1,000                              │
│     ├─ Reorder Level: 2,500                            │
│     ├─ Net Requirement: 2,000 ⚠️                        │
│     ├─ Suggested Supplier: SUP-2025-00007              │
│     ├─ Unit Price: 5,500 VND                            │
│     ├─ Total Cost: 11,000,000 VND                       │
│     ├─ Lead Time: 5 days                                │
│     ├─ Order Date: 14/11/2025                          │
│     └─ Expected Delivery: 19/11/2025                    │
│                                                         │
│  3. TUI-20X30                                           │
│     ├─ Forecasted Demand: 25,000                        │
│     ├─ Current Stock: 20,000 (WO-00005)                │
│     ├─ Reserved: 5,000                                  │
│     ├─ Projected Qty: 25,000                           │
│     ├─ Safety Stock: 3,000                              │
│     ├─ Reorder Level: 8,000                            │
│     ├─ Net Requirement: 3,000 ⚠️                        │
│     ├─ BUT: MOQ = 10,000 → Order 10,000                │
│     ├─ Suggested Supplier: SUP-2025-00008              │
│     ├─ Unit Price: 800 VND                              │
│     ├─ Total Cost: 8,000,000 VND                        │
│     ├─ Lead Time: 8 days                                │
│     └─ Expected Delivery: 22/11/2025                    │
│                                                         │
└─────────────────────────────────────────────────────────┘

📊 DETAILED OUTPUTS
1. Purchase Plan Document (DocType)
pythonAPS Purchase Plan:
├─ planning_date: 09/11/2025
├─ planning_period: "December 2025"
├─ status: "Draft" / "Approved" / "Ordered"
├─ total_items: 5
├─ total_value: 185,500,000 VND
├─ created_by: Administrator
│
└─ items: [Child Table]
    ├─ Item 1:
    │   ├─ item_code: "CHAI-1L"
    │   ├─ forecasted_demand: 8,000
    │   ├─ current_stock: 6,000
    │   ├─ projected_qty: 7,000
    │   ├─ safety_stock: 1,000
    │   ├─ net_requirement: 2,000
    │   ├─ suggested_qty: 2,000
    │   ├─ suggested_supplier: "SUP-2025-00007"
    │   ├─ unit_price: 5,500
    │   ├─ total_cost: 11,000,000
    │   ├─ lead_time: 5
    │   ├─ required_date: "19/11/2025"
    │   └─ priority: "Medium"
    │
    ├─ Item 2: ...
    └─ Item 3: ...
```

---

### **2. Reorder Alert Report**

**Items CẦN ĐẶT HÀNG NGAY:**

| Item | Warehouse | Projected | Reorder Level | Shortage | Priority | Action |
|------|-----------|-----------|---------------|----------|----------|--------|
| CHAI-1L | WO-00005 | 7,000 | 2,500 | -1,000 | 🔴 HIGH | Order 2,000 |
| TUI-20X30 | WO-00005 | 25,000 | 8,000 | -3,000 | 🟡 MEDIUM | Order 10,000 |
| HOP-NHUA-1KG | WO-00006 | 3,400 | 1,500 | OK | 🟢 LOW | Monitor |

---

### **3. Supplier Purchase Summary**

**Group by Supplier:**
```
SUP-2025-00007 (Vietnam Packaging Solutions)
├─ CHAI-1L: 2,000 units × 5,500 = 11,000,000 VND
├─ Lead Time: 5 days
└─ Total: 11,000,000 VND

SUP-2025-00008 (Asian Polymer Corporation)
├─ TUI-20X30: 10,000 units × 800 = 8,000,000 VND
├─ Lead Time: 8 days
└─ Total: 8,000,000 VND

SUP-2025-00009 (Global Plastics Trading)
├─ TUI-30X40: 15,000 units × 1,000 = 15,000,000 VND
├─ Lead Time: 12 days
└─ Total: 15,000,000 VND

TOTAL ALL SUPPLIERS: 34,000,000 VND
```

---

### **4. Inventory Projection Timeline**

**Dự báo tồn kho 3 tháng tới:**
```
CHAI-1L Projection:
┌─────────────────────────────────────┐
│ Nov: 6,000 ─────┐                  │
│ Dec: 5,000      ├──── Sales        │
│ Jan: 3,000 ─────┘                  │
│                                     │
│ Expected Receipt (19/11): +2,000   │
│ After Receipt: 8,000               │
│                                     │
│ Feb: 6,000                         │
│ Mar: 4,000 ⚠️ Below Safety Stock   │
└─────────────────────────────────────┘
```

---

### **5. Cost Analysis**
```
┌─────────────────────────────────────────┐
│  PURCHASE COST BREAKDOWN                │
├─────────────────────────────────────────┤
│  Items Cost:        34,000,000 VND      │
│  Shipping (est.):    2,000,000 VND      │
│  Tax (10%):          3,400,000 VND      │
│  ─────────────────────────────────      │
│  TOTAL:             39,400,000 VND      │
│                                         │
│  Budget Available:  50,000,000 VND      │
│  Remaining:         10,600,000 VND ✅   │
└─────────────────────────────────────────┘
```

---

### **6. Action Items List**
```
📋 IMMEDIATE ACTIONS REQUIRED:

1. ⚠️ URGENT - Order CHAI-1L (2,000 units)
   - Contact: SUP-2025-00007
   - Budget: 11,000,000 VND
   - Deadline: Order by 14/11 to receive 19/11

2. 🔔 IMPORTANT - Order TUI-20X30 (10,000 units)
   - Contact: SUP-2025-00008
   - Budget: 8,000,000 VND
   - Deadline: Order by 14/11 to receive 22/11

3. ℹ️ MONITOR - CHAI-500ML
   - Current stock sufficient
   - Next review: 30/11/2025
```

---

## 🎯 TÓM LẠI - OUTPUTS CỦA SUPPLY PLANNING:

### **Documents được tạo:**
1. ✅ **APS Purchase Plan** (Main Output)
2. ✅ **APS Reorder Alert** (Report)
3. ✅ **Draft Purchase Orders** (Optional - ready to approve)

### **Reports được generate:**
1. 📊 Net Requirement Analysis
2. 📈 Inventory Projection
3. 💰 Cost Summary by Supplier
4. ⚠️ Stockout Risk Report
5. 📅 Delivery Timeline

### **Notifications/Alerts:**
1. 🔴 Critical: Items below safety stock
2. 🟡 Warning: Items approaching reorder level
3. 🟢 Info: Recommendations for optimization

---

## 💡 WORKFLOW SAU KHI CÓ KẾT QUẢ
```
Supply Planning Output
         ↓
    [Review & Approve]
         ↓
    ┌─────────────┐
    │ Convert to  │
    │ Purchase    │
    │ Orders      │
    └─────────────┘
         ↓
    Send to Suppliers
         ↓
    Track Deliveries
         ↓
    Goods Receipt
         ↓
    Update Inventory (APS Bin)s