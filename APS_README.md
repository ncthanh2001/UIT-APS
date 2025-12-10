# APS Module – README Documentation

## Giới thiệu
Hệ thống APS (Advanced Planning & Scheduling) hỗ trợ hoạch định & tối ưu toàn bộ chuỗi cung ứng – từ nhu cầu → cung ứng → sản xuất → giao hàng. Tài liệu này mô tả cấu trúc DocType của toàn bộ hệ thống, chức năng từng nhóm module và luồng nghiệp vụ tổng thể.

## Tổng quan số lượng DocType
| Module | Tổng | Document | Child Table | Single | Submittable |
|-------|------|----------|-------------|--------|-------------|
| APS Buying | 2 | 2 | 0 | 0 | 0 |
| APS Manufacturing | 31 | 13 | 18 | 0 | 4 |
| APS Selling | 7 | 3 | 4 | 0 | 2 |
| APS Setup | 6 | 6 | 0 | 0 | 0 |
| APS Stock | 10 | 6 | 4 | 0 | 2 |
| Dbiz APS | 54 | 21 | 31 | 2 | 12 |
| **Tổng cộng** | **110** | **51** | **57** | **2** | **10** |

## 1. APS Buying – Quản lý Mua hàng
### DocTypes
- **APS Materials Lead Time** – Quản lý thời gian chờ vật tư từ nhà cung cấp.
- **APS Supplier** – Quản lý thông tin nhà cung cấp.

## 2. APS Manufacturing – Quản lý Sản xuất
- **APS BOM** – Định mức nguyên vật liệu.
- **APS BOM Creator** – Công cụ tạo BOM nhanh.
- **APS Routing** – Định tuyến sản xuất.
- **APS Operation** – Các công đoạn sản xuất.
- **APS Work Order** – Lệnh sản xuất.
- **APS Job Card** – Phiếu công việc.
- **APS Work Center** – Trung tâm làm việc.
- **APS Workstation** – Trạm làm việc.
- **APS Workstation Type** – Phân loại trạm làm việc.
- **APS Capacity** – Năng lực sản xuất.
- **APS Production Plan** – Kế hoạch sản xuất.
- **APS Plant Floor** – Mặt bằng nhà máy.
- **APS Bin** – Vị trí lưu trữ.
- **APS Material Consumption Entry** – Ghi nhận tiêu hao vật tư.

## 3. APS Selling – Quản lý Bán hàng
- **APS Customer** – Khách hàng.
- **APS Sales Order** – Đơn hàng bán.
- **APS Sales Order History** – Lịch sử đơn hàng.

## 4. APS Setup – Cài đặt hệ thống
- **APS Customer Group**
- **APS Supplier Group**
- **APS Item Group**
- **APS UOM**
- **APS Employee**
- **APS Work Calendar**

## 5. APS Stock – Quản lý Kho
- **APS Item**
- **APS Warehouse**
- **APS Warehouse Type**
- **APS Stock On Hand**
- **APS Delivery Note**
- **APS Shipment History**

## 6. Dbiz APS – Lõi Advanced Planning & Scheduling

### 6.1 Demand Forecasting
- **APS Forecast Result**
- **APS Demand Forecast History**
- **APS ML Model**
- **APS Forecast Product/Customer Detail**
- **APS Forecast MDS Month**

### 6.2 MRP – Hoạch định nhu cầu vật tư
- **APS MRP Optimization**
- **APS MRP Planned Order**
- **APS MRP Inventory Projection**
- **APS MRP Demand Timeline**

### 6.3 Supply Planning
- **APS Supply Planning**
- **APS Supply Planning Run**
- **APS Supply Planning Result**
- **APS Purchase Recommendation**

### 6.4 Production Scheduling
- **APS Production Planning Result**
- **APS Production Planning History**
- **APS Schedule Optimization Result**
- **APS Schedule Optimization Config**
- **APS Schedule Optimization History**
- **APS Batch Schedule**

### 6.5 Phân tích & Cảnh báo
- **APS Risk Alert**
- **APS Planning Bottleneck**
- **APS Planning Material Shortage**
- **APS Scenario Comparison**

### 6.6 Cấu hình & Tiện ích
- **APS Settings**
- **APS Company**
- **APS Prompt Template**
- **APS Optimization Run Log**
- **APS Item Supplier / APS Supplier Item**

## Luồng nghiệp vụ APS
```
Sales Order → Demand Forecast → MRP Optimization  
       ↓  
MRP → Supply Planning → Purchase Recommendation  
       ↓  
Production Plan → Schedule Optimization → Work Order → Job Card  
       ↓  
Material Consumption → Delivery Note → Shipment History  
```

