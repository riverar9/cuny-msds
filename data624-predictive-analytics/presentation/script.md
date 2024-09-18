# Slide 1 - SEATS Decomposition

- Similar to X11 and Classical deocmposition, SEATS is another method to perform timeseries decomposition.

- SEATS stands for SEASONAL Extraction in ARIMA Time Series, using a model-based approach to time series deconstruction.

- Once an ARIMA model is fit to the data, SEATS breaks it out to its components.

- Developed by the Bank of Spain and is used widely by governement agencies.

- Although we will go over ARIMA in Weeks 7 & 8, just know for now that SEATS is better at handling random fluctuations, making it a great choice for noisier data. This is due to the ARIMA model which takes into consideration how past values could affect future ones.

- This give SEATS more ability to extract evolving patterns. This makes me belive that it may be a specifically good decomposition model for stock price predictions as they are full of randomness and whose future values are affected by past values.

- SEATS typically outperforms Classical and X11 decomposition on real world data as it's able to remove noise and adjust for randomness by using ARIMA.

- To conclude on SEATS, it's a powerful decomposition method as it leverages a statistically sound method to decompose timeseries and can handle complex and evolutionary patterns.

# Slide 2 - STL Decomposition

- The last timeseries decomposition method we'll discuss is STL Decomposition.

- STL stands for Seasonal and Trend decomposition using Loess is a method that fits smooth, non-linear relationships to data. Loess, refers to a regression method that it uses.

    - Loess is a regression method that it essentially creates multiple localized linear regression models which makes it helpful for non-linear data.

- This means that STL can capture more flexible patterns. Pratically, this means that STL is especially good at handling changing trends or seasonal patterns over time.

- Something about STL that makes it attractive is it's customizability. When using it, the user must specify two parameters:
1. The trend-cycle window
    - The trend-cycle window controls how quickly the trend can change over time. A smaller window will result in a trend that changes quicker to changes in the data whle a larger window will smooth out changes.
2. The seasonal-window
    - The seasonal window controls how quickly the seasonal components can change. A smaller window allows seasonal componets to change more quickly


# Slide 3 - Pros and Cons of STL Decomposition

##### Pros:

- It is very flexible since it can handle all types of seasonality.
- Not just monthly or quarterly like X-11 and SEATS. Making it a good choice for time sereis with more irregular or complex seasonal cycles.

- The seasonal and trend components can change at a rate defined by the user. This allows you to control how dynamic the seasonality is and how the component will adapt to changes.

- The smoothness of the trend can be controlled by updating hte trend-cycle.

- Lastly, outliers won't distort the seasonal and trend components. This is very useful for handling data with occasional anomalies.

##### Cons:

- STL still isn't perfect.

- It can not natively handle multiplicative decompositons. This means that you will likely need to perform a Box-Cox transform first in order to handle multiplicative patterns.
    - an example of a multiplicative pattern would be retails sales that increase greatly during holiday seasons. Where the size of seasonal increase grows as year over year sales increase.

- STL doesn't automatically adjust for calendar variations. This means that you will need to manually adjust for events such as holidays or work-day fluctuations.
    - A way to account for work-day fluctuations in the retail sales context would be to use averaage average daily sales 

- STL conclusion:
    -   Before we close out, STL Decomposition uses Loess regression method which makes it a good choice for non-linear patterns in time series data. It's especially powerful as you can specify how quickly trends and seasonal factors can change to the data.