
# Movie Recommendation System

This project is a Recommendation system built from scrath using content based filtering. My own documentation about different recommendation systems to help understand this concept better can be found here : https://docs.google.com/document/d/1x565uFocLPXZFKefvBBzQAaV4A1gtXbWjgTrv-VFMFs/edit?usp=sharing

The data set used can be downloaded from the link : https://github.com/dhananjay-deshmukh/Movie_recommendation/blob/main/movies.csv

The system recommends the user 5 new movies based on the input of a favourite movie provided by the user.

The metric used to build the recommendation system is "Cosine similarity".

This project has been provided with an interactive demo using streamlit.

## Demo Screenshot <br>

![Screenshot 2023-04-02 232341](https://user-images.githubusercontent.com/112422798/229371787-abc22c25-99d6-478b-a11a-3423c7d31903.png)




## Run Locally

Clone the project

```bash
  git clone https://github.com/dhananjay-deshmukh/Movie_recommendation.git
```

Go to the project directory

```bash
  cd Movie_recommendation
```

Install dependencies

```bash
  pip install requirements.txt 
```

Run the web app

```bash
  streamlit run app.py
```

