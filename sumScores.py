class Solution:
	def sumScores(self, s: str) -> int:
		def calculate_z_array(s):
			N = len(s)
			Z = [0] * N
			L, R = 0, 0
			for i in range (1, N):
				if i > R:
					L = R = i
					while R < N and s[R - L] == s[R]:
						R += 1
					R -= 1
					Z[i] = R - L + 1
				else:
					k = i - L
					if Z[k] + i <= R:
						Z[i] = Z[k]
					else:
						L = i
						while R < N and s[R - L] == s[R]:
							R += 1
						R -= 1
						Z[i] = R - L + 1
			return Z

		z_array = calculate_z_array(s)
		return sum(z_array) + len(s)
