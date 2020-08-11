<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/reubence/heroku-template">
    <img src="images/download.png" alt="Logo" >
  </a>

  <h3 align="center">HEROKU Script-Deployment Template</h3>

  <p align="center">
    An awesome template to jumpstart your python script hosting projects on Heroku!
    <!--<br />
    <a href="https://github.com/reubence/Heroku-Script-Deployment-Template"><strong>Explore the docs »</strong></a> -->
    <br />
    <br />
    <a href="https://github.com/reubence/Heroku-Script-Deployment-Template">View Demo</a>
    ·
    <a href="https://github.com/reubence/Heroku-Script-Deployment-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/reubence/Heroku-Script-Deployment-Template/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Template](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
<!--* [Roadmap](#roadmap)-->
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

<p align="center">
  <a href="https://github.com/reubence/heroku-template">
    <img src=https://lh3.googleusercontent.com/proxy/l3Fi5jqPd6axyq2qRIgC_LqGaQgY4TplQuqMBctQlzhH2wEidEIbA2BNpVOrSC7idwzDB6G_pm-tLvZMbJa6BVznty5hQH7XlSWe4XjbHO_tAgO7H7o4-3IUERI6Kqgs alt="Logo" >
  </a> <!--[![Product Name Screen Shot][product-screenshot]](https://example.com) --></p>

There are many great heroku templates available on GitHub, however, I didn't find one that was configured to host and run python scripts quickly on heroku (on a worker dyno) so I created this enhanced one. I want to create a deployment template so amazing that it'll be the last one you ever need.

Here's why:
* Your time should be focused on creating something amazing. A project that solves a problem and helps others
* You shouldn't be doing the same tasks over and over like preparing a script for deployment on heroku from scratch. In my case, I didn't want to spend time waiting for my code to run. I'd rather just host it on a server and used the freed up space on my PC to play games :stuck_out_tongue_winking_eye:.
* You should reserve the DRY principles to the rest of your life :smile:

Of course, no one template will serve all projects since your needs may be different. So I'll be adding more in the near future. You may also suggest changes by forking this repo and creating a pull request or opening an issue.

A list of commonly used resources that I find helpful are listed in the acknowledgements.

### Built With

* [Heroku](https://heroku.com/)
<!--*** [JQuery](https://jquery.com)
*** [Laravel](https://laravel.com)-->



<!-- GETTING STARTED -->
## Getting Started
First things first, this template is configured to host a worker dyno which allows you to host python scripts on heroku using this template. You can modify this template to run a flask frontend by editing the procfile to ``` web: gunicorn app:server ``` (Renamed server.py file to app.py). Many templates and/or documentations are available online for the same. I'll be going over the steps to configure a worker dyno for hosting scripts on heroku only for the purposes of this guide.

### Prerequisites

Before we begin, you need a couple of things installed...
* Download and Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) and type the following to log into your heroku account ```heroku login ```. 
* Download and Install [git](https://git-scm.com/downloads)

After Downloading git, you can run these commands to set your **username** and **password**.
```git config --global user.email "your_email_address@example.com" 
   git config --global user.name "your_username" 
``` 
<!--```sh
npm install npm@latest -g
```-->

### Installation

1. Scroll to the top of this page, and click on the **Use This Template** button to use this template and create your own repo.
2. Connect the remote repo to your local machine using ``` git remote add origin <remote-repo-url> ```

<!-- USAGE EXAMPLES -->
## Usage

1. Edit the ***server.py*** file in the repo to add your own python scripts. 
2. If you've used any external packages you need to mention them in the ***requirements.txt*** file. 
3. If you've changed the name of the file in **Step 1** then you need to edit it in the ***Procfile*** as well.
```worker: python file-name.py```
4. To deploy to heroku, follow the usual steps for any heroku deployment.
```
git add.
git commit -m"Heroku push"
heroku create
git push heroku master
```



<!-- ROADMAP 
## Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues).

-->

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE 
## License

Distributed under the MIT License. See `LICENSE` for more information.
-->


<!-- CONTACT -->
## Contact

Reuben Rapose - [@reubence](https://www.linkedin.com/in/reubence/) - reuben.rapose@gmail.com

Project Link: [https://github.com/reubence/Heroku-Script-Deployment-Template](https://github.com/reubence/Heroku-Script-Deployment-Template)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Heroku](https://heroku.com/)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
<!--* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)-->





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/reubence/Heroku-Script-Deployment-Template.svg?style=flat-square
[contributors-url]: https://github.com/reubence
[forks-shield]: https://img.shields.io/github/forks/reubence/Heroku-Script-Deployment-Template.svg?style=flat-square
[forks-url]: https://github.com/reubence/Heroku-Script-Deployment-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/reubence/Heroku-Script-Deployment-Template.svg?style=flat-square
[stars-url]: https://github.com/reubence/heroku-template/stargazers
[issues-shield]: https://img.shields.io/github/issues/reubence/Heroku-Script-Deployment-Template.svg?style=flat-square
[issues-url]: https://github.com/reubence/heroku-template/issues
[license-shield]: https://img.shields.io/github/license/reubence/Heroku-Script-Deployment-Template.svg?style=flat-square
[license-url]: https://github.com/reubence/Heroku-Script-Deployment-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/reubence/
[product-screenshot]: https://lh3.googleusercontent.com/proxy/l3Fi5jqPd6axyq2qRIgC_LqGaQgY4TplQuqMBctQlzhH2wEidEIbA2BNpVOrSC7idwzDB6G_pm-tLvZMbJa6BVznty5hQH7XlSWe4XjbHO_tAgO7H7o4-3IUERI6Kqgs