""" Script for batch processing all data in the walking dataset.
   
   The script runs batch processing in three steps:

   1. Runs all the standing reference trials to 
      calculate scaling and marker positions for each subject. 

   2. Runs marker tracking for all trials, saving joint angles to files. 

   3. It runs the inverse dyanmic analysis for all trials.
      This steps outputs the EKin variable as an example. 
      It can be extended to output any variable from the model. 

   Note: The script uses AnyPyTools, which is an open source library for 
         working with the AnyBody Modeling System. If you use this library 
         for publication please cite:

         Lund et al., (2019). AnyPyTools: A Python package for reproducible 
         research with the AnyBody Modeling System. Journal of Open Source 
         Software, 4(33), 1108, https://doi.org/10.21105/joss.01108

"""
import os


from anypytools import AnyPyProcess
from anypytools import macro_commands as mc

# Create folder for storing batch processing logfiles
# NOTE: Log files are automatically deleted unless the model fails.
os.makedirs("BatchProcessingLogs", exist_ok=True)

# Process options for the batch processing
app_opts = {
    # Run only one paralllel process in github actions to avoid memory problems
    "num_processes": 1 if os.environ.get("CI") else 3,
    "ignore_errors": [".anyset"],
}


#%% Process all standing reference trials
macro = [mc.Load("Main.any"), mc.OperationRun("Main.RunParameterIdentification")]

app = AnyPyProcess(**app_opts)
app.start_macro(
    macro,
    search_subdirs=r".*_StandingRef[\\/]Main.any",
    logfile="BatchProcessingLogs/ParameterOptimization.txt",
)


#%% Process all marker tracking

macro = [
    mc.Load("Main.any"),
    mc.OperationRun("Main.RunAnalysis.LoadParameters"),
    mc.OperationRun("Main.RunAnalysis.MarkerTracking"),
]

nproc = 1 if os.environ.get("GITHUB_ACTIONS") else 3

app = AnyPyProcess(**app_opts)
app.start_macro(
    macro,
    search_subdirs=r"Subjects.+Gait.+Main.any",
    logfile="BatchProcessingLogs/MarkerTracking.txt",
)

#%% Process all Inverse dynamics and export results

# Please see this link for how to work with the results from AnyPyTools:
# https://anybody-research-group.github.io/anypytools-docs/Tutorial/01_Getting_started_with_anypytools.html
macro = [
    mc.Load("Main.any"),
    mc.OperationRun("Main.RunAnalysis.LoadParameters"),
    mc.OperationRun("Main.RunAnalysis.InverseDynamics"),
    mc.Dump("Main.Studies.InverseDynamicStudy.Ekin"),
    # Add more output here
]

app = AnyPyProcess(**app_opts)
results = app.start_macro(
    macro,
    search_subdirs=r"Subjects.+Gait.+Main.any",
    logfile="BatchProcessingLogs/InverseDynamics.txt",
)
