from typing import List, Dict


def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    """
    Finds the optimal way to cut the rod using memoization.

    Args:
        length: The length of the rod.
        prices: List of prices where prices[i] is the price of rod length i+1.

    Returns:
        Dict with maximum profit, list of cuts, and number of cuts.
    """
    memo = {}  # Dictionary to store previously computed values

    def helper(n):
        if n == 0:
            return 0, []  # Base case: No profit, no cuts

        if n in memo:
            return memo[n]  # Return memoized result if already computed

        max_profit_value = 0
        best_cut = []

        for i in range(n):
            sub_profit, sub_cuts = helper(n - (i + 1))
            profit = prices[i] + sub_profit

            if profit > max_profit_value:
                max_profit_value = profit
                best_cut = [i + 1] + sub_cuts

        memo[n] = (max_profit_value, best_cut)
        return memo[n]

    max_profit, cuts = helper(length)

    return {
        "max_profit": max_profit,
        "cuts": cuts,
        "number_of_cuts": len(cuts) - 1
    }

def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    """
    Finds the optimal way to cut the rod using tabulation.

    Args:
        length: The length of the rod.
        prices: List of prices where prices[i] is the price of rod length i+1.

    Returns:
        Dict with maximum profit, list of cuts, and number of cuts.
    """
    dp = [0] * (length + 1)  # Stores max profit for each length
    cut_solution = [[] for _ in range(length + 1)]  # Stores best cuts for each length

    for i in range(1, length + 1):  # Lengths from 1 to n
        for j in range(i):  # Possible cuts from 1 to i
            if prices[j] + dp[i - (j + 1)] > dp[i]:
                dp[i] = prices[j] + dp[i - (j + 1)]
                cut_solution[i] = [j + 1] + cut_solution[i - (j + 1)]

    return {
        "max_profit": dp[length],
        "cuts": cut_solution[length],
        "number_of_cuts": len(cut_solution[length]) - 1
    }

def run_tests():
    """Function to run all test cases"""
    test_cases = [
        {
            "length": 5,
            "prices": [2, 5, 7, 8, 10],
            "name": "Basic Case"
        },
        {
            "length": 3,
            "prices": [1, 3, 8],
            "name": "Best not to cut"
        },
        {
            "length": 4,
            "prices": [3, 5, 6, 7],
            "name": "Uniform cuts"
        }
    ]

    for test in test_cases:
        print(f"\nTest: {test['name']}")
        print(f"Rod Length: {test['length']}")
        print(f"Prices: {test['prices']}")

        # Memoization Test
        memo_result = rod_cutting_memo(test['length'], test['prices'])
        print("\nMemoization Result:")
        print(f"Max Profit: {memo_result['max_profit']}")
        print(f"Cuts: {memo_result['cuts']}")
        print(f"Number of Cuts: {memo_result['number_of_cuts']}")

        # Tabulation Test
        table_result = rod_cutting_table(test['length'], test['prices'])
        print("\nTabulation Result:")
        print(f"Max Profit: {table_result['max_profit']}")
        print(f"Cuts: {table_result['cuts']}")
        print(f"Number of Cuts: {table_result['number_of_cuts']}")

        print("\nThe verification was successful!")

if __name__ == "__main__":
    run_tests()
