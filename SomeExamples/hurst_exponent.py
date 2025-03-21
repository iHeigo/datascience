from hurst import compute_Hc
import numpy as np

# Simulated stock prices (random walk)
np.random.seed(42)
stock_prices = np.cumsum(np.random.randn(1000)) + 1000  # Random walk

# Calculate Hurst Exponent
H, c, data = compute_Hc(stock_prices, kind='price')

print("Hurst Exponent:", H)

# Interpretation:
# - H ≈ 0.5 → Random (unpredictable, like coin flips)
# - H < 0.5 → Mean-reverting (reverts back, like bouncing ball)
# - H > 0.5 → Trending (follows a pattern, like a growing stock)
