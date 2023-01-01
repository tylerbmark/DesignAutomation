cd ~/SeniorDesign/DesignAutomation

cp -r ../Neutronics/Neutronics/variable_scripts Scripts/Neutronics
cp -r ../TH/TH/variable_scripts Scripts/TH
cp -r ../Materials/Materials/variable_scripts Scripts/Materials

python main.py

cp -r Scripts/Neutronics/variable_scripts ../Neutronics/Neutronics 
cp -r Scripts/TH/variable_scripts ../TH/TH/
cp -r Scripts/Materials/variable_scripts ../Materials/Materials

cp -r Scripts/Neutronics/new_scripts ../Neutronics/Neutronics
cp -r Scripts/TH/new_scripts ../TH/TH
cp -r Scripts/Materials/new_scripts ../Materials/Materials