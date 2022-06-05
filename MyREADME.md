# Portfolio Project 3: Python Essentials Project
## Dive Tables
### This command-line interface was built as a Python essentials project as part of the diploma in software development at the code institute. It is designed for academic purposes only.

This command-line interface project is built around the concept of a dive computer. Dive planning and decompression control are essential elements of safe diving. The invention of the dive computer has taken much of the guess work out of it in recent years, however, those not diving a computer must utilise an algorithm such as the Buehlmann tables to ensure thir dive is safe.

This is due, predominantly, to the risk of decompression illness. When at depth and at an increased ambient pressure, the divers tissues absorb nitrogen faster. When surfacing from a dive, the diver must give adequate time for their body tissues to 'off-gas'. Not allowing enough time for this or ascending too quickly, can cause the nitrogen in the blood to form bubbles and block off essential tissues, such as the brain, spinal cord etc.

All computers operate off an algorithm that woks out how long a diver can stay at the depth they are at before they will need to add additional ascent stops to ensure they have off-gassed properly.

This project aims to create a simple and interactive dive computer based on the Buehlmann tables that can be used to plan and calculate depths, times and decos. This can provide an understanding of how dive computers work as well as aiding in dive planning and understanding the tables.

### Lisa Butler

## **[Live Quiz] (https://lisa-butler.github.io/Dive-Quiz/)** CHANGE THIS!!!!!!!!


------------------------------------------------------------------

## **[Repository](https://github.com/lisa-butler/Dive-Quiz)** CHANGE THIS !!!!

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



![Quiz Start Page](images/startpage.jpg)


## User Experience 

<a name="ux"></a>

### **Pre project planning** 
Before starting this project i investigated the criteria in depth and opted to make an algorithm based project rather than a game or choose your own adventure. I have an interest in how dive computers work and have used dive tables quite a lot in my diver training. I have also found that many people struggle with dive tables and how to work them accurately. This project idea wasformed from this, as an attempt to create an online platform that a user could utilise to make a dive plan or a studnet could test their knowledge with.
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

![Initial logic test](images/initialqtest.jpg)


**Dive planning option:**
The dive planning option was created secondary to the deco calculationn option. It was made into its own element as it is very often the case that divers will be planning their dive and opt to dive a certain feature that they know is in a set depth, they will need to calculate how long they will have on this feature (eg. a wreck) before they will hit a deco. Thus, having a time calculation based on a desired depth was a beneficial option. 
When diving for a set time frame, divers may like to check that they wont run into a deco due to being underwater at a shallower depth for a prolongued period. ie. if the divers were opting to dive from shore to a feature and return underwater. They may know this would take 30 minutes to complete. This may be fine at low water, however, at high water, or on a spring tide, there may be an additional 3 meters of water above them. And this traverse may land them in a deco, forcing an earlier surfacing and potentially leaving divers exposed in a shipping lane or other dangerous situation.

**Deco calculator option:**
The deco calculator option was put in as a way for divers to both learn about deco stops and as a way for divers to calculate their decos before or after a dive. The primary function of the deco calculator was to demonstrate the functionality of a dive computer. However, it can be used in this context; If i was planning a dive to 30m and knew that i would be down there for 35 minutes, i would need to check what decos i would be hitting. By inputting these numbers into the calculator, i would see that i would need to do a 4 munute stop at 6m and an 11 minute stop at 3m. These times would then be factored into my plan to enable me to ensure that i had enough breathing gas to achieve this. As most recreational divers should not be hitting deco stops, the calclator should primarily be used to double check computer readings.


**Wireframes:**
For this project i started with wire frames drawn on paper, these were then mocked up on a wrod docuemnt to form a basic idea of the proposed layout of the quiz pages.
The basic plan for the quiz was to keep it as simple and uncluttered as possible while creating an asthetically pleasing and enjoyable user experience. 

![Wire frame of quiz page](images/wireframequizq.jpg)
