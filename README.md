# CPU Scheduling Algorithm Simulator & Comparison

โปรแกรมจำลองและเปรียบเทียบประสิทธิภาพการทำงานของ **CPU Scheduler** ในระบบปฏิบัติการ (Operating System) พัฒนาด้วยภาษา **Python 3** ทำหน้าที่รับข้อมูล Process (PID, Arrival Time, Burst Time, Priority) แล้วคำนวณการจัดลำดับการทำงานของ CPU ตาม Scheduling Algorithms ต่างๆ พร้อมแสดงผลลัพธ์เชิงสถิติผ่านตารางสรุป และแสดงแผนภาพ **Gantt Chart** ด้วย `matplotlib`

---

## 📌 คุณสมบัติของโปรแกรม (Features)

1. **รองรับ 4 Scheduling Algorithms หลัก:**
   * **FCFS (First Come First Served):** จัดคิวตามลำดับเวลาที่มาถึง (Arrival Time) ใครมาก่อนได้ทำก่อน
   * **SJF (Shortest Job First - Non-Preemptive):** เลือก Process ที่มี Burst Time สั้นที่สุดในกลุ่ม Process ที่มาถึงระบบแล้ว
   * **Priority Scheduling (Non-Preemptive):** เลือก Process ที่มีลำดับความสำคัญสูงสุดก่อน (ตัวเลข Priority น้อย = ความสำคัญสูง)
   * **Round Robin (RR):** สลับกันทำงานตามช่วงเวลา (Time Quantum) โดยใช้ Ready Queue หมุนเวียน
2. **ระบบเมนู Interactive & ชุดข้อมูลทดสอบ (Test Cases):**
   * **[1] Sample Case:** ชุดข้อมูล 3 Process ตามตัวอย่างในเอกสารข้อกำหนด (หน้า 3)
   * **[2] Complex Case:** ชุดข้อมูล 5 Process ที่มี Burst Time และ Priority หลากหลาย
   * **[3] CPU Idle Case:** ชุดข้อมูลทดสอบกรณีมีช่วงเวลา CPU ว่าง (Arrival Time Gaps)
   * **[4] Convoy Effect Case:** ชุดข้อมูลทดสอบผลกระทบของงานขนาดใหญ่ต่อ FCFS เปรียบเทียบกับ SJF และ Round Robin
   * **[5] Custom Input:** ระบบให้ผู้ใช้ป้อนข้อมูล Process เองผ่าน Terminal พร้อมการตรวจสอบข้อมูล (Input Validation)
   * **[6] Batch Benchmark:** รันการทดสอบทุก Test Case อัตโนมัติในคำสั่งเดียว
3. **การคำนวณสถิติอัตโนมัติ:**
   * Completion Time (CT): เวลาที่แต่ละ Process ทำงานเสร็จสิ้น
   * Turnaround Time ($TAT = CT - \text{Arrival Time}$): เวลาตั้งแต่ Process เข้าสู่ระบบจนทำงานเสร็จ
   * Waiting Time ($WT = TAT - \text{Burst Time}$): เวลาที่ Process ต้องรออยู่ใน Ready Queue
   * Average Waiting Time (Avg WT) และ Average Turnaround Time (Avg TAT)
4. **การแสดงผลเชิงทัศน์ (Visualization):**
   * วาด **Gantt Chart** เปรียบเทียบทั้ง 4 อัลกอริทึมในหน้าต่างเดียวกัน
   * **เรียงลำดับ Process จากบนลงล่าง (P1 ถึง PN) อย่างสม่ำเสมอทุกกราฟ** ไม่สลับตำแหน่งกัน
   * **กำหนดสีประจำตัว Process คงที่** เพื่อให้อ่านและเปรียบเทียบข้ามอัลกอริทึมได้ง่าย
   * บันทึกภาพลงไฟล์ `.png` อัตโนมัติ (รองรับการใช้งานบน Ubuntu หรือเครื่อง Server ที่ไม่มี GUI)

---

## 📁 โครงสร้างโปรเจกต์ (Project Structure)

```text
os-mini-project-CPU-Scheduling-Algorithm-Comparison-and-Simulation/
├── .gitignore
├── README.md
└── cpu-scheduler-sim/
    ├── models/
    │   ├── __init__.py
    │   └── process.py           # Class Process เก็บข้อมูลและคำนวณสถิติ
    ├── algorithms/
    │   ├── __init__.py
    │   ├── fcfs.py              # First-Come First-Served
    │   ├── sjf.py               # Shortest Job First (Non-Preemptive)
    │   ├── priority.py          # Priority Scheduling (Non-Preemptive)
    │   └── round_robin.py       # Round Robin Scheduling
    ├── utils/
    │   ├── __init__.py
    │   ├── metrics.py           # ฟังก์ชันคำนวณสถิติและพิมพ์ตารางเปรียบเทียบ
    │   └── visualization.py     # ฟังก์ชันวาดและบันทึก Gantt Chart
    ├── test_cases.py            # รวมชุดข้อมูลทดสอบ และฟังก์ชัน Custom Input
    ├── main.py                  # ไฟล์หลักสำหรับรันโปรแกรมพร้อมเมนูควบคุม
    └── requirements.txt         # รายการ Dependencies (matplotlib)
```

---

## 🛠️ การติดตั้งและการเตรียมระบบ (Installation)

### 1. Requirements

* **Python:** เวอร์ชัน 3.8 ขึ้นไป
* **Library:** `matplotlib`

### 2. ขั้นตอนการติดตั้ง Dependencies

เปิด Terminal หรือ Command Prompt ในโฟลเดอร์โปรเจกต์:

```bash
pip install -r cpu-scheduler-sim/requirements.txt
```

---

## 🚀 วิธีการใช้งาน (Usage)

### รันบน Windows / VS Code / macOS

```bash
cd cpu-scheduler-sim
python main.py
```

### รันบน Ubuntu (ห้องแล็บ)

```bash
cd cpu-scheduler-sim
python3 main.py
```

เมื่อเปิดโปรแกรม จะมีเมนูให้เลือกเคสทดสอบตามต้องการ:

```text
============================================================
    CPU SCHEDULING ALGORITHM SIMULATOR & COMPARISON
============================================================
กรุณาเลือกรายการทดสอบ:
  [1] Sample Case (3 Processes จากเอกสารข้อกำหนด หน้า 3)
  [2] Complex Case (5 Processes หลากหลาย Burst & Priority)
  [3] CPU Idle Case (มีช่วงเวลา CPU ว่าง / Arrival gaps)
  [4] Convoy Effect Case (ทดสอบผลกระทบงานยาวใน FCFS vs SJF/RR)
  [5] ป้อนข้อมูลด้วยตนเอง (Custom Process Input)
  [6] รัน Benchmark เปรียบเทียบทุก Test Case อัตโนมัติ (Batch Run)
  [0] ออกจากโปรแกรม (Exit)
```

---

## 📊 ตัวอย่างข้อมูลทดสอบและผลลัพธ์ (Sample Case)

### ชุดข้อมูลทดสอบ (Input Data)

| Process | Arrival Time | Burst Time | Priority |
| :---: | :---: | :---: | :---: |
| **P1** | 0 | 5 | 2 |
| **P2** | 1 | 3 | 1 |
| **P3** | 2 | 8 | 3 |

### ตารางสรุปผลเปรียบเทียบประสิทธิภาพ

| Algorithm | Avg Waiting Time | Avg Turnaround Time |
| :--- | :---: | :---: |
| **FCFS** | 3.33 | 8.67 |
| **SJF (Non-Preemptive)** | 3.33 | 8.67 |
| **Priority Scheduling** | 3.33 | 8.67 |
| **Round Robin (Q=2)** | 6.00 | 11.33 |

---

## 📐 สูตรการคำนวณทางทฤษฎี

* $\text{Turnaround Time (TAT)} = \text{Completion Time} - \text{Arrival Time}$
* $\text{Waiting Time (WT)} = \text{Turnaround Time} - \text{Burst Time}$
* $\text{Average Waiting Time (Avg WT)} = \frac{1}{N} \sum_{i=1}^{N} \text{WT}_i$
* $\text{Average Turnaround Time (Avg TAT)} = \frac{1}{N} \sum_{i=1}^{N} \text{TAT}_i$