import copy
from collections import deque

def round_robin(processes, time_quantum):
    """
    Round Robin Scheduling Algorithm
    :param processes: list ของ Process objects
    :param time_quantum: เวลาสูงสุดที่แต่ละ process สลับกันทำต่อรอบ
    :return: (gantt_log, updated_processes)
    """
    proc_list = copy.deepcopy(processes)
    
    # เรียงลำดับตาม Arrival Time ก่อนเริ่ม
    proc_list.sort(key=lambda x: (x.arrival_time, x.pid))
    
    # กำหนด remaining_time สำหรับใช้ตัดเวลา
    for proc in proc_list:
        proc.remaining_time = proc.burst_time

    current_time = 0
    completed_count = 0
    n = len(proc_list)
    
    ready_queue = deque()
    in_queue = [False] * n
    gantt_log = []

    # เพิ่ม process ตัวแรกที่มาถึงลงในคิว
    current_time = proc_list[0].arrival_time
    for i in range(n):
        if proc_list[i].arrival_time <= current_time:
            ready_queue.append(i)
            in_queue[i] = True

    while completed_count < n:
        if not ready_queue:
            # ถ้าคิวว่าง ให้หาเวลาที่ process ถัดไปจะมาถึง
            next_arrival = min(p.arrival_time for i, p in enumerate(proc_list) if p.remaining_time > 0)
            current_time = max(current_time, next_arrival)
            for i in range(n):
                if proc_list[i].arrival_time <= current_time and proc_list[i].remaining_time > 0 and not in_queue[i]:
                    ready_queue.append(i)
                    in_queue[i] = True
            continue

        idx = ready_queue.popleft()
        proc = proc_list[idx]
        
        # คำนวณเวลาที่จะประมวลผลในรอบนี้
        exec_time = min(proc.remaining_time, time_quantum)
        start_time = current_time
        end_time = start_time + exec_time
        
        gantt_log.append((proc.pid, start_time, end_time))
        
        current_time = end_time
        proc.remaining_time -= exec_time

        # ตรวจสอบ process ใหม่ที่มาถึงระหว่างที่ process ปัจจุบันกำลังทำงาน แล้วเพิ่มเข้าคิว
        for i in range(n):
            if (proc_list[i].arrival_time <= current_time and 
                proc_list[i].remaining_time > 0 and 
                not in_queue[i] and 
                i != idx):
                ready_queue.append(i)
                in_queue[i] = True

        # ถ้า process ปัจจุบันยังทำไม่เสร็จ ให้ใส่กลับเข้าคิว
        if proc.remaining_time > 0:
            ready_queue.append(idx)
        else:
            proc.completion_time = current_time
            completed_count += 1

    return gantt_log, proc_list