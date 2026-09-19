# CPU Scheduling Algorithm Simulator

โปรแกรมจำลองการทำงานของ **CPU Scheduler** ในระบบปฏิบัติการ (Operating System) พัฒนาด้วยภาษา **Python 3** ทำหน้าที่รับข้อมูล Process (เช่น Arrival Time, Burst Time, Priority) แล้วคำนวณการจัดลำดับการทำงานของ CPU ตาม Scheduling Algorithms ต่างๆ พร้อมแสดงผลลัพธ์เปรียบเทียบประสิทธิภาพผ่านตารางสรุปและภาพ **Gantt Chart**

---

## 📌 คุณสมบัติของโปรแกรม (Features)

1. **รองรับ 4 Scheduling Algorithms หลัก:**
   * **FCFS (First Come First Served):** จัดลำดับตามเวลาที่มาถึงระบบ
   * **SJF (Shortest Job First - Non-Preemptive):** เลือก Process ที่ใช้ Burst Time น้อยที่สุด ณ เวลาปัจจุบัน
   * **Priority Scheduling (Non-Preemptive):** เลือก Processที่มีลำดับความสำคัญสูงสุด (ตัวเลข Priority น้อย = ความสำคัญสูง)
   * **Round Robin (RR):** สลับกันทำงานตามช่วงเวลา (Time Quantum) โดยใช้ Ready Queue
2. **การคำนวณสถิติอัตโนมัติ:**
   * Completion Time (CT)
   * Turnaround Time (TAT = CT - Arrival Time)
   * Waiting Time (WT = TAT - Burst Time)
   * Average Waiting Time และ Average Turnaround Time
3. **การแสดงผลเชิงทัศน์ (Visualization):**
   * วาด **Gantt Chart** แสดงช่วงเวลาการทำงานของแต่ละ Process ด้วย `matplotlib`
   * พิมพ์ตารางสรุปเปรียบเทียบค่าเฉลี่ยสถิติลงบน Terminal

---

## 📁 โครงสร้างโปรเจกต์ (Project Structure)

```text
cpu-scheduler-sim/
├── models/
│   ├── __init__.py
│   └── process.py           # Class สำหรับเก็บข้อมูลของ Process
├── algorithms/
│   ├── __init__.py
│   ├── fcfs.py              # First Come First Served Algorithm
│   ├── sjf.py               # Shortest Job First Algorithm
│   ├── priority.py          # Priority Scheduling Algorithm
│   └── round_robin.py        # Round Robin Algorithm
├── utils/
│   ├── __init__.py
│   ├── metrics.py           # ฟังก์ชันคำนวณสถิติและพิมพ์ตารางสรุป
│   └── visualization.py     # ฟังก์ชันวาด Gantt Chart
├── test_cases.py            # ชุดข้อมูลทดสอบ (Input Test Cases)
├── main.py                  # ไฟล์หลักสำหรับสั่งรันระบบ
├── requirements.txt         # รายการ Library ที่ต้องใช้
└── README.md                # เอกสารกำกับโปรเจกต์

---

## 🛠️ การติดตั้งและการเตรียมระบบ (Installation)

### 1. Requirements

* Python 3.x
* Library: `matplotlib`

### 2. ขั้นตอนการติดตั้ง Dependencies

เปิด Terminal หรือ Command Prompt ในโฟลเดอร์โปรเจกต์ แล้วรันคำสั่ง:

```bash
pip install -r requirements.txt

```

---

## 🚀 วิธีการใช้งาน (Usage)

### รันบน VS Code / Windows / macOS

```bash
python main.py

```

### รันบน Ubuntu (ห้องแล็บ)

เปิด Terminal บน Ubuntu แล้วใช้คำสั่ง:

```bash
python3 main.py

```

---

## 📊 ตัวอย่างข้อมูลทดสอบและผลลัพธ์ (Example Case)

### ชุดข้อมูล Process

| Process | Arrival Time | Burst Time | Priority |
| --- | --- | --- | --- |
| P1 | 0 | 5 | 2 |
| P2 | 1 | 3 | 1 |
| P3 | 2 | 8 | 3 |

### สูตรการคำนวณที่ใช้

* $\text{Turnaround Time (TAT)} = \text{Completion Time} - \text{Arrival Time}$
* $\text{Waiting Time (WT)} = \text{Turnaround Time} - \text{Burst Time}$

---