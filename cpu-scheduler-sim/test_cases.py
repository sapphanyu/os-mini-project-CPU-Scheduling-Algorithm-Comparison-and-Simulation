from models import Process

def get_sample_processes():
    """
    ชุดข้อมูลทดสอบตามตัวอย่างในเอกสาร
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
    ชุดข้อมูลทดสอบที่ซับซ้อนขึ้นสำหรับทดสอบ Edge Cases
    """
    return [
        Process(pid='P1', arrival_time=0, burst_time=4, priority=3),
        Process(pid='P2', arrival_time=1, burst_time=2, priority=1),
        Process(pid='P3', arrival_time=2, burst_time=5, priority=4),
        Process(pid='P4', arrival_time=3, burst_time=1, priority=2),
        Process(pid='P5', arrival_time=6, burst_time=3, priority=5),
    ]