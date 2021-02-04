from Runner.cpu_warmer import run as run_cpu
from Runner.memory_killer import run as run_mem


if __name__ == '__main__':
    p_list = run_cpu()
    for _sub_proc in p_list:
        _sub_proc.join()

