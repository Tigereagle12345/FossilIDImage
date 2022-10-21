import os

yn_list = {
  "y": ["Yes", "yes", "YES", "y", "Y"]
  "n": ["No", "no", "NO", "n", "N"]
}

def pip(yn_list):
  yn = str(input("Do you use pip to install python packages? Y/N "))
  if yn in yn_list["y"]:
    packages = ["tensorflow", "pyyaml h5py", "os", "pandas", "numpy"]
    for p in packages:
      os.system("pip install "+p)
  
  elif yn in yn_list["n"]:
    print("Ok! In order to use this program, you will need to install the 'tensorflow', 'pyyaml h5py', 'os', 'pandas' and 'numpy' python modules.")
    
  else:
    print("Error! Invalid Input.")
    pip(yn_list)
    
