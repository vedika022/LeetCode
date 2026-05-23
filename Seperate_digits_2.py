class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer=[]

        def twodigit(i):
            answer.append(i//10)
            answer.append(i%10)

        def threedigit(i):
            answer.append(i//100)
            twodigit(i%100)

        def fourdigit(i):
            answer.append(i//1000)
            threedigit(i%1000)

        for i in nums:
            if 10 > i > -1 :
                answer.append(i)
            elif 100 > i > 9 :
                twodigit(i)
            elif 1000> i > 99 :
                threedigit(i)
            elif 10000 > i > 999 :
                fourdigit(i)
            elif 100000 > i > 9999:
                answer.append(i//10000)
                fourdigit(i%10000)
            else :
                print("error")
        return answer
        