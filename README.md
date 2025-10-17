# Portfolio-Risk-Return-Analyzer
A Python-based finance project that analyzes stock performance, calculates portfolio returns and risk, and exports a full analytical report to Excel.

This project helps investors and finance enthusiasts evaluate how different stocks perform individually and together in a portfolio.
It retrieves real market data using the yfinance API, calculates key financial metrics such as annualized return, volatility, and covariance, and generates a clean Excel report with all insights.

**-Key Features**

 Fetches live historical stock data from Yahoo Finance

 Automatically generates an Excel report

Supports one or multiple stocks

Applies core financial concepts like diversification and risk-return analysis

**-Example Stock Symbols (Ticker Codes)**
Company Name	               Ticker Symbol
Apple Inc.	                      [AAPL], 
Microsoft Corp.	                  [MSFT],
Tesla Inc.           	            [TSLA],
Amazon.com Inc.	                  [AMZN],
NVIDIA Corp.	                    [NVDA],
Alphabet (Google)	              [GOOG or GOOGL],

You can input any of these tickers (or others) to analyze their financial performance.

**-Example Use Case**

1. You can input multiple stock tickers such as:

AAPL, MSFT, TSLA

2. The program will:

Download their last 1 year of daily prices

3. Compute each stock’s annual return and volatility

Calculate the portfolio’s overall risk and performance

Save everything in a file named portfolio_analysis.xlsx

