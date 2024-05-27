### Blog

#### Description:
The Blog project is a web application developed using Django, 
aiming to provide a platform for users to create, 
manage, and share their blog posts effectively. 

#### Guide:
To run this application, you need to have Python and Django installed on your system. 
After cloning the repository, navigate to the project directory and ensure that you have installed crispy forms. 
Use the following command to install crispy forms: pip install django-crispy-forms

If you're using a Linux distribution like Ubuntu, it's recommended to set up a virtual environment to manage your project dependencies. Here's how you can do it:

  1. Create a new virtual environment named "myenv": python3 -m venv myenv
  2. Activate the virtual environment:source myenv/bin/activate
  3. Once the virtual environment is activated, install crispy forms: pip install django-crispy-forms

### Current Progress:

- Django templates have been created.
- Connection to a remote PostgreSQL database has been established.
- The entire authentication system has been implemented.
- Users are able to create, update, and delete their own posts.
- Users can view posts created by other users, as well as their own.
- When a user creates an account, they now have access to their profile information, where they can update their data.
- Users can now comment on all posts and can also update and delete their own comments.
- Pagination has been added to reduce potential issues with large amounts of data when rendering posts.

### Usage:

To test the application, you can use the following credentials:

- **Username:** Admin
- **Password:** Password123+
