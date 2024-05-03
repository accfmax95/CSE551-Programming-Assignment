def schedule_wafers(wafers):
    # Sort wafers by the minimum time for the first or second station
    # Wafer format: [(time1, time2), ...]
    front_jobs = []
    end_jobs = []

    # Separate the jobs based on whether their first or second station time is shorter
    for i, (time1, time2) in enumerate(wafers):

        if time1 <= time2:

            front_jobs.append((i, time1, time2))
        else:

            end_jobs.append((i, time1, time2))

    # Sort the jobs by the shortest processing time for the first station
    # and by longest processing time for the second station (if the second station is shorter)
    front_jobs.sort(key=lambda x: x[1])
    end_jobs.sort(key=lambda x: x[2], reverse=True)

    # Combine the two lists to get the job order
    job_order = front_jobs + end_jobs

    # Calculate the total processing time
    time_s1, time_s2 = 0, 0
    for _, time1, time2 in job_order:

        time_s1 += time1
        time_s2 = max(time_s2, time_s1) + time2

    # Get the wafer order and total time
    wafer_order = [i + 1 for i, _, _ in job_order]
    total_time = max(time_s1, time_s2)

    return total_time, wafer_order

# A set of test cases to ensure that the output is correct.
test_cases = [
    ([(2, 3)], (5, [1])),
    ([(3, 3), (3, 3)], (9, [1, 2])),
    ([(4, 5), (2, 3)], (11, [2,1 ])),
    ([(1, 2), (2, 3), (3, 4)], (10, [1, 2, 3])),
    ([(3, 4), (2, 3), (1, 2)], (10, [3, 2, 1])),
    ([(100, 200), (300, 400)], (800, [1, 2])),
    ([(1, 2), (2, 4), (3, 6), (4, 8), (5, 10)], (31, [1, 2, 3, 4, 5])),
    ([(17,8), (2, 4), (10, 2), (4, 9), (4, 12), (13,4),(13,13)], (65, [2, 4, 5, 7, 1, 6, 3])),
    ([(10, 20), (20, 10), (5, 15), (15, 5), (25, 35), (35, 25), (8, 18), (18, 8), (30, 40), (40, 30)], (211, [3, 7, 1, 5, 9, 10, 6, 2, 8, 4])),
    ([(7, 12), (16, 9), (5, 15), (12, 5), (10, 20), (20, 10), (14, 7), (6, 18), (18, 6), (15, 10), (10, 15), (8, 17)], (149, [3, 8, 1, 12, 5, 11, 6, 10, 2, 7, 9, 4])),
    ([(21, 25), (25, 19), (17, 23), (23, 16), (15, 26), (26, 14), (13, 27), (27, 13), (11, 30), (30, 11), (9, 33), (33, 8), (8, 35), (35, 7), (6, 37)], (330, [15, 13, 11, 9, 7, 5, 3, 1, 2, 4, 6, 8, 10, 12, 14]))
]

# Function to run all test cases
def run_test_cases(test_cases):

    all_passed = True
    for i, (input_data, expected) in enumerate(test_cases, 1):

        result = schedule_wafers(input_data)
        if result != expected:

            print(f"Test case {i} failed: expected {expected}, got {result}")
            all_passed = False
            
    if all_passed:

        print("All test cases passed!")

def main():
    #run_test_cases(test_cases)
    num_wafers = int(input('Enter the number of wafers: '))
    wafers = []
    
    for i in range(num_wafers):
        
        times = input(f'Enter the processing times for wafer {i+1} (format "time1,time2"): ')
        time1, time2 = map(int, times.split(','))
        wafers.append((time1, time2))

    minimum_total_time, wafer_order = schedule_wafers(wafers)
    
    print(f'The minimum total processing time is: {minimum_total_time}')
    print(f'The order of wafers is: {wafer_order}')

if __name__ == '__main__':
    main()
