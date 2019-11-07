# Mydia

**Author**: Skyler Burger

**Version**: 1.3.0

## Overview
Have you ever forgotten if you purchased that movie on DVD or Google Play? From which online book store did you pick up that copy of Stephen King's IT? Did I pay for the latest season of American Horror Story on Prime Video or Vudu? 

Whether digital or physical, :star: **Mydia** :star: is here to catalog your media and the many places it may live.

## Architecture
### Frameworks
- [**Django**](https://www.djangoproject.com/): Web framework for developing applications in Python

### Packages
- [**Django REST Framework**](https://www.django-rest-framework.org/): Tools for building APIs with Django
- [**Django REST Framework Simple JWT**](https://github.com/davesque/django-rest-framework-simplejwt): Plugin for DRF that allows easy creation and refreshing of JSON Web Tokens for user auth.

### Continuous Integration
**TDB**

## API
**Under Construction**

## Change Log
10-17-2019 - 1.0.0
- Scaffolded Django application
- Added Movie model

10-18-2019
- Added Shows model
- Added Books model

10-19-2019
- Added list and detail view for models

10-24-2019 - 1.1.0
- Added copy models for each media type
- Added copies to detail views

10-27-2019 - 1.2.0
- Integrated Django REST Framework
- Added serializers and new views for models

11-07-2019 - 1.3.0
- Integrated Django REST Framework Simple JWT with help from [this tutorial](https://iheanyi.com/journal/user-registration-authentication-with-django-django-rest-framework-react-and-redux/)
- Added accounts app
- Users can be created and assigned tokens
