# public class MaxProduct {
#
#     public static void main(String ... args) {
#         System.out.println(solve(args[0], Integer.parseInt(args[1])));
#     }
#
#     static long solve(String digits, int k) {
#         if (k == 0)
#             return Long.parseLong(digits);
#
#         int N = digits.length();
#         long[][] T = new long[N][k+1];
#         for (int i = 0; i < N; i++) {
#             T[i][0] = Long.parseLong(digits.substring(0,i+1));
#             for (int j = 1; j <= Math.min(k,i); j++) {
#                 long max = Integer.MIN_VALUE;
#                 for (int a = 0; a < i; a++) {
#                     long l = Long.parseLong(digits.substring(a+1,i+1));
#                     long prod = l * T[a][j-1];
#                     max = Math.max(max, prod);
#                 }
#                 T[i][j] = max;
#             }
#         }
#         return T[N-1][k];
#     }
# }

def multiply(str,k):
    n = len(str)
    T = [[0]* (k+1) for j in range(n)]

    for i in range(n):
        T[i][0] = str[0:i+1]
        for j in range(1, min(k,i)):
            maximum = float("-inf")
            for a in range(0,i):
                l = int(str[a+1:i+1])
                print (T[a][j-1])
                prod = l*int(T[a][j-1])
                maximum  = max(maximum,prod)

            T[i][j] = maximum

    return T[n-1][k]

    print (T)

print (multiply("1234",2))