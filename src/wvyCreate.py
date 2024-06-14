import random

r = """CV	B   s	1	0	0	0	0	1	0	0	0	0	0	0	0
13.600	1.0000	0	0	1	0	0.000	0	0	0.0	0.0	50.00	50.00	0	0	50.0	1
18.100	3600.0000	0	0	1	0	13.600	0	0	0.0	0.0	50.00	50.00	0	0	50.0	1
13.600	1.0000	0	0	1	0	18.100	0	0	0.0	0.0	50.00	50.00	0	0	50.0	1
12.000	1.0000	0	0	1	0	13.600	0	0	0.0	0.0	50.00	50.00	0	0	50.0	1"""

rlist = r.split("\n")
'''
15
['CV', 'B   s', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0']
17
['13.600', '0001.0000', '0', '0', '1', '0', '00.000', '0', '0', '0.0', '0.0', '50.00', '50.00', '0', '0', '50.0', '1']
17
['18.100', '3600.0000', '0', '0', '1', '0', '13.600', '0', '0', '0.0', '0.0', '50.00', '50.00', '0', '0', '50.0', '1']
17
['13.600', '0001.0000', '0', '0', '1', '0', '18.100', '0', '0', '0.0', '0.0', '50.00', '50.00', '0', '0', '50.0', '1']
'''
for i in rlist:
    print(len(i.split("\t")))
    print(i.split("\t"))

file_count = 100
# Generate 100 random float numbers between 4 and 20, rounded to 2 decimal places
# 生成了100个随机浮点数 4-20
start_1_random_floats = [round(random.uniform(4, 20), 2) for _ in range(file_count)]
process_1_random_floats = [round(random.uniform(4, 20), 2) for _ in range(file_count)]
run_time_1_random_floats = [round(random.uniform(1, 3), 2) for _ in range(file_count)]
run_time_2_random_floats = [round(random.uniform(1, 3), 2) for _ in range(file_count)]

print(start_1_random_floats)


def createWvy(start_1, process_1, run_time_1, run_time_2):
    demoWvy = """CV	B   s	1	0	0	0	0	1	0	0	0	0	0	0	0
13.600	1.0000	0	0	1	0	0.000	0	0	0.0	0.0	50.00	50.00	0	0	50.0	1
18.100	3600.0000	0	0	1	0	13.600	0	0	0.0	0.0	50.00	50.00	0	0	50.0	1
13.600	1.0000	0	0	1	0	18.100	0	0	0.0	0.0	50.00	50.00	0	0	50.0	1"""

    demo = f"""CV	B   s	1	0	0	0	0	1	0	0	0	0	0	0	0
{start_1}	{run_time_1}	0	0	1	0	0.000	0	0	0.0	0.0	50.00	50.00	0	0	50.0	1
{process_1}	{run_time_2}	0	0	1	0	{start_1}	0	0	0.0	0.0	50.00	50.00	0	0	50.0	1
{start_1}	{run_time_1}	0	0	1	0	{process_1}	0	0	0.0	0.0	50.00	50.00	0	0	50.0	1
12.000	1.0000	0	0	1	0	{start_1}	0	0	0.0	0.0	50.00	50.00	0	0	50.0	1"""
    # print(demo)
    return demo


if __name__ == '__main__':
    for i, v in enumerate(start_1_random_floats):
        d = createWvy(
            start_1_random_floats[i],
            process_1_random_floats[i],
            run_time_1_random_floats[i],
            run_time_2_random_floats[i],
        )
        with open(f'./resultWvy/波形{i + 1}.wvy', 'w', encoding='utf-8') as f:
            f.write(d)

    print(start_1_random_floats)
    print(process_1_random_floats)
    print(run_time_1_random_floats)
    print(run_time_2_random_floats)
