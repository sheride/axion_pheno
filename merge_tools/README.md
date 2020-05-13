# axion_data

### Process for merging lhe.gz files:

First, extract all of the `.lhe.gz` files located within the given folder. This can be achieved by making a bash script `gunzip.sh` with the following contents

~~~~
#! /usr/bin/env bash

for f in ./[DIRECTORY]/*.gz ; do gunzip -c "$f" > ./[DIRECTORY]"${f%.*}" ; done
~~~~

Where `[DIRECTORY]` is file path to the folder with the `.lhe.gz` files. If preferred, the second instance of `[DIRECTORY]` can be replaced with a different directory where the extracted lhe files will be deposited. This file can be run with the command `. gunzip.sh` (if you're in the same directory as the script).

After this, we can prepare our merging script. Create a file called `merge.cpp` with the following contents

~~~~
  #include <string>
  std::cout << "initialFileName = " << initialFileName << std::endl;

  std::vector<char*> fileToAddNames;
  for(int fileIt = 0; fileIt < argc-2; ++fileIt)
  {
    fileToAddNames.push_back( argv[2+fileIt] );
    std::cout << "fileToAddName = " << fileToAddNames.at(fileIt) << std::endl;
    }  */


  // open lhe file
  std::string outFileName = "merged.lhe"
  std::ifstream initialFile(initialFileName, std::ios::in);
  std::ofstream outFile(outFileName, std::ios::out);
  
  bool writeEvent = false;
  int eventIt = 0;

  while(!initialFile.eof())
  {
    getline(initialFile, line);
    if( !initialFile.good() ) break;

    if( line == "</LesHouchesEvents>" )
    {
      for(int fileIt2 = 0; fileIt2 < fileIt-1; ++fileIt2)
      {
        std::ifstream fileToAdd(fileToAddNames.at(fileIt2), std::ios::in);

        while(!fileToAdd.eof())
        {
          getline(fileToAdd, line2);

          // decide whether to skip event or not
          if( line2 == "<event>" )
          {
            ++eventIt;
            writeEvent = true;
          }


          // write line to outFile
          if(writeEvent == true)
            outFile << line2 << std::endl;


          // end of event
          if( line2 == "</event>" )
            writeEvent = false;
        }
      }
      break;
    }
    else outFile << line << std::endl;

  }
  outFile << "</LesHouchesEvents>" << std::endl;

  std::cout << "Added " << eventIt << " events from " << fileIt << " files to file " << outFileName << std::endl;
  return 0;
}
~~~~

On the twelfth line, you can replace `"merge.lhe"` with the desired file name for the merged lhe file. Compile this script with the following command.

~~~~
g++ -Wall -o merge merge.cpp
~~~~

This produce an executable file called `merge`. To use this executable, you must prepare a text file containing a list of all of the `.lhe` files you will be merging. If the files you'd like to merge constitute all of the `.lhe` files in a given folder, from the directory containing `merge.cpp` you can run the following command to make this text file.

~~~~
ls ./[DIRECTORY]/*.lhe > lhe_list
~~~~

Where `[DIRECTORY]` is the path from the current folder to the folder containing the `.lhe` files, and the text file created is called `lhe_list`. You can now run your script executable with the following command.

~~~~
./merge lhe_list
~~~~
