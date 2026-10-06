import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

from models import Process

def get_sample_processes():
    """
    ชุดข้อมูลทดสอบตามตัวอย่างในเอกสาร (หน้า 3)
    P1: Arrival=0, Burst=5, Priority=2
    P2: Arrival=1, Burst=3, Priority=1
    P3: Arrival=2, Burst=8, Priority=3
    """
    return [
        Process(pid='P1', arrival_time=0, burst_time=5, priority=2),
        Process(pid='P2', arrival_time=1, burst_time=3, priority=1),
        Process(pid='P3', arrival_time=2, burst_time=8, priority=3),
    ]


def get_complex_test_case():
    """
    ชุดข้อมูลทดสอบ 5 Process ที่มี Burst Time และ Priority หลากหลาย
    """
    return [
        Process(pid='P1', arrival_time=0, burst_time=4, priority=3),
        Process(pid='P2', arrival_time=1, burst_time=2, priority=1),
        Process(pid='P3', arrival_time=2, burst_time=5, priority=4),
        Process(pid='P4', arrival_time=3, burst_time=1, priority=2),
        Process(pid='P5', arrival_time=6, burst_time=3, priority=5),
    ]


def get_cpu_idle_case():
    """
    ชุดข้อมูลทดสอบกรณีมีช่วงเวลา CPU ว่าง (CPU Idle Gaps)
    เนื่องจาก Process ถัดไปมาถึงหลัง Process ก่อนหน้าทำงานเสร็จ
    """
    return [
        Process(pid='P1', arrival_time=0, burst_time=3, priority=2),
        Process(pid='P2', arrival_time=5, burst_time=4, priority=1),
        Process(pid='P3', arrival_time=12, burst_time=3, priority=3),
    ]


def get_convoy_effect_case():
    """
    ชุดข้อมูลทดสอบปรากฏการณ์ Convoy Effect
    (มี Process ยาวมากมาถึงก่อน ทำให้ Process สั้นต้องรอนานใน FCFS)
    """
    return [
        Process(pid='P1', arrival_time=0, burst_time=24, priority=3),
        Process(pid='P2', arrival_time=1, burst_time=3, priority=1),
        Process(pid='P3', arrival_time=2, burst_time=3, priority=2),
    ]


def get_custom_processes():
    """
    ฟังก์ชันสำหรับให้ผู้ใช้ป้อนข้อมูล Process เองผ่านทาง Terminal (Interactive Input)
    พร้อมการตรวจสอบความถูกต้องของข้อมูล (Input Validation)
    """
    print("\n" + "=" * 50)
    print("[+] กรอกข้อมูล Process ด้วยตนเอง (Custom Input)")
    print("=" * 50)

    while True:
        try:
            num_input = input("[?] ระบุจำนวน Process ทั้งหมด (เช่น 3 หรือ 4): ").strip()
            num_proc = int(num_input)
            if num_proc <= 0:
                print("[-] จำนวน Process ต้องมากกว่า 0 กรุณากรอกใหม่")
                continue
            if num_proc > 20:
                print("[!] แนะนำไม่เกิน 20 Process เพื่อการแสดงผลกราฟที่ชัดเจน")
            break
        except ValueError:
            print("[-] กรุณากรอกตัวเลขจำนวนเต็มบวกเท่านั้น")

    processes = []
    print("\nกรอกรายละเอียดของแต่ละ Process (ตัวเลข Priority น้อย = ความสำคัญสูง):")
    for i in range(1, num_proc + 1):
        print(f"\n--- ข้อมูล Process ตัวที่ {i}/{num_proc} ---")
        
        # PID
        pid_default = f"P{i}"
        pid_input = input(f"PID (กด Enter เพื่อใช้ '{pid_default}'): ").strip()
        pid = pid_input if pid_input else pid_default

        # Arrival Time
        while True:
            try:
                arr_input = input("Arrival Time (เวลามาถึง >= 0): ").strip()
                arrival = float(arr_input)
                if arrival < 0:
                    print("[-] Arrival Time ต้องไม่ติดลบ")
                    continue
                # แปลงเป็น int หากไม่มีทศนิยม
                arrival = int(arrival) if arrival.is_integer() else arrival
                break
            except ValueError:
                print("[-] กรุณากรอกตัวเลขที่ถูกต้อง")

        # Burst Time
        while True:
            try:
                burst_input = input("Burst Time (เวลาประมวลผล > 0): ").strip()
                burst = float(burst_input)
                if burst <= 0:
                    print("[-] Burst Time ต้องมากกว่า 0")
                    continue
                burst = int(burst) if burst.is_integer() else burst
                break
            except ValueError:
                print("[-] กรุณากรอกตัวเลขที่ถูกต้อง")

        # Priority
        while True:
            try:
                prio_input = input("Priority (ลำดับความสำคัญ, กด Enter เพื่อใช้ค่าเริ่มต้น 1): ").strip()
                if not prio_input:
                    priority = 1
                    break
                priority = int(prio_input)
                if priority < 0:
                    print("[-] Priority ต้องไม่ติดลบ")
                    continue
                break
            except ValueError:
                print("[-] กรุณากรอกตัวเลขจำนวนเต็ม")

        processes.append(Process(pid=pid, arrival_time=arrival, burst_time=burst, priority=priority))

    return processes