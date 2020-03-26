# musiceval
### @author: [Mel Mark](https://m3l.me), Park University, 2020
------------------------------------------------------------------------------------------------
#### Updates
* **March 2020 update:** despite the pandemic going on in the world, I am still working on this research (while quarantined to my house). Everything is working properly and I am able to make predictions based off various ML models for any song I choose. I chose 4 (in my opinion) different songs and have their ARFF data with various attribute sets uploaded to data.zip. In addition, a variety of ML models (including SMO, neuralnetwork/multilayer perception, simple logistic, and J48 tree) are available to apply on any song with matching attributes, and can be found in models.zip. To see how the various models preform against the 4 songs I chose, the statistics, corresponding attribute list and model name, and results can all be found in the ML comparison files. Currently I am working on perfecting my algorithms and attribute sets to get the best results. Hoping to present at virtual honors symposium but nothing is really for sure these days.
* **Nov 2019 update:** The converter is now working and I am now able to analyze any song in Weka. Working on the analysis and tweaking algorithms.
------------------------------------------------------------------------------------------------
#### Description
* The training data set came from a very specific dataset retrieved from the University of Geneva in Switzerland ([DEAM: MediaEval Database for Emotional Analysis in Music](http://cvml.unige.ch/databases/DEAM/manual.pdf)).
* It takes the arousal and valence values of each song and plots it on a 2D graph, according to [Thayer's model](https://www.researchgate.net/figure/Thayers-model-of-mood-adapted-from-8_fig1_257307898).
* It then divides it into four quadrants, and even further into 9 subdivisions for 3 categories within each quadrant, to categorize the song into one of twelve moods (three moods for each of the four quadrants): happy, pleased, excited, angry, nervous, annoyed, sad, bored, sleepy, peaceful, relaxed, or calm.
* From the training set of songs and emotions, various machine learning models make emotional predictions for other songs with matching attribute sets
