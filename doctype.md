📘 APS Module – README Documentation
🏭 Giới thiệu

Hệ thống APS (Advanced Planning & Scheduling) hỗ trợ hoạch định & tối ưu toàn bộ chuỗi cung ứng – từ nhu cầu → cung ứng → sản xuất → giao hàng.
Tài liệu này mô tả cấu trúc DocType của toàn bộ hệ thống, chức năng từng nhóm module và luồng nghiệp vụ tổng thể.

📂 Tổng quan số lượng DocType
Module	Tổng	Document	Child Table	Single	Submittable
APS Buying	2	2	0	0	0
APS Manufacturing	31	13	18	0	4
APS Selling	7	3	4	0	2
APS Setup	6	6	0	0	0
APS Stock	10	6	4	0	2
Dbiz APS	54	21	31	2	12
Tổng cộng	110	51	57	2	10
🛒 1. APS Buying – Quản lý Mua hàng
DocTypes
DocType	Chức năng
APS Materials Lead Time	Quản lý thời gian chờ vật tư (lead time) từ nhà cung cấp – phục vụ tính toán kế hoạch mua hàng.
APS Supplier	Quản lý thông tin nhà cung cấp trong hệ thống APS.
🏗️ 2. APS Manufacturing – Quản lý Sản xuất
DocType	Chức năng
APS BOM	Định mức nguyên vật liệu (Bill of Materials).
APS BOM Creator	Công cụ hỗ trợ tạo BOM nhanh.
APS Routing	Định tuyến sản xuất – danh sách công đoạn cần thực hiện.
APS Operation	Danh mục các công đoạn sản xuất.
APS Work Order	Lệnh sản xuất chính thức.
APS Job Card	Phiếu công việc cho từng công đoạn của Work Order.
APS Work Center	Trung tâm làm việc – nhóm máy móc/nhân công.
APS Workstation	Trạm làm việc hoặc máy móc cụ thể.
APS Workstation Type	Phân loại trạm làm việc.
APS Capacity	Quản lý năng lực sản xuất.
APS Production Plan	Kế hoạch sản xuất tổng thể.
APS Plant Floor	Quản lý mặt bằng nhà máy.
APS Bin	Quản lý vị trí lưu trữ (bin).
APS Material Consumption Entry	Ghi nhận tiêu hao nguyên vật liệu trong sản xuất.

Ngoài ra có 18 child table hỗ trợ các chi tiết như BOM Item, Operation, Time Log, Scrap Item, Work Order Item,...

🛍️ 3. APS Selling – Quản lý Bán hàng
DocType	Chức năng
APS Customer	Quản lý thông tin khách hàng.
APS Sales Order	Đơn hàng bán (submittable).
APS Sales Order History	Ghi nhận lịch sử thay đổi đơn hàng.
⚙️ 4. APS Setup – Cài đặt hệ thống
DocType	Chức năng
APS Customer Group	Nhóm khách hàng.
APS Supplier Group	Nhóm nhà cung cấp.
APS Item Group	Nhóm hàng hóa.
APS UOM	Đơn vị tính.
APS Employee	Nhân viên sử dụng trong APS.
APS Work Calendar	Lịch làm việc của nhà máy.
📦 5. APS Stock – Quản lý Kho
DocType	Chức năng
APS Item	Quản lý vật tư & sản phẩm.
APS Warehouse	Danh mục kho.
APS Warehouse Type	Phân loại kho (NVL, bán thành phẩm, thành phẩm…).
APS Stock On Hand	Tồn kho hiện tại.
APS Delivery Note	Phiếu xuất kho / giao hàng (submittable).
APS Shipment History	Lịch sử giao hàng.
🧠 6. Dbiz APS – Lõi Advanced Planning & Scheduling
6.1. 🔮 Demand Forecasting – Dự báo nhu cầu
DocType	Chức năng
APS Forecast Result	Kết quả dự báo nhu cầu.
APS Demand Forecast History	Lịch sử & độ chính xác dự báo.
APS ML Model	Mô hình Machine Learning phục vụ dự báo.
APS Forecast Product Detail / Customer Detail	Chi tiết dự báo theo khách hàng và sản phẩm.
APS Forecast MDS Month	Dự báo theo tháng.
6.2. 📊 MRP – Hoạch định nhu cầu vật tư
DocType	Chức năng
APS MRP Optimization	Thuật toán tối ưu nhu cầu vật tư.
APS MRP Planned Order	Đề xuất mua/sản xuất.
APS MRP Inventory Projection	Dự báo tồn kho.
APS MRP Demand Timeline	Timeline nhu cầu NVL.
6.3. 🚚 Supply Planning – Hoạch định cung ứng
DocType	Chức năng
APS Supply Planning	Hoạch định cung ứng tổng thể.
APS Supply Planning Run	Lần chạy hoạch định cung ứng.
APS Supply Planning Result	Kết quả hoạch định.
APS Purchase Recommendation	Đề xuất mua hàng.
6.4. 🕒 Production Scheduling – Lập lịch sản xuất
DocType	Chức năng
APS Production Planning Result	Kết quả lập kế hoạch sản xuất.
APS Production Planning History	Lịch sử lập kế hoạch.
APS Schedule Optimization Result	Kết quả tối ưu hóa lịch sản xuất.
APS Schedule Optimization Config	Cấu hình thuật toán tối ưu.
APS Schedule Optimization History	Lịch sử tối ưu hóa.
APS Batch Schedule	Lập lịch theo batch.
6.5. ⚠️ Phân tích & Cảnh báo
DocType	Chức năng
APS Risk Alert	Cảnh báo rủi ro (tiến độ, thiếu NVL…).
APS Planning Bottleneck	Xác định nút thắt trong sản xuất.
APS Planning Material Shortage	Thiếu nguyên vật liệu.
APS Scenario Comparison	So sánh nhiều kịch bản kế hoạch.
6.6. ⚙️ Cấu hình & Tiện ích
DocType	Chức năng
APS Settings	Cài đặt hệ thống APS.
APS Company	Thông tin công ty.
APS Prompt Template	Template prompt cho AI.
APS Optimization Run Log	Log các lần chạy tối ưu.
APS Item Supplier / APS Supplier Item	Mapping giữa Item và NCC.