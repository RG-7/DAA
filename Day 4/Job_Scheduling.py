# Day 4
# February 05, 2024
# Design & Analysis of Algorith

#Job Sequencing Problem
jobs_id = ['J1','J2','J3','J4','J4','J5','J6','J7','J8','J9']
jobs_profit = [15,20,30,18,18,10,23,16,25]
jobs_deadline = [7,2,5,3,7,5,2,7,3]

# Combine the three lists into a single list of tuples
jobs = list(zip(jobs_id, jobs_profit, jobs_deadline))

jobs.sort(key=lambda x: x[1],reverse=True)

# Extract the sorted lists
sorted_jobs_id, sorted_jobs_profit, sorted_jobs_deadline = zip(*jobs)

