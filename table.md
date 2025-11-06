# Danh Sách DocTypes - Hệ Thống APS

## Tổng Quan
- **Tổng số DocTypes**: 82
- **Modules**: APS Manufacturing, APS Selling, APS Stock, APS Buying, APS Setup, Dbiz Aps

---

## 1. APS Manufacturing (30 DocTypes)

### Normal DocTypes (11)
1. **APS BOM** - Bill of Materials
2. **APS BOM Creator** - Công cụ tạo BOM
3. **APS Capacity** - Quản lý công suất
4. **APS Job Card** - Thẻ công việc
5. **APS Operation** - Thao tác sản xuất
6. **APS Plant Floor** - Mặt bằng nhà máy
7. **APS Routing** - Quy trình sản xuất
8. **APS Work Order** - Lệnh sản xuất
9. **APS Workstation** - Trạm làm việc
10. **APS Workstation Type** - Loại trạm làm việc

### Child Tables (20)
1. **APS BOM Creator Item** - Chi tiết item trong BOM Creator
2. **APS BOM Item** - Nguyên vật liệu trong BOM
3. **APS BOM Operation** - Công đoạn trong BOM
4. **APS Job Card Item** - Item trong Job Card
5. **APS Job Card Operation** - Công đoạn trong Job Card
6. **APS Job Card Scheduled Time** - Lịch làm việc Job Card
7. **APS Job Card Scrap Item** - Phế liệu Job Card
8. **APS Job Card Time Log** - Nhật ký thời gian
9. **APS Sub Operation** - Công đoạn phụ
10. **APS Work Order Item** - Item trong Work Order
11. **APS Work Order Operation** - Công đoạn Work Order
12. **APS Workstation Working Hour** - Giờ làm việc trạm

---

## 2. APS Selling (8 DocTypes)

### Normal DocTypes (3)
1. **APS Customer** - Khách hàng
2. **APS Sales Order** - Đơn hàng bán
3. **APS Sales Order History** - Lịch sử đơn hàng

### Child Tables (5)
1. **APS Production Planning Item** - Item lập kế hoạch sản xuất
2. **APS Production Planning SO** - Sales Order trong kế hoạch
3. **APS Sales Order History Item** - Chi tiết lịch sử đơn hàng
4. **APS Sales Order Item** - Chi tiết đơn hàng

---

## 3. APS Stock (10 DocTypes)

### Normal DocTypes (4)
1. **APS Delivery Note** - Phiếu giao hàng
2. **APS Item** - Sản phẩm/Vật tư
3. **APS Shipment History** - Lịch sử giao hàng
4. **APS Stock On Hand** - Tồn kho
5. **APS Warehouse** - Kho
6. **APS Warehouse Type** - Loại kho

### Child Tables (4)
1. **APS Delivery Note Item** - Chi tiết phiếu giao hàng
2. **APS Packed Item** - Sản phẩm đóng gói
3. **APS Shipment History Item** - Chi tiết lịch sử giao hàng
4. **APS UOM Conversion Detail** - Chi tiết chuyển đổi đơn vị

---

## 4. APS Buying (2 DocTypes)

### Normal DocTypes (2)
1. **APS Materials Lead Time** - Thời gian đặt hàng nguyên vật liệu
2. **APS Supplier** - Nhà cung cấp

---

## 5. APS Setup (6 DocTypes)

### Normal DocTypes (6)
1. **APS Customer Group** - Nhóm khách hàng
2. **APS Employee** - Nhân viên
3. **APS Item Group** - Nhóm sản phẩm
4. **APS Supplier Group** - Nhóm nhà cung cấp
5. **APS UOM** - Đơn vị đo lường
6. **APS Work Calendar** - Lịch làm việc

---

## 6. Dbiz APS - Core Planning Module (26 DocTypes)

### Planning & Forecasting (8 Normal DocTypes)
1. **APS Cateogry** - Phân loại
2. **APS Demand Forecast History** - Lịch sử dự báo nhu cầu
3. **APS Forecast Result** - Kết quả dự báo
4. **APS MRP Optimization** - Tối ưu hóa MRP
5. **APS Production Planning History** - Lịch sử kế hoạch sản xuất
6. **APS Production Planning Result** - Kết quả kế hoạch sản xuất
7. **APS Schedule Optimization History** - Lịch sử tối ưu lịch trình
8. **APS Supplier Item** - Sản phẩm từ nhà cung cấp
9. **APS Supply Planning** - Kế hoạch cung ứng
10. **APS Supply Planning Result** - Kết quả kế hoạch cung ứng
11. **APS Supply Planning Run** - Chạy kế hoạch cung ứng

### Child Tables - Planning Details (17)
1. **APS Demand Forecast History Item** - Chi tiết dự báo
2. **APS Forecast Customer Detail** - Chi tiết dự báo theo khách hàng
3. **APS Forecast MDS Month** - Dự báo theo tháng (MDS)
4. **APS Forecast Product Detail** - Chi tiết dự báo sản phẩm
5. **APS Forecast Seasonality Factor** - Hệ số mùa vụ
6. **APS MRP Demand Timeline** - Timeline nhu cầu MRP
7. **APS MRP Inventory Projection** - Dự báo tồn kho MRP
8. **APS MRP Optimization Item** - Chi tiết tối ưu MRP
9. **APS Planning Bottleneck** - Điểm nghẽn trong kế hoạch
10. **APS Planning Daily Summary** - Tổng hợp hàng ngày
11. **APS Planning Material Shortage** - Thiếu hụt nguyên vật liệu
12. **APS Planning Timeline** - Timeline kế hoạch
13. **APS Planning Workstation Util** - Sử dụng trạm làm việc
14. **APS Production Planning Constraint** - Ràng buộc kế hoạch sản xuất
15. **APS Production Planning History Item** - Chi tiết lịch sử kế hoạch
16. **APS Production Planning Item Result** - Kết quả item trong kế hoạch
17. **APS Production Planning Material Requirement** - Yêu cầu nguyên vật liệu
18. **APS Production Planning Timeline** - Timeline sản xuất
19. **APS Production Planning Workstation Schedule** - Lịch trình trạm làm việc
20. **APS Purchase Recommendation** - Đề xuất mua hàng
21. **APS Supply Constraint** - Ràng buộc cung ứng
22. **APS Supply Planning Detail** - Chi tiết kế hoạch cung ứng
23. **APS Supply Planning Run Item** - Item trong chạy kế hoạch
24. **APS Supply Planning Timeline** - Timeline cung ứng

---

## Phân Loại Theo Chức Năng

### 📦 Master Data (19)
- Items, Customers, Suppliers, Warehouses, UOM, Groups, Calendar, Employee

### 🏭 Manufacturing (30)
- BOM, Routing, Operations, Work Orders, Job Cards, Workstations, Capacity

### 📊 Planning & Optimization (26)
- Forecasting, MRP, Production Planning, Supply Planning, Schedule Optimization

### 📈 Sales & Distribution (8)
- Sales Orders, Delivery Notes, Shipments

### 🔄 Inventory Management (4)
- Stock On Hand, Warehouse Management

### 📋 Historical Tracking (5)
- Sales Order History, Forecast History, Planning History, Shipment History

---

## Tỷ Lệ DocType

- **Normal DocTypes**: 32 (39%)
- **Child Tables**: 50 (61%)

## Modules Chính

1. **APS Manufacturing**: 30 (37%)
2. **Dbiz APS**: 26 (32%)
3. **APS Stock**: 10 (12%)
4. **APS Selling**: 8 (10%)
5. **APS Setup**: 6 (7%)
6. **APS Buying**: 2 (2%)
