# Voice-Assistant (in polish)
A voice assistant that answers specific types of questions about cinematography. The assistant takes a request from the user, searches the TMDB database for the given title and gives an answer based on this.

Types of questions that can be asked:
- who is the director of the movie
- how much did the movie make
- movies similar to the movie
- when was the movie made
- what is the description of the movie
- how is the movie rated
- how long is this movie
- what was the budget of the movie
- what is the tagline of the movie

Question construction: question from the list of questions (lines 17-19 in the code) + movie title.

Examples od requests: 
[Reżyser filmu] [Łowca Jeleni]? - Michael Cimino  
[Kiedy powstał] [Czas Apokalipsy]? - 1979.05.10  
[Ile kosztowała] [Odyseja Kosmiczna]? - 12000000$  
[Jakie jest motto filmu] [Obcy]? - W kosmosie nikt nie usłyszy twego krzyku.
