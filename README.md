# musiceval
### @author: [Mel Mark](https://m3l.me), Park University, 2019
* Nov 2019 update: The converter is now working and I am now able to analyze any song in Weka. Working on the analysis and tweaking algorithims.
* This program is meant for a specific dataset retrieved from the University of Geneva in Switzerland ([DEAM: MediaEval Database for Emotional Analysis in Music](http://cvml.unige.ch/databases/DEAM/manual.pdf)).
* It takes the arousal and valence values of each song and plots it on a 2D graph, according to [Thayer's model](https://www.researchgate.net/figure/Thayers-model-of-mood-adapted-from-8_fig1_257307898).
* It then divides it into four quadrants, and even further into 9 subdivisions for 3 categories within each quadrant, to categorize the song into one of twelve moods (three moods for each of the four quadrants): happy, pleased, excited, angry, nervous, annoyed, sad, bored, sleepy, peaceful, relaxed, or calm.
* It is eventually going to be an algorithim for a machine learning tool, right now it bases the origin of the graph based on the means for the valence and arousal of the dataset.
