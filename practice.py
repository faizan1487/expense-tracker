class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        len_pre = len(prerequisites) * 2

        if len_pre == 0:
            return True

        pre_pre_req = {}
        course_nums = set()

        for i in prerequisites:
            if i[0] == i[1]:
                return False
            print("i", i)
            # [[1,0],[0,2],[2,1]]
            course_nums.add(i[0])
            course_nums.add(i[1])
            print("pre_pre_req", pre_pre_req)
            print("i[0]", i[0])
            if i[0] in pre_pre_req:
                print("in pre pre req")
                print("pre_pre_req[i[0]]", pre_pre_req[i[0]][0])
                prev_req = pre_pre_req[i[0]][0]
                if i[1] in pre_pre_req[i[0]]:
                    return False
                elif prev_req in pre_pre_req:
                    if i[1] in pre_pre_req[prev_req]:
                        return False
                else:
                    if i[1] in pre_pre_req:
                        pre_pre_req[i[1]].append(pre_pre_req[i[0]])
                    else:
                        include_prev_req = list(pre_pre_req[i[0]])
                        print(" before include pre_pre_req", pre_pre_req)
                        include_prev_req.append(i[0])
                        print("pre_pre_req", pre_pre_req)
                        print("include_prev_req", include_prev_req)
                        pre_pre_req[i[1]] = include_prev_req
                        print("pre_pre_req", pre_pre_req)
            elif i[1] in pre_pre_req:
                print("elif 1")
                pre_pre_req[i[1]].append(i[0])
            else:
                pre_pre_req[i[1]] = [i[0]]

            print("pre_pre_req", pre_pre_req)
            print("---------------")

        print("len")
        print(course_nums)

        largest = max(course_nums)
        if largest < numCourses:
            return True

        return False

sol = Solution()
numCourses = 4
prerequisites = [[3,1],[0,3],[1,2],[2,0]]
print("result", sol.canFinish(numCourses, prerequisites))
