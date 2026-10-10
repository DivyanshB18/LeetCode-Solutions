class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def solve(ind, total, brackets, result):
            if ind >= len(brackets):
                if total == 0:
                    result.append("".join(brackets))
                return

            if total > len(brackets) // 2:
                return
            elif total < 0:
                return

            brackets[ind] = "("
            sum = total + 1
            solve(ind + 1, sum, brackets, result)

            brackets[ind] = ")"
            sum = total - 1
            solve(ind + 1, sum, brackets, result)

        brackets = [""] * (2 * n)
        result = []
        solve(0, 0, brackets, result)
        return result