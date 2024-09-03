# Slide 1: Title
Hi my Name is Richie and today we will be going over the saftety of vehicles. As some of you may be aware, NYC and other cities across the country are implementing Vision 0 initiatives in order to reduce the number of people seriously hurt or killed by cars to 0.

There are a growing number of articles that suggest that cars are growing larger and heavier. In addition to the obvious eviornmental cost there seems to be a human cost associated with this. In this report, we will undertake an observational statistical study to invesitgate whether crashes involving larger vehicles have a statistically significant increased liklihood to cause injury or death.

# Slide 2: Abstract

--SKIP

# Slide 3: Data

- We will be analyzing the "Motor Vehicle Collisions - Crashes" dataset provided by the City of New York.
- This dataset contains 2,084,770 observations, spanning from July 2012 through the end of April 2024 and contains records of vehicular crashes reported by the NYPD.
- Each observation in the dataset represents a single crash incident.
- Among these, there are 1,651 unique entries for vehicle class, indicating the diversity of vehicle types involved in the crashes.
- Key variables of interest include the number of people killed and injured in each crash.

- For the purpose of our analysis, we will categorize each vehicle class into one of three groups: "Passenger Vehicle", "SUV/Pickup Truck", or "Other".
- This grouping allows us to simplify the analysis and focus on broader vehicle categories that are relevant to our research question.

# Slide 4: Research Question

- Objective: Determine if there's a statistically significant difference in crash incidents among vehicles of different body types when a crash results in injury or fatality.
- Definition: An incident is defined as a crash where at least one person is injured or killed.
- Method: Analyze the total incidents (dependent variable) by vehicle class (independent variable).
- Hypotheses:
  - Null Hypothesis (H0): There is no difference in incident rates across different vehicle classes.
  - Alternative Hypothesis (H1): There is a difference in incident rates across different vehicle classes.
- Goal: Understand the potential impact of vehicle type on crash outcomes.

# Slide 5: Summary Statistics

- Incident Mean across the groups
  - Other - 1.22
  - Passenger Vehicle - 1.39
  - SUV/Pickup Truck - 1.38

- Killed mean across the groups
  - Other - 5.124 / K Crashes
  - Passenger Vehicle - 4.825 / K Crashes
  - SUV/Pickup Truck - 6.235 / K Crashes

# Slide 6: Histogram of Incidents

- It's bounded at 1 as our definition for incident means that at least one person needed to be affected

- The vast majority of incidents only involved one person

- Really hard to make a case here that it's normal

# Slide 7: Histogram of Log Incidents

- By taking the log, we can manipulate the datasetset to be much more normal. Although it's still very right-skewed

- We can at least try to see if this distribution is normal-ish

# Slide 8: QQ Plot of Log Incidents

- From here, we can see that the QQ Plot is kinda diagonal.

- Although it is pretty far from perfectly normal, we are going to take the leap of faith that it's normal enough to continue.

# Slide 9: Requirements for ANOVA

- From the definition of the dataset, these events are independent within and across groups
- We have taken our leap of faith on normality
- The variability across the groups is about equal
    - We satisfied this by looking at how the distributions tapered off very quickly.
    - I intended to use a box plot but the 3rd quartile was at 1, making it a poor visualizaiton

# Slide 10: ANOVA Results for log of Incidents

- From here, we can see that our F-Value is 2031 which is stating that there is a difference in the number of incidents
- The low p value of essentially 0 shows that the results are statistically significant.

# Slide 11: Regression of the Results

- Going over coefficents:
  - Passenger Vehicles - 0.010
  - SUV/Pickup Trucks - 0.089
  - Y-intercept - 0.12

- Adjusted R Squared
  - 0.008 suggests that vehicle type only accounts for 0.8% of the observed variance
  - P value of essentially 0 suggests that our result is statistically signficant

# Slide 12: Conclusion

- Findings: Passenger vehicles exhibited the highest mean number of incidents, suggesting they are more likely to be involved in crashes (1.390 incidents vs 1.377 for other vehicle types).

- National Statistics: In 2021, according to NHTSA, there were 42,939 fatalities and 2,497,657 injuries in car crashes nationwide.

- Importance: Recognizing the significance of every life, it's crucial to understand how vehicle choices impact people's lives.

# Slide 13: Total Monthly Crashes by Vehicle Category

- This graph just shows the number of total crashes by month

- Passenger Vehicles and Other have actually had decreases over time

- SUV/Pickup Trucks have increased quickly over time

- This speaks to the reason why this analysis and analysis of this type are important as these vehicle choices are changing and impacting people's lives in different ways

# Slide 14: Limitations & Next Steps

- Scope: The analysis focused solely on crash data from New York City, suggesting that results may differ across various levels of government and locations.

- Future Research: Next, exploring fatality rates across different vehicles could be insightful. The statistical summary reveals that SUV/Pickup Trucks have a higher fatality rate compared to other vehicle types (0.006235 vs 0.004825).

- Significance: If the difference in mean fatality rates across vehicle types is statistically significant, it could provide evidence that SUV/Pickup Trucks are more fatal.