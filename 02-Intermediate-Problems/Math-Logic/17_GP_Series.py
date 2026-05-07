def gp_series(a,r,n):
  series = [a * (r**i) for i in range(n)]
  return *(series)
