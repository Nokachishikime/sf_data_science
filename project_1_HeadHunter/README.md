# Project 1 HeadHunter data analysis

## List of contents

[1. Project description](https://github.com/Nokachishikime/sf_data_science/tree/main/project_0/README.md#Project-description)

[2. What case we are solwing?](https://github.com/Nokachishikime/sf_data_science/tree/main/project_0/README.md#What-case-we-are-solwing)

[3. Shorts about data](https://github.com/Nokachishikime/sf_data_science/tree/main/project_0/README.md#Shorts-about-data)

[4. Project stages](https://github.com/Nokachishikime/sf_data_science/tree/main/project_0/README.md#Project-stages)

[5. Results](https://github.com/Nokachishikime/sf_data_science/tree/main/project_0/README.md#Results)

[6. Conclusions](https://github.com/Nokachishikime/sf_data_science/tree/main/project_0/README.md#Conclusions)


### Project description
Skills practice on dataset containing information abouts candidates from HeadHunter.

:arrow_up:[to list of contents](https://github.com/Nokachishikime/sf_data_science/tree/main/project_0/README.md#List-of-contents)

### What case we are solwing?
We need to make preparations on raw data for futher model creation.   
All the anomalies, outlying data and duplicates should be detected and deleted.
Also some empty cells should be filled with sintetic data.

**Terms:**

We could use only libriares given earlyer in the course:
- pandas
- numpy
- matplotlib.pyplot
- seaborn
- plotly.express
- re

Also we should follow given roadmap from teamplate Jupiter Notebook.

**Quality metrics**

Results evaluates on expert opinion.

**Practice goal**

Nice and clean code on Python writing practice

IDE working practice

GitHub working practice

Data visualization practice

Conclusions making practice

:arrow_up:[to list of contents](https://github.com/Nokachishikime/sf_data_science/tree/main/project_0/README.md#List-of-contents)

### Shorts about data

44744 records with raw information about candidates, with a gaps in cells.   

Each record has following structure:      
0   Пол, возраст   
1   ЗП   
2   Ищет работу на должность:   
3   Город, переезд, командировки   
4   Занятость   
5   График   
6   Опыт работы   
7   Последнее/нынешнее место работы   
8   Последняя/нынешняя должность   
9   Образование и ВУЗ   
10  Обновление резюме   
11  Авто   
   
All the records are strings, except empty cells.

:arrow_up:[to list of contents](https://github.com/Nokachishikime/sf_data_science/tree/main/project_0/README.md#List-of-contents)

### Project stages

Data structure investigation   
Data transformation   
Data dependences investigation   
Data cleaning   

:arrow_up:[to list of contents](https://github.com/Nokachishikime/sf_data_science/tree/main/project_0/README.md#List-of-contents)

### Results

Dataset acceptable for futher modeling.

:arrow_up:[to list of contents](https://github.com/Nokachishikime/sf_data_science/tree/main/project_0/README.md#List-of-contents)

### Conclusions

First, the data was processed, and on the basis of the initial information, attributes that were convenient in the future were constructed.
Secondly, an exploratory analysis was carried out, the results of which revealed suspicious entries in the table.
And, finally, the data was cleaned from both service columns and suspicious records.

:arrow_up:[to list of contents](https://github.com/Nokachishikime/sf_data_science/tree/main/project_0/README.md#List-of-contents)