# -*- coding: cp1252 -*-
import firstweb
import media

toy_story = media.Movie("Toy Story 4",
                        "Woody has always been confident about his place in the world and that his priority is taking care of his kid, whether that’s Andy or Bonnie. But when Bonnie adds a reluctant new toy called “Forky” to her room, a road trip adventure alongside old and new friends will show Woody how big the world can be for a toy. Directed by Josh Cooley (“Riley’s First Date?”) and produced by Jonas Rivera (“Inside Out,” “Up”) and Mark Nielsen (associate producer “Inside Out”), Disney•Pixar’s “Toy Story 4” ventures to U.S. theaters on June 21, 2019.",
                        "https://pre00.deviantart.net/240d/th/pre/i/2017/050/a/1/toy_story_4_poster_by_messypandas-dazmysf.png",
                        "https://www.youtube.com/watch?v=LDXYRzerjzU")


ff8 = media.Movie("Fate of the Furious FF8",
                  "Dom and Letty are on their honeymoon and Brian and Mia have retired from the game—and the rest of the crew has been exonerated—the globetrotting team has found a semblance of a normal life. But when a mysterious woman (Oscar® winner Charlize Theron) seduces Dom into the world of crime he can’t seem to escape and a betrayal of those closest to him, they will face trials that will test them as never before. From the shores of Cuba and the streets of New York City to the icy plains off the arctic Barents Sea, our elite force will crisscross the globe to stop an anarchist from unleashing chaos on the world’s stage…and to bring home the man who made them a family. ",
                  "https://cdn.empireonline.com/jpg/70/0/0/1280/960/aspectfit/0/0/0/0/0/0/c/articles/58bc4a051268b33f1bc0b1de/ff8-poster.jpg",
                  "https://www.youtube.com/watch?v=uisBaTkQAEs")


school_of_rock = media.Movie("School of Rock", "storyLine",
                             "https://img.reelgood.com/content/movie/f1adb47d-d488-4d60-94ca-ce258b303797/poster-780.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")


jumanji2 = media.Movie("Jumanji 2", "storyLine",
                       "https://i0.wp.com/teaser-trailer.com/wp-content/uploads/Jumanji-International-Poster.jpg?ssl=1",
                       "https://www.youtube.com/watch?v=2QKg5SZ_35I")


ted2 = media.Movie("Ted 2", "storyLine",
                   "https://m.media-amazon.com/images/M/MV5BMjEwMDg3MDk1NF5BMl5BanBnXkFtZTgwNjYyODA1NTE@._V1_.jpg",
                   "https://www.youtube.com/watch?v=S3AVcCggRnU")


blackpanther = media.Movie("Black Panther", "storyLine",
                           "https://imgix.ttcdn.co/i/product/original/0/277303-566b9e0774f5414582dd24eb88ea09f8.jpeg?q=100&auto=format%2Ccompress&w=2000",
                           "https://www.youtube.com/watch?v=xjDjIWPwcPU")


ratchasan = media.Movie("Ratchasan","storyLine",
                        "https://www.comingtrailer.com/images/poster/Ratchasan2.jpg",
                        "https://www.youtube.com/watch?v=GsrN7rNch9Y")


sarkar = media.Movie("Sarkar","storyLine",
                     "https://moviegalleri.net/wp-content/uploads/2018/10/Actor-Vijay-Sarkar-Teaser-Release-Date-on-19-October-Poster-HD.jpg",
                     "https://www.youtube.com/watch?v=VkkyaodksT4&t=9s")


TwopointO = media.Movie("2.O","storyLine",
                      "https://m.media-amazon.com/images/M/MV5BNmJjNzI2MjktYjMwYi00NDk4LWEwNWYtNzYxZWU4ODdhMTAyXkEyXkFqcGdeQXVyODIwMDI1NjM@._V1_.jpg",
                      "https://www.youtube.com/watch?v=jrETX2eDhL8")


enpt = media.Movie("Ennai Noki Payum Thota","storyLine",
                   "https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/ecc9f069437775.5b813c0c8dc60.jpg",
                   "https://www.youtube.com/watch?v=rr1f5GXtpe0")


key = media.Movie("Key","storyLine",
                  "https://moviegalleri.net/wp-content/uploads/2017/08/Actor-Jiiva-Kee-Movie-First-Look-Poster.jpg",
                  "https://www.youtube.com/watch?v=IWqeTxCdsrk")


dt2 = media.Movie("Dhilluku Thuddu 2", "storyLine",
                  "https://moviegalleri.net/wp-content/uploads/2018/10/Santhanam-Dhilluku-Dhuddu-2-Teaser-from-Oct-29th-Poster.jpg",
                  "https://www.youtube.com/watch?v=MB0vhP6m9SQ")

Taxiwaala = media.Movie("Taxi Waala", "storyLine",
                        "https://m.media-amazon.com/images/M/MV5BMTVmMTg5Y2UtOTVmYi00M2E1LWFhYzgtMjFkMjMyOGFhZDVjXkEyXkFqcGdeQXVyNTgxODY5ODI@._V1_.jpg",
                        "https://www.youtube.com/watch?v=9KN3dbZVRwQ")

pokemon = media.Movie("POKÉMON Detective Pikachu", "storyline",
                      "https://i.pinimg.com/originals/c9/71/de/c971de9c30007e1b0d2a69132ba78021.jpg",
                      "https://www.youtube.com/watch?v=du88WArjb8w")

kgf = media.Movie("KGF","storyLine",
                   "https://i2.wp.com/www.socialnews.xyz/wp-content/uploads/2018/11/08/KGF-Movie-Trailer-Posters-.jpg?fit=893%2C1200&quality=90&zoom=1&ssl=1",
                   "https://www.youtube.com/watch?v=qXgF-iJ_ezE")


movies = [toy_story, ff8, school_of_rock, jumanji2, ted2, blackpanther, ratchasan, sarkar, TwopointO, enpt,
          key, dt2, Taxiwaala, pokemon, kgf]
firstweb.open_movies_page (movies)
