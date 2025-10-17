import yfinance as yf
import pandas as pd
import numpy as np

# -----------------------------
# 1️⃣ INPUT
# -----------------------------
tickers = input("Enter stock tickers separated by commas (e.g. AAPL,MSFT,TSLA): ")
tickers = [t.strip().upper() for t in tickers.split(",")]

period = "1y"
print(f"\nFetching data for: {', '.join(tickers)} ...")

# -----------------------------
# 2️⃣ DOWNLOAD DATA
# -----------------------------
data = yf.download(tickers, period=period, auto_adjust=True)["Close"]

# -----------------------------
# 3️⃣ CALCULATE RETURNS
# -----------------------------
returns = data.pct_change().dropna()
mean_returns = returns.mean() * 252   # annualized
cov_matrix = returns.cov() * 252      # annualized covariance

# -----------------------------
# 4️⃣ PORTFOLIO ANALYSIS
# -----------------------------
weights = np.array([1/len(tickers)] * len(tickers))  # equal weights
port_return = np.dot(weights, mean_returns)
port_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

summary_df = pd.DataFrame({
    "Stock": tickers,
    "Annual Return (%)": np.round(mean_returns.values * 100, 2)
})
summary_df.loc[len(summary_df.index)] = ["Portfolio (Equal Weight)", round(port_return * 100, 2)]

# -----------------------------
# 5️⃣ EXPORT TO EXCEL
# -----------------------------
file_name = "portfolio_analysis.xlsx"
with pd.ExcelWriter(file_name, engine="openpyxl") as writer:
    data.to_excel(writer, sheet_name="Price Data")
    returns.to_excel(writer, sheet_name="Daily Returns")
    cov_matrix.to_excel(writer, sheet_name="Covariance Matrix")
    summary_df.to_excel(writer, sheet_name="Summary", index=False)

print(f"\n✅ Excel report saved as: {file_name}")
print("\nPortfolio Summary:")
print(summary_df)
print(f"\nPortfolio Volatility: {round(port_volatility*100,2)}%")
