# NumericalOptimization
Thesis Project 

@Giulia Faletti

## Lists of files present in the directory

  - [Compar_L_int_Mes_Real](https://github.com/GiuliaFaletti/NumericalOptimization/blob/main/Compar_L_int_Mes_Real.py)
  - [DataModel](https://github.com/GiuliaFaletti/NumericalOptimization/blob/main/DataModel.py)
  - [DataModel2](https://github.com/GiuliaFaletti/NumericalOptimization/blob/main/DataModel2.py)
  - [DataModel3](https://github.com/GiuliaFaletti/NumericalOptimization/blob/main/DataModel3.py)
  -
  -
  -
  -
  -
  -
  -
  - [LoadData](https://github.com/GiuliaFaletti/LuminosityOptimization/blob/main/LoadData.py): Module that defines different functions able to extract data from FillData.xlsx and TurnAroundData.xlsx. It is important to say that the loaded data have been previously cut considering only the turnaround times that can be used for statistical purposes, and the fills defined "physics fills";
  - [LuminosityOptimization](https://github.com/GiuliaFaletti/LuminosityOptimization/blob/main/LuminosityOptimization.py): Module that defines different functions that evaluate the optimization model parameters, like the optimized fill times;
  - [TurnArounData](https://github.com/GiuliaFaletti/LuminosityOptimization/blob/main/TurnAroundData.xlsx): Excel file with sorted statistical samples of turn around times (sample16, sample17, sample18).
  - [FillData](https://github.com/GiuliaFaletti/LuminosityOptimization/blob/main/FillData.xlsx): Excel file with turnaround times and fill times for each year (t16, tf16, ta17, tf17, ta18, tf18), fills numbers (NrFill_2016, NrFill_2017, Nr_fill2018) and statistical samples of turn around times (sample16, sample17, sample18);
  - [ATLAS](https://github.com/GiuliaFaletti/LuminosityOptimization/blob/main/ATLAS.zip):
  
      -------------------------- Input Floders ---------------------------------------------------

       - ATLAS_fill_2016: Atlas lumi files for 2016, whose detailed description is available on   
         [https://lpc.web.cern.ch/MassiFileDefinition_v2.htm].
       - ATLAS_fill_2017: Atlas lumi files for 2017, whose detailed description is available on
          [https://lpc.web.cern.ch/MassiFileDefinition_v2.htm];
       - ATLAS_fill_2018: Atlas lumi files for 2018, whose detailed description is available on
                        [https://lpc.web.cern.ch/MassiFileDefinition_v2.htm];
       - ATLAS_summary_2016: Atlas summary files for 2016, whose detailed description is available on
                        [https://lpc.web.cern.ch/MassiFileDefinition_v2.htm];
       - ATLAS_summary_2017: Atlas summary files for 2016, whose detailed description is available on
                        [https://lpc.web.cern.ch/MassiFileDefinition_v2.htm];
       - ATLAS_summary_2018: Atlas summary files for 2016, whose detailed description is available on 
                        [https://lpc.web.cern.ch/MassiFileDefinition_v2.htm].
                       
       -------------------------- Output Floders ---------------------------------------------------

       - FillsLuminosityEvolution2016: Plots of the Luminosity evolution of 2016;
       - FillsLuminosityEvolution2017: Plots of the Luminosity evolution of 2017;
       - FillsLuminosityEvolution2018: Plots of the Luminosity evolution of 2018;
       - OptimalFillsLuminosityEvolution2016: Hypotetical fill plots of the Luminosity evolution of 2016;
       - OptimalFillsLuminosityEvolution2017: Hypotetical fill plots of the Luminosity evolution of 2017;
       - OptimalFillsLuminosityEvolution2018: Hypotetical fill plots of the Luminosity evolution of 2018.
