# DEMOS Stair Assist Exoskeleton Model

## Introduction:

This is the model that was used to evaluate the biomechanical effects of an active exoskeleton in the [DEMOS](https://demos.htwk-leipzig.de/) project [1]. The exoskeleton is for the lower limbs and aims to assist the elderly in stair negotiation. The exoskeleton assists in knee extension through an active cable drive, whose line of action passes anteriorly to the knee of the user.

![Picture1](https://user-images.githubusercontent.com/102362310/190962371-76cfc349-1daa-4f3c-87ab-da9183ec0bc7.png)
## Description:

The model demonstrates some trials with the exoskeleton in stair ascent. The trials were performed in a biomechanical laboratory using a custom-built staircase consisting of a force plate on the second step to record the ground reaction force and moment. The motion of the subject and the exoskeleton were recorded using a marker-based motion capture system. The assistive force from the exoskeleton was recorded using a built-in strain gauge that recorded the tensile force on the cable.

The protocol ensured that the subject performed the stair ascent motion without using the handrail and the subject climbed the stair in a step-over-step manner with the right leg landing on the second step, which consisted of the force plate.

## Model:

The human-exoskeleton co-simulation model was built starting from an [example model](https://anyscript.org/ammr-doc/auto_examples/Mocap/plot_Plug-in-gait_MultiTrial_StandingRef.html#sphx-glr-auto-examples-mocap-plot-plug-in-gait-multitrial-standingref-py) in the AMMR. A computer aided design (CAD) model of the exoskeleton was prepared in SolidWorks and exported using the AnyExp4SOLIDWORKS add-in. The human-exoskeleton interface can be simulated through different interface models [2,3].

## Usage:

Please download the model and save on your computer. The model is setup using the [multi trial model](https://anyscript.org/ammr-doc/auto_examples/Mocap/plot_Plug-in-gait_MultiTrial_StandingRef.html#sphx-glr-auto-examples-mocap-plot-plug-in-gait-multitrial-standingref-py), where you can see the general folder structure. The main files can be found in the `Subjects/S1/S1_*` directory. In addition to the general mocap model structure, the folder `Exo` contains files related to the exoskeleton and interface models. The folder `SupportingFiles` contains some other files needed in this model.

-	Please load the main file.
-	All the changes related to the exoskeleton and the environment can be accessed through the `SupportingFiles/AddOns.any` file, which is included in the `LabSpecificData.any` file:
    -	Importing the exoskeleton and staircase model
    -	Interface model
    -	Including the exoskeleton model in the study
    -	Exporting results in a csv file
-	To run the model, please load the standing ref model and run the parameter identification study first. Subsequently, load any of the stair ascent trial and run RunAnalysis operation.

## Acknowledgements:

The model was developed in a joint cooperation between the [Ergonomics group](https://www.dimeas.polito.it/en/research/research_groups/ergonomics) at Department of Mechanical and Aerospace Engineering, Politecnico di Torino (ITALY), the [Faculty of Engineering](https://ing-emb.htwk-leipzig.de/institut/), Leipzig University of Applied Sciences (GERMANY), and the [Biomechanics research group](https://www.biomechanics.mp.aau.dk/) at Department of Materials and Production, Aalborg University (DENMARK). We would like to thank the following persons for developing the model and allowing it to be publicly released:
-	Divyaksh Subhash Chander (formerly at Politecnico di Torino)
-	Max Böhme (formerly at Leipzig University of Applied Sciences)
-	Michael Skipper Andersen (Aalborg University)
-	John Rasmussen (Aalborg University)
-	Johannes Zentner (Leipzig University of Applied Sciences)
-	Maria Pia Cavatorta (Politecnico di Torino)

## References:
1. Böhme, M., Köhler, H. P., Thiel, R., Jäkel, J., Zentner, J., & Witt, M. (2022). Preliminary Biomechanical Evaluation of a Novel Exoskeleton Robotic System to Assist Stair Climbing. Applied Sciences, 12(17), 8835. [DOI](https://doi.org/10.3390/app12178835)

2. Chander, D. S., Böhme, M., Andersen, M. S., Rasmussen, J., Zentner, J., & Cavatorta, M. P. (2022). A comparison of different methods for modelling the physical human-exoskeleton interface. International Journal of Human Factors Modelling and Simulation, 7(3-4), 204-230. [DOI](https://doi.org/10.1504/IJHFMS.2022.124310)
3. Chander, D. S., Böhme, M., Andersen, M. S., Rasmussen, J., & Cavatorta, M. P. (2023). Simulating the Dynamics of a Human-Exoskeleton System Using Kinematic Data with Misalignment Between the Human and Exoskeleton Joints. In International Symposium on Computer Methods in Biomechanics and Biomedical Engineering (pp. 65-73). Springer, Cham. [DOI](https://doi.org/10.1007/978-3-031-10015-4_6)
