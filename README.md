[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=23574068&assign26ai.phutd@vnu.edu.vnment_repo_type=AssignmentRepo)
# Day 10 Lab: Data Pipeline & Data Observability

**Student Email:** nhinnhuphu@gmail.com
**Student ID** 2A202600322
**Name:** Trinh Dac Phu

---

## Mo ta

Nhiệm vụ:
Extract: Đọc dữ liệu từ file JSON (raw_data.json)
Validate: Kiểm tra chất lượng — loại bỏ các record có giá ≤ 0 hoặc category rỗng
Transform:
Chuẩn hóa category thành Title Case
Tính discounted_price (giảm 10%)
Thêm timestamp processed_at
Load: Lưu dữ liệu đã xử lý ra file CSV (processed_data.csv)
Đã hoàn thành:
✅ Implement hàm extract() — đọc JSON và xử lý lỗi
✅ Implement hàm validate() — kiểm tra dữ liệu & đếm số lượng records hợp lệ / lỗi
✅ Implement hàm transform() — tạo DataFrame, tính discount và chuẩn hóa category
✅ Implement hàm load() — lưu kết quả ra CSV
✅ Logging: In ra số lượng records processed / dropped

---

## Cach chay (How to Run)

### Prerequisites
```bash
pip install pandas
```

### Chay ETL Pipeline
```bash
python solution.py
```

### Chay Agent Simulation (Stress Test)
```bash
python agent_simulation.py
```
Thi nghiem nay so sanh performance cua pipeline voi clean data vs garbage data.

---

## Cau truc thu muc

```
├── solution.py              # ETL Pipeline script
├── processed_data.csv       # Output cua pipeline
├── experiment_report.md     # Bao cao thi nghiem
└── README.md                # File nay
```

---

## Ket qua

**Pipeline Execution Summary:**
- Total records extracted: 5
- Valid records: 3 ✅
- Records dropped: 2 ❌ (do gia <= 0 hoac category rong)
- Final output: 3 records saved to processed_data.csv

**Transformations Applied:**
- Discounted price calculated (10% off)
- Category converted to Title Case
- Timestamp added (processed_at)
