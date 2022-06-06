# cat-carer-5000
## A lightweight web app made to ensure any number of cats you share your home with are kept track of and well cared for. 

> "The smallest feline is a masterpiece"
>  _-Leonardo Da Vinci_

Index:

<details>
<summary> User Stories</summary>

1. As someone with cats and access to the Cat-Carer, \
I want to record details of my cats,\
So I can keep track of them all.

2. As someone with cats and access to the Cat-Carer, \
I want to record what food they like and do not like to eat\
So I can provide them with food they like, and food isn't wasted

3. As someone with cats and access to the Cat-Carer, \
I want to record any special requirements my cats might have, \
So that I can recall their needs and care for them better. 

4. As someone with cats and access to the Cat-Carer, \
I want to be able to change my cat's details in case they change their minds (as cats often do),\
So I can adjust to the whims of my cats as easily as possible. 

5. As someone with cats and access to the Cat-Carer, 
I want to be able to record the amount of pet food and other supplies I have at home, 
So that I can know for sure my cats will be well fed.

</details>

<details>
<summary>From these stories, we can construct **acceptance criteria**:</summary>
1. Given a user has access to the web app, when they enter details of their pet, then they can update a database with those details  
2. Given a user has access to the web app, when they access their pet details, then they can somehow indicate the foods that cat is fond of or dislikes  
3. Given a user has access to the web app, when they access details of their pet, then they can record the medicinal or health needs of that specific pet.  
4. Given a user has access to the web app, when they edit an entry of a requirement or a cat, that change will remain in the database and appear when called next  
5. Given a user has access to the web app, they can easily adjust the app to show how much food they have, and whether that will satisfy their cats.   
</details>
##Initial Planning
We can now construct a plan for functionality of the project. It's clear from the user stories that the app needs to be CRUD capable (create, read, update, delete). It'll need to be connected to a database to ensure entries are retained between visits to the app, and that changes are remembered. The app will make use of a mySQL database for this functionality, and will be developed using python and the Flask micro-framework. 
Progress throughout the project will be tracked using the Jira Board, made for agile development. Different epics have been created based on different phases of the development, extrapolated from the above Use Cases and broken into tasks to facilitate the design of a project like this. 

#***INSERT PICTURE OF JIRA BOARD***
![jira_board](https://user-images.githubusercontent.com/100293943/171617985-7344a58e-e9a2-4e25-be84-92d09cd47587.jpg)

##Design
I created models for the database components of the project by examnining the user stories and deciding upon the minimum requirements for the project as a whole. Below is an Entity Relationship Model I decided upon, in the UML format: 

#***INSERT PICTURE OF DATABASE PLAN***![DB_RM(relationship model)](https://user-images.githubusercontent.com/100293943/171618009-46e888ed-f492-44c1-a055-745cbabc3846.png)


While designing the model, I realised quickly that implementing both a foods liked and foods disliked field would be complicated, both in terms of back-end and front facing UI - already we're looking at a many to many relationship, so doubling up that relationship seemed like something that could potentially be added to the app later if there was time. Using MoSCoW principles, I decided specifying what the cats liked was a Must and what the cats did not like was a Could. I also realised that I'd be looking at another many to many relationship including the medical care information for the cats, so decided to simplify. Instead of a full care app, the cat-carer-5000 will aim specifically at feeding the cats food that they like the most. Given the time constraints of the project, that seemed like a more reasonable aim. Other aspects of care could be added later. 

##Definition of Done
With these adjustments made to the project, I've focused and redefined and am ready to consider the DoD(definition of done) for each main task on the project. 
- Testing must be written and passed with 100% coverage
- Features must meet or excell acceptance criteria

##Risk Assessment
With a small project like this handling non-sensitive data, the risks are not particularly severe, but a risk assessment has been carried out, the results of which are below.

#**INSERT RISK ASSESSMENT**[Risk Assessment - Sheet1.pdf](https://github.com/jd7994/cat-carer-5000/files/8823228/Risk.Assessment.-.Sheet1.pdf)


Another way the project could be extended in the future would be add the funcionality to login as a particular user and access only your own files. As the app stands at the moment, it's only suitable for one user, as all information will be available to anyone who uses it. 


##Implementation
Creating the code and building functionality was fairly trouble free, apart from one feature - I was keen to implement a page that allowed the user to pick form the list of foods which foods their cat liked. This required me to create a form with a field for each item on the food table in the database. This proved quite tricky, shifting several 'for loops' around, and experimenting with feeding various types of data into jinja2 to get the desired response. Eventually it worked as intended, but I still had a problem. The form is instantiated when the app is launched, and if you then add a food item to it, because the route to the page expects a field for each food item in the database, the table is a field short because it doesn't update each time an item is added, only each time the app restarts. 

Here's the error I keep running into:
![error2](https://user-images.githubusercontent.com/100293943/171618127-a9f79a35-1b9f-4212-b2ca-36ab5f8f1bf8.jpg)
![error3](https://user-images.githubusercontent.com/100293943/171618132-ab510139-4c62-46f6-89e1-c22767d91a41.jpg)
![error1](https://user-images.githubusercontent.com/100293943/171618135-cc8fcb75-590e-4502-bf80-dc004196dc86.jpg)


Ultimately, for the timeframe of the project I made the decision to simplify again. The app will now be planned to only support recording a cat's single favourite food - the many to many relationship for liked food is very interesting, and hopefully could be added to the project later. 

