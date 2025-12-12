# --- Part Two ---
# Thanks in part to your analysis, the Elves have figured out a little bit about the issue. They now know that the problematic data path passes through both dac (a digital-to-analog converter) and fft (a device which performs a fast Fourier transform).
#
# They're still not sure which specific path is the problem, and so they now need you to find every path from svr (the server rack) to out. However, the paths you find must all also visit both dac and fft (in any order).
#
# For example:
#
# svr: aaa bbb
# aaa: fft
# fft: ccc
# bbb: tty
# tty: ccc
# ccc: ddd eee
# ddd: hub
# hub: fff
# eee: dac
# dac: fff
# fff: ggg hhh
# ggg: out
# hhh: out
# This new list of devices contains many paths from svr to out:
#
# svr,aaa,fft,ccc,ddd,hub,fff,ggg,out
# svr,aaa,fft,ccc,ddd,hub,fff,hhh,out
# svr,aaa,fft,ccc,eee,dac,fff,ggg,out
# svr,aaa,fft,ccc,eee,dac,fff,hhh,out
# svr,bbb,tty,ccc,ddd,hub,fff,ggg,out
# svr,bbb,tty,ccc,ddd,hub,fff,hhh,out
# svr,bbb,tty,ccc,eee,dac,fff,ggg,out
# svr,bbb,tty,ccc,eee,dac,fff,hhh,out
# However, only 2 paths from svr to out visit both dac and fft.
#
# Find all of the paths that lead from svr to out. How many of those paths visit both dac and fft?

def parse_devices(filename):
    graph = {}
    with open(filename, 'r') as f:
        for line in f:
            if ':' in line:
                device, outputs = line.strip().split(':')
                graph[device.strip()] = [o.strip() for o in outputs.strip().split()]
    return graph

def count_paths_with_dac_fft(graph, current, end, visited_dac, visited_fft, memo):
    key = (current, visited_dac, visited_fft)
    if key in memo:
        return memo[key]
    if current == end:
        return int(visited_dac and visited_fft)
    if current not in graph:
        return 0
    total = 0
    for node in graph[current]:
        total += count_paths_with_dac_fft(
            graph,
            node,
            end,
            visited_dac or (node == 'dac'),
            visited_fft or (node == 'fft'),
            memo
        )
    memo[key] = total
    return total

if __name__ == "__main__":
    graph = parse_devices('devices_list_main.txt')
    memo = {}
    count = count_paths_with_dac_fft(graph, 'svr', 'out', False, False, memo)
    print(f"Number of paths from 'svr' to 'out' that visit both 'dac' and 'fft': {count}")
    # Number of paths from 'svr' to 'out' that visit both 'dac' and 'fft': 370500293582760

