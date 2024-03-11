# AnomalousCongress
Experimenting if anomalies in congressional trading patterns can be used as a trading signal in US equity markets.

This project is to develop a method for anomaly detection of congressional trades as a trading strategy.

The avenues to explore:
* Different anomaly detection methods
    * Rules based
    * Machine learning

* Different things to compare to for anomaly
    * Streetwide activity
    * Other members of congress
    * Their own trading habits

We will use predominantly Python.

There will be 3 portions of this project:
- 1:
    - Pulling in financial data and using google sheets as the database
- 2: 
    - Trying some anomaly detection to flag anomalous congress trades.
    - This can be heavily expanded upon with different congressmen/women and trading ideas.
- 3: 
    - Creating an index to mimic those trades and then test on composer.trade