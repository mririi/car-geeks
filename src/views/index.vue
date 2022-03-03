<template>
<html lang="en">
<body style="background:#060818">
<section class="hero">
    <div class="hero-content">
        <h1 class="hero-title">Car <span> </span> Geeks</h1>
        <p class="hero-paragraph">
            Question and Answer website for cars professional and enthusiast.
        </p>
        <div class="hero-options">
            <a href="/auth/register" class="btn btn-developers">Get Started !</a>
            <a href="/auth/login-boxed" class="btn btn-businesses">Sign In</a>
        </div>
    </div>
</section>


<section class="for-enthusiast">
   <div class="container">
       <div class="section-head">
           <h2 class="section-title">For enthusiast
           </h2>
           <div class="section-line"></div>
           <p class="section-description">Car Geeks is an <a href="#">open community</a> for anyone that love cars. We help you get answers to your toughest cars questions and share knowledge with other members
           </p>
       </div>
       <div class="options">
           <div class="option">
               <div class="option-icon">
                   <img src="https://cdn.sstatic.net/Img/home/public-qa.svg?v=d82acaa7df9f" alt="Public Q & A">
               </div>
               <div class="option-title">
                   Public Q&A
               </div>
               <div class="option-description">
                   Get answers to all your questions and give back by sharing your knowledge with others.
                   
               </div>
               <div class="option-button">
                   <a href="/questions" class="option-link btn btn-dark-blue">
                       Browse questions
                   </a>
               </div>
           </div>
           <div class="option">
               <div class="option-icon">
                   <img src="https://cdn.sstatic.net/Img/home/private-qa.svg?v=2c1de180b6d7" alt="Private Q & A">
               </div>
               <div class="option-title">
                   Public Q&A
               </div>
               <div class="option-description">
                   Level up your work with Car Geeks. Share knowledge privately with your clients.
               </div>
               <div class="option-button">
                   <a href="/services" class="option-link btn btn-dark-blue">
                       Browse Services
                   </a>
               </div>
           </div>
           <div class="option">
               <div class="option-icon">
                   <img src="https://cdn.sstatic.net/Img/home/jobs.svg?v=931d6c0863ee" alt="Browse jobs
">
               </div>
               <div class="option-title">
                   Public Q&A
               </div>
               <div class="option-description">
                  Join your friends and other cars lovers to communities groups and share you knowledge with them


               </div>
               <div class="option-button">
                   <a href="/groups" class="option-link btn btn-dark-blue">
                       Browse Groups
                   </a>
               </div>
           </div>
       </div>
   </div>
</section>

<section class="for-businesses">
    <div class="container">
        <div class="section-head">
            <h2 class="section-title">For businesses</h2>
            <div class="section-line"></div>
            <p class="section-description">Our mission is to help companies to become close to their customers. This means helping companies to expose their portfolio in a very beautiful place.</p>
        </div>



        <div class="options">
            <div class="option">
                <div class="option-icon">
                    <img src="https://cdn.sstatic.net/Img/home/private-questions.svg?v=a4f1cfb08f7e" alt="Private Q&A">
                </div>
                <div class="option-description">
                    Quickly find and share internal knowledge with <a href="#" class="option-link">Public Q&A</a>
                </div>
            </div>
            <div class="option">
                <div class="option-icon">
                    <img src="https://cdn.sstatic.net/Img/home/find-candidate.svg?v=9099aa106ad3" alt="Talent solutions">
                </div>
                <div class="option-description">
                    Find the perfect customer for your company with great interactions


                </div>
            </div>
            <div class="option">
                <div class="option-icon">
                    <img src="https://cdn.sstatic.net/Img/home/accelerate.svg?v=9d4c2786ff02" alt=" Advertising platform">
                </div>
                <div class="option-description">
                    Accelerate the discovery of your products or services through our <a href="#" class="option-link">promoting feauture</a>
                </div>
            </div>
        </div>

    </div>
</section>

<section class="questions">
    <div class="container">
       <div class="questions-content">
           <div class="questions-header">
               <h3 class="question-title">Questions are everywhere, answers are on Car Geeks</h3>
           </div>
           <div class="questions-body">
               <div class="questions-body-items">
                   <div class="questions-body-item" data-id="0">
                       <img src="@/assets/images/ask.png" alt="" class="question-item-icon">
                       <div class="question-item-text">Ask a question</div>
                       <div class="question-arrow-right"></div>
                   </div>
                   <div class="questions-body-item"  data-id="1">
                       <img src="@/assets/images/likee.png" alt="" class="question-item-icon">
                       <div class="question-item-text">Like everything</div>
                       <div class="question-arrow-right"></div>
                   </div >
                   <div class="questions-body-item"  data-id="2">
                       <img src="@/assets/images/answer.png" alt="" class="question-item-icon">
                       <div class="question-item-text">Answer questions</div>
                       <div class="question-arrow-right"></div>
                   </div>
               </div>
               <div class="questions-body-item-content">
                   <img src="@/assets/images/quest.png" alt="" class="question-item-content-img">
                   <h4 class="question-item-content-text">
                       Accept the answer which solved your problem to let others benefit from the valuable information.
                   </h4>
                   <a href="/auth/register" class="btn btn-dark-blue question-item-content-btn">Create an account</a>
               </div>
               <div class="questions-body-items">
                   <div class="questions-body-item"  data-id="3">
                       <img src="@/assets/images/search.png" alt="" class="question-item-icon">
                       <div class="question-item-text">Search questions</div>
                       <div class="question-arrow-left"></div>
                   </div>
                   <div class="questions-body-item"  data-id="4">
                       <img src="@/assets/images/check.png" alt="" class="question-item-icon">
                       <div class="question-item-text">Check answers</div>
                       <div class="question-arrow-left"></div>
                   </div>
                   <div class="questions-body-item"  data-id="5">
                       <img src="@/assets/images/badges.png" alt="" class="question-item-icon">
                       <div class="question-item-text">Get Badges</div>
                       <div class="question-arrow-left"></div>
                   </div>
               </div>
           </div>
          
       </div>
    </div>
</section>



<footer class="footer">
    <img src="https://cdn.sstatic.net/Img/home/robot.svg?v=dfa16a330cbd" alt="" class="footer-robot-img">
<div class="container">
    <div class="footer-content">
        <div class="footer-icon">
            <i class="fab fa-stack-overflow"></i>
        </div>
        <div class="footer-nav">
            <div class="footer-nav-col">
                <div class="footer-links-title"><a href="#">Car Geeks</a></div>
                <ul class="footer-links">
                    <li class="footer-link-item"><a href="/questions" class="footer-link">Questions</a></li>
                    <li class="footer-link-item"><a href="/services" class="footer-link">Services</a></li>
                    <li class="footer-link-item"><a href="/entreprises" class="footer-link">Entreprises</a></li>
                    <li class="footer-link-item"><a href="/groups" class="footer-link">Groups</a></li>
                    <li class="footer-link-item"><a href="/news" class="footer-link">News</a></li>
                    <li class="footer-link-item"><a href="/contactus" class="footer-link">Contact Us</a></li>
                </ul>
            </div>
            <div class="footer-nav-col">
                <div class="footer-links-title"><a href="#">Questions</a></div>
                <ul class="footer-links">
                    <li class="footer-link-item"><a href="#" class="footer-link">Add Question</a></li>
                    <li class="footer-link-item"><a href="#" class="footer-link">Explore Questions</a></li>
                    
                </ul>
            </div>
            <div class="footer-nav-col">
                <div class="footer-links-title"><a href="#">Services</a></div>
                <ul class="footer-links">
                    <li class="footer-link-item"><a href="#" class="footer-link">Add Service</a></li>
                    <li class="footer-link-item"><a href="#" class="footer-link">Explore Services</a></li>
                </ul>
            </div>
           
        </div>
        <div class="footer-another-links">
            <div class="social-media">
                <ul>
                    
                    <li>
                        <a href="#">Facebook</a>
                    </li>
                    <li>
                        <a href="#">Twitter</a>
                    </li>
                    <li>
                        <a href="#">LinkedIn</a>
                    </li>
                    <li>
                        <a href="#">Instagram</a>
                    </li>
                </ul>
            </div>
            <div class="copyright text-center">
                <p>Car Geeks 2022</p>
            </div>
        </div>
    </div>

</div>
</footer>


</body>
</html>
</template>

<script>
export default {

}
</script>

<style scoped>
/* Global Styles */
:root {
  --white: #fff;
  --primary:#060818;
  --black: #0c0d0e;
  --orange: #f48024;
  --yellow: #fbf2d4;
  --green: #5eba7d;
  --blue: #0077cc;
  --powder: #e1ecf4;
  --red: #d1383d;
  --black-025: #fafafb;
  --black-050: #eff0f1;
  --black-075: #e4e6e8;
  --black-100: #d6d9dc;
  --black-150: #c8ccd0;
  --black-200: #bbc0c4;
  --black-300: #9fa6ad;
  --black-350: #9199a1;
  --black-400: #848d95;
  --black-500: #6a737c;
  --black-600: #535a60;
  --black-700: #3c4146;
  --black-750: #2f3337;
  --black-800: #242729;
  --black-900: #0c0d0e;
  --orange-050: #fff7f2;
  --orange-100: #fee3cf;
  --orange-200: #fcd0ad;
  --orange-300: #f7aa6d;
  --orange-400: #f48024;
  --orange-500: #f2720c;
  --orange-600: #da670b;
  --orange-700: #bd5c00;
  --orange-800: #a35200;
  --orange-900: #874600;
  --blue-050: #f2f9ff;
  --blue-100: #cfeafe;
  --blue-200: #addafc;
  --blue-300: #6cbbf7;
  --blue-400: #379fef;
  --blue-500: #0095ff;
  --blue-600: #0077cc;
  --blue-700: #0064bd;
  --blue-800: #0054a3;
  --blue-900: #004487;
  --powder-050: #f4f8fb;
  --powder-100: #e1ecf4;
  --powder-200: #d1e5f1;
  --powder-300: #b3d3ea;
  --powder-400: #a0c7e4;
  --powder-500: #7aa7c7;
  --powder-600: #5b8db1;
  --powder-700: #39739d;
  --powder-800: #2c5777;
  --powder-900: #1e3c52;
  --green-025: #eef8f1;
  --green-050: #dcf0e2;
  --green-100: #cae8d4;
  --green-200: #a6d9b7;
  --green-300: #82ca9a;
  --green-400: #5eba7d;
  --green-500: #48a868;
  --green-600: #3d8f58;
  --green-700: #2f6f44;
  --green-800: #29603b;
  --green-900: #1e472c;
  --yellow-050: #fdf7e3;
  --yellow-100: #fbf2d4;
  --yellow-200: #f1e5bc;
  --yellow-300: #e6d178;
  --yellow-400: #e9c63f;
  --yellow-500: #ddb624;
  --yellow-600: #cea51b;
  --yellow-700: #b89516;
  --yellow-800: #9f8010;
  --yellow-900: #826a0b;
  --red-050: #fdf3f4;
  --red-100: #f9d3d7;
  --red-200: #f4b4bb;
  --red-300: #e87c87;
  --red-400: #de535e;
  --red-500: #d1383d;
  --red-600: #c02d2e;
  --red-700: #ac2726;
  --red-800: #942121;
  --red-900: #7a1819;
  --gold: #ffcc01;
  --gold-lighter: #fff4d1;
  --gold-darker: #f1b600;
  --silver: #b4b8bc;
  --silver-lighter: #e8e8e8;
  --silver-darker: #9a9c9f;
  --bronze: #caa789;
  --bronze-lighter: #f2e9e1;
  --bronze-darker: #ab825f;
  --fc-dark: #0c0d0e;
  --fc-medium: #3c4146;
  --fc-light: #6a737c;
  --focus-ring: rgba(0,149,255,0.15);
  --focus-ring-success: rgba(166,217,183,0.4);
  --focus-ring-warning: rgba(233,198,63,0.4);
  --focus-ring-error: rgba(192,45,46,0.15);
  --focus-ring-muted: rgba(36,39,41,0.1);
  --bs-sm: 0 1px 2px rgba(0,0,0,0.05),0 1px 4px rgba(0,0,0,0.05),0 2px 8px rgba(0,0,0,0.05);
  --bs-md: 0 1px 3px rgba(0,0,0,0.06),0 2px 6px rgba(0,0,0,0.06),0 3px 8px rgba(0,0,0,0.09);
  --bs-lg: 0 1px 4px rgba(0,0,0,0.09),0 3px 8px rgba(0,0,0,0.09),0 4px 13px rgba(0,0,0,0.13);
  --scrollbar: rgba(0,0,0,0.2);
  --highlight-bg: #f6f6f6;
  --highlight-color: #2f3337;
  --highlight-comment: #656e77;
  --highlight-punctuation: var(--black-600);
  --highlight-namespace: #b75501;
  --highlight-attribute: #015692;
  --highlight-literal: #b75501;
  --highlight-symbol: #803378;
  --highlight-keyword: #015692;
  --highlight-variable: #54790d;
  --highlight-addition: #2f6f44;
  --highlight-deletion: #c02d2e;
  --dark-blue:#2b2d6e;
  --magnolia:#f7f6f9;
}

@font-face {
  font-family: "Source Sans Pro";
  font-style: normal;
  font-weight: 400;
  src: local("Source Sans Pro Regular"), local("SourceSans Pro-Regular"), local("Source Sans Pro 400"), local("SourceSans Pro-400"), local("Source Sans Pro"), url("https://cdn.sstatic.net/Fonts/source-sans-pro/source-sans-pro-regular-webfont.woff?v=993db0ec4347") format("woff");
}
@font-face {
  font-family: "Source Sans Pro Bold";
  font-style: normal;
  font-weight: 700;
  src: local("Source Sans Pro Bold Bold"), local("SourceSans Pro Bold-Bold"), local("Source Sans Pro Bold 700"), local("SourceSans Pro Bold-700"), url("https://cdn.sstatic.net/Fonts/source-sans-pro/source-sans-pro-bold-webfont.woff?v=f52ccc0bbce9") format("woff");
}
@font-face {
  font-family: "Roboto Slab";
  font-style: normal;
  font-weight: 400;
  src: local("Roboto Slab Regular"), local("RobotoSlab-Regular"), local("Roboto Slab 400"), local("RobotoSlab-400"), local("Roboto Slab"), url("https://cdn.sstatic.net/Fonts/roboto-slab/roboto-slab-regular-webfont.woff?v=a75088a46d79") format("woff");
}
@font-face {
  font-family: "Roboto Slab Bold";
  font-style: normal;
  font-weight: 700;
  src: local("Roboto Slab Bold Bold"), local("RobotoSlab Bold-Bold"), local("Roboto Slab Bold 700"), local("RobotoSlab Bold-700"), url("https://cdn.sstatic.net/Fonts/roboto-slab/roboto-slab-bold-webfont.woff?v=719d1c709127") format("woff");
}
*, *::before, *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-family: Arial, "Helvetica Neue", Helvetica, sans-serif;
  font-size: 10px;
  color: var(--black-800);
}

.container {
  width: 100%;
  max-width: 126.4rem;
  margin: 0 auto;
  padding: 0 1.5rem;
}

section {
  padding: 5rem 0;
}

ul {
  list-style: none;
}

a {
  text-decoration: none;
  color: var(--blue-600);
  cursor: pointer;
}

img {
  width: 100%;
  max-width: 100%;
  height: auto;
}

.btn {
  text-align: center;
  font-size: 1.3rem;
  border-radius: 3px;
  transition: all 0.5s;
  padding: 1.3rem 2.5rem;
}

.btn-orange {
  background-color: var(--orange);
  color: var(--white);
}

.btn-dark-blue {
  background-color: #4361ee;
  color: var(--white);
}

/* Hero */
.hero {
  background-image: url("../assets/images/CarGEEKS.png");
  background-repeat: no-repeat;
  background-position: top center;
  background-color: #060818;
  height: 80vh;
  display: flex;
  justify-content: center;
  align-items: center;

}

.hero-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 0 3rem;
}

.hero-title {
  color: var(--black-800);
  font-family: "Roboto Slab Bold", serif;
  font-weight: 700;
  font-weight: bold;
  font-size: 5.5rem;
  text-align: center;
  max-width: 100%;
}
.hero-title span {
  font-family: Consolas, Menlo, Monaco, Lucida Console, Liberation Mono, DejaVu Sans Mono, Bitstream Vera Sans Mono, Courier New, monospace, sans-serif;
}

.hero-paragraph {
  margin: 2rem 0;
  font-size: 2rem;
  color: var(--black-800);
  max-width: 40rem;
  font-weight: 400;
  text-align: center;
  font-family: "Source Sans Pro", sans-serif;
}

.hero-options {
  display: flex;
}

.btn-developers {
  background-color: #4361ee;
  color: var(--white);
  border: 1px solid var(--orange-400);
}

.btn-businesses {
  background-color: var(--orange-400);
  color: var(--white);
  margin-left: 0.5rem;
}

/*End Hero*/
/* For enthusiast*/
.section-head {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: var(--black-800);
}

.section-title {
  font-size: 3.4rem;
  font-family: "Roboto Slab Bold", serif;
  font-weight: 700;
}

.section-line {
  width: 64px;
  height: 8px;
  margin: 3rem auto;
  border-radius: 100rem;
  background-color: var(--orange-400);
}

.section-description {
  font-size: 1.7rem;
  max-width: 52.6rem;
  text-align: center;
}
.section-description a {
  color: var(--orange-400);
}

.for-enthusiast .options {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 90%;
  margin-left: auto;
  margin-right: auto;
}
.for-enthusiast .option {
  flex-basis: 30%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 3rem;
  background-color: #060818;
  border-color:#191e3a;
  border-width: 2px;
  box-shadow: var(--bs-md);
  border-radius: 0.7rem;
}
.for-enthusiast .option:nth-child(1), .for-enthusiast .option:nth-child(3) {
  margin-top: 12rem;
}
.for-enthusiast .option:hover {
  box-shadow: var(--bs-lg);
}
.for-enthusiast .option-title {
  color: var(--black-800);
  font-size: 2.1rem;
  font-weight: 400;
  margin: 2rem 0;
}
.for-enthusiast .option-description {
  font-size: 1.4rem;
  font-weight: 400;
  text-align: center;
  color: var(--black-800);
}
.for-enthusiast .option-description a {
  color: var(--orange-400);
}
.for-enthusiast .option-button {
  margin: 3rem 0 2rem;
  background: #4361ee;
}
.for-enthusiast .option-link {
  color: var(--white);
}

/* End For enthusiast*/
/*For Businesses*/
.for-businesses {
  background-color: var(--magnolia);
  padding: 10rem 0;
}
.for-businesses .options {
  margin-top: 6rem;
  display: flex;
  justify-content: space-evenly;
}
.for-businesses .option {
  flex-basis: 30%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 3.5rem;
  background-color: 
#060818;
  box-shadow: var(--bs-md);
  border-radius: 0.7rem;
}
.for-businesses .option-description {
  font-size: 1.7rem;
  font-weight: 400;
  margin-left: 1rem;
  color: var(--black-800);
}
.for-businesses .option-link {
  color: var(--orange-400);
}

/* End For Businesses */

/* Questions */
.questions-content {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
.questions-content .question-title {
  font-family: "Roboto Slab Bold", serif;
  font-weight: 900;
  color: var(--black-800);
  font-size: 3.4rem;
  text-align: center;
}

.questions-header {
  margin: 3rem 0 6rem;
}

.questions-body {
  display: flex;
  justify-content: center;
}

.questions-body-item {
  flex-basis: 20%;
  display: flex;
  align-items: center;
  padding: 1.5rem 5rem 1.5rem 1.5rem;
  margin-bottom: 2rem;
  position: relative;
  cursor: pointer;
  z-index: 2;
}
.questions-body-item:hover {
  border-color: transparent;
  box-shadow: var(--bs-md);
}
.questions-body-item.active {
  box-shadow: var(--bs-lg);
}
.questions-body-item.active:hover {
  box-shadow: var(--bs-md);
}
.questions-body-item.active .question-arrow-right {
  position: absolute;
  top: 0;
  height: 100%;
  overflow: hidden;
  width: 1.6rem;
  left: 100%;
}
.questions-body-item.active .question-arrow-right:after {
  position: absolute;
  top: 50%;
  content: "";
  width: 1.6rem;
  height: 1.6rem;
  background-color: #fff;
  border: 1px solid #d6d9dc;
  box-shadow: 2px 0 8px rgba(59, 64, 69, 0.1);
  transform: translate(-50%, -50%) rotate(45deg);
  transition: all 0.2s;
}
.questions-body-item.active .question-arrow-left {
  position: absolute;
  top: 0;
  height: 100%;
  overflow: hidden;
  width: 1.6rem;
  right: 100%;
}
.questions-body-item.active .question-arrow-left:before {
  position: absolute;
  top: 50%;
  content: "";
  width: 1.6rem;
  height: 1.6rem;
  background-color: #fff;
  border: 1px solid #d6d9dc;
  box-shadow: 2px 0 8px rgba(59, 64, 69, 0.1);
  transform: translate(-50%, -50%) rotate(45deg);
  transition: all 0.2s;
  right: -100%;
}

.question-item-icon {
  width: 5rem;
}

.question-item-text {
  margin-left: 1rem;
  color: var(--black-800);
  font-size: 1.7rem;
  font-family: "Source Sans Pro", sans-serif;
  font-weight: 400;
}

.questions-body-item-content {
  flex-basis: 40%;
  margin: 0 3rem;
  display: block;
  text-align: center;
}

.question-item-content-text {
  padding: 4rem 0;
  font-size: 2.1rem;
  font-family: "Roboto Slab", serif;
  font-weight: 500;
  color: var(--black-800);
}

.question-item-content-btn {
  margin-top: 2rem;
  padding: 1.5rem 2.5rem;
}

.questions-footer {
  margin: 20rem 0 10rem;
  width: 100%;
}

.questions-grid {
  margin-top: 6rem;
  padding: 0 5rem;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(20rem, 1fr));
  grid-gap: 2.5rem;
}

.grid-item-img {
  max-height: 15rem;
}
.grid-item-img img {
  width: auto;
}

.grid-item-title {
  font-size: 1.9rem;
  font-family: "Roboto Slab Bold", serif;
  font-weight: 700;
  margin: 2rem 0;
}

.grid-item-description {
  font-family: "Source Sans Pro", sans-serif;
  font-size: 1.5rem;
  line-height: 19px;
  font-weight: 400;
}

/* End Questions */

/* Footer */
.footer {
  background-color: var(--black-800);
  color: var(--black-500);
  padding-top: 4rem;
  padding-bottom: 4rem;
  position: relative;
}

.footer-content {
  display: flex;
}

.footer-icon {
  flex: 0 0 64px;
}
.footer-icon i {
  font-size: 4rem;
  margin-top: -2rem;
  margin-bottom: 2rem;
}

.footer-nav {
  display: flex;
  flex: 2 1 auto;
  flex-wrap: wrap;
}

.footer-nav-col {
  flex: 1 0 auto;
  padding-right: 1rem;
  padding-bottom: 2.4rem;
}

.footer-another-links {
  flex: 1 1 150px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.footer-links-title {
  margin-bottom: 1rem;
}
.footer-links-title a {
  color: var(--black-200);
  font-size: 1.3rem;
  font-family: Arial, "Helvetica Neue", Helvetica, sans-serif;
  font-weight: 700;
  text-transform: uppercase;
}

.footer-link-item {
  padding: 0.4rem 0;
  display: flex;
  align-items: center;
}

.footer-arrow-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 1.2rem;
  height: 1.2rem;
  background-color: rgba(132, 141, 149, 0.35);
  opacity: 0.5;
  border-radius: 0.3rem;
  margin-left: 1rem;
}
.footer-arrow-icon i {
  font-size: 0.5rem;
  color: var(--black-200);
}

.footer-link {
  color: var(--black-400);
  font-size: 1.3rem;
  font-family: Arial, "Helvetica Neue", Helvetica, sans-serif;
  font-weight: 400;
}

.social-media ul {
  display: flex;
}
.social-media ul li {
  margin-right: 1rem;
}
.social-media ul li a {
  color: var(--black-400);
  font-size: 1.1rem;
}

.copyright {
  color: var(--black-500);
  font-size: 1.1rem;
  font-family: Arial, "Helvetica Neue", Helvetica, sans-serif;
  font-weight: 400;
}
.copyright a {
  color: var(--black-400);
}

.footer-robot-img {
  width: 5.1rem;
  height: 5.1rem;
  position: absolute;
  right: 6rem;
  top: -4.5rem;
}

/* End Footer */
/* Media Queries */
@media screen and (max-width: 1100px) {
  .for-businesses .option {
    flex-direction: column;
  }
  .for-businesses .option-icon {
    margin-bottom: 1.5rem;
  }
  .for-businesses .option-icon img {
    max-width: 7.6rem;
  }

  .jobs-title {
    text-align: center;
  }

  .jobs-body {
    flex-direction: column;
  }

  .jobs-items {
    flex-direction: column;
  }
  .jobs-items .column:nth-child(even) {
    margin-left: initial;
  }

  .jobs-item {
    margin-bottom: 3rem;
  }

  .hire-content {
    grid-template-columns: repeat(auto-fill, minmax(35rem, 1fr));
  }
}
@media screen and (max-width: 850px) {
  .hire-content {
    grid-template-columns: repeat(auto-fill, minmax(25rem, 1fr));
  }
}
@media screen and (max-width: 830px) {
  .footer-content {
    flex-wrap: wrap;
  }

  .social-media {
    margin-bottom: 1rem;
  }
}
@media screen and (max-width: 810px) {
  .nav-brand {
    flex: initial;
  }

  .nav-base-links ul li:not(:nth-child(2)) {
    display: none;
  }

  .nav-search {
    flex: initial;
    align-items: center;
    width: 100%;
    position: absolute;
    top: 4.7rem;
    padding: 0.8rem 1rem;
    background-color: var(--black-100);
    margin-right: initial;
    display: none;
  }
  .nav-search.open {
    display: flex;
  }

  .search-btn {
    display: flex;
  }

  .nav-right-buttons {
    flex: initial;
    margin-right: 1rem;
  }

  .search-hints {
    width: 94%;
    left: 3%;
    top: 5.2rem;
  }

  .for-enthusiast .options {
    justify-content: initial;
    flex-direction: column;
    max-width: initial;
    margin-top: 6rem;
  }
  .for-enthusiast .options > .option {
    margin-top: initial;
  }
  .for-enthusiast .option {
    max-width: 28rem;
    margin-bottom: 3rem;
    margin-top: initial;
  }

  .for-businesses .options {
    flex-direction: column;
  }
  .for-businesses .option {
    flex-direction: row;
    margin-bottom: 2.5rem;
    max-width: 35rem;
    margin-left: auto;
    margin-right: auto;
  }
  .for-businesses .option-icon {
    margin-bottom: 0;
  }
  .for-businesses .option-icon img {
    max-width: initial;
  }

  .teams {
    background-image: none;
  }

  .teams-plan {
    width: 90%;
  }
  .teams-plan .card {
    flex-basis: initial;
  }
  .teams-plan .card:nth-child(2) {
    order: -1;
  }

  .teams-footer {
    width: 90%;
  }

  .questions-content .question-title {
    font-size: 2.3rem;
  }

  .questions-body {
    flex-direction: column;
    justify-content: initial;
  }

  .questions-body-items {
    display: flex;
  }

  .questions-body-item {
    flex-basis: 33%;
    flex-direction: column;
    padding: 1rem;
    justify-content: center;
    text-align: center;
    margin: 0;
  }

  .question-item-text {
    margin-left: initial;
    margin-top: 1rem;
  }

  .question-arrow-right, .question-arrow-left {
    display: none;
  }

  .questions-body-item-content {
    margin: 2rem 0 0;
    order: 3;
  }

  .question-item-content-img {
    padding: 0 2rem;
  }

  .question-item-content-text {
    font-size: 1.8rem;
    padding-left: 1rem;
    padding-right: 1rem;
  }

  .questions-grid-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-bottom: 3rem;
    text-align: center;
  }
}
@media screen and (max-width: 640px) {
  .nav-icon {
    padding: 0 1rem;
  }

  .nav-icon-text {
    display: none;
  }

  .nav-base-links {
    font-size: 1.1rem;
  }

  .search-hint-body {
    flex-direction: column;
  }

  .hero {
    background-image: url("https://cdn.sstatic.net/Img/home/illo-hero-small.svg?v=884735d21ea5");
  }

  .hero-title {
    font-size: 3rem;
  }

  .hero-options {
    flex-direction: column;
  }

  .btn-developers {
    margin-bottom: 1rem;
  }

  .btn-businesses {
    margin-left: initial;
  }

  .section-title {
    font-size: 2.3rem;
  }

  .section-description {
    font-size: 1.4rem;
    line-height: 2rem;
  }

  .for-businesses .option-description {
    font-size: 1.4rem;
    line-height: 2rem;
  }

  .teams-head {
    padding: 0 6rem;
  }

  .teams-title {
    font-size: 2.3rem;
  }

  .teams-description {
    font-size: 1.4rem;
    line-height: 2rem;
  }

  .questions-grid {
    grid-template-columns: repeat(auto-fit, minmax(25rem, 1fr));
    padding: 0 9rem;
  }

  .jobs-title {
    font-size: 2.3rem;
  }

  .jobs-items .column {
    flex-direction: column;
  }
  .jobs-items .jobs-item {
    margin-left: initial;
    margin-bottom: 2rem;
  }

  .footer-icon {
    display: none;
  }

  .footer-links-title a {
    font-size: 1.1rem;
  }

  .footer-link {
    font-size: 1.1rem;
  }

  .hire .container {
    padding: 0 3rem;
  }
}
@media screen and (max-width: 500px) {
  .questions-grid {
    padding: 0;
  }
}
/* End Media Queries */

/*# sourceMappingURL=main.css.map */
</style>