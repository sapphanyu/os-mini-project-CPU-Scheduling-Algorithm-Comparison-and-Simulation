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


def print_summary_table(results):
    """
    แสดงตารางสรุปเปรียบเทียบผลลัพธ์ของแต่ละ Algorithm
    :param results: dict ในรูปแบบ { 'Algorithm Name': (gantt_log, process_list) }
    """
    print("\n" + "=" * 65)
    print(f"{'Algorithm':<20} | {'Avg Waiting Time':<20} | {'Avg Turnaround Time':<20}")
    print("=" * 65)

    for algo_name, (_, processes) in results.items():
        metrics = calculate_metrics(processes)
        print(f"{algo_name:<20} | {metrics['avg_wt']:<20.2f} | {metrics['avg_tat']:<20.2f}")

    print("=" * 65 + "\n")