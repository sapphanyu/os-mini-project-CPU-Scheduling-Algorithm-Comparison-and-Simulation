# เอกสารรายงานโครงงาน (Project Report)
## การจำลองและเปรียบเทียบประสิทธิภาพของอัลกอริทึมจัดตารางเวลาซีพียู
### (CPU Scheduling Algorithm Comparison & Simulation)

**วิชา:** ระบบปฏิบัติการ (Operating Systems)  
**ภาษาที่ใช้พัฒนา:** Python 3  
**ไลบรารีเสริม:** Matplotlib  
**แหล่งเก็บซอร์สโค้ด:** [GitHub Repository](https://github.com/sapphanyu/os-mini-project-CPU-Scheduling-Algorithm-Comparison-and-Simulation)

---

## 📋 สารบัญ
1. [บทคัดย่อ (Abstract)](#1-บทคัดย่อ-abstract)
2. [บทนำและวัตถุประสงค์ (Introduction & Objectives)](#2-บทนำและวัตถุประสงค์-introduction--objectives)
3. [ทฤษฎีและหลักการที่เกี่ยวข้อง (Theoretical Background)](#3-ทฤษฎีและหลักการที่เกี่ยวข้อง-theoretical-background)
4. [การออกแบบและการพัฒนาระบบ (System Architecture & Design)](#4-การออกแบบและการพัฒนาระบบ-system-architecture--design)
5. [ผลการทดลองและการวิเคราะห์ (Experimental Results)](#5-ผลการทดลองและการวิเคราะห์-experimental-results)
6. [การอภิปรายผลและตารางเปรียบเทียบ (Discussion & Trade-offs)](#6-การอภิปรายผลและตารางเปรียบเทียบ-discussion--trade-offs)
7. [สรุปผลโครงงาน (Conclusion)](#7-สรุปผลโครงงาน-conclusion)
8. [เอกสารอ้างอิง (References)](#8-เอกสารอ้างอิง-references)

---

## 1. บทคัดย่อ (Abstract)

ในระบบปฏิบัติการ (Operating System) ทรัพยากรหน่วยประมวลผลกลาง (CPU) ถือเป็นหัวใจสำคัญที่มีอยู่อย่างจำกัด การจัดสรรเวลาให้แต่ละ Process เข้าใช้งาน CPU อย่างมีประสิทธิภาพและเป็นธรรมจึงเป็นหน้าที่สำคัญของ **CPU Scheduler** โครงงานนี้จัดทำขึ้นเพื่อพัฒนาโปรแกรมจำลองการทำงาน (Simulator) ของอัลกอริทึมการจัดตารางเวลาซีพียู 4 อัลกอริทึมหลัก ได้แก่:
1. **First-Come, First-Served (FCFS)**
2. **Shortest Job First (SJF - Non-Preemptive)**
3. **Priority Scheduling (Non-Preemptive)**
4. **Round Robin (RR)**

โปรแกรมถูกพัฒนาด้วยภาษา Python 3 รองรับการคำนวณค่าทางสถิติที่สำคัญ ได้แก่ Completion Time (CT), Turnaround Time (TAT), Waiting Time (WT), Average Waiting Time (Avg WT) และ Average Turnaround Time (Avg TAT) พร้อมทั้งสร้างแผนภาพ **Gantt Chart** แสดงลำดับและช่วงเวลาที่แต่ละ Process ครอบครอง CPU ได้อย่างชัดเจน ผลการทดสอบเชิงประจักษ์ยืนยันว่า SJF สามารถให้ค่าเฉลี่ยเวลารอคอยต่ำที่สุดในสภาวะทั่วไป ในขณะที่ Round Robin ช่วยขจัดปัญหา Convoy Effect ได้อย่างมีประสิทธิภาพ

---

## 2. บทนำและวัตถุประสงค์ (Introduction & Objectives)

### 2.1 ที่มาและความสำคัญ
ในสภาพแวดล้อมระบบปฏิบัติการแบบมัลติโปรแกรมมิ่ง (Multiprogramming) มักจะมีหลาย Process พร้อมเข้าทำงานในเวลาเดียวกัน ระบบปฏิบัติการจำเป็นต้องมีกลไกในการตัดสินใจเลือก Process ใน Ready Queue ขึ้นมาประมวลผลบน CPU การตัดสินใจดังกล่าวขึ้นอยู่กับเป้าหมายที่ต้องการ เช่น การลดเวลารอคอยเฉลี่ย, การเพิ่ม Throughput, หรือการกระจายเวลาอย่างเท่าเทียม การเขียนโปรแกรมจำลองจึงช่วยให้ผู้ศึกษาเข้าใจการทำงาน ลอจิกการตัดสินใจ และข้อดีข้อเสียของแต่ละอัลกอริทึมได้เป็นอย่างดี

### 2.2 วัตถุประสงค์ของโครงงาน
1. พัฒนาโปรแกรมจำลองการทำงานของ CPU Scheduler 4 อัลกอริทึมหลักด้วยภาษา Python 3
2. คำนวณและเปรียบเทียบค่าทางสถิติประสิทธิภาพตามหลักวิชาการระบบปฏิบัติการ
3. แสดงผลลำดับการทำงานผ่านตารางสรุป และแผนภาพแท่ง Gantt Chart ด้วย Matplotlib
4. ศึกษากรณีพิเศษ เช่น ปรากฏการณ์ Convoy Effect, ช่วงเวลา CPU ว่าง (CPU Idle), และผลกระทบของ Time Quantum

---

## 3. ทฤษฎีและหลักการที่เกี่ยวข้อง (Theoretical Background)

### 3.1 คุณลักษณะของ Process
แต่ละ Process ประกอบด้วยคุณสมบัติพื้นฐานดังนี้:
* **Process ID (PID):** ตัวระบุหรือชื่อประจำของ Process (เช่น P1, P2)
* **Arrival Time (AT):** เวลาที่ Process เดินทางมาถึงระบบและเข้าสู่ Ready Queue
* **Burst Time (BT):** ระยะเวลาทั้งหมดที่ Process ต้องใช้ CPU ในการประมวลผลจนเสร็จสิ้น
* **Priority:** ลำดับความสำคัญของ Process (ในการทดลองนี้กำหนดให้: ตัวเลขน้อย = ความสำคัญสูง)

### 3.2 สูตรและตัวชี้วัดประสิทธิภาพ (Performance Metrics)
* **Completion Time (CT):** เวลา ณ จุดที่ Process ทำงานเสร็จสิ้นทั้งหมด
* **Turnaround Time (TAT):** ระยะเวลาตั้งแต่ Process เข้าสู่ระบบจนทำงานเสร็จสิ้น
  $$\text{Turnaround Time (TAT)} = \text{Completion Time (CT)} - \text{Arrival Time (AT)}$$
* **Waiting Time (WT):** ระยะเวลาทั้งหมดที่ Process ต้องรอคอยอยู่ใน Ready Queue โดยไม่ได้ใช้งาน CPU
  $$\text{Waiting Time (WT)} = \text{Turnaround Time (TAT)} - \text{Burst Time (BT)}$$
* **Average Waiting Time (Avg WT):** ค่าเฉลี่ยของเวลารอคอยจากทุก Process
  $$\text{Avg WT} = \frac{1}{N} \sum_{i=1}^{N} \text{WT}_i$$
* **Average Turnaround Time (Avg TAT):** ค่าเฉลี่ยของเวลาที่ใช้ในระบบจากทุก Process
  $$\text{Avg TAT} = \frac{1}{N} \sum_{i=1}^{N} \text{TAT}_i$$

### 3.3 รายละเอียดของอัลกอริทึมทั้ง 4 ตัว
1. **First-Come, First-Served (FCFS):**
   * ลำดับการประมวลผลเป็นแบบเข้าก่อนได้ก่อน (FIFO) ตาม Arrival Time
   * เป็นแบบ Non-Preemptive เมื่อ Process ได้ CPU แล้วจะทำจนเสร็จ
   * ข้อเสีย: เสี่ยงต่อการเกิด **Convoy Effect** หาก Process แรกใช้ Burst Time นานมาก Process สั้นๆ ด้านหลังจะต้องรอนานผิดปกติ
2. **Shortest Job First (SJF - Non-Preemptive):**
   * คัดเลือก Process ในกลุ่มที่มาถึงแล้ว (Arrival Time $\le$ Current Time) ที่มี Burst Time สั้นที่สุดขึ้นมาทำงาน
   * ได้รับการพิสูจน์ทางทฤษฎีว่าให้ค่า **Average Waiting Time ต่ำที่สุด (Optimal)** สำหรับชุดงานที่กำหนด
   * ข้อเสีย: ในระบบจริงคาดเดาความยาวของ Burst Time ได้ยาก
3. **Priority Scheduling (Non-Preemptive):**
   * คัดเลือก Process ที่มี Priority สูงที่สุดในกลุ่มที่พร้อมทำงาน
   * ข้อเสีย: อาจเกิดปัญหา **Starvation (การอดตาย)** หรืองานที่มีความสำคัญต่ำไม่เคยได้รันเลยหากมีงานสำคัญสูงเข้ามาเรื่อยๆ (แก้ได้ด้วยการทำ Aging)
4. **Round Robin (RR):**
   * ออกแบบมาสำหรับระบบ Time-Sharing โดยกำหนดกรอบเวลาคงที่เรียกว่า **Time Quantum (Q)**
   * แต่ละ Process จะได้ประมวลผลไม่เกิน Q หน่วยเวลา หากยังไม่เสร็จจะถูกสลับออก (Preempted) ไปต่อท้าย Ready Queue
   * รับประกันการตอบสนองที่รวดเร็วและเป็นธรรม

---

## 4. การออกแบบและการพัฒนาระบบ (System Architecture & Design)

### 4.1 โครงสร้างซอร์สโค้ด (Project Structure)
```text
cpu-scheduler-sim/
├── models/
│   ├── __init__.py
│   └── process.py           # คลาส Process สำหรับจัดการ Attributes และคำนวณ Property
├── algorithms/
│   ├── __init__.py
│   ├── fcfs.py              # ลอจิกอัลกอริทึม FCFS
│   ├── sjf.py               # ลอจิกอัลกอริทึม SJF (Non-Preemptive)
│   ├── priority.py          # ลอจิกอัลกอริทึม Priority Scheduling
│   └── round_robin.py       # ลอจิกอัลกอริทึม Round Robin พร้อม Ready Queue (deque)
├── utils/
│   ├── __init__.py
│   ├── metrics.py           # ฟังก์ชันคำนวณ Avg WT, Avg TAT และจัดรูปแบบตาราง
│   └── visualization.py     # ฟังก์ชันวาด Gantt Chart ด้วย Matplotlib
├── test_cases.py            # ชุดข้อมูลทดสอบ (Sample, Complex, Idle, Convoy, Custom)
├── main.py                  # เมนู Interactive และฟังก์ชันควบคุมการรัน
└── requirements.txt         # รายการ Dependencies (matplotlib)
```

### 4.2 จุดเด่นในการออกแบบ
* **Object-Oriented Design:** คลาส `Process` คำนวณ TAT และ WT ผ่าน `@property` อัตโนมัติเมื่อกำหนด `completion_time`
* **Consistent Gantt Chart Layout:** แก้ปัญหาแกน Y สลับตำแหน่งด้วยการทำ Natural Sort ล็อคให้แถว Process เรียงลำดับจากบนลงล่างเป็น `P1 ถึง PN` เสมอในทุกแถบกราฟ พร้อมล็อคคู่สีประจำตัว Process เพื่อความสะดวกในการเปรียบเทียบ
* **Headless & Cross-Platform Support:** รองรับการบันทึกภาพลงไฟล์ `.png` อัตโนมัติ และปรับแก้ Encoding เป็น UTF-8 ป้องกันปัญหาบน Windows PowerShell และ Ubuntu Terminal

---

## 5. ผลการทดลองและการวิเคราะห์ (Experimental Results)

### 5.1 การทดลองที่ 1: Sample Case (ชุดข้อมูลมาตรฐาน 3 Process)
* **ข้อมูลนำเข้า:**
  * P1: Arrival=0, Burst=5, Priority=2
  * P2: Arrival=1, Burst=3, Priority=1
  * P3: Arrival=2, Burst=8, Priority=3
* **ผลลัพธ์การเปรียบเทียบ:**

| Algorithm | ลำดับการทำงาน (Gantt Order) | Avg Waiting Time | Avg Turnaround Time |
| :--- | :--- | :---: | :---: |
| **FCFS** | P1(0-5) $\rightarrow$ P2(5-8) $\rightarrow$ P3(8-16) | **3.33** | **8.67** |
| **SJF** | P1(0-5) $\rightarrow$ P2(5-8) $\rightarrow$ P3(8-16) | **3.33** | **8.67** |
| **Priority** | P1(0-5) $\rightarrow$ P2(5-8) $\rightarrow$ P3(8-16) | **3.33** | **8.67** |
| **Round Robin (Q=2)** | P1(0-2) $\rightarrow$ P2(2-4) $\rightarrow$ P3(4-6) $\rightarrow$ ... | 6.00 | 11.33 |

* **วิเคราะห์:** ในเคสนี้ FCFS, SJF และ Priority ให้ผลลัพธ์ตรงกัน เนื่องจาก P1 มาถึงตัวแรกและรันจนถึง t=5 ซึ่ง ณ จุดนั้น ทั้ง P2 และ P3 ได้มาถึงแล้ว และ P2 มีทั้ง Burst สั้นกว่าและ Priority สูงกว่า P3

---

### 5.2 การทดลองที่ 2: Complex Case (ชุดข้อมูล 5 Process หลากหลายเงื่อนไข)
* **ข้อมูลนำเข้า:**
  * P1 (AT=0, BT=4, Priority=3), P2 (AT=1, BT=2, Priority=1), P3 (AT=2, BT=5, Priority=4)
  * P4 (AT=3, BT=1, Priority=2), P5 (AT=6, BT=3, Priority=5)
* **ผลลัพธ์การเปรียบเทียบ:**

| Algorithm | ลำดับการทำงาน (Gantt Order) | Avg WT | Avg TAT |
| :--- | :--- | :---: | :---: |
| **FCFS** | P1(0-4) $\rightarrow$ P2(4-6) $\rightarrow$ P3(6-11) $\rightarrow$ P4(11-12) $\rightarrow$ P5(12-15) | 4.20 | 7.20 |
| **SJF (Optimal)** | P1(0-4) $\rightarrow$ **P4(4-5)** $\rightarrow$ **P2(5-7)** $\rightarrow$ **P5(7-10)** $\rightarrow$ P3(10-15) | **2.80** | **5.80** |
| **Priority** | P1(0-4) $\rightarrow$ P2(4-6) $\rightarrow$ P4(6-7) $\rightarrow$ P3(7-12) $\rightarrow$ P5(12-15) | 3.40 | 6.40 |
| **Round Robin (Q=2)** | P1(0-2) $\rightarrow$ P2(2-4) $\rightarrow$ P3(4-6) $\rightarrow$ P1(6-8) $\rightarrow$ ... | 4.60 | 7.60 |

* **วิเคราะห์:** จะเห็นได้ชัดเจนว่า **SJF ให้ค่า Avg WT ต่ำที่สุด (2.80)** เพราะเมื่อ P1 ทำงานเสร็จที่ t=4 ระบบเลือก P4 (BT=1) และ P2 (BT=2) ขึ้นมาทำก่อน ทำให้ Process สั้นๆ ออกจากระบบได้เร็ว ส่งผลให้เวลารวมในการรอคอยลดลงอย่างมาก

---

### 5.3 การทดลองที่ 3: Convoy Effect Case (พิสูจน์จุดอ่อนของ FCFS)
* **ข้อมูลนำเข้า:**
  * P1: Arrival=0, Burst=**24** (งานยาวมาก)
  * P2: Arrival=1, Burst=3
  * P3: Arrival=2, Burst=3
* **ผลลัพธ์การเปรียบเทียบ:**

| Algorithm | ลำดับการทำงาน (Gantt Order) | Avg WT | Avg TAT |
| :--- | :--- | :---: | :---: |
| **FCFS** | P1(0-24) $\rightarrow$ P2(24-27) $\rightarrow$ P3(27-30) | **16.00** | **26.00** |
| **Round Robin (Q=4)** | P1(0-4) $\rightarrow$ P2(4-7) $\rightarrow$ P3(7-10) $\rightarrow$ P1(10-30) | **4.67** | **14.67** |

* **วิเคราะห์:** ใน FCFS เกิดปรากฏการณ์ **Convoy Effect** อย่างรุนแรง ทำให้ P2 และ P3 ต้องรอนานถึง 23 และ 25 หน่วยเวลา ส่งผลให้ Avg WT พุ่งสูงถึง 16.00 ในขณะที่ Round Robin (Q=4) ให้โอกาส P2 และ P3 ได้แทรกคิวและทำงานจนเสร็จอย่างรวดเร็ว ส่งผลให้ Avg WT ลดลงเหลือเพียง **4.67** (ลดลงมากกว่า 3 เท่า)

---

## 6. การอภิปรายผลและตารางเปรียบเทียบ (Discussion & Trade-offs)

| Algorithm | ข้อดี (Pros) | ข้อจำกัด (Cons) | กรณีการใช้งานที่เหมาะสม |
| :--- | :--- | :--- | :--- |
| **FCFS** | • เรียบง่าย ไม่ซับซ้อน<br>• ไม่มี Context Switch Overhead | • เสี่ยงต่อ Convoy Effect<br>• Avg WT มักสูง | ระบบ Batch Processing ที่ Process ใช้เวลาใกล้เคียงกัน |
| **SJF** | • ให้ Avg WT ต่ำที่สุด (Optimal)<br>• ขจัดงานสั้นได้เร็ว | • คาดเดา Burst Time ล่วงหน้าได้ยาก<br>• เสี่ยงต่อ Starvation สำหรับงานยาว | ระบบที่ทราบระยะเวลาประมวลผลล่วงหน้าอย่างแน่นอน |
| **Priority** | • ตอบสนองงานสำคัญเร่งด่วนได้ดี<br>• จัดระดับความสำคัญได้ยืดหยุ่น | • เกิด Starvation ได้ง่ายหากงานสำคัญเข้าตลอดเวลา | ระบบ Real-Time หรือระบบที่มีงาน Critical เชิงภารกิจ |
| **Round Robin** | • ยุติธรรม กระจายเวลาเท่าเทียม<br>• ไม่เกิด Starvation<br>• ตอบสนองผู้ใช้ได้เร็ว | • มี Overhead จากการสลับ Context บ่อย<br>• ประสิทธิภาพขึ้นกับค่า Quantum | ระบบ Interactive และระบบ Multi-user Time-Sharing |

---

## 7. สรุปผลโครงงาน (Conclusion)

โครงงานนี้ประสบความสำเร็จในการจำลองอัลกอริทึมจัดตารางเวลาซีพียูทั้ง 4 ตัว ผลการทดลองสอดคล้องกับทฤษฎีระบบปฏิบัติการอย่างสมบูรณ์:
1. **SJF** เป็นอัลกอริทึมที่ให้ผลรวมเวลารอคอยเฉลี่ยดีที่สุด (Avg WT ต่ำสุด)
2. **Round Robin** เป็นทางออกที่ยอดเยี่ยมในการแก้ไขปัญหา Convoy Effect ของ FCFS และป้องกัน Starvation
3. การออกแบบโปรแกรมแบบโมดูลาร์ช่วยให้เพิ่มชุดทดสอบ รองรับ Custom Input และนำผลลัพธ์ไปวิเคราะห์ผ่าน Gantt Chart ได้อย่างมีประสิทธิภาพ

---

## 8. เอกสารอ้างอิง (References)
1. Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley.
2. Tanenbaum, A. S., & Bos, H. (2015). *Modern Operating Systems* (4th ed.). Pearson.
3. Matplotlib Development Team. (2024). *Matplotlib: Visualization with Python*. https://matplotlib.org
