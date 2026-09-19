import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def plot_gantt_chart(results):
    """
    วาด Gantt Chart เปรียบเทียบทุก Algorithm ในหน้าต่างเดียว
    :param results: dict ในรูปแบบ { 'Algorithm Name': (gantt_log, process_list) }
    """
    num_algos = len(results)
    fig, axes = plt.subplots(num_algos, 1, figsize=(10, 2.5 * num_algos), sharex=True)

    if num_algos == 1:
        axes = [axes]

    # กำหนดพาเลตสีให้กับแต่ละ PID
    colors = ['#4E79A7', '#F28E2B', '#E15759', '#76B7B2', '#59A14F', '#EDC948', '#B07AA1']

    for ax, (algo_name, (gantt_log, _)) in zip(axes, results.items()):
        # ดึง PID ทั้งหมดแบบไม่ซ้ำเพื่อกำหนดสี
        unique_pids = list(dict.fromkeys(item[0] for item in gantt_log))
        pid_color_map = {pid: colors[i % len(colors)] for i, pid in enumerate(unique_pids)}

        for pid, start_time, end_time in gantt_log:
            duration = end_time - start_time
            ax.barh(y=str(pid), width=duration, left=start_time, 
                   color=pid_color_map[pid], edgecolor='black', height=0.5)
            # แสดงป้ายตัวเลขช่วงเวลาบนแท่งกราฟ
            ax.text(start_time + duration / 2, str(pid), f"{start_time}-{end_time}",
                    ha='center', va='center', color='white', fontsize=8, fontweight='bold')

        ax.set_title(algo_name, fontsize=12, fontweight='bold', loc='left')
        ax.set_ylabel("Process")
        ax.grid(axis='x', linestyle='--', alpha=0.5)

    axes[-1].set_xlabel("Time Unit")
    plt.tight_layout()
    plt.show()