from liquidity_delay import analyze_coin
import pandas as pd

# 你的观察：选不同流动性山寨币
coins = [
    "ETH-USD",   # 高流动性
    "SOL-USD",   # 中等
    "DOGE-USD",  # 低流动性
    "SHIB-USD",  # 极低
    "PEPE1886-USD",  # 超低（如果可用）
]

results = []
for coin in coins:
    try:
        res = analyze_coin(coin)
        results.append(res)
        print(f"✓ {coin}: delay={res['delay']}h, TE_false={res['TE_false']:.3f}, r={res['r_ratio']:.1f}")
    except:
        print(f"✗ {coin} failed")

df = pd.DataFrame(results)
df.to_csv("results/crypto_te_analysis.csv", index=False)
