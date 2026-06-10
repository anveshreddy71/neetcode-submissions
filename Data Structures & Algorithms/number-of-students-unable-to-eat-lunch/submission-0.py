class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i=0
        l_original = len(students)
        l= len(students)
        while i<l:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                i=0
                l= l-1
            else:
                last = students.pop(0)
                students.append(last)
                i=i+1
        return l


        