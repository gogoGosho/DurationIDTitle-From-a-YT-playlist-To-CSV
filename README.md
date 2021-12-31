# calculateYT-PlaylistDurationCSV<br />
~~ just a smaaal insignificant issue - it counts all the privated videos as well, works perfectly fine so long as you dont run it on a playlist that has privated videos, if the videos were public and you ran in- it will work as intended but if you try it again after the vid's been privated it'll count it and fuck up the duration for the other vids unlucky<br />~~ 
<b>Goes through an entire playlist, grabs the ID of the video, the duration and the title and saves them to a csv file</b>
it goes through an entire playlist, calculates the duration and saves it to a csv file<br />
i fixed file creation, just set the default(permanent) folder if u plan on turning this into a bat file <br />
VVV<br />
THE CSV FILE MUST BE IN THE SAME DIRECTORY AS THE PYTHON SCRIPT<br />
the csv file must have<br /> VIDID,LENGHT<br />
as the first line,using the lenght part and pandas we calculate the total duration<br />
you have to create your own yt3 API key<br />
![優越感](https://user-images.githubusercontent.com/91748572/147839314-b95013ff-46af-4188-b600-cbb68c2ee6d0.PNG)
