import copy

def sjf(processes):
    """
    Non-Preemptive Shortest Job First (SJF) Scheduling Algorithm
    :param processes: list ของ Process objects
    :return: (gantt_log, updated_processes)
    """
    proc_list = copy.deepcopy(processes)
    
    current_time = 0
    completed_count = 0
    n = len(proc_list)
    is_completed = [False] * n
    
    gantt_log = []

    while completed_count < n:
        idx = -1
        min_burst = float('inf')

        # ค้นหา process ที่มาถึงแล้ว และยังทำไม่เสร็จ ที่มี burst time สั้นที่สุด
        for i in range(n):
            if proc_list[i].arrival_time <= current_time and not is_completed[i]:
                if proc_list[i].burst_time < min_burst:
                    min_burst = proc_list[i].burst_time
                    idx = i
                # ถ้า burst time เท่ากัน ให้เลือกตัวที่มาถึงก่อน
                elif proc_list[i].burst_time == min_burst:
                    if proc_list[i].arrival_time < proc_list[idx].arrival_time:
                        idx = i

        # ถ้าพบ process ที่พร้อมทำงาน
        if idx != -1:
            proc = proc_list[idx]
            start_time = current_time
            end_time = start_time + proc.burst_time

            gantt_log.append((proc.pid, start_time, end_time))

            current_time = end_time
            proc.completion_time = current_time
            is_completed[idx] = True
            completed_count += 1
        else:
            # ถ้า ณ เวลาปัจจุบันยังไม่มี process ไหนมาถึง ให้ข้ามเวลาไปยัง process ที่มาถึงเร็วที่สุด
            uncompleted_arrivals = [p.arrival_time for i, p in enumerate(proc_list) if not is_completed[i]]
            current_time = min(uncompleted_arrivals)

    return gantt_log, proc_list