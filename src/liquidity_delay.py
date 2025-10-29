import yfinance as yf
import pandas as pd

def get_coin_data(symbol, period="60d", interval="1h"):
    df = yf.download(symbol, period=period, interval=interval)
    df['return'] = df['Close'].pct_change().fillna(0)
    df['volume_usd'] = df['Volume'] * df['Close']
    return df

def analyze_coin(altcoin):
    btc = get_coin_data("BTC-USD")
    alt = get_coin_data(altcoin)
    
    # 对齐时间
    common_idx = btc.index.intersection(alt.index)
    btc_r = btc.loc[common_idx, 'return'].values
    alt_r = alt.loc[common_idx, 'return'].values
    vol = alt.loc[common_idx, 'volume_usd'].mean()
    
    # 1. 延迟 τ*
    corr = [np.corrcoef(alt_r[:-τ] if τ > 0 else alt_r[τ:], 
                        btc_r[τ:])[0,1] if τ < len(alt_r)-10 else 0 
            for τ in range(-50, 50)]
    tau_star = np.argmax(corr) - 50
    
    # 2. 虚假 TE: T_{ALT → BTC}(τ*)
    te_false = compute_te(btc_r, alt_r, delay=tau_star)
    
    # 3. 真实 TE: T_{BTC → ALT}
    te_true = compute_te(alt_r, btc_r, delay=0)
    
    return {
        'coin': altcoin,
        'liquidity': vol,
        'delay': abs(tau_star),
        'TE_false': te_false,
        'TE_true': te_true,
        'r_ratio': te_false / te_true if te_true > 1e-6 else np.inf
    }
