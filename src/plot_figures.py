import matplotlib.pyplot as plt

# 复现论文 Fig.1(b) 风格
plt.figure(figsize=(10,6))
plt.subplot(1,2,1)
plt.scatter(df['liquidity'], df['delay'], s=100, c='blue', alpha=0.7)
plt.xlabel('Liquidity (Avg Volume USD)')
plt.ylabel('Delay τ* (hours)')
plt.title('Your Insight: Lower Liquidity → Larger Delay')
plt.xscale('log')

plt.subplot(1,2,2)
plt.scatter(df['delay'], df['TE_false'], s=100, c='red', alpha=0.7)
plt.xlabel('Delay τ* (hours)')
plt.ylabel('Spurious TE: T_{ALT→BTC} (bits)')
plt.title('Paper Prediction: Larger Delay → Larger Spurious TE')

plt.tight_layout()
plt.savefig("results/your_insight_vs_smirnov2013.png", dpi=300)
plt.show()
