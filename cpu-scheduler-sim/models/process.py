class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        """
        :param pid: หมายเลข หรือ ชื่อของ Process (เช่น 'P1', 1)
        :param arrival_time: เวลาที่ process มาถึงระบบ
        :param burst_time: เวลาที่ process ต้องใช้ CPU จนเสร็จ
        :param priority: ลำดับความสำคัญ (ตัวเลขน้อย = ความสำคัญสูง)
        """
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        
        # ตัวแปรสำหรับคำนวณผลลัพธ์
        self.completion_time = 0
        self.remaining_time = burst_time  # สำหรับ Round Robin
        
    @property
    def turnaround_time(self):
        """ Turnaround Time = Completion Time - Arrival Time """
        return self.completion_time - self.arrival_time

    @property
    def waiting_time(self):
        """ Waiting Time = Turnaround Time - Burst Time """
        return self.turnaround_time - self.burst_time

    def __repr__(self):
        return (f"Process(PID={self.pid}, Arrival={self.arrival_time}, "
                f"Burst={self.burst_time}, Priority={self.priority}, "
                f"CT={self.completion_time}, TAT={self.turnaround_time}, WT={self.waiting_time})")