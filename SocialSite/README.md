## Introduction
SocialSite provides registration and login functionality with social platform. It is used to create gravities and other users can repost this gravities based on their follow list.

## Features
### User Registration and Login
- Users can register with their email or mobile number.
- Social media login options are available using Facebook, Apple, and Gmail.
- User profiles can include a username, full name, phone number, gender, birth date, bio, interests, profile type (public/private), and profile photo.

### Posting Gravities
- Users can post Gravities with descriptions, optional tagged users, and the option to allow comments.
- Gravities must belong to at least one category.
- Users can add images or videos to their Gravities, with a required thumbnail for videos.
- Gravities can be retweeted by other users, similar to Twitter.

### Displaying Gravities
- Gravities are displayed in reverse chronological order based on user interest areas.
- Gravities can be reposted (retweeted) by other users, with different display scenarios depending on the interaction.

## Getting Started
Follow these steps to set up the SocialSite project on your local system:

1. #### Clone the Repository:
    ```git clone https://github.com/Meet26499/SocialSite```

2. #### Create an Environment File:
    Create an environment file (.env) and add the necessary variables to configure the project. You will need to set up environment variables for Social Auth login for Facebook, Google and Apple.

3. #### Create a Virtual Environment (Optional):

## API Endpoints
SocialSite provides the following API endpoints:

- `Register`
    - `Endpoint`: http://127.0.0.1:8000/register
    - `Description`: This API is used to register user with different fields

- `Login`
    - `Endpoint` - http://127.0.0.1:8000/login
    - `Description` - This API is used to vauthenticate user and login in our site

- `gravity/list`
    - `Endpoint` - http://127.0.0.1:8000/gravity/list
    - `Description` - This API is used to list out all the gravities which are in area of current user's interest

- `gravity/post`
    - `Endpoint` - http://127.0.0.1:8000/gravity/post
    - `Description` - This API is used to create gravity for current user

- `gravity/repost/id`
    - `Endpoint` - http://127.0.0.1:8000/gravity/post/id
    - `Description` - This API is used to repost existing post of other user.

- `follow/id`
    - `Endpoint` - http://127.0.0.1:8000/follow/id
    - `Description` - This API is used to follow existd user.

- `unfollow/id`
    - `Endpoint` - http://127.0.0.1:8000/unfollow/id
    - `Description` - This API is used to unfollow following user.

- `edit-user`
    - `Endpoint` - http://127.0.0.1:8000/edit-user
    - `Description` - This API is used to edit information which user has put while registering in the system.

## Configuration Of Social Auth

### For this I have used AllAuth library of django

### Facebook Login
To login using Facebook

- Set up a Facebook Developer account and create your app.
- Get your Facebook information (e.g., Client Token, Secret Token).
- Set these Facebook variables in your .env file.

To Login with Facebook use below endpoint

``` http://127.0.0.1:8000/socialauth/facebook/login/ ```

### Google Login
To login using Google

- Set up a Google Console account and create your app.
- Get your Google information (e.g., Client Token, Secret Token).
- Set these Google variables in your .env file.

To Login with Google use below endpoint

``` http://127.0.0.1:8000/socialauth/google/login/ ```

### Apple Login
To login using Apple

- Get your Apple information (e.g., Client Token, Secret Token).
- Set these Apple variables in your .env file.

To Login with Apple use below endpoint

``` http://127.0.0.1:8000/socialauth/apple/login/ ```