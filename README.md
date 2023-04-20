<h1>Yoga</h1>
Yoga website is created with a Django functionality, bootstrap and HTML. The healthy life style yoga blog website can be assessed, navigated to the blog that interest the user. As it is a crud functionality, the app can post testimonials,comments, read, update or delete comment. The website was builth using Agile methodology for structure, and for UI Design Bootstrap technology.

<h2><Strong>Image:</strong></h2>

<li>The Image in defferent views </li>
</ul>

![image](/static/images/yoga%20front.PNG)


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

<h2><Strong>Create:</strong></h2>
<li>User to be able to create comment in the blog post or testimonies</li>

![image](/static/images/create.PNG)

<h2><Strong>Read:</strong></h2>
<li>User to be able login to view their testimony or comment</li>

![image](/static/images/read.PNG)

<h2><Strong>Udate:</strong></h2>
<li>User can be able to make changes to their testimony or comment</li>

![image](/static/images/update.PNG)

<h2><Strong>Delete:</strong></h2>
<li>User will be able to delete testimony or comment.</li>

![image](/static/images/nocomment.PNG)


<h2><Strong>Diet stretching :</strong></h2>


![image](/static/images/feat1.PNG)


<h2><Strong>Shoulder & chest stretch:</strong></h2>


![image](/static/images/feat2.PNG)


<h2><Strong>Back health & balance:</strong></h2>

![image](/static/images/feat3.PNG)


<h2><Strong>Features unsolved:</strong></h2>

<li>The login functionality in the site does not provide the ability for user to delete registered account, as users can only create account.</li>
<li>The waitlist field in the site, for the user to enter their email address to the wait list is not rendering the user's email address to the data base but instead, the email address in the database is only showing the registered email address of users</li>

<h3>Database</h3>
<li>A postgreSQL database offered by elephantSQL was the choice of database connected with the django framework during project development.</li>


<h2><Strong>Security:</strong></h2>
<li>The admin path was changed from the conventional name admin</li>
<li>The website as a secure HTTP to prevent cyber attacks during data sharing.</li>
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

![image](/static/images/Yoga-lighthouse.PNG)

<li>validator</li>

<li>CSS validatorr</li>

-[Jigsaw](https://jigsaw.w3.org/css-validator/) 

![image](/static/images/Yoga-css.PNG)

<h2><Strong>Unfixed Bugs:</strong></h2>
<li>The waiting list of the site</li>

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

<h2><Strong>Acknowledgement:</strong></h2>
<li>My Mentor, Daisy.</li>

