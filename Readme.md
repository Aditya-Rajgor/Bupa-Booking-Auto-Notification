# Bupa Booking auto notification.

This repository provides code for automatically send a email notification, when prefered dates are availble on Bupa site.

## Disclamination

This code is provided as is, without any warranty. Use it at your own risk. It does not encourage to abuse any website and made for educational purpose only.

# Objective

Open the bupa website using Selenium and then search for the booking available for the near given post code. If the booking is available send an email notification to my email including booking link.

# Code walkthrough

The `main.py` file runs and creates bot using `botBupa.py` file, further, it opens selenium webdriver and clicks indivial booking and then search for the specific post code.
Later, it checks if the desired bookign is available, if do, it sends an email with details.

### Install the dependencies

```python
pip install -r requirements.txt
```

# Change the credentials

Add your email address and password on the alert.py file.

# Run the code.

`python main.py`

### Please check the branch `remote` to complate this setup handsfree.
