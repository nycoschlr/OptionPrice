import math
import pandas as pd
from scipy.stats import norm
import tkinter as tk

def black_scholes_merton(S, K, r, T, sigma):
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    call_price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    put_price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

    return call_price, put_price

def calculate_option_prices():
    # Get input values from the GUI
    stock_price = float(stock_price_entry.get())
    risk_free_rate = float(risk_free_rate_entry.get())
    time_to_maturity = float(time_to_maturity_entry.get())
    volatility = float(volatility_entry.get())
    strike_prices = [float(sp) for sp in strike_prices_entry.get().split(',')]

    # Calculate option prices for each strike price
    option_prices = []
    for strike_price in strike_prices:
        call_price, put_price = black_scholes_merton(stock_price, strike_price, risk_free_rate, time_to_maturity, volatility)
        option_prices.append((strike_price, round(call_price, 2), round(put_price, 2)))  # Round the prices

    # Create a pandas DataFrame for the option prices
    df = pd.DataFrame(option_prices, columns=['Strike Price', 'Call Price', 'Put Price'])

    # Display the DataFrame in the GUI window
    result_text.delete(1.0, tk.END)  # Clear previous results
    result_text.insert(tk.END, df)

# Create the main window
root = tk.Tk()
root.title("Option Pricing")

# Create labels and entry fields for input values with descriptions
tk.Label(root, text="Stock Price:").grid(row=0, column=0, sticky="E")
stock_price_entry = tk.Entry(root)
stock_price_entry.grid(row=0, column=1)
tk.Label(root, text="(e.g., 100.0)").grid(row=0, column=2, sticky="W")

tk.Label(root, text="Risk-Free Rate:").grid(row=1, column=0, sticky="E")
risk_free_rate_entry = tk.Entry(root)
risk_free_rate_entry.grid(row=1, column=1)
tk.Label(root, text="(e.g., 0.05 for 5%)").grid(row=1, column=2, sticky="W")

tk.Label(root, text="Time to Maturity:").grid(row=2, column=0, sticky="E")
time_to_maturity_entry = tk.Entry(root)
time_to_maturity_entry.grid(row=2, column=1)
tk.Label(root, text="(e.g., 1.0 for 1 year)").grid(row=2, column=2, sticky="W")

tk.Label(root, text="Volatility:").grid(row=3, column=0, sticky="E")
volatility_entry = tk.Entry(root)
volatility_entry.grid(row=3, column=1)
tk.Label(root, text="(e.g., 0.2 for 20%)").grid(row=3, column=2, sticky="W")

tk.Label(root, text="Strike Prices (comma-separated):").grid(row=4, column=0, sticky="E")
strike_prices_entry = tk.Entry(root)
strike_prices_entry.grid(row=4, column=1)
tk.Label(root, text="(e.g., 90, 95, 100)").grid(row=4, column=2, sticky="W")

# Create a button to calculate option prices
calculate_button = tk.Button(root, text="Calculate", command=calculate_option_prices)
calculate_button.grid(row=5, column=1, pady=10)

# Create a text widget to display the table with results
result_text = tk.Text(root, width=40, height=10)
result_text.grid(row=6, column=0, columnspan=3, pady=10)

# Run the main window loop
root.mainloop()

