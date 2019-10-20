# musiceval
## @author: [Mel Mark](https://m3l.me), Park University, 2019
This program is meant for a specific dataset retrieved from the University of Geneva in Switzerland ([DEAM: MediaEval Database for Emotional Analysis in Music](http://cvml.unige.ch/databases/DEAM/manual.pdf)).
It takes the arousal and valence values of each song and plots it on a 2D graph, according to [Thayer's model](https://www.researchgate.net/figure/Thayers-model-of-mood-adapted-from-8_fig1_257307898), and divides it into four quadrants (and even further into 9 subdivisions for 3 categories within each quadrant) to categorize the song into one of twelve moods (happy, pleased, excited, angry, nervous, annoyed, sad, bored, sleepy, peaceful, relaxed, or calm).
It is eventually going to be an algorithim for a machine learning tool, right now it bases the origin of the graph based on the means for the valence and arousal of the dataset. 
