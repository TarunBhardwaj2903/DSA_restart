class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        k = r - l + 1
        m = 2 * k

        def mat_mul(A, B):
            C = [[0] * m for _ in range(m)]

            for i in range(m):
                Ai = A[i]
                Ci = C[i]

                for t in range(m):
                    if Ai[t] == 0:
                        continue

                    at = Ai[t]
                    Bt = B[t]

                    for j in range(m):
                        if Bt[j]:
                            Ci[j] = (Ci[j] + at * Bt[j]) % MOD

            return C

        def mat_pow(MAT, power):
            R = [[0] * m for _ in range(m)]

            for i in range(m):
                R[i][i] = 1

            while power:
                if power & 1:
                    R = mat_mul(R, MAT)

                MAT = mat_mul(MAT, MAT)
                power >>= 1

            return R

        # Transition matrix
        T = [[0] * m for _ in range(m)]

        # up[v] <- down[u], u < v
        for v in range(k):
            row = v
            for u in range(v):
                T[row][k + u] = 1

        # down[v] <- up[u], u > v
        for v in range(k):
            row = k + v
            for u in range(v + 1, k):
                T[row][u] = 1

        # state for length 2
        S = [0] * m

        for v in range(k):
            S[v] = v
            S[k + v] = k - 1 - v

        P = mat_pow(T, n - 2)

        final_state = [0] * m

        for i in range(m):
            total = 0
            Pi = P[i]

            for j in range(m):
                total = (total + Pi[j] * S[j]) % MOD

            final_state[i] = total

        return sum(final_state) % MOD