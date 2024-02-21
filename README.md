# cyb600_Lab1
PyPi page: https://pypi.org/project/cyb600-lab1-perreaua10/
Github page: https://github.com/perreaua10/cyb600_Lab1

	For my simple web server I used the package FastAPI, a very quick and barebones way of making a web server or RESTful API. There are 2 methods of spinning up the web server, however the main/intended way is to use the script which is installed with the PyPi project. To use this script, on Linux you must first make sure that you can run scripts by entering the following commands from out module 3 exercise:
______________________________________________________________________________
First, run
echo "export PATH=$PATH:~/.local/bin/" >> ~/.bashrc
This command is going to add an entry to the Linux Environment variable called PATH to also look in ~/.local/bin/ for executables. We append this to the file ~/.bashrc so that every time you login to the machine, Linux will know where to look for executables you installed there.
Next run
source ~/.bashrc
______________________________________________________________________________

Once you’ve made sure you can run the script, next you should use pip to install the LATEST version of the package from PyPi, which is version 1.1.0. This can be achieved by running the following command: 
pip install cyb600-lab1-perreaua10 
After running the command it’s now time to run the script that came with the package. Assuming you’ve followed the previous steps, you can run the following command from your terminal window: 
start-web-server
There should now be a web server running on your machine, at localhost:8000. If you go to that point however, you will notice that there will be nothing but a screen that  says “Not Found”. That’s because the endpoint for the lab’s web page is at localhost:8000/time. At this point, following that end point should give you the following screen in your browser:

This fulfills the requirements for lab 1! To close the server, either close the terminal window from which the script is running, or press “Ctrl+C” in that window to terminate the process.
