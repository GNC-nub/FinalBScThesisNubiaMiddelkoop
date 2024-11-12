'''
READ ME
    Run this file ONLY after running loading_matlab_file.py first!!
    Put in the paths to the matlab file and the place to store the data in loading_matlab_file.py first!!

DESCRIPTION
    This script puts out all the data needed for the BSc Thesis of Nubia Middelkoop.
    This code uses 3 classes from the file ClassMosquito.py:
        Track (to load single tracks), Trials (to load single trials) and Dataset (to load the whole dataset).

PARAMETERS
    The class Dataset does not take any parameters
    The class Trial takes only one integer as an input: The trial nuber
    The class Track takes two integers parameters: the trial number and the track number
        Some tracks don't exist in this dataset,then an error message arises.

'''

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Antoine, this is main!\n Run this script AFTER loading the data into the correct folders/directory with the loading_matlab_file.py.')


import ClassMosquito


#run loading_matlab_file.py first!
    #Put in your own paths to the matlab file and the place to store the data!

dataset = ClassMosquito.Dataset()
trial = ClassMosquito.Trial(1)
track = ClassMosquito.Track(1, 2)


#Basic dataset analysis

landing_count = dataset.countLandingPoints()
capturing_count = dataset.countCapturingPoints()
total_tracks = sum(dataset.getNumTracksPerTrial())
print(f'Total tracks = {total_tracks}')
print(f'In the whole dataset {landing_count} mosquitos are landing. ({round(landing_count/total_tracks*100, 2)} % of the tracks end in landing)')
print(f'From this testing: In the whole dataset {capturing_count} mosquitos are captured. ({round(capturing_count/total_tracks*100, 2)} % of the tracks end in capture)')
print(f'From the capture rate of the article: In the whole dataset 1335 mosquitos are captured. ({round(1335/total_tracks*100, 2)} % of the tracks end in capture)')


#General dataset analysis
dataset.testNormalDistribution(dataset.getNumTracksPerTrial())
print(dataset.testConfidenceInterval(dataset.getNumTracksPerTrial()))


#Durations
dataset.plotDuration()
dataset.plotViolinStartEndTimes()

#basic 3D plotting

track.plotTrack()
track.plotTheta2DTrack()
trial.plotTrial()
trial.plotTheta2DTrial()


#Boxplots (it prints significance)
dataset.plotBoxplotCatchesConditions()
dataset.plotBoxplotLandingCondition()
dataset.plotBoxplotCatchesVsLandings()



#Resting time
print(f'Average resting time of the whole dataset = {dataset.getAvarageRestingTime()}')
print(f'The median resting time of the whole dataset = {dataset.getMedianRestingTime()}')
print(f'The longest resting time of the whoe dataset is = {dataset.getLongestRestingTime()}')


dataset.plotHistogramRestingTime()
dataset.plotHistogramRestingTimeZoomedIn(0, 30)

print(f'The amount of very small resting times (below 1 second) = {dataset.countSmallRestingTimes(1)}, this is {dataset.countSmallRestingTimes(1)/dataset.countTotalRestingTimes()*100}%')
print(f'The amount of very small resting times (below 0.5 seconds) = {dataset.countSmallRestingTimes(0.5)}, this is {dataset.countSmallRestingTimes(0.5)/dataset.countTotalRestingTimes()*100}%')

dataset.plotHistogramRestingTimeCondition('without')
dataset.plotHistogramRestingTimeCondition('with_heat')
dataset.plotHistogramRestingTimeCondition('with_heat_water')
dataset.plotViolinplotRestingTimeCondition()


#Landing Heatmaps
dataset.plotHeatmapLandingPointNormilized()
dataset.plotHeatmapRestingPoints(title = 'Density Resting Points all.')
dataset.plotHeatmapRestingPoints(upper_time_boundary=0.5, title='Density Resting Points below 0.5 s.')
dataset.plotHeatmapRestingPoints(lower_time_boundary=0.5, title='Density Resting Points above 0.5 s.')
dataset.plotHeatmapRestingPoints(upper_time_boundary=1, title='Density Resting Points below 1 s.')
dataset.plotHeatmapRestingPoints(lower_time_boundary=1, title='Density Resting Points above 1 s.')



#Heatmap resting time
dataset.plotHeatmapRestingTimes()
dataset.plotHeatmapRestingTimes(lower_time_boundary=0.5, title = 'bigger then 0.5s') # --> a heatmap of only the time bigger then 0.5s
dataset.plotHeatmapRestingTimes(upper_time_boundary=0.5, title = 'smaler than 0.5s') # --> a heatmap of only the times smaller than 0.5s
dataset.plotHeatmapRestingTimes(lower_time_boundary=1, title = 'bigger then 1s') # --> a heatmap of only the time bigger then 1s
dataset.plotHeatmapRestingTimes(upper_time_boundary=1, title = 'smaller then 1s') # --> a heatmap of only the times smaller than 1s

dataset.plotHeatmapRestingTimePerCondition()


#Probability capture/land again after landing
trial.plotTrackLandingAgainTrial(8)
trial.plotTrackLandingToCaptureTrial(1)

dataset.plotBoxplotRadiusAssociations()
dataset.plotBoxplotCountLandingTakeOffAccosiation()

dataset.plotHeatmapLandingAgainProbability()
dataset.plotHeatmapLandingToCaptureProbability()
percentage_land_again = dataset.calculatingPercentagesLandingAgain()
percentage_land_to_capture = dataset.calculatingPercentagesLandingToCapture()

print(f'Percentage of take offs that land again is {percentage_land_again}\nPercentage of take offs that lead to capture {percentage_land_to_capture}')

