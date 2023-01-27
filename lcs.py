def longest_substring(a, b, len_a, len_b, dp):
    if (len_a == 0 or len_b == 0):
        return 0

    if (dp[len_a][len_b] != -1):
        return dp[len_a][len_b]

    if (a[len_a-1] == b[len_b-1]):
        dp[len_a][len_b] = 1 + longest_substring(a, b, len_a-1, len_b-1, dp)

    dp[len_a][len_b] = max(longest_substring(
        a, b, len_a, len_b-1, dp), longest_substring(a, b, len_a-1, len_b, dp))

    return dp[len_a][len_b]


a = input("Enter String A ===    ")
b = input("Enter String B ===    ")

len_a = len(a)
len_b = len(b)

dp = [[-1 for i in range(len_b + 1)] for j in range(len_a + 1)]

print(longest_substring(a, b, len_a, len_b, dp))
