Python code to study the dynamics of inertial particles in a double gyre flow with the inclusion of Coriolis force. Use the following steps:

1. Firstly, run the code Initial Grid of particles.py
2. Then run the code inertial_mapping.py to advect the inertial particles up to a finite time T. If you want to just advect the tracers, you can run the code tracer_mapping.py instead.  
3. Optional. Then run Scatterplots.m to see the particle aggreagtion plot.
4. Then run the FTLE.py code to calculate the FTLE field. 
5. Then, you can run the code FTLE maker.py to visualize the FTLE field. 

Make sure all the codes are reading the proper file before you get started. Initial Grid of Particles.py file will write a file with all the grid positions.

inertial_mapping.py or tracer_mapping.py reads the initial grid of particles file and outputs the final position of particle	at time T file. 

Scatterplots.m  file reads the final position of particle at time T file that was written by mapping.py file. 

FTLE.py file reads the final position of particle at time T file that was written by mapping.py file and outputs the calculated the FTLE file.

FTLE maker.py file reads the reads the calculated FTLE field file and visualizes the FTLE plot. 

