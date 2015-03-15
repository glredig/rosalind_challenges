def mendel():
	k = float(raw_input("K: "))
	m = float(raw_input("M: "))
	n = float(raw_input("N: "))

	total = k + m + n

	prob_k_k = (k / total) * ((k - 1) / (total - 1))
	prob_k_m = (k / total) * (m / (total - 1))
	prob_k_n = (k / total) * (n / (total - 1))

	prob_m_k = (m / total) * (k / (total - 1))
	prob_m_m = (m / total) * ((m - 1) / (total - 1)) * .75
	prob_m_n = (m / total) * (n / (total - 1)) * .5

	prob_n_k = (n / total) * (k / (total - 1))
	prob_n_m = (n / total) * (m / (total - 1)) * .5

	print prob_k_k + prob_k_m + prob_k_n + prob_m_k + prob_m_m + prob_m_n + prob_n_k + prob_n_m
	
mendel()   
