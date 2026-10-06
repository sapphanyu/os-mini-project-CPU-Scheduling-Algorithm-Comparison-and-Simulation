import sys
import io

# ปรับการเข้ารหัส stdout/stderr ให้รองรับ UTF-8 เพื่อป้องกันปัญหาบน Windows Terminal / PowerShell
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

from test_cases import (
    get_sample_processes,
    get_complex_test_case,
    get_cpu_idle_case,
    get_convoy_effect_case,
    get_custom_processes
)
from algorithms import fcfs, sjf, priority_scheduling, round_robin
from utils import (
    print_process_table,
    print_algorithm_details,
    print_summary_table,
    plot_gantt_chart
)


def run_simulation(processes, time_quantum=2, show_chart=True, save_filename="gantt_chart.png"):
    """
    ฟังก์ชันหลักในการรันการจำลอง Scheduling Algorithms ทั้ง 4 ตัว
    """
    # 1. แสดงข้อมูล Process ก่อนประมวลผล
    print_process_table(processes)

    # 2. จำลองการทำงานของแต่ละ Algorithm
    results = {}

    # FCFS
    fcfs_gantt, fcfs_procs = fcfs(processes)
    results['FCFS'] = (fcfs_gantt, fcfs_procs)
    print_algorithm_details('FCFS', fcfs_procs, fcfs_gantt)

    # SJF (Non-preemptive)
    sjf_gantt, sjf_procs = sjf(processes)
    results['SJF (Non-Preemptive)'] = (sjf_gantt, sjf_procs)
    print_algorithm_details('SJF (Non-Preemptive)', sjf_procs, sjf_gantt)

    # Priority Scheduling (Non-preemptive)
    prio_gantt, prio_procs = priority_scheduling(processes)
    results['Priority Scheduling'] = (prio_gantt, prio_procs)
    print_algorithm_details('Priority Scheduling', prio_procs, prio_gantt)

    # Round Robin
    rr_gantt, rr_procs = round_robin(processes, time_quantum)
    results[f'Round Robin (Q={time_quantum})'] = (rr_gantt, rr_procs)
    print_algorithm_details(f'Round Robin (Time Quantum = {time_quantum})', rr_procs, rr_gantt)

    # 3. แสดงตารางสรุปผลเปรียบเทียบ
    print_summary_table(results)

    # 4. วาดและบันทึก Gantt Chart
    print("[*] กำลังสร้างแผนภาพ Gantt Chart...")
    plot_gantt_chart(results, save_path=save_filename, show=show_chart)


def run_batch_benchmark():
    """
    รันชุดทดสอบทั้งหมดแบบอัตโนมัติ (Batch Testing) เพื่อตรวจสอบความถูกต้องและเปรียบเทียบผลลัพธ์
    """
    cases = [
        ("Case 1: Sample Case (จากเอกสารหน้า 3)", get_sample_processes(), 2, "gantt_sample.png"),
        ("Case 2: Complex Case (5 Processes)", get_complex_test_case(), 2, "gantt_complex.png"),
        ("Case 3: CPU Idle Case (Arrival Gaps)", get_cpu_idle_case(), 2, "gantt_idle.png"),
        ("Case 4: Convoy Effect Case", get_convoy_effect_case(), 4, "gantt_convoy.png"),
    ]

    print("\n" + "=" * 70)
    print("[BENCHMARK] เริ่มการทดสอบอัตโนมัติครบทุก Test Case (Batch Benchmark)")
    print("=" * 70)

    for title, procs, q, img_name in cases:
        print(f"\n>>>>>>>> {title} (Time Quantum={q}) <<<<<<<<")
        run_simulation(procs, time_quantum=q, show_chart=False, save_filename=img_name)

    print("\n[OK] การทดสอบทุก Test Case เสร็จสมบูรณ์! ภาพ Gantt Chart ทั้งหมดถูกบันทึกเรียบร้อยแล้ว\n")


def prompt_quantum():
    """
    ถามผู้ใช้สำหรับกำหนดค่า Time Quantum
    """
    while True:
        user_input = input("[?] กำหนดค่า Time Quantum สำหรับ Round Robin (กด Enter เพื่อใช้ค่าเริ่มต้น 2): ").strip()
        if not user_input:
            return 2
        try:
            q = float(user_input)
            if q <= 0:
                print("[-] Time Quantum ต้องมากกว่า 0")
                continue
            return int(q) if q.is_integer() else q
        except ValueError:
            print("[-] กรุณากรอกตัวเลขที่ถูกต้อง")


def prompt_show_chart():
    """
    ถามผู้ใช้ว่าต้องการเปิดหน้าต่างกราฟ (GUI Window) หรือไม่
    """
    ans = input("[?] ต้องการเปิดหน้าต่างกราฟ (GUI Window) หรือไม่? [Y/n]: ").strip().lower()
    return ans not in ['n', 'no']


def main():
    while True:
        print("\n" + "=" * 60)
        print("    CPU SCHEDULING ALGORITHM SIMULATOR & COMPARISON")
        print("=" * 60)
        print("กรุณาเลือกรายการทดสอบ:")
        print("  [1] Sample Case (3 Processes จากเอกสารข้อกำหนด หน้า 3)")
        print("  [2] Complex Case (5 Processes หลากหลาย Burst & Priority)")
        print("  [3] CPU Idle Case (มีช่วงเวลา CPU ว่าง / Arrival gaps)")
        print("  [4] Convoy Effect Case (ทดสอบผลกระทบงานยาวใน FCFS vs SJF/RR)")
        print("  [5] ป้อนข้อมูลด้วยตนเอง (Custom Process Input)")
        print("  [6] รัน Benchmark เปรียบเทียบทุก Test Case อัตโนมัติ (Batch Run)")
        print("  [0] ออกจากโปรแกรม (Exit)")
        print("-" * 60)

        choice = input("[?] เลือกเมนู [0-6]: ").strip()

        if choice == '1':
            procs = get_sample_processes()
            q = prompt_quantum()
            show = prompt_show_chart()
            run_simulation(procs, time_quantum=q, show_chart=show, save_filename="gantt_sample.png")

        elif choice == '2':
            procs = get_complex_test_case()
            q = prompt_quantum()
            show = prompt_show_chart()
            run_simulation(procs, time_quantum=q, show_chart=show, save_filename="gantt_complex.png")

        elif choice == '3':
            procs = get_cpu_idle_case()
            q = prompt_quantum()
            show = prompt_show_chart()
            run_simulation(procs, time_quantum=q, show_chart=show, save_filename="gantt_idle.png")

        elif choice == '4':
            procs = get_convoy_effect_case()
            q = prompt_quantum()
            show = prompt_show_chart()
            run_simulation(procs, time_quantum=q, show_chart=show, save_filename="gantt_convoy.png")

        elif choice == '5':
            procs = get_custom_processes()
            if procs:
                q = prompt_quantum()
                show = prompt_show_chart()
                run_simulation(procs, time_quantum=q, show_chart=show, save_filename="gantt_custom.png")

        elif choice == '6':
            run_batch_benchmark()

        elif choice == '0':
            print("\nขอบคุณที่ใช้งานโปรแกรม CPU Scheduling Simulator!\n")
            sys.exit(0)

        else:
            print("[-] ตัวเลือกไม่ถูกต้อง กรุณาเลือกตัวเลข 0 ถึง 6")


if __name__ == '__main__':
    main()