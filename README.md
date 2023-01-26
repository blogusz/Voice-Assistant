# Voice-Assistant (in polish)
A voice assistant that answers specific types of questions about cinematography. The assistant takes a request from the user, searches the TMDB database for the given title and gives an answer based on this.

## Types of questions that can be asked:
- ***who is the director of the movie*** (Kto nakręcił|Reżyser filmu|Kto jest reżyserem|Ile zarobił|Ile zarobiła|Ile zarobiło|Ile zarobili|Ile zarobiły|Box office filmu)
- ***how much did the movie make*** (Ile zarobił|Ile zarobiła|Ile zarobiło|Ile zarobili|Ile zarobiły|Box office filmu)
- ***movies similar to the movie*** (Filmy podobne do|Rekomendacje do)
- ***when was the movie made*** (Kiedy nakręcono|Kiedy powstał|Kiedy powstała|Kiedy powstało|Kiedy powstali|Kiedy powstały)
- ***what is the description of the movie*** (Jaki jest opis|Fabuła filmu|O czym jest|O czym są)
- ***how is the movie rated*** (Jaką ocenę ma|Jaką ocenę mają|Jak oceniany jest|Jak oceniana jest|Jak oceniane jest|Jak oceniani są|Jak oceniane są)
- ***how long is this movie*** (Ile trwa|Ile trwają)
- ***what was the budget of the movie*** (Ile kosztował|Ile kosztowała|Ile kosztowało|Ile kosztowali|Ile kosztowały|Budżet filmu)
- ***what is the tagline of the movie*** (Jakie jest motto filmu)

### Question construction: question from the list of questions (lines 17-19 in the code) + movie title.

## Examples od requests:   
[Reżyser filmu] [Łowca Jeleni]? - Michael Cimino  
[Kiedy powstał] [Czas Apokalipsy]? - 1979.05.10  
[Ile kosztowała] [Odyseja Kosmiczna]? - 12000000$  
[Jakie jest motto filmu] [Obcy]? - W kosmosie nikt nie usłyszy twego krzyku.
