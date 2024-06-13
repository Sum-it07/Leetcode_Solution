class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        # Sort both lists
        seats.sort()
        students.sort()
        
        # Calculate the total number of moves required
        count = 0
        for i in range(len(students)):
            count += abs(seats[i] - students[i])
        
        return count
