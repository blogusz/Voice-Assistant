import speech_recognition as sr
import pyttsx3
import re
from tmdbv3api import TMDb
from tmdbv3api import Movie
from num2words import num2words

tmdb = TMDb()
tmdb.api_key = '39dbdab5e788eaf8492192773dbf42d7'
tmdb.language = 'pl'
tmdb.debug = True

movie = Movie()

def process_question(transcribed_text):
    match = re.search(
        r"(Kto nakręcił|Reżyser filmu|Kto jest reżyserem|Ile zarobił|Ile zarobiła|Ile zarobiło|Ile zarobili|Ile zarobiły|Box office filmu|Filmy podobne do|Rekomendacje do|"
        r"Kiedy nakręcono|Kiedy powstał|Kiedy powstała|Kiedy powstało|Kiedy powstali|Kiedy powstały|Jaki jest opis|Fabuła filmu|O czym jest|O czym są|Jaką ocenę ma|Jaką ocenę mają"
        r"Jak oceniany jest|Jak oceniana jest|Jak oceniane jest|Jak oceniani są|Jak oceniane są|Ile trwa|Ile trwają|Ile kosztował|Ile kosztowała|Ile kosztowało|Ile kosztowali|Ile kosztowały|Budżet filmu|Jakie jest motto filmu) (.*?)\?",
        transcribed_text)

    if match:
        question_type = match.group(1)
        movie_title = match.group(2)

        try:
            tytul = movie.search(movie_title)
            tytul = max(tytul, key=lambda x: x['vote_count']) # w przypadku wielu filmow o tym samym tytule wybieramy ten o najwiekszej ilosci ocen
            nr_id = int(tytul['id'])
        except ValueError:
            return "Nie rozpoznano tytułu filmu."


        if question_type == 'Kto nakręcił' or question_type == 'Reżyser filmu' or question_type == 'Kto jest reżyserem':
            find_by_id = movie.credits(nr_id)
            director = [d['name'] for d in find_by_id['crew'] if d['job'] == 'Director']

            for d in director:
                print(d)

            return director

        elif question_type == 'Ile zarobił' or question_type == 'Ile zarobiła' or question_type == 'Ile zarobiło' or question_type == 'Ile zarobili' or question_type == 'Ile zarobiły' or question_type=='Box office filmu':
            find_by_id = movie.details(nr_id)
            revenue = find_by_id['revenue']
            print(str(revenue)+ " dolarów")
            revenue=num2words(revenue, lang='pl') + " dolarów"

            return revenue

        elif question_type == 'Filmy podobne do' or question_type=='Rekomendacje do':
            find_by_id = movie.recommendations(nr_id)
            results=[]
            for f in find_by_id[:5]:
                print(f['title'])
                print()
                results.append(f['title'])

            return results

        elif question_type == 'Kiedy nakręcono' or question_type=='Kiedy powstał' or question_type=='Kiedy powstała' or question_type=='Kiedy powstało' or question_type=='Kiedy powstali' or question_type=='Kiedy powstały':
            find = movie.details(nr_id)
            print(find['release_date'])

            return find['release_date']

        elif question_type == 'Jaki jest opis' or question_type=='Fabuła filmu' or question_type=='O czym jest' or question_type=='O czym są':
            find = movie.details(nr_id)
            print(find['overview'])

            return find['overview']

        elif question_type == 'Jaką ocenę ma' or question_type =='Jaką ocenę mają' or question_type == 'Jak oceniany jest' or question_type=='Jak oceniana jest' or question_type=='Jak oceniane jest' or question_type=='Jak oceniani są' or question_type=='Jak oceniane są':
            find = movie.details(nr_id)
            print(find['vote_average'])

            return find['vote_average']

        elif question_type == 'Ile trwa' or question_type=='Ile trwają':
            find = movie.details(nr_id)
            find=find['runtime']
            print(str(find) + " minuty")
            find = num2words(find, lang='pl') + " minuty"

            return find

        elif question_type == 'Ile kosztował' or question_type == 'Ile kosztowała' or question_type == 'Ile kosztowało' or question_type == 'Ile kosztowali' or question_type == 'Ile kosztowały' or question_type=='Budżet filmu':
            find = movie.details(nr_id)
            find=find['budget']
            print(str(find) + " dolarów")
            find = num2words(find, lang='pl') + " dolarów"
            return find

        elif question_type == 'Jakie jest motto filmu':
            find=movie.details(nr_id)
            print(find['tagline'])

            return find['tagline']

    else:
        return "Nie zrozumiano pytania."


if __name__ == "__main__":
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False

    # for voice in engine.getProperty('voices'):
    #     print(voice.id)

    engine.setProperty('voice', engine.getProperty('voices')[2].id) # w moim systemie [2] odpowiada polskiemu glosowi, byc moze konieczne jest na innym komputerze wybranie innego indeksu. W tym celu nalezy uruchomic kod w linijkach 113-114 i zobaczyc ktory pakiet odpowiada jezykowi polskiemu.
    while True:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            recordedAudio = recognizer.listen(source)

        try:
            transcribed_text = recognizer.recognize_google(recordedAudio, language='pl_PL')
            transcribed_text = ''.join((transcribed_text, '?')).capitalize()
            print()

            answer=process_question(transcribed_text)
            engine.say(answer)
            engine.runAndWait()
            print()

        except sr.UnknownValueError:
            transcribed_text = "Nie rozpoznano tekstu"
        except sr.RequestError as e:
            transcribed_text = "Błąd połączenia z API: {0}".format(e)
