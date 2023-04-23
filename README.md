<h1>Yoga</h1>
Yoga website is created with a Django functionality, bootstrap and HTML. The healthy life style yoga blog website can be assessed, navigated to the blog that interest the user. As it is a crud functionality, the app can post testimonials,comments, read, update or delete comment. The website was builth using Agile methodology for structure, and for UI Design Bootstrap technology.

<h2><Strong>Image:</strong></h2>

<li>The Image in defferent views </li>
</ul>

![image](/static/images/landingpage.PNG)


<h2><Strong>User Experience Design:</strong></h2>

<li>For user to understand what the site is all about and to know the importane of the website and the organization.</li>
<li>For user to navigate to the post of interest</li>
<li>Reaching out to the organization through the contact page</li>
<li>To create an account with the website</li>
<li>To be able to create,update and delete testimonies</li>
<li>To access the webpage using handy divices like smart phones, ipad etc </li>

<h2><Strong>Features and the render testing images:</strong></h2>
<li>The webpage has a landing contents and features providing information about the website and the importance of Yoga fitness and blog posts for users to read more and positioning to balance a healthy life style and the benifits of it.</li>

![image](/static/images/IMG_7491.jpg)



<h2><Strong>Create Comment:</strong></h2>
<li>Users are unable to comment or give testimony regarding their experience with the Yoga organization or blog, rather a pop up messge will appear asking the user, 'You must be logged in to comment' </li>

![image](/static/images/co1.PNG)




<h2><Strong>Create:</strong></h2>
<li>Users are able to create comment in the blog post or testimonies after they have register an account with the site</li>

![image](/static/images/create2.PNG)

<h2><Strong>Read:</strong></h2>
<li>User to be able login to view their testimony or comment</li>

![image](/static/images/testi-create.PNG)

<h2><Strong>Update:</strong></h2>
<li>User can be able to make changes to their testimony or comment</li>

![image](/static/images/update23.PNG)


<h2><Strong>Delete:</strong></h2>
<li>User will be able to delete testimony or comment but before the delete is gone, a pop up message appears "Are you sure you want to delete?"</li>

![image](/static/images/delei.PNG)


<h2><Strong>Notification:</strong></h2>
<li>For users to be able to see if there are any testimonies or comments on the post.</li>

![image](/static/images/dele.PNG)

<h2><Strong>Wait List :</strong></h2>
<li>Individuals showing interest in our Yoga training will have to register an account and also register their email address in our data base inorder to know the counts of individuals that we be joing the next Yoga programme and the benifits joining us.</li>

![image](/static/images/waitlist.PNG)



<h2><Strong>Sign Up :</strong></h2>

<li>It is important for user to register an account inorder for them to comment or testify </li>

![image](/static/images/sign.PNG)

<h2><Strong>Sign In :</strong></h2>

<li>It is important for user to sign into their account inorder for them to comment or testify </li>

![image](/static/images/signin.PNG)


<h2><Strong>Sign Out :</strong></h2>

<li>User can sign out from his or her account </li>

![image](/static/images/signout.PNG)



<h2><Strong>Diet stretching :</strong></h2>


![image](/static/images/diet.PNG)


<h2><Strong>Shoulder & chest stretch:</strong></h2>


![image](/static/images/shoulder.PNG)


<h2><Strong>Back health & balance:</strong></h2>

![image](/static/images/back.PNG)


<h2><Strong>Footer:</strong></h2>

<li>A footer has been added to the bottom of the site with social media icons, aria-labels to ensure users with assistive screen reading technology and to know what the purpose of the links are for and it also contains a  Facebook, Twitter,instagram and youtube link as the social icons only on the footer and the direct links that opens are on the left side on the top of the site 'under social media' so that users can follow us on social media if they want to keep up to date with our organization and events. The links navigate users away from the site.</li>

![image](/static/images/footer.PNG)


<h2><Strong>Agile Planning:</strong></h2>
<li>This project was developed using agile methodologies</li>

<li>All tasks were assigned to epics, prioritized under the Todo, Progress and Done.</li>

<li>They were assigned to carry along as the project is progressing and stories allocated accordingly to the complexity. "Todo" stories is where I have listed the 'must have' stories lines, and "In progress" is where I have on going work in the tast mangement listed, likewise 'Done list', where I have the task completed.

<li>The Kanban board was created using github projects, the image can be viewed to see more information on the project cards. All stories except the documentation tasks have a full set of acceptance criteria in order to define the functionality that marks that story as complete.</li>
  
<li>It was done this way to ensure that all core requirements were completed first to give the project a complete sense of work.</li>

The Kanban board was created using github projects and the below image is where you can view the information on the project cards. All stories except the documentation tasks have a set of acceptance criteria in order to define the functionality that marks that story as completed.</li>

  <li>    
  
  -[Agile Board](https://github.com/users/email2ify/projects/11) 
  
  </li>
  
  ![image](/static/images/agile.PNG)



<h2><Strong>Features unsolved:</strong></h2>

<li>The login functionality in the site does not provide the ability for user to delete registered account, as users can only create account.</li>

<h2><Strong>Database:</strong></h2>

<li>A postgreSQL database offered by elephantSQL was the choice of database connected with the django framework during project development.</li>
<li>The database was designed to allow CRUD functionality to be available to registered users, when signed in. The user model is the main application as it is connected the main comment and post, linked by primary/foreign key relationships.</li>

<li>The comment model holds objects that are linked to the comment Models by a many to many relationship. This allows users to create comment or testimony to others.</li>

<li>Written testimony or comments by a Foreign Key which allows the users to be able to view and update testimony after registration.</li>


<h2><Strong>Security:</strong></h2>
<li>The admin path was changed from the conventional name admin</li>
<li>The website as a secure HTTP to prevent cyber attacks during data sharing.</li>
<li>Environment variables were stored in an env.py for local development for security purposes to ensure no secret keys, api keys or sensitive information was added the repository. In production, these variables were added to the heroku config vars within the project.</li>
<li>Django has a security line code wriiten CSRF for forms in this website to prevent malicious cyber attacks.</li>
<li>The Debug is set to false before production.</li>


<h2><Strong>Testing:</strong></h2>
<li>The manual testing of the site was rendering as expected. Each section of the site was tested and no errors were found.</li>
<li>From the view page, the navbar was working as expected and I was able to navigate to the preferred section as expected on the about page, contact page,home page, the external links for the social media and the internal navigation for the login ,register and logout navbar.</li>
<li>In the body of the site, there is a created post and date and when a user want to read about the post, I tested the read more to confirm the navigation of the read more of the post which the navigation of the read more worked as expected and the full details of the post was open</li>

<li>I also tested the features navigation read more and the link was open as expected</li>

<li>I also tested the crud functionality. Users and registered users are to read,create, update and delete their content or testimonies and these functions are working as expected having tested the functionality</li>
<li>I tested the admin panel for registered users and also to delete posts and these functions are working as expected</li>

<h2><Strong>Validator testing:</strong></h2>
<li>Lighthouse testing</li>

![image](/static/images/lightHouse%20new.PNG)

<li>validator</li>

<li>CSS validatorr</li>

-[Jigsaw](https://jigsaw.w3.org/css-validator/) 

![image](/static/images/Yoga-css.PNG)

<h2><Strong>Bugs:</strong></h2>
<li>The waiting list field of the site was really a problem to create, inorder to see the registered Yoga email addresses on the database, but at the end the bug was solved and I was able to users email addresses at the database</li>

![image](/static/images/Yogaemail.PNG)

<h2><Strong>Project Deployment:</strong></h2>
<li>The Django project settings Debug is set to be False.</li>

<h2><Strong>Heroku Deployment:</strong></h2>

-[Heroku](https://www.heroku.com/github-students/signup)


Heroku is the hosting platform for the project to deploy. Below are steps taken:

<li>First you need to signin to Heroku or create an account</li>
<li>From Heroku Dashboard,click Create new app,Enter a unique App name,create app after selecting region.</li>
<li>Navigate to Config Vars The config vars should contain the following keys and their corresponding values: DATABASE_URL,CLOUDINARY_URL,SECRET_KEY,PORT and finally to make sure the DISABLE_COLLECTSTATIC is removed before production.</li>
<li>Navigate back to Deploy section and Select Github to connect to Github, Search for github repository using the name of the repository and click connect.</li>
<li>Scroll down to Deploy branch and Select deploy branch to deploy manually.</li>
<li>Click on the button but bear in mind it will take some few seconds for completion,and a View button below will show to click at.</li>
<li>Click to view live website</li>


<h2><Strong>Surface-Colour-Scheme:</strong></h2>
<li>The main color schemes for the website are background-color is faded White (f8f8f808) and dark grayish (#423e3e) for the text and footer (#1a1716),to the website.</li>

<h2><Strong>Typography:</strong></h2>
<li>The Roboto font was used throughout the website. This font is from google fonts and was imported into the style sheet.</li>

<h2><Strong>Image:</strong></h2>
<li>The mark image was taken freepik, which is a free image site at least for many of them</li>


<h2><Strong>Technologies:</strong></h2>


<li> Bootstrap

-[Bootstrap](https://getbootstrap.com) 
</li> 

<li>Github is the site used for the deployment and hosting of this website.              

-[Github](https://github.com/) </li>

<li>Gitpod is the open-source developer platform used in tandem with github for the deployment of the website source code.

-[Gitpod](https://gitpod.io/) </li>

</li>

<li>The postgreSQL Database used for the program.

-[postgresSQL](https://www.elephantsql.com/)</li>
</li>

<li>Freepik. The beautiful Yoga image picture with face masks Cartoon Illustrations.</li>

-[freepik](https://nl.freepik.com//)</li>

<h2><Strong>Credits:</strong></h2>

<li>Documentation Django models and Academy.</li>

-[Django](https://www.djangoproject.com/)
</li>


<li>Code Institute tuturial</li>

-[Code Institute](https://codeinstitute.net/)

<li>Freepik. The beautiful Yoga image picture with face masks Cartoon Illustrations and the other two pictures for the about page and contact page.</li>

-[freepik](https://nl.freepik.com//)</li>

<h2><Strong>Acknowledgement:</strong></h2>
<li>My Mentor, Daisy.</li>

