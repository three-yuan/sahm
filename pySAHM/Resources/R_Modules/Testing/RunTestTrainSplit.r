### This file runs the TestTrainSplit and checks that all ratios end up being what they should if RatioPresAbs is set at an extreme value
### an excessive number of values are deleted and ratios and be drastically off might want to include future error checking
#=================================================================#
                   ## Specifying input
#=================================================================#

setwd("I:\\VisTrails\\DevWorkspace\\Marian\\userpackages\\sahm\\pySAHM\\Resources\\R_Modules")
ScriptPath="I:\\VisTrails\\DevWorkspace\\Marian\\userpackages\\sahm\\pySAHM\\Resources\\R_Modules"
source("TestTrainSplit.r")


i="I:\\VisTrails\\WorkingFiles\\workspace\\MarianTesting\\TestSuite\\MergedDataset_2.csv"
seed=2 
es=TRUE 
o="I:\\VisTrails\\WorkingFiles\\workspace\\MarianTesting\\TestSuite\\ModelEvaluation_Split_2.csv" 
rc="responseBinary" 
#=================================================================#
                   ## Running the code
TestTrainSplit(input.file=i,output.file=o,response.col=rc,trainProp=.7,seed=seed,Eval.Split=es)  #tried also with .8, and no RatioPresAb
#=================================================================#
## Running some tests on the output
input.file<-output.file
dat<-read.csv(input.file,skip=3,header=FALSE)

          hl<-readLines(input.file,1)
          hl=strsplit(hl,',')
          colnames(dat) = hl[[1]]

          tif.info<-readLines(input.file,3)
          tif.info<-strsplit(tif.info,',')
          include<-(as.numeric(tif.info[[2]]))
          
# checking that trainProp is correct
ta<-table(dat$Split,dat$responseBinary)
ta
#if there are background points, remove them here
ta<-ta[-1,]
ta<-ta[,-1]

#checking that the trainProp was ballanced for each count all of these
#should be approximately equal to the trainProp this works less well for
#smaller sample sizes
ta[2,]/(ta[1,]+ta[2,])

#checks trainProp is correct
sum(ta[2,])/sum(ta)
sum(ta[1,])/sum(ta)

#checking ratio of presence to absence should equal RatioPresAbs
sum(ta[1,2:dim(ta)[2]])/ta[1,1]
sum(ta[2,2:dim(ta)[2]])/ta[2,1]

#######################################################
#### testing looking at an mds with counts case 1. appears to be working###########
input.file<-"H:\\Desktop\\SAHM\\Data\\ChangeFamilyData\\MergedDataSet_1.csv"
output.file<-"H:\\Desktop\\SAHM\\Output\\TestTrainSplit\\testtrain.mds"
TestTrainSplit(input.file,output.file,response.col="ResponseCount",trainProp=.7,RatioPresAbs=.9,seed=NULL)

input.file<-output.file
dat<-read.csv(input.file,skip=3,header=FALSE)

          hl<-readLines(input.file,1)
          hl=strsplit(hl,',')
          colnames(dat) = hl[[1]]

          tif.info<-readLines(input.file,3)
          tif.info<-strsplit(tif.info,',')
          include<-(as.numeric(tif.info[[2]]))

# checking that trainProp is correct
ta<-table(dat$Split,dat$responseCount)
ta

#if there are background points, remove them here
ta<-ta[-1,]
ta<-ta[,-1]

#checking that the trainProp was ballanced for each count all of these
#should be approximately equal to the trainProp this works less well for
#smaller sample sizes
ta[2,]/(ta[1,]+ta[2,])

#checks trainProp is correct
sum(ta[2,])/sum(ta)
sum(ta[1,])/sum(ta)

#checking ratio of presence to absence should equal RatioPresAbs
sum(ta[1,2:dim(ta)[2]])/ta[1,1]
sum(ta[2,2:dim(ta)[2]])/ta[2,1]


#######################################################
#### testing looking at an mds with counts case 2. Looks like this is working too###########
input.file<-"H:\\Desktop\\SAHM\\Data\\ChangeFamilyData\\MergedDataSet_1.csv"
output.file<-"H:\\Desktop\\SAHM\\Output\\TestTrainSplit\\testtrain.mds"
TestTrainSplit(input.file,output.file,response.col="ResponseCount",trainProp=.7,RatioPresAbs=.4,seed=NULL)

input.file<-output.file
dat<-read.csv(input.file,skip=3,header=FALSE)

          hl<-readLines(input.file,1)
          hl=strsplit(hl,',')
          colnames(dat) = hl[[1]]

          tif.info<-readLines(input.file,3)
          tif.info<-strsplit(tif.info,',')
          include<-(as.numeric(tif.info[[2]]))

# checking that trainProp is correct
ta<-table(dat$Split,dat$responseCount)
ta

#if there are background points, remove them here
ta<-ta[-1,]
ta<-ta[,-1]

#checking that the trainProp was ballanced for each count all of these
#should be approximately equal to the trainProp this works less well for
#smaller sample sizes
ta[2,]/(ta[1,]+ta[2,])


#checks trainProp is correct
sum(ta[2,])/sum(ta)
sum(ta[1,])/sum(ta)

#checking ratio of presence to absence should equal RatioPresAbs for both the test and train split
sum(ta[1,2:dim(ta)[2]])/ta[1,1]
sum(ta[2,2:dim(ta)[2]])/ta[2,1]


#######################################################
#### testing looking at an mds with counts case 3. Without a RatioPresAbs###########
input.file<-"H:\\Desktop\\SAHM\\Data\\ChangeFamilyData\\MergedDataSet_1.csv"
output.file<-"H:\\Desktop\\SAHM\\Output\\TestTrainSplit\\testtrain.mds"
TestTrainSplit(input.file,output.file,response.col="ResponseCount",trainProp=.7,seed=NULL)

input.file<-output.file
dat<-read.csv(input.file,skip=3,header=FALSE)

          hl<-readLines(input.file,1)
          hl=strsplit(hl,',')
          colnames(dat) = hl[[1]]

          tif.info<-readLines(input.file,3)
          tif.info<-strsplit(tif.info,',')
          include<-(as.numeric(tif.info[[2]]))

# checking that trainProp is correct
ta<-table(dat$Split,dat$responseCount)
ta

#if there are background points, remove them here
ta<-ta[-1,]
ta<-ta[,-1]

#checking that the trainProp was ballanced for each count all of these
#should be approximately equal to the trainProp this works less well for
#smaller sample sizes
ta[2,]/(ta[1,]+ta[2,])


#checks trainProp is correct
sum(ta[2,])/sum(ta)
sum(ta[1,])/sum(ta)

#checking ratio of presence to absence should equal RatioPresAbs for both the test and train split
sum(ta[1,2:dim(ta)[2]])/ta[1,1]
sum(ta[2,2:dim(ta)[2]])/ta[2,1]

I:\VisTrails\Central_VisTrailsInstall\Central_R\R-2.12.1\bin\i386\Rterm.exe --vanilla -f I:\VisTrails\Central_VisTrailsInstall\vistrails\packages\sahm\pySAHM\Resources\R_Modules\TestTrainSplit.r --args i="C:\temp\SAHM_workspace\mtalbert_20111121T094519\MergedDataset_1.csv" o="C:\temp\SAHM_workspace\mtalbert_20111121T094519\TestTrainingSplit.csv" rc=responseBinary