
### Maxwell Berry / 1219830248

#### Overview
This Python script schedules wafer processing tasks across two stations to minimize the total processing time. 
Each wafer has specific processing times for two different stations. The code sorts and schedules the wafers 
based on their processing times to ensure optimal processing sequence.

#### How to Run the Code

1. **Requirements:**
   - Python 3.x must be installed.

2. **Execution:**
   - Open your terminal or command prompt.
   - Navigate to the directory containing the script.
   - Run the script by typing `python wafer_scheduling.py`.
   - Follow the on-screen prompts to input the number of wafers and their respective processing times.

3. **Inputs:**
   - First, you'll be prompted to enter the number of wafers you wish to schedule.
   - For each wafer, enter the processing times for station 1 and station 2, separated by a comma (e.g., `3,5`).

4. **Output:**
   - The script will output the minimum total processing time to complete all wafers and the optimal 
     order in which the wafers should be processed (Note: there may be instances where two or more orders will
     result in the same minimum processing time. In this case, it will only output the first order found).

#### Code Analysis

1. **Functionality:**
   - The `schedule_wafers` function takes a list of tuples, where each tuple represents the processing times for a 
     wafer at two stations.
   - Wafers are first categorized into two groups based on which station (first or second) has the shorter processing time.
   - Wafers are then sorted within these groups: those processed first by their time at station 1, and those processed 
     later by their time at station 2 in descending order.
   - The script then schedules the wafers sequentially, calculating the total processing time by simulating the processing 
     at both stations.

2. **Complexity Analysis:**
   - Sorting operations (`sort()`) dominate the complexity, which is O(n log n), where n is the number of wafers.
   - The final loop that calculates the total processing time is O(n).
   - Therefore, the overall time complexity of the algorithm is O(n log n).

#### Example

- **Input:**
  ```
  Enter the number of wafers: 3
  Enter the processing times for wafer 1 (format "time1,time2"): 2,3
  Enter the processing times for wafer 2 (format "time1,time2"): 4,1
  Enter the processing times for wafer 3 (format "time1,time2"): 5,2
  ```

- **Output:**
  ```
  The minimum total processing time is: 12
  The order of wafers is: [1, 3, 2]
  ```