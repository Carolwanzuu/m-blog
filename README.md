# BLOGS

## By Carolyne Wanzuu

## Description
This is a a personal blogging website where you can create and share your opinions and other users can read and comment on them.

Additionally, there is a feature that displays random quotes to inspire  users. 



With the application, a user will be able to:

* View the blog posts on the site.
*Comment on the blog posts
*View the most recent posts
*See random quotes on the site
* Sign in and create new blogs
* Update or delete blogs

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display Blogs | **On page load** | List of various Blogs|
**On signing in** | create a new blog|
| Display blogs created within your profile page | **On page load** | view blogs created |
| update or delete blogs| **Signing out** |displays the home page  |

### Prerequisites

You need the following to start working on the project on your local computer:

* A computer running on either Windows, MacOS or Ubuntu operating system installed with the following:

```
-Python version 3.8
-Flask
-Pip
-virtualenv
-A text  Editor
```

## Getting Started

* Clone this repository to your local computer.
* Ensure you have python3.8 installed in your computer.
* From the terminal navigate to the cloned project folder.
* Create a virtual environment and access the folder via your virtual amchine.

* Create start.sh file and in it write the following lines:
```
 export SECRET_KEY='<Your-secret-Key>'
 python3.8 manage.py server
```
* Run ```chmod +x start.sh``` follwoed by ``` ./start.sh ``` while in the project folder to start the project.
* Once started, the project can be accessed on your localhost using the address: ``` localhost:5000 ```.
* Alternatively the application can be accessed by visiting blogmorg.herokuapp.com/

## Technologies Used

* Python v3.8
* Boostrap
* Flask


## License

MIT License

Copyright (c) 2021 Carol Wanzuu