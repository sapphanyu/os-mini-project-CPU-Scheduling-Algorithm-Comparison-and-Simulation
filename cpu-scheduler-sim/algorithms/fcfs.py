import copy

def fcfs(processes):
    """
    First-Come, First-Served (FCFS) Scheduling Algorithm
    :param processes: list ของ Process objects
    :return: (gantt_log, updated_processes)
             - gantt_log: list ของ tuple (pid, start_time, end_time)
             - updated_processes: list ของ Process ที่อัปเดต completion_time แล้ว
    """
    # คัดลอก list เพื่อไม่ให้กระทบข้อมูลต้นฉบับ
    proc_list = copy.deepcopy(processes)
    
    # เรียงลำดับตาม Arrival Time (ถ้าเท่ากัน ให้เรียงตาม PID)
    proc_list.sort(key=lambda x: (x.arrival_time, x.pid))
    
    current_time = 0
    gantt_log = []

    for proc in proc_list:
        # หาก CPU ว่างเนื่องจากยังไม่มี process ไหนมาถึง ให้ข้ามเวลาไปจุดที่ process มาถึง
        if current_time < proc.arrival_time:
            current_time = proc.arrival_time

        start_time = current_time
        end_time = start_time + proc.burst_time
        
        # บันทึกประวัติการทำงานสำหรับทำ Gantt Chart
        gantt_log.append((proc.pid, start_time, end_time))
        
        # อัปเดตเวลาปัจจุบันและ completion_time ของ process
        current_time = end_time
        proc.completion_time = current_time

    return gantt_log, proc_list