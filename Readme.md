# Bupa Booking auto notification.

## Motivation

I had to book my medical appointment, however, I had to check every now and then for the slot availibility. It was boring and frustrating at the same time. Moreover, I was going on a work trip, and I had little to no-time to check website every 5 minute and I cannot rely on luck either!!!

Thus, I decided to code and automate the process a day before my work trip and made it complete automated, so that I can focus on my work and don't have to worry about anything.

## Introduction

This repository provides code for automatically send a email notification, when prefered dates are availble on Bupa site, and it runs hands-free on pythonanywhere server.

To make it complete automated, you need to purchase a subscription on pythonanywhere, that costs 5$/month at the time of writing.

## Disclamination

This code is provided as is, without any warranty. Use it at your own risk. It does not encourage to abuse any website and made availabel for educational purpose only. I do not endorse any website or tools that are mentioned in this source code.

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

Add your email address and password on the `alert.py` file.

# Run the code.

### For `pythonanywhere` active the environment first by

`workon myvirtualenv` and then run the file.

`python main.py`

### Please check the branch `master` to basic code.
