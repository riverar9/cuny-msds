# DATA624 Notes

by: Richie Rivera

# 2024 09 03
Jeffery Nieman (Jeff) is the professor
- Worked at 4 Fortune 500 companies
- He started at cisco and now works as senior director at best buy
- Owns data governance and data quality

The class is a lot of work. Doing the work is the only way to be succesful. It  takes a while though.

**MEETUPS WILL BE A DISCUSSION**

We did an intro to everyone.

Everything we need to know is on brightspace. Every week is outlind on each "week" block.

**Can do homework in python**
- But the homework is specifically from an R textbook

For the textbook, use the 3rd Edition (NOT THE SECOND)

Grade will be broken down by:
1. Homework
2. Quizzes
3. Projects
4. Presentation


## Slack Channel
- 10% of grade is based on my participation in the slack channel
- Share articles and etc!
> Richie can share the fast.ai timeseries. Let them know what fast.ai is.

Signed up for the 9-17 presentation

# 2024 09 10

## Housekeeping

We'll make some slides on what we think is the most important things.
- explain concepts
    - STL, classical decomp, Loess
- Present for about 20 minutes
- Be ready for some Q&A

Slack channel is graded by general participation.
- sharing content
- responding to content
- asking questions

## Homework 1

*going through Marley's RPubs Submission*
- What is linear/multivariable regression?
    - Trying to predict something using "predictor" values.
- What is timeseries?
    - The same but wrt time.

In an example with ford's app:
    - most people remote started their car between 7-9 AM
    - most people remote started their car on weekdays
    - more remote starts in the north during the winter
    - more remote starts in the south during the summer

These patterns can be understood and classical timeseries decomposition tries to extract:
- A trend
- A season- 
- A cycle - A cycle is essentially a larger season that smaller seasons happen within.
    -   Within cars, there's a season where more sales happen during X time of the season but there's a cycle of people getting new vehicles
- the Error

**when using gg_lag(), make sure to update lags to include the entire season length. IE, monthly should be updated to at least 1:12**

ACF provides a plot of correlation scores with respect to certain lags.

- x-axis is the lags and the y is the pearson correlation score from 0-1
- **ACF should replace gg_lag(). Provides the same insight**
