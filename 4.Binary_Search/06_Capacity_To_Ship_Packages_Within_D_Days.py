"""
Problem:
Capacity to shp packages within D days

Pattern:
Binary Search

Difficulty:
Medium

--------------------------------------------------

My First Thought:
This is a problem of finding the first feasible version.

--------------------------------------------------

Observation:
The invariant is that the minimum feasible ship capacity lies between [left, right], where
left = max(weights) and right = sum(weights). During feasiblily check, current_weight never 
exceeds the candidate capacity mid.

--------------------------------------------------

Data Structure Chosen:
None

Reason:
None

--------------------------------------------------

Time Complexity:
O(nlog m) , Binary search will take log m (were m is the range of weight values) time until the 
loop terminater and for every mid value in the weight we will calculate the number of days it
take to ship the cargo. Each calculation is equal to the length of the list(weights) of length n. 

Space Complexity:
O(1), only for variale declaration

--------------------------------------------------

Learnings:
This is a kind of first bad version problem. Alss one logic help I have to take is how to 
keep the running sum going and also checking for the codition where the running sum is 
less than the mid value to calculate the number of days. Also we should take care of the 
range of values , not everytime it starts from 1.

Mistakes:

"""

def ship_within_days(weights, days):
    left = max(weights)
    right = sum(weights)

    while left < right:
        mid = (left + right) // 2
        days_used = 0
        current_weight = 0

        for weight in weights:
            if current_weight + weight > mid:
                current_weight = 0
                days_used += 1

            current_weight += weight

        if current_weight > 0:
            days_used += 1

        if days_used <= days:
            right = mid

        else:
            left = mid + 1

    return left

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

print(ship_within_days(weights, days))