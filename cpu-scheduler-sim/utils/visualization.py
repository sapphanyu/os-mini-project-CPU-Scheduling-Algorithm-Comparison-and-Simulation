import re
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def plot_gantt_chart(results, save_path="gantt_chart.png", show=True):
    """
    วาด Gantt Chart เปรียบเทียบทุก Algorithm ในหน้าต่างเดียว และบันทึกภาพลงไฟล์
    โดยเรียงลำดับ Process จากบนลงล่างอย่างสม่ำเสมอ (เช่น P1, P2, ..., P5) ทุก Algorithm
    :param results: dict ในรูปแบบ { 'Algorithm Name': (gantt_log, process_list) }
    :param save_path: path สำหรับบันทึกรูปภาพ (เช่น 'gantt_chart.png')
    :param show: กำหนดว่าต้องการเรียก plt.show() หรือไม่
    """
    # 1. รวบรวม PID ทั้งหมดจากทุก Algorithm เพื่อจัดเรียงลำดับคงที่และกำหนดสีเดียวอย่างสม่ำเสมอ
    all_pids = set()
    for _, (gantt_log, processes) in results.items():
        for p in processes:
            all_pids.add(str(p.pid))
        for item in gantt_log:
            all_pids.add(str(item[0]))

    # เรียงลำดับ PID ตามธรรมชาติ (P1, P2, ..., P10 ไม่ให้ P10 ลัดคิวมาหลัง P1)
    def natural_sort_key(s):
        return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

    sorted_pids = sorted(all_pids, key=natural_sort_key)

    # กำหนดพาเลตสีคงที่ให้กับแต่ละ PID ตลอดทุกกราฟ
    colors = ['#4E79A7', '#F28E2B', '#E15759', '#76B7B2', '#59A14F', '#EDC948', '#B07AA1', '#9C755F', '#BAB0AC']
    pid_color_map = {pid: colors[i % len(colors)] for i, pid in enumerate(sorted_pids)}
    y_positions = {pid: i for i, pid in enumerate(sorted_pids)}

    num_algos = len(results)
    fig, axes = plt.subplots(num_algos, 1, figsize=(11, 2.5 * num_algos), sharex=True)

    if num_algos == 1:
        axes = [axes]

    for ax, (algo_name, (gantt_log, _)) in zip(axes, results.items()):
        for pid, start_time, end_time in gantt_log:
            duration = end_time - start_time
            y_pos = y_positions[str(pid)]
            ax.barh(y=y_pos, width=duration, left=start_time, 
                   color=pid_color_map[str(pid)], edgecolor='black', height=0.55)
            # แสดงป้ายตัวเลขช่วงเวลาบนแท่งกราฟ
            ax.text(start_time + duration / 2, y_pos, f"{start_time}-{end_time}",
                    ha='center', va='center', color='white', fontsize=8, fontweight='bold')

        # ล็อคแกน Y ให้คงที่ เรียง P1 -> PN จากบนลงล่างเสมอทุกกราฟ
        ax.set_yticks(range(len(sorted_pids)))
        ax.set_yticklabels(sorted_pids)
        ax.set_ylim(-0.6, len(sorted_pids) - 0.4)
        ax.invert_yaxis()

        ax.set_title(algo_name, fontsize=12, fontweight='bold', loc='left')
        ax.set_ylabel("Process", fontweight='bold')
        ax.grid(axis='x', linestyle='--', alpha=0.5)

    axes[-1].set_xlabel("Time Unit", fontsize=11, fontweight='bold')
    plt.tight_layout()

    # บันทึกภาพลงไฟล์เสมอ เพื่อความสะดวกบนเครื่องที่ไม่มี GUI (เช่น Ubuntu แล็บ)
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"[OK] บันทึกภาพ Gantt Chart สำเร็จ: {save_path}")

    if show:
        try:
            plt.show()
        except Exception as e:
            print(f"[!] ไม่สามารถเปิดหน้าต่าง GUI ได้ ({e}) สามารถเปิดดูภาพจากไฟล์ '{save_path}' ได้โดยตรง")