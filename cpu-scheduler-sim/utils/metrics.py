import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def calculate_metrics(processes):
    """
    คำนวณค่า Average Waiting Time และ Average Turnaround Time
    :param processes: list ของ Process objects ที่อัปเดต completion_time แล้ว
    :return: dict เก็บค่า avg_wt และ avg_tat
    """
    n = len(processes)
    if n == 0:
        return {"avg_wt": 0, "avg_tat": 0}

    total_wt = sum(p.waiting_time for p in processes)
    total_tat = sum(p.turnaround_time for p in processes)

    return {
        "avg_wt": total_wt / n,
        "avg_tat": total_tat / n
    }


def print_process_table(processes):
    """
    แสดงตารางข้อมูล Process เริ่มต้นก่อนเริ่มจำลอง
    """
    print("\n" + "=" * 50)
    print("[INPUT] ตารางข้อมูล Processes (Input Data)")
    print("=" * 50)
    print(f"{'PID':<8} | {'Arrival':<10} | {'Burst':<10} | {'Priority':<10}")
    print("-" * 50)
    for p in sorted(processes, key=lambda x: (x.arrival_time, x.pid)):
        print(f"{str(p.pid):<8} | {p.arrival_time:<10} | {p.burst_time:<10} | {p.priority:<10}")
    print("=" * 50 + "\n")


def print_algorithm_details(algo_name, processes, gantt_log):
    """
    แสดงรายละเอียดผลลัพธ์ของ Algorithm แต่ละตัว
    """
    print(f"\n--- รายละเอียดผลลัพธ์: {algo_name} ---")
    gantt_str = " -> ".join([f"{pid}({s}-{e})" for pid, s, e in gantt_log])
    print(f"Gantt Order: {gantt_str}")
    print("-" * 65)
    print(f"{'PID':<6} | {'Arrival':<8} | {'Burst':<8} | {'CT':<6} | {'TAT':<6} | {'WT':<6}")
    print("-" * 65)
    for p in sorted(processes, key=lambda x: str(x.pid)):
        print(f"{str(p.pid):<6} | {p.arrival_time:<8} | {p.burst_time:<8} | {p.completion_time:<6} | {p.turnaround_time:<6} | {p.waiting_time:<6}")
    metrics = calculate_metrics(processes)
    print("-" * 65)
    print(f"Average Waiting Time (Avg WT)      = {metrics['avg_wt']:.2f}")
    print(f"Average Turnaround Time (Avg TAT)  = {metrics['avg_tat']:.2f}\n")


def print_summary_table(results):
    """
    แสดงตารางสรุปเปรียบเทียบผลลัพธ์ของแต่ละ Algorithm
    :param results: dict ในรูปแบบ { 'Algorithm Name': (gantt_log, process_list) }
    """
    print("\n" + "=" * 65)
    print("[SUMMARY] ตารางสรุปเปรียบเทียบประสิทธิภาพทุก Algorithm")
    print("=" * 65)
    print(f"{'Algorithm':<24} | {'Avg Waiting Time':<18} | {'Avg Turnaround Time':<18}")
    print("-" * 65)

    best_wt_name = None
    best_wt_val = float('inf')

    for algo_name, (_, processes) in results.items():
        metrics = calculate_metrics(processes)
        if metrics['avg_wt'] < best_wt_val:
            best_wt_val = metrics['avg_wt']
            best_wt_name = algo_name
        print(f"{algo_name:<24} | {metrics['avg_wt']:<18.2f} | {metrics['avg_tat']:<18.2f}")

    print("=" * 65)
    if best_wt_name:
        print(f"[*] อัลกอริทึมที่ให้ Average Waiting Time ต่ำที่สุดสำหรับชุดข้อมูลนี้คือ: {best_wt_name} ({best_wt_val:.2f})")
    print("=" * 65 + "\n")