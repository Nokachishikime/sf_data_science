# Project 3 Booking review score model

## List of contents

[1. Project description](https://github.com/Nokachishikime/sf_data_science/tree/main/Project_3_Booking/README.md#Project-description)

[2. What case we are solwing?](https://github.com/Nokachishikime/sf_data_science/tree/main/Project_3_Booking/README.md#What-case-we-are-solwing)

[3. Shorts about data](https://github.com/Nokachishikime/sf_data_science/tree/main/Project_3_Booking/README.md#Shorts-about-data)

[4. Project stages](https://github.com/Nokachishikime/sf_data_science/tree/main/Project_3_Booking/README.md#Project-stages)

[5. Results](https://github.com/Nokachishikime/sf_data_science/tree/main/Project_3_Booking/README.md#Results)

[6. Conclusions](https://github.com/Nokachishikime/sf_data_science/tree/main/Project_3_Booking/README.md#Conclusions)


### Project description
Model creation for Booking.com to predict review score for the hotel.

:arrow_up:[to list of contents](https://github.com/Nokachishikime/sf_data_science/tree/main/Project_3_Booking/README.md#List-of-contents)

### What case we are solwing?
We need to make preparations on raw data for futher model creation, including:.   
- basic analysys;
- data transformation;
- emply cells filling;
- feature selection; 
- categorial features encoding;
- feature scaling;
- feature significance analysys.

**Terms:**

We should save all the rows, no matter if they are outliers or duplicates.

Also we should follow given roadmap from teamplate Jupiter Notebook called Baseline to evaluate our efforts.

**Quality metrics**

MAPE - mean absolute persantage error, calculated after applying model to test dataset.

**Practice goal**

Nice and clean code on Python writing practice

IDE working practice

GitHub working practice

Data visualization practice

Conclusions making practice

Natural language processing, geocoding, feature encoding, feature scaling, featyre significance analysys

Mashine learning basics practice.

Keggle competition experience.

:arrow_up:[to list of contents](https://github.com/Nokachishikime/sf_data_science/tree/main/Project_3_Booking/README.md#List-of-contents)

### Shorts about data

386803 records with raw information about hotels reviews from Booking.com users.   

Each record has following structure:      
 0   hotel_address                               386803 non-null  object   
 1   additional_number_of_scoring                386803 non-null  int64   
 2   review_date                                 386803 non-null  object   
 3   average_score                               386803 non-null  float64   
 4   hotel_name                                  386803 non-null  object   
 5   reviewer_nationality                        386803 non-null  object   
 6   negative_review                             386803 non-null  object   
 7   review_total_negative_word_counts           386803 non-null  int64   
 8   total_number_of_reviews                     386803 non-null  int64   
 9   positive_review                             386803 non-null  object   
 10  review_total_positive_word_counts           386803 non-null  int64   
 11  total_number_of_reviews_reviewer_has_given  386803 non-null  int64   
 12  reviewer_score                              386803 non-null  float64   
 13  tags                                        386803 non-null  object   
 14  days_since_review                           386803 non-null  object   
 15  lat                                         384355 non-null  float64   
 16  lng                                         384355 non-null  float64   

 There ara a bunch og non-numeric features, and some empty cells in dataset.

:arrow_up:[to list of contents](https://github.com/Nokachishikime/sf_data_science/tree/main/Project_3_Booking/README.md#List-of-contents)

### Project stages

0. Lib improt   
1. Data import   
2. Data basic information   
3. Data transform   
4. Correlation analysys
5. Features scaling
6. Model learning
7. Model evaluation

:arrow_up:[to list of contents](https://github.com/Nokachishikime/sf_data_science/tree/main/Project_3_Booking/README.md#List-of-contents)

### Results

Commit for Kaggle competition.

---

:arrow_up:[to list of contents](https://github.com/Nokachishikime/sf_data_science/tree/main/Project_3_Booking/README.md#List-of-contents)

### Conclusions

Kaggle expirience gone wrong - I lost my progress with Notebook, and has had to go back to local solution.
Also, not all the libs were available.

My score was not on the top. Probably i will make some impruvements later - i see some interesting but complex directions to mine more data from given information.

But, at all, it was interesting and challenging task.

:arrow_up:[to list of contents](https://github.com/Nokachishikime/sf_data_science/tree/main/Project_3_Booking/README.md#List-of-contents)