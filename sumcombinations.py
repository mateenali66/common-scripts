def buying_candy( amount_of_money ) :
	if amount_of_money == 0:
		return 0
	if amount_of_money < 2:
		return 1
	prices= [1, 2]	
	dp = { 0: 1 }
	for total in range(1, amount_of_money + 1):
		dp[total] = 0
		for n in prices:
			dp[total] += dp.get(total - n, 0)
			
	return dp[amount_of_money]
