# Các Chức Năng Trong Hệ Thống APS

## 1. Demand Forecast (Dự báo nhu cầu)

### Ý nghĩa
Dự đoán nhu cầu sản phẩm trong tương lai dựa trên dữ liệu lịch sử và xu hướng thị trường.

### Chức năng
- Phân tích dữ liệu bán hàng quá khứ
- Áp dụng các mô hình thống kê (Moving Average, Exponential Smoothing, ARIMA...)
- Xét các yếu tố: xu hướng, tính mùa vụ, chu kỳ, sự kiện đặc biệt
- Dự báo theo sản phẩm, khu vực, khách hàng
- Tạo nhiều kịch bản dự báo (conservative, moderate, aggressive)

### Output
Con số dự báo nhu cầu cho từng kỳ (tuần/tháng/quý)

---

## 2. MRP Optimization (Tối ưu hóa MRP)

### Ý nghĩa
Tính toán chính xác nhu cầu nguyên vật liệu, linh kiện cần thiết để sản xuất, có tối ưu hóa.

### Chức năng
- Phân khai BOM (Bill of Materials) để tính nhu cầu nguyên liệu
- Xét tồn kho hiện tại, đơn hàng đang về
- Tính toán thời điểm đặt hàng tối ưu (Order Point)
- Xác định số lượng đặt hàng tối ưu (EOQ - Economic Order Quantity)
- Cân đối giữa chi phí đặt hàng và chi phí tồn kho
- Xử lý lead time của nhà cung cấp
- Gộp đơn hàng để giảm chi phí

### Output
Danh sách nguyên vật liệu cần mua, số lượng, thời điểm

---

## 3. Supply Planning (Kế hoạch cung ứng)

### Ý nghĩa
Đảm bảo nguồn cung nguyên vật liệu/linh kiện đáp ứng đủ nhu cầu sản xuất.

### Chức năng
- Quản lý quan hệ với nhà cung cấp
- Đánh giá năng lực cung ứng của supplier
- Lập kế hoạch đặt hàng dài hạn và ngắn hạn
- Quản lý safety stock (tồn kho an toàn)
- Xử lý rủi ro đứt gãy chuỗi cung ứng
- Tối ưu chi phí vận chuyển và logistics
- Cân bằng giữa nhiều nguồn cung

### Output
Kế hoạch đặt hàng, phân bổ nhà cung cấp, lịch trình giao hàng

---

## 4. Production Planning (Kế hoạch sản xuất)

### Ý nghĩa
Xác định SẢN PHẨM gì, SẢN XUẤT BAO NHIÊU, KHI NÀO để đáp ứng nhu cầu.

### Chức năng
- Chuyển đổi forecast thành kế hoạch sản xuất cụ thể
- Cân bằng giữa nhu cầu và công suất khả dụng
- Xét đến:
  - Tồn kho thành phẩm hiện tại
  - Đơn hàng khách hàng đã xác nhận
  - Công suất máy móc
  - Nguồn nhân lực
  - Thời gian sản xuất
- Lập kế hoạch theo kỳ (tuần/tháng)
- Xác định sản lượng cho từng dây chuyền/nhà máy
- Quyết định Make-to-Stock vs Make-to-Order

### Output
Kế hoạch sản xuất tổng thể (Master Production Schedule - MPS)

---

## 5. Schedule Optimization (Tối ưu hóa lịch trình)

### Ý nghĩa
Lập LỊCH TRÌNH CHI TIẾT cho từng máy móc, công đoạn, thời điểm cụ thể để tối ưu hiệu quả.

### Chức năng
- Phân bổ lệnh sản xuất cho từng máy/dây chuyền
- Xác định trình tự sản xuất tối ưu
- Xét các ràng buộc:
  - Công suất máy móc (machine capacity)
  - Thời gian setup/changeover
  - Kỹ năng công nhân
  - Độ ưu tiên đơn hàng
  - Due date
- Tối ưu hóa mục tiêu:
  - Giảm thiểu thời gian chờ
  - Tối đa hóa throughput
  - Giảm setup time
  - Đảm bảo on-time delivery
- Xử lý các thay đổi real-time (máy hỏng, thiếu nguyên liệu...)
- Lập lịch chi tiết đến cấp độ giờ/phút

### Output
Lịch sản xuất chi tiết (Gantt chart) cho từng máy móc, công đoạn

---

## Mối Quan Hệ Giữa Các Chức Năng

```
Demand Forecast 
    ↓
Supply Planning ← → Production Planning
    ↓                      ↓
MRP Optimization    Schedule Optimization
```

### Luồng hoạt động

1. **Demand Forecast** tạo nhu cầu dự kiến
2. **Production Planning** quyết định sản xuất bao nhiêu
3. **MRP Optimization** tính nguyên liệu cần thiết
4. **Supply Planning** đảm bảo đủ nguyên liệu
5. **Schedule Optimization** lập lịch chi tiết thực thi

---

## Lưu Ý

Mỗi ngành nghề sẽ có trọng tâm khác nhau cho các chức năng này. Ví dụ:
- **Ngành thực phẩm**: Tập trung vào Demand Forecast (tính mùa vụ cao) và Schedule Optimization (hạn sử dụng)
- **Ngành ô tô**: Tập trung vào MRP Optimization (hàng nghìn linh kiện) và Supply Planning (nhiều supplier)
- **Ngành dược phẩm**: Tập trung vào Supply Planning (nguyên liệu đặc biệt) và Schedule Optimization (quy trình nghiêm ngặt)