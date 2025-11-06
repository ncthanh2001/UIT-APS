# Schedule Optimization - Input & Output Specification

## 📥 INPUT - Dữ Liệu Đầu Vào

### 1. Sales Orders & Demands (Đơn Hàng & Nhu Cầu)

**DocType**: `APS Sales Order` và child table `APS Sales Order Item`

```
Input Fields:
├── Sales Order Information
│   ├── customer (Khách hàng)
│   ├── delivery_date (Ngày giao hàng - DEADLINE)
│   ├── priority (Độ ưu tiên: High/Medium/Low)
│   └── order_status (Trạng thái đơn)
│
└── Sales Order Items
    ├── item_code (Mã sản phẩm)
    ├── qty (Số lượng)
    ├── delivery_date (Ngày giao từng item)
    ├── reserved_qty (Đã đặt trước)
    └── production_item (Item cần sản xuất)
```

**Từ**: `APS Production Planning SO` (Child Table)
- Danh sách các SO cần lập kế hoạch
- Link đến các Sales Orders
- Số lượng và thời hạn

---

### 2. Bill of Materials & Routing (BOM & Quy Trình)

**DocType**: `APS BOM`, `APS Routing`

```
BOM Input (APS BOM):
├── item (Sản phẩm thành phẩm)
├── quantity (Số lượng output)
│
├── APS BOM Item (Child Table)
│   ├── item_code (Nguyên vật liệu)
│   ├── qty (Số lượng cần)
│   ├── stock_uom (Đơn vị)
│   └── lead_time_days (Thời gian lead)
│
└── APS BOM Operation (Child Table)
    ├── operation (Tên công đoạn)
    ├── workstation (Trạm làm việc)
    ├── time_in_mins (Thời gian thực hiện)
    ├── operating_cost (Chi phí vận hành)
    └── sequence_id (Thứ tự công đoạn)

Routing Input (APS Routing):
├── routing (Tên routing)
└── operations[] (Danh sách công đoạn theo thứ tự)
    ├── operation_name
    ├── workstation
    ├── time_in_mins
    ├── hour_rate
    └── dependencies (Phụ thuộc công đoạn nào)
```

---

### 3. Workstation & Capacity (Trạm Làm Việc & Công Suất)

**DocType**: `APS Workstation`, `APS Capacity`

```
Workstation Input:
├── workstation_name (Tên trạm)
├── workstation_type (Loại trạm)
├── production_capacity (Công suất/giờ)
├── hour_rate_electricity (Chi phí điện/giờ)
├── hour_rate_labour (Chi phí nhân công/giờ)
├── hour_rate_rent (Chi phí thuê/giờ)
│
└── APS Workstation Working Hour (Child Table)
    ├── enabled (Có hoạt động không)
    ├── start_time (Giờ bắt đầu ca)
    ├── end_time (Giờ kết thúc ca)
    ├── working_days[] (Thứ 2-CN)
    └── break_start/break_end (Giờ nghỉ)

Capacity Input (APS Capacity):
├── workstation (Trạm)
├── date (Ngày)
├── available_capacity (Công suất khả dụng)
├── planned_capacity (Đã lập kế hoạch)
└── remaining_capacity (Còn lại)
```

---

### 4. Work Calendar (Lịch Làm Việc)

**DocType**: `APS Work Calendar`

```
Calendar Input:
├── calendar_name (Tên lịch)
├── working_days[] (Ngày làm việc: Mon-Sun)
├── holidays[] (Ngày nghỉ lễ)
├── start_time (Giờ bắt đầu)
├── end_time (Giờ kết thúc)
└── shifts[] (Ca làm việc nếu có)
```

---

### 5. Material Availability (Tồn Kho Hiện Tại)

**DocType**: `APS Stock On Hand`

```
Stock Input:
├── item_code (Mã sản phẩm/NVL)
├── warehouse (Kho)
├── actual_qty (Số lượng thực tế)
├── reserved_qty (Đã đặt trước)
├── projected_qty (Dự kiến)
├── planned_qty (Đã lập kế hoạch)
└── available_qty (actual - reserved)
```

---

### 6. Existing Work Orders (Lệnh Sản Xuất Hiện Tại)

**DocType**: `APS Work Order`

```
Work Order Input:
├── production_item (Sản phẩm)
├── qty (Số lượng)
├── planned_start_date (Ngày bắt đầu dự kiến)
├── planned_end_date (Ngày kết thúc dự kiến)
├── status (Draft/In Progress/Completed)
├── bom_no (BOM sử dụng)
│
└── APS Work Order Operation (Child Table)
    ├── operation (Công đoạn)
    ├── workstation (Trạm)
    ├── time_in_mins (Thời gian)
    ├── completed_qty (Đã hoàn thành)
    └── status (Pending/In Progress/Completed)
```

---

### 7. Constraints & Parameters (Ràng Buộc & Tham Số)

**DocType**: `APS Production Planning Constraint` (Child Table)

```
Constraint Input:
├── constraint_type (Loại ràng buộc)
│   ├── "Max Lead Time" (Thời gian tối đa)
│   ├── "Min Batch Size" (Batch tối thiểu)
│   ├── "Setup Time Required" (Cần thời gian setup)
│   ├── "Sequence Dependency" (Phụ thuộc thứ tự)
│   └── "Resource Availability" (Khả dụng tài nguyên)
│
├── constraint_value (Giá trị)
├── applies_to (Áp dụng cho: item/workstation/operation)
└── priority_level (Mức độ ưu tiên)

Planning Parameters:
├── optimization_objective (Mục tiêu tối ưu)
│   ├── "Minimize Makespan" (Giảm thời gian hoàn thành)
│   ├── "Maximize Utilization" (Tối đa hóa sử dụng)
│   ├── "Minimize Tardiness" (Giảm trễ deadline)
│   └── "Balance Load" (Cân bằng tải)
│
├── planning_horizon (Khoảng thời gian lập kế hoạch)
├── scheduling_method (Phương pháp: Forward/Backward)
└── allow_overtime (Cho phép làm thêm giờ)
```

---

### 8. Supply Planning Data (Kế Hoạch Cung Ứng)

**DocType**: `APS Supply Planning` và related tables

```
Supply Input:
├── supplier_lead_times (Thời gian NCC)
├── minimum_order_qty (Số lượng đặt tối thiểu)
├── safety_stock_levels (Mức tồn kho an toàn)
└── procurement_schedule (Lịch mua hàng)
```

---

## 📤 OUTPUT - Kết Quả Đầu Ra

### 1. Optimized Production Schedule (Lịch Trình Tối Ưu)

**DocType**: `APS Production Planning Result`

```
Main Output:
├── name (ID kết quả)
├── planning_date (Ngày lập kế hoạch)
├── from_date (Từ ngày)
├── to_date (Đến ngày)
├── status (Draft/Optimized/Approved/Cancelled)
├── optimization_score (Điểm tối ưu: 0-100)
├── total_makespan (Tổng thời gian hoàn thành)
├── average_utilization (Tỷ lệ sử dụng TB)
├── on_time_delivery_rate (% giao đúng hạn)
└── total_cost (Tổng chi phí)
```

---

### 2. Production Planning Items (Chi Tiết Sản Phẩm)

**Child Table**: `APS Production Planning Item Result`

```
Item Schedule Output:
├── item_code (Mã sản phẩm)
├── sales_order (Đơn hàng gốc)
├── required_qty (Số lượng cần)
├── planned_qty (Số lượng kế hoạch)
├── start_date (Ngày bắt đầu)
├── end_date (Ngày kết thúc)
├── delivery_date (Ngày giao hàng)
├── slack_time (Thời gian dư - buffer)
├── is_on_time (Có đúng hạn không)
├── work_order (Link đến Work Order tạo ra)
└── priority_score (Điểm ưu tiên)
```

---

### 3. Workstation Schedule (Lịch Trình Từng Trạm)

**Child Table**: `APS Production Planning Workstation Schedule`

```
Workstation Schedule Output:
├── workstation (Tên trạm)
├── operation (Công đoạn)
├── work_order (Lệnh sản xuất)
├── item_code (Sản phẩm)
├── sequence (Thứ tự thực hiện)
├── planned_start_datetime (Thời gian bắt đầu)
├── planned_end_datetime (Thời gian kết thúc)
├── duration_mins (Thời lượng phút)
├── setup_time_mins (Thời gian setup)
├── utilization_percent (% sử dụng)
└── status (Scheduled/In Progress/Completed)
```

---

### 4. Timeline Visualization (Timeline Tổng Thể)

**Child Table**: `APS Production Planning Timeline`

```
Timeline Output:
├── date (Ngày)
├── hour (Giờ)
├── workstation (Trạm)
├── operation (Công đoạn)
├── work_order (Lệnh sản xuất)
├── item_code (Sản phẩm)
├── status (Idle/Running/Setup/Maintenance)
└── load_percentage (% tải: 0-100%)
```

---

### 5. Bottleneck Analysis (Phân Tích Điểm Nghẽn)

**Child Table**: `APS Planning Bottleneck`

```
Bottleneck Output:
├── workstation (Trạm nghẽn)
├── date (Ngày xảy ra)
├── bottleneck_severity (Mức độ: High/Medium/Low)
├── utilization_percent (% sử dụng - thường >95%)
├── queue_time_mins (Thời gian chờ)
├── affected_orders[] (Các đơn bị ảnh hưởng)
├── suggested_action (Đề xuất hành động)
│   ├── "Add Overtime"
│   ├── "Use Alternative Workstation"
│   ├── "Reschedule Orders"
│   └── "Increase Capacity"
└── estimated_delay_hours (Ước tính trễ)
```

---

### 6. Workstation Utilization Report (Báo Cáo Sử Dụng Trạm)

**Child Table**: `APS Planning Workstation Util`

```
Utilization Output:
├── workstation (Trạm)
├── date (Ngày)
├── total_available_mins (Tổng phút khả dụng)
├── scheduled_mins (Phút đã lập lịch)
├── idle_mins (Phút rảnh)
├── utilization_percent (% = scheduled/available)
├── efficiency_score (Điểm hiệu suất)
└── recommendation (Khuyến nghị)
```

---

### 7. Material Requirements Timeline (Timeline Yêu Cầu NVL)

**Child Table**: `APS Production Planning Material Requirement`

```
Material Timeline Output:
├── item_code (Mã NVL)
├── warehouse (Kho)
├── required_date (Ngày cần)
├── required_qty (Số lượng cần)
├── available_qty (Số lượng có)
├── shortage_qty (Thiếu hụt)
├── work_order (WO cần NVL này)
├── status (Available/Short/On Order)
└── action_required (Hành động cần thiết)
```

---

### 8. Material Shortage Alert (Cảnh Báo Thiếu Hụt)

**Child Table**: `APS Planning Material Shortage`

```
Shortage Output:
├── item_code (NVL thiếu)
├── required_date (Ngày cần)
├── shortage_qty (Số lượng thiếu)
├── affected_work_orders[] (WO bị ảnh hưởng)
├── severity (Critical/High/Medium/Low)
├── suggested_procurement_date (Ngày nên đặt hàng)
└── alternative_items[] (NVL thay thế nếu có)
```

---

### 9. Daily Summary (Tổng Hợp Hàng Ngày)

**Child Table**: `APS Planning Daily Summary`

```
Daily Summary Output:
├── date (Ngày)
├── total_work_orders (Tổng WO trong ngày)
├── total_operations (Tổng công đoạn)
├── total_production_mins (Tổng phút sản xuất)
├── average_utilization (% sử dụng TB)
├── on_time_orders (Số đơn đúng hạn)
├── late_orders (Số đơn trễ)
├── material_shortages (Số NVL thiếu)
└── bottleneck_count (Số điểm nghẽn)
```

---

### 10. Purchase Recommendations (Đề Xuất Mua Hàng)

**Child Table**: `APS Purchase Recommendation`

```
Purchase Output:
├── item_code (NVL cần mua)
├── supplier (Nhà cung cấp đề xuất)
├── required_date (Ngày cần có hàng)
├── order_date (Ngày nên đặt)
├── qty_to_order (Số lượng đặt)
├── estimated_cost (Chi phí ước tính)
├── lead_time_days (Thời gian giao hàng)
└── priority (Urgent/High/Normal)
```

---

### 11. Schedule Optimization History (Lịch Sử Tối Ưu)

**DocType**: `APS Schedule Optimization History`

```
History Output:
├── optimization_run_id (ID lần chạy)
├── run_datetime (Thời gian chạy)
├── optimization_method (Thuật toán sử dụng)
├── execution_time_seconds (Thời gian thực thi)
├── iterations (Số vòng lặp)
├── initial_score (Điểm ban đầu)
├── final_score (Điểm sau tối ưu)
├── improvement_percent (% cải thiện)
├── status (Success/Failed/Partial)
├── input_parameters (Tham số đầu vào)
└── result_link (Link đến kết quả)
```

---

## 🔄 Quy Trình Xử Lý Input → Output

```
[STEP 1: Data Collection]
├── Thu thập Sales Orders
├── Lấy BOM & Routing
├── Đọc Workstation Capacity
├── Kiểm tra Stock On Hand
└── Load Constraints

[STEP 2: Data Validation]
├── Validate BOM integrity
├── Check resource availability
├── Verify material availability
└── Validate date constraints

[STEP 3: Optimization Algorithm]
├── Initialize population/solution space
├── Apply constraints
├── Calculate objective function
├── Iterate to find optimal solution
├── Apply genetic/heuristic algorithms
└── Validate feasibility

[STEP 4: Generate Outputs]
├── Create Production Planning Result
├── Generate Workstation Schedules
├── Calculate Timeline
├── Identify Bottlenecks
├── Calculate Utilization
├── Generate Material Requirements
└── Create Purchase Recommendations

[STEP 5: Save & Present]
├── Save to APS Production Planning Result
├── Update child tables
├── Generate Gantt Chart
├── Create reports
└── Send notifications
```

---

## 📊 Ví Dụ Cụ Thể

### Input Example:
```
Sales Orders:
- SO-001: 100 units "Product A", delivery: 2025-11-15
- SO-002: 50 units "Product B", delivery: 2025-11-20

Workstations:
- WS-CNC-01: 8 hours/day, efficiency 85%
- WS-MILL-01: 8 hours/day, efficiency 90%

Current Stock:
- Raw Material X: 500 units
- Raw Material Y: 200 units (need 300!)

BOM Product A:
- Operation 1: CNC (30 mins) → MILL (20 mins)
- Materials: 2x Material X, 3x Material Y
```

### Output Example:
```
Optimized Schedule:
├── SO-001 Start: 2025-11-10 08:00
│   ├── WS-CNC-01: 2025-11-10 08:00-13:00
│   └── WS-MILL-01: 2025-11-10 13:30-16:00
│
├── SO-002 Start: 2025-11-12 08:00
│   └── ...
│
├── Material Shortage Alert:
│   └── Material Y: Need 100 more units by 2025-11-09
│
├── Utilization:
│   ├── WS-CNC-01: 92%
│   └── WS-MILL-01: 78%
│
└── Bottleneck: WS-CNC-01 on 2025-11-10
    └── Suggestion: Add overtime 2 hours
```

---

## 🎯 Key Performance Indicators (KPIs)

Output còn bao gồm các KPI:

1. **Makespan**: Tổng thời gian hoàn thành tất cả orders
2. **Tardiness**: Tổng thời gian trễ deadline
3. **Utilization**: % sử dụng trung bình các workstation
4. **On-Time Delivery Rate**: % đơn giao đúng hạn
5. **Material Shortage Rate**: % NVL thiếu
6. **Total Cost**: Tổng chi phí sản xuất
7. **Optimization Score**: Điểm tổng hợp (0-100)

---

## 💡 Lưu Ý Quan Trọng

### Input Requirements:
- ✅ BOM phải hoàn chỉnh với routing
- ✅ Workstation phải có lịch làm việc
- ✅ Material availability phải cập nhật
- ✅ Sales Order phải có delivery date

### Output Usage:
- 📋 Production Planning Result → Approval workflow
- 🏭 Workstation Schedule → Shop floor execution
- 📦 Material Requirements → Purchase planning
- 📊 Utilization Report → Capacity planning
- ⚠️ Bottleneck Analysis → Process improvement