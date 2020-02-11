# Title:
    Data centric milestone by Patrick Trollip.
    Project name: Security products and reviews.

#Deployment:
    The code wa made on Gitpod then pushed to my remote repository on my github account.
    From there my github repository is connected to my Heroku account where the website is hosted.
    I then connected up the Heroku app to the online database on Mongo DB Atlas where data is retrieved and pushed via the website.
    Link to the website is : https://locks-data-centric.herokuapp.com/

# Aims and Objectives:
    The aim of this Project is to meet the requirements of the milestone project and try use C.R.U.D(Create,Read,Update and Delete) to develop a website that 
    will send requests from a user and take user input so that they can make changes to the database. When it does this it should retrieve data from my MongoDB Atlas database using a GET request and return 
    to the user the the data they are looking for.Likewise the user will be able to use a POST method request to the database that allows the user to send to the database edited data which includes deleting,updating and creating data.
    The user should also be able to appropriatly interact with the user interface and interact with the database through the website accordingly and with ease to envoke positive user interaction and experience.
    The objective is to provide a positive interaction with the user and allow them to find a lock on the market an compare it's security specifications with alternative products so they can make a informed decision on what lock to buy.
    Also users of other locks can add to the database and share their experience in the description of the lock giving it's,brand,general description and the Pros and Cons the lock offers the user based on theior experience.

# UX and wireframes:

Homepage wire frame : https://www.wireframes.org/tiger/data/codinghamster90/home_5e418536d06db.htm

List all locks : https://www.wireframes.org/tiger/data/codinghamster90/list_of_locks_5e42ea00c9506.htm 

Expanded details : https://www.wireframes.org/tiger/mt.php?pa=product_details_expanded__5e42d468ef917.htm

Read data : https://www.wireframes.org/tiger/data/codinghamster90/read_data_page_5e42e0afde91d.htm 

Edit data : https://www.wireframes.org/tiger/data/codinghamster90/edit_data_5e42e1080754f.htm 

Delete data : https://www.wireframes.org/tiger/data/codinghamster90/delete_data_5e42e0eabb0c2.htm 

Add data : https://www.wireframes.org/tiger/data/codinghamster90/add_data_5e42e8aad7241.htm


# User stories:

    As a user I want to find a good lock, save money, make a informed choice on a product, promote a good product and make changes.
    I wanted a simple website with a database that is easy to navigate and understand.

    As a customer looking to buy a Padlock to secure my bike,gate,shed or even locker, I needed a way to make an informed
    decision when choosing what lock I wanted to use to secure my property.

    As a user I wanted to have a resource that I could reference that is unbiased and not trying to sell me a lock that is
    simply not suited to my application and budget. I needed a resource where I could give a honest review to other customers
    using my experience owning a particular lock and give a honest representation of how it performed in practice to save 
    others on what they will get when they buy a lock.

    As a expert on locks I wanted a way to inform the public on what they get when they buy a lock. The reason is that
    the lock manufacturers are not always honest when selling a product and very often cut corners to save money at the expense of 
    the user. I want a way to educate people and do my part to remove the ignorance about security devices such as locks.
    To do this I need a way to tell potential lock users exactly what a lock offers and what security it can be expected to
    provide. In order to do this though I need some way of storing my knowledge in a accessable manner that is not hard to
    find and can be updated by myself or others as the products evolve.

    As someone who has bought a lock that was not sold with honest advertising and packaging, I wanted to inform or warn
    others about what I expected and what I got so that others can avoid the locks that are literally trash. I have had to learn
    the hard way that it is better to invest in a quality security device than buy something just to save money and get a inferior lock.


# Technologies used:
    Html5,CSS3,Javascript,Jquery,Python3,Heroku,MongoDB Atlas,
    Materialize framework,Gitpod,Github and the MockupTiger wireframes tool.

# Testing:
    I constantly tested my code online through running it on heroku and via the gitpod CLI. I kept testing the code and debugging it until I 
    corrected the code so that it ran properly and all connections were correct.
    When testing I found that sometimes I had to use alternative platforms to test the code when debugging as the website and code would not launch properly. 
    To achieve that I used Codepen and webbased inspection tool to try find the problems.
    Then corrected them on the gitpod server.

# Defensive Programming:
    I used git ignore to hide files with passwords and user information. ALso added asecurity key to the app.py file.

# Version Control:
    I used Github to save files and updates to the files through regular Git commands like add,commit and push when developing my code.

#Data handling and Database structure:
    I used Mongo Database Atlas with the Flask library in my project to store user data to the database and allow them to manipulate the data from my
    web application.

#User functionality and structure:
    I used a navigation button for users to navigate from page to page with a common layout across each page.
    I also made sure I was allowing the user to Create data in the data base, Read data, Update or edit the existing data and to allow them functionality to Delete data.

#Attribution and resources:
    Github for deployment.

    Gitpod for building the projct.

    I used tutorials on my coding course to help me in getting the project functionality.

    Used Slack and my tutors at code institute to help address questions about code.

    Wire frames = Mockup Tiger wireframes https://www.wireframes.org/tiger/getin.php.

    Materialize Framework = https://materializecss.com/about.html

    Cloud application platform Heroku = https://www.heroku.com

    DeploymentDeploymentMongoDataBase = https://cloud.mongodb.com

    Image I borowed = https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwisenetasia.com%2Fwp-content%2Fuploads%2F2016%2F09%2Fhdr-lock-dlp.png&f=1&nofb=1

