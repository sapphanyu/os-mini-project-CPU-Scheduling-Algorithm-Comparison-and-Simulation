from test_cases import get_sample_processes
from algorithms import fcfs, sjf, priority_scheduling, round_robin
from utils import print_summary_table, plot_gantt_chart

def main():
    # 1. โหลดข้อมูลทดสอบ
    processes = get_sample_processes()
    time_quantum = 2  # กำหนด Quantum สำหรับ Round Robin

    print("=== Starting CPU Scheduling Simulation ===")
    print(f"Loaded {len(processes)} processes for simulation.\n")

    # 2. รัน Algorithm ทั้งหมด
    results = {}

    # FCFS
    fcfs_gantt, fcfs_procs = fcfs(processes)
    results['FCFS'] = (fcfs_gantt, fcfs_procs)

    # SJF
    sjf_gantt, sjf_procs = sjf(processes)
    results['SJF'] = (sjf_gantt, sjf_procs)

    # Priority
    prio_gantt, prio_procs = priority_scheduling(processes)
    results['Priority'] = (prio_gantt, prio_procs)

    # Round Robin
    rr_gantt, rr_procs = round_robin(processes, time_quantum)
    results[f'Round Robin (Q={time_quantum})'] = (rr_gantt, rr_procs)

    # 3. แสดงผลตารางสรุปเปรียบเทียบค่า Average Waiting Time & Turnaround Time
    print_summary_table(results)

    # 4. วาดภาพ Gantt Chart
    print("Opening Gantt Chart visualization...")
    plot_gantt_chart(results)

if __name__ == '__main__':
    main()