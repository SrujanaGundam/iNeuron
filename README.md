## iNeuron Internship
# Metro Interstate Prediction

### Overview 
This is a regression model for a most common dataset, Metro Interstate Prediction. Here we are predicting the traffic based on different factors like whether it a holiday or not, Temperature, Date, Clouds(%), etc.

### Motivation
Nowadays, traffic is a major issue for everyone, and it is a source of stress for anyone who has to deal with it on a daily basis. The growth of the population delays traffic and makes it worse day by day. The settlement of modern civilization looks at it, but it is unable to act in such a way as to protect people. Being stuck in a cosmopolitan city's traffic is the most common occurrence in one's life. 
To reduce the time wasted in the traffic, this model has been developed in order to give an estimate of the traffic based on the demographic data like whether it is a holiday, datae, temperature, weather and clouds(%).

### Dataset Information
The dataset contains information on holiday, temperature, rain, snow , weather description and traffic volume of Hourly Minneapolis-St Paul, MN traffic volume for westbound I-94. Includes weather and holiday features from 2012-2018.

### Technical Aspect
1. Training a RandomForestRegressor Regression model to predict defaulter as accurate as possible <br />
  a. Cleaning the datasets, fixing all features <br />
  b. Apply Regression ML model <br />
2. Building and hosting a Flask API and hosting the model Locally. <br />
  a. Build the web app using Flask API , HTML & CSS<br />
  b. Upload the project on GitHub <br />
  
  
### Installation

The Code is written in Python 3.7. To install the required packages and libraries, run this command in the project directory after cloning the repository:

```
pip install -r requirements.txt
```


### Directory Tree
```  
├── server and client<br />
    └── artifacts <br/>
         └──weather.json <br/>
    └──templates <br/>
         └──index.html <br/>
    └──server.py <br/>
    └──util.py <br/>
├── HLD document <br />
├── LLD Document <br />
├── Detailed Description Presentation <br />
├── wireframe.jpg <br />
├── README.md <br />
└── requirements.txt <br />
└── Architecture.jpg <br />
```
  
 ### Technologies Used
  
  
![unnamed](https://user-images.githubusercontent.com/76945262/172669981-734680f7-7346-4d09-87bd-1cdd494f7577.png)


### Team Mates

###### Aditi Pagey: https://github.com/AditiPagey

### Credits
The original dataset can be found here at the UCI Machine Learning Repository. This project wouldn't have been possible without this dataset.
We would also like to thank iNeuron for providing us with this opportunity and for their constant guidance and support.



