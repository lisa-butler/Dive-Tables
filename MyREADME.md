# Portfolio Project 3: Python Essentials Project
## Dive Tables

### This command-line interface was built as a Python essentials project as part of the diploma in software development at the code institute. It is designed for academic purposes only.


This command-line interface project is built around the concept of a dive computer. Dive planning and decompression control are essential elements of safe diving. The invention of the dive computer has taken much of the guess work out of it in recent years, however, those not diving a computer must utilise an algorithm such as the Buehlmann tables to ensure thir dive is safe.

This is due, predominantly, to the risk of decompression illness. When at depth and at an increased ambient pressure, the divers tissues absorb nitrogen faster. When surfacing from a dive, the diver must give adequate time for their body tissues to 'off-gas'. Not allowing enough time for this or ascending too quickly, can cause the nitrogen in the blood to form bubbles and block off essential tissues, such as the brain, spinal cord etc.

All computers operate off an algorithm that woks out how long a diver can stay at the depth they are at before they will need to add additional ascent stops to ensure they have off-gassed properly.
If a diver was using these tables, he or she would carry them with them on a dive and would plan their dive strictly within the rules drawn out by the tables.

This project aims to create a simple and interactive dive computer based on the Buehlmann tables that can be used to plan and calculate depths, times and decos. This can provide an understanding of how dive computers work as well as aiding in dive planning and understanding the tables.

An image of the tables that this project is based on can be viewed below. It may be important to understand the logic behind these tables in order to test my projects logic. The depth in meters is the first column, displayed in white featuring the numbers 12, 15, 18 etc. As a diver using these tables, i would look for my depth on this coloum. If i was diving to a depth not displayed, i would select the nearest higher value, always rounding upwards. So for example, i am doing a dive to 13m, i do not calculate based on 12m, i move to the 15m category.
The next column of numbers is the time, this depicts the longest i can stay at these depths for. The numbers are the RNT or residual nitrogen time, these were an element ii wanted to add to this project but simply didnt have the time. These show how much nitrogen is left in the divers blood after x amount of time on the surface, and hence, help them calculate their next max dive time and depth. This is where time would come in, so if i dive to 12m for 40 minutes, i would refernece the RG for 57 minutes, which would put me in category D. These tables do not cater for dives outside of 125 minutes or deeper than 51 meters. A diver at a depth of 12m should not exceed 125 minutes, a diver at 15m should not exceed 90 minutes etc. 




![Dive Tables](images/tables.jpg)

### Lisa Butler

## **[Live Terminal] (https://dive-tables.herokuapp.com/)**


------------------------------------------------------------------

## **[Repository](https://github.com/lisa-butler/Dive-Tables)**

------------------------------------------------------------------

## Contnets

 1. [User Experience](#ux)
 2. [Website Features](#features)   
 3. [Technology Used](#tech) 
 4. [Testing](#testing)  
 5. [Bugs](#bugs)  
 6. [Deployment](#deploy)
 7. [Credits](#credits)
 8. [Content](#content)  



![Terminal Launch Page](images/start_terminal.jpg)


## User Experience 

<a name="ux"></a>

### **Pre project planning** 
Before starting this project i investigated the criteria in depth and opted to make an algorithm based project rather than a game or choose your own adventure. I have an interest in how dive computers work and have used dive tables quite a lot in my diver training. I have also found that many people struggle with dive tables and how to work them accurately. This project idea wasformed from this, as an attempt to create an online platform that a user could utilise to make a dive plan or a student could test their knowledge with.
I opted to have an information section in the project to make it a more useful tool for newcomers and those just getting to grips with tables. I also opted to have the option of analysing your decos as well as being able to plan to avoid them. In this way the calculator can be used both premtively and retrospectively.

Lucid charts was used to develop a flow of logic for each option and how it would flow through the code.

**Strategy:**
Determining the best approach meant investigating the needs of the potential users. This included the needs of the divers looking to plan their dives and calculate their decos and the students looking to learn about dive tables and to input different values to see the outcome.
**User stories:**
As a qualified diver:
I want to be able to input my depth and time and find out if i would have hit a deco stop and at what depth.
I want to be able to plan a dive based on a dive time.
I want to plan a dive based on a depth.
I want to know what algorithmm this calculator is using.
I want a quick and easy way to navigate through this program.

As a student:
I want to be able to learn some theory about dive tables.
I want to be able to input depths and times to see if they would require a deco.
I want to be able to find out the max depth i can go to for a given time without incurring a deco.
I want to find out the max time i can dive for at a given depth without incurring a deco.

**Scope:**
The program shoud have a simple interface and be intuitive to work through.
The program should be accessible on all devices.
The program should perform a function correctly.
The diver should be able to use the program as a tool to effectively plan a dive.
The information the program provided should be accurate and correct.
Ideally the program should utilise Google Sheets and an API for development purposes.

### **Structural planning**

UI was very basic for this project as it was a simple command line interface. However, the navigation had to be designed in a user friendly manner. Establishing how to create a good user experience and intuitive process on the application took some thought.

**Main menu:**
A main menu or landing menu was opted for as it provided the opportunity to have an introduction to the page and alert the user to the options avalible within the program. This served as the 'home page' and etablished what the program was for and how to select various options.


**Info option:**
The information option provided the user with a more in depth way to explore the logic behind dive tables and was a way for the developer to explain how the dive table algorithm works and why it is used in the first place. A simple line by line readout was used to provide the user with the information in a steady fashion. The option to return home was presented at the end.


**Dive planning option:**
The dive planning option was created secondary to the deco calculationn option. It was made into its own element as it is very often the case that divers will be planning their dive and opt to dive a certain feature that they know is in a set depth, they will need to calculate how long they will have on this feature (eg. a wreck) before they will hit a deco. Thus, having a time calculation based on a desired depth was a beneficial option. 
When diving for a set time frame, divers may like to check that they wont run into a deco due to being underwater at a shallower depth for a prolongued period. ie. if the divers were opting to dive from shore to a feature and return underwater. They may know this would take 30 minutes to complete. This may be fine at low water, however, at high water, or on a spring tide, there may be an additional 3 meters of water above them. And this traverse may land them in a deco, forcing an earlier surfacing and potentially leaving divers exposed in a shipping lane or other dangerous situation.

**Deco calculator option:**
The deco calculator option was put in as a way for divers to both learn about deco stops and as a way for divers to calculate their decos before or after a dive. The primary function of the deco calculator was to demonstrate the functionality of a dive computer. However, it can be used in this context; If i was planning a dive to 30m and knew that i would be down there for 35 minutes, i would need to check what decos i would be hitting. By inputting these numbers into the calculator, i would see that i would need to do a 4 munute stop at 6m and an 11 minute stop at 3m. These times would then be factored into my plan to enable me to ensure that i had enough breathing gas to achieve this. As most recreational divers should not be hitting deco stops, the calclator should primarily be used to double check computer readings.


**Flow chart:**
Lucid charts was used to generate a flow chart of the program and to plan how to create the code. This was helpful in working out how i wanted the program to flow and where i would need to branch the code to take the user to different options.

![Lucid Charts Flow Chart](images/flow_chart.jpg)


### **Style**

This program is designed to be a simple command line interface and reflects this in its styling. Spacing was left between sentences to allow for better readability and inputs were clearly indicated. 

**Fonts:**
Fonts were the basic command line fonts and were checked to ensure that they were clear and easy to read.

------------------------------------------------------------------

## Website Features

<a name="features"></a>

### **Main menu**


The main menu features a brief print statement that welcomes the user and declares what this program is designed to do. It then gives the user three options;

read some information on dive tables
make a dive plan
or calculate a deco stop

These options are presented and then an input is requested. The user is asked to type 'info' to access the information page, 'plan' to access the dive planning page and 'deco' to access the deco calculator.
When the user types their selection and hits enter the program replies with 'You have selected to visit the x page'.


### **Info Option:**
The info page provides information about the tables to the user in a clear and measured way. It then waits on the screen and propts the user to press any key to return home when they have finished reading. By asking the user to signal that they have finished reading by pressing any key, we prevent the program from moving on before they have finished reading.

### **Dive planning Option**


The dive planning option takes the user to a section that gives them the option to select to plan their dive based on depth or time. When they user makes a selction of time, the program prints 'You have selected to work out how long you can stay at a given depth'. When the suer selects to work out how deep they can be for their dive, the program prints 'You have selected to work out how deep you can go for a given time'.
The user is then propted to imput either their set depth or time and the program reads back to them this selection before directing them to the function that calculates depth or time respectively.

### **Deco calculator option:**

On selecting this option the diver is taken to the deco calculator function. This then asks the user if they would like to start a calculation. Choosing n (no) will take the user back to the meain menu, while choosing y (yes) propts the program to ask further questions. The program will then request a depth and time input. It will then print what the inoutted depth and time was to the user.
If the depth or time fall out of the range supported by the bulhemann tables then the program will inform the user that the tables does not support depths exceeding 51m or times exceeding 125 minutes. It will then give the user the opportunity to start again.
If the depth and time are within the range, the program will check row 2, the row that contains the 3 minute stop time. If this is zero then all other stops are 0. However if this is not 0, then it will check row 3 for 0, if this is zero it gives the number in row 2 as a 3m deco time. If row 3 contains a number > than 0, it will then check row 4, the 9m stop time row. If this contains 0, it will give the time for 3m and 6m. If this contains a number > 0, it will give the stop time for 3m, 6m and 9m.
This information will be printed to the terminal. The user will then be asked if they wish to make another calculation or return to the main landing menu.

**Further features I would implement:**

If I was to build this program with more time and scope I would implement some different features.

* I would have more options for information, such as a history option that would explore the history of dive tables and decompression theory (which is quite fascinating!).
* I would have a user information storage option so that the user could come back and view their previous calculations.
* I would have a front end to improve user experience.
* I would have an option to make your calculations using different algorithms, rather than solely bulhmann.

------------------------------------------------------------------

## Technologies Used 

<a name="tech"></a>


### **Languages** 

The languages used in this project were;

* Python

### **Frameworks/Libraries/programs:**

* GitHub: Used to store the project and to deploy the finished project.
* Fork: This was used as a local place to push code to and to pull from the Git repository.
* Brackets text editor: This was used to write the code locally.
* Lucid Chart was used to plan the flow of my code.
* Heroku was used to deploy my project.

### **Testing software used:**

* I used PEP8 to test my program (http://pep8online.com/).


------------------------------------------------------------------

## Troubleshooting and testing

<a name="test"></a>

### **Troubleshooting:**
Troubleshooting in this project was predominantly focused around issues related to being new to the language. Simple synthax errors as well as function placement and errors in logic made up the bulk of issues that were encountered.


**Testing the program:**
    
* All input sections worked effectively. Yes.
* All requested inputs were assigned an output. Yes.
* Outputs were correct for the input. Yes.
* The text was legible and there were no typos . Yes.
* There was smooth transition between sections. Yes.
* The program was user friendly and intuitive. Yes.
* The outpts given where the program needed to reference the google sheet were correct. Yes.


**Error Handling and input control:**
Error handling and input control were very interesting elements of this project to tackle.
I encountered potential errors at each input and had to put measures in place to mitigate them.

The initial input is asking for a user name, i worded the welcome message below in such a way that it was still accurate if the user just hit return, for example: the input requests a name, the terminal then prints "Welcome to the Buehlmann Tables {name}". This can be read just as cleanly with the name left blank.

The second set of options where this was encountered was the main menu. The user selects between the options of;
    deco
    plan
    info
    and exit

In order to ensure that the input was one of these, i used a simple else statement in the else if these options were within. This simply printed "Invalid input, please try again".

The plan options were slightly more difficult to account for. I needed to ensure that the dept did not exceed 51m and the time did not exceed 125 minutes, as these tables do no account for values outside of this range. I did this by having the program check if they were >125 or >51. I then needed to ensure that the inputs were numbers only. This was done using the except ValueError function inside a while statement. This proved to be a very efficient way of doing this and held up to testing.

The same methods as above were used to ensure that the numbers inputted for the deco calculations were both >51 and >125 and also that they were numbers.


**Testing using PEP8:**

I used the software PEP8 to test each python file individually. The results were all errors pertaining to line length being too long and trailing white spaces. I broke the lines up by using ''' but could not remedy the whitespaces without removing spaces from between words. When i deployed with the lines broken they were displayig wrong so i decided to return them to their previous state as i did not have time to seek another way to solve the line too long error.
No other errors were present.

![PEP8 Testing](images/pep8.jpg)

## Bugs

<a name="bugs"></a>

### **Bugs Found:**


Some interesting bugs were;

 An infinite loop within a while statement that continued to print a statement eternally until i hit cntrl + c. This was fixed by calling the function again after printing the error message once and then breaking the loop.

 ![Infinite loop error](images/infinite_loop.jpg)

 Another bug that was occuring was particularly interesting and difficult to find. After a user had calculated a deco and returned to the main menu, the program remained in a loop and would only return 'No deco needed' to any input. This was solved by having the exit function in the main menu call the landing page function.

Initially i had all of my functions in one file run.py, I eventully decided to break them out into classes in different files and this dramatically improved the ease with which i could fix errors.



------------------------------------------------------------------

## Deployment

<a name="deploy"></a>

Deployment of the program was done via github and Heroku;
* Initially, i opened Heroku and created an account. 
* I then created an app in Heroku and named it dive-tables.
* Returing to my code in gitpod i entered the following command in the terminal: heroku login -i.
* I then entered the following command in the terminal: heroku apps.
* Followed by the command: heroku git:remote -a dive-tables.
* I committed any changes and pushed both to my main branch and Heroku using the terminal commands: git push origin main and git push heroku main respectively.
* In GitHub i clicked on my project dive-tables and went into the settings, there i selcted pages from the menu on the left.
* In source at the top i clicked the pulldown and selcted 'main'.
* I then opened Heroku and selected to connect my app via GitHub.
* This directed me to log into my GitHub and select my project from the list.
* I was then given the option to deploy.
* I hit deploy and the program opened in a new tab.


------------------------------------------------------------------

## Credits and Acknowledgements

<a name="credits"></a>

### **Credits:**

* Code: Code advice was taken from Stack Overflow (https://stackoverflow.com/) and the Code Institutes workthrough projct and course content.
* Information: Some information was taken from dive-tach (http://www.dive-tech.co.uk/workman%20and%20buhlmann.htm) and from Dip N Dive (https://dipndive.com/blogs/dive-gear/dive-computer-algorithms-for-dummies).


### **Acknowledgements:** 

* My program coordinator Kasia for contiuned support and advice throughout.
* My software developer friends (Joshua Butler-senior dev at Overstock Ireland and Glenn Gilmartin- senior dev at Overstock Ireland) for their advice and patience.
* My mentor Seun Owonikoko for advising on the development stages of my project.

------------------------------------------------------------------

## Content and resources

<a name="content"></a>

* All content was written by the developer as part of an academic exercise for the Code Institute.
