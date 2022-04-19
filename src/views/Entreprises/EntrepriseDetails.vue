<template>
  <div class="layout-px-spacing">
    <portal to="breadcrumb">
      <ul class="navbar-nav flex-row">
        <li>
          <div class="page-header">
            <nav class="breadcrumb-one" aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item active" aria-current="page"><span>Entreprise Portfolio</span></li>
              </ol>
            </nav>
          </div>
        </li>
      </ul>
    </portal>
    <div class="fq-header-wrapper">
      <div class="container">
        <div class="row">
          <div class="col-md-6 align-self-center order-md-0 order-1">
            <h1 class="">{{ userentreprise.nameE }}</h1>
            <h6 class="">{{ userentreprise.bio }}</h6>
          </div>
          <div class="col-md-6 order-md-0 mt-4 order-0">
            <div class="banner-img">
              <b-avatar :src=" userentreprise.imageE" size="25rem" class="mb-5 bg-transparent img-fluid" style="width: 100%" rounded="lg" alt="header-image" />
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="faq container mt-5">
      <div class="faq-layouting layout-spacing">
        <div class="fq-comman-question-wrapper">
          <div class="row">
            <div class="col-md-12">
              <h3>You can Reach Us via the following contact details</h3>
              <div class="row">
                <div class="col-md-7 ml-2">
                  <ul class="">
                    <li class="list-unstyled">
                      <div class="icon-svg">
                        <a :href="'mailto:' + user.email" target="_blank"
                          ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="2em" height="2em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16">
                            <path
                              fill="currentColor"
                              d="M4 3a2 2 0 0 0-2 2v.201l6 3.231l6-3.23V5a2 2 0 0 0-2-2H4Zm10 3.337L8.237 9.44a.5.5 0 0 1-.474 0L2 6.337V11a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V6.337Z"
                            />
                          </svg>
                          {{ user.email }}
                        </a>
                      </div>
                    </li>
                    <li class="list-unstyled">
                      <div class="icon-svg">
                        <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 20 20">
                          <path
                            fill="currentColor"
                            d="m19.799 5.165l-2.375-1.83a1.997 1.997 0 0 0-.521-.237A2.035 2.035 0 0 0 16.336 3H9.5l.801 5h6.035c.164 0 .369-.037.566-.098s.387-.145.521-.236l2.375-1.832c.135-.091.202-.212.202-.334s-.067-.243-.201-.335zM8.5 1h-1a.5.5 0 0 0-.5.5V5H3.664c-.166 0-.37.037-.567.099c-.198.06-.387.143-.521.236L.201 7.165C.066 7.256 0 7.378 0 7.5c0 .121.066.242.201.335l2.375 1.832c.134.091.323.175.521.235c.197.061.401.098.567.098H7v8.5a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-17a.5.5 0 0 0-.5-.5z"
                          />
                        </svg>
                      </div>
                      {{ userentreprise.addressE }}
                    </li>
                  </ul>
                </div>
                <div class="col-md-4">
                  <ul class="">
                    <li class="list-unstyled">
                      <div class="icon-svg">
                        <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32">
                          <path fill="currentColor" d="M24 13h-2a3.003 3.003 0 0 0-3-3V8a5.006 5.006 0 0 1 5 5Z" />
                          <path
                            fill="currentColor"
                            d="M28 13h-2a7.008 7.008 0 0 0-7-7V4a9.01 9.01 0 0 1 9 9zm-7.667 8.482l2.24-2.24a2.167 2.167 0 0 1 2.337-.48l2.728 1.092A2.167 2.167 0 0 1 29 21.866v4.961a2.167 2.167 0 0 1-2.284 2.169C7.594 27.806 3.732 11.61 3.015 5.408A2.162 2.162 0 0 1 5.169 3h4.873a2.167 2.167 0 0 1 2.012 1.362l1.091 2.728a2.167 2.167 0 0 1-.48 2.337l-2.24 2.24s1.242 8.732 9.908 9.815z"
                          />
                        </svg>
                      </div>
                      {{ userentreprise.contactE }}
                    </li>
                    <li class="list-unstyled">
                      <div class="icon-svg">
                        <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32">
                          <path
                            fill="currentColor"
                            d="M16 2A11.013 11.013 0 0 0 5 13a10.889 10.889 0 0 0 2.216 6.6s.3.395.349.452L16 30l8.439-9.953c.044-.053.345-.447.345-.447l.001-.003A10.885 10.885 0 0 0 27 13A11.013 11.013 0 0 0 16 2Zm0 15a4 4 0 1 1 4-4a4.005 4.005 0 0 1-4 4Z"
                          />
                          <circle cx="16" cy="13" r="4" fill="none" />
                        </svg>
                      </div>
                      {{ userentreprise.country }}
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="faq container mt-5">
      <div class="faq-layouting layout-spacing">
        <div class="fq-comman-question-wrapper">
          <div class="row">
            <div class="col-md-12">
              <h3>Our Statistics</h3>
              <div class="row">
                <div class="col-md-6">
                  <ul class="">
                    <li class="list-unstyled">
                      <div id="countericon" class="col-lg-12 col-12 layout-spacing">
                        <div class="panel-body text-center">
                          <div class="icon--counter-container">
                            <div class="counter-container">
                              <div class="counter-content">
                                <h1 class="ico-counter1 ico-counter">
                                  <number ref="counter4" :from="0" :to="average" :duration="0.5" :delay="1" />
                                </h1>
                              </div>

                              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24">
                                <path
                                  fill="none"
                                  stroke="currentColor"
                                  stroke-linecap="round"
                                  stroke-linejoin="round"
                                  stroke-width="1.5"
                                  d="m4.635 14.415l1.039-2.203a.357.357 0 0 1 .652 0l1.04 2.203l2.323.356c.298.045.416.429.2.649l-1.68 1.713l.396 2.421c.051.311-.26.548-.527.401L6 18.812l-2.078 1.143c-.267.147-.578-.09-.527-.4l.396-2.422l-1.68-1.713c-.217-.22-.098-.604.2-.65l2.324-.355Zm12 0l1.039-2.203a.357.357 0 0 1 .652 0l1.04 2.203l2.323.356c.298.045.416.429.2.649l-1.68 1.713l.396 2.421c.051.311-.26.548-.527.401L18 18.812l-2.078 1.143c-.267.147-.578-.09-.527-.4l.396-2.422l-1.68-1.713c-.216-.22-.098-.604.2-.65l2.324-.355Zm-6-9l1.039-2.203a.357.357 0 0 1 .652 0l1.04 2.203l2.323.356c.298.045.416.429.2.649l-1.68 1.713l.396 2.421c.051.311-.26.548-.527.401L12 9.812l-2.078 1.143c-.267.147-.578-.09-.527-.4l.396-2.422l-1.68-1.713c-.217-.22-.098-.604.2-.65l2.324-.355Z"
                                />
                              </svg>
                              <p class="ico-counter-text">Rating</p>
                            </div>
                          </div>
                        </div>
                      </div>
                    </li>
                  </ul>
                </div>
                <div class="col-md-6">
                  <ul class="">
                    <li class="list-unstyled">
                      <div id="countericon" class="col-lg-12 col-12 layout-spacing">
                        <div class="panel-body text-center">
                          <div class="icon--counter-container">
                            <div class="counter-container">
                              <div class="counter-content">
                                <h1 class="ico-counter1 ico-counter">
                                  <number ref="counter4" :from="0" :to="nbStat" :duration="0.5" :delay="1" />
                                </h1>
                              </div>

                              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1.25em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 640 512">
                                <path
                                  fill="currentColor"
                                  d="M96 224c35.3 0 64-28.7 64-64s-28.7-64-64-64s-64 28.7-64 64s28.7 64 64 64zm448 0c35.3 0 64-28.7 64-64s-28.7-64-64-64s-64 28.7-64 64s28.7 64 64 64zm32 32h-64c-17.6 0-33.5 7.1-45.1 18.6c40.3 22.1 68.9 62 75.1 109.4h66c17.7 0 32-14.3 32-32v-32c0-35.3-28.7-64-64-64zm-256 0c61.9 0 112-50.1 112-112S381.9 32 320 32S208 82.1 208 144s50.1 112 112 112zm76.8 32h-8.3c-20.8 10-43.9 16-68.5 16s-47.6-6-68.5-16h-8.3C179.6 288 128 339.6 128 403.2V432c0 26.5 21.5 48 48 48h288c26.5 0 48-21.5 48-48v-28.8c0-63.6-51.6-115.2-115.2-115.2zm-223.7-13.4C161.5 263.1 145.6 256 128 256H64c-35.3 0-64 28.7-64 64v32c0 17.7 14.3 32 32 32h65.9c6.3-47.4 34.9-87.3 75.2-109.4z"
                                />
                              </svg>
                              <p class="ico-counter-text">Users</p>
                            </div>
                          </div>
                        </div>
                      </div>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="faq container mt-5">
      <div class="faq-layouting layout-spacing">
        <div class="fq-comman-question-wrapper">
          <div class="row">
            <div class="col-md-12">
              <h3>Actions</h3>
              <div class="row">
                <div class="col-md-6">
                  <ul class="">
                    <li class="list-unstyled">
                      <h4 class="text-center mt-2">Rate Us !</h4>
                      <span v-if="userentreprise.userE != CurrentUser.id">
                        <span v-if="isLoggedIn && existe==false">
                          <span v-b-modal.Rating>
<div class="d-flex col-xl-12 col-lg-12 col-md-12 mt-4 mb-4">
                  <div class="text-center mt-3">
                    <span class="h1 font-weight-bolder mr-1">{{ average }}</span
                    ><br />
                    <span class="p">out of 5</span>
                  </div>
                  <div class="flex-grow-1">
                    <div class="row">
                      <div class="col-lg-6 text-right">
                        <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          />
                        </svg>
                      </div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb5" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-lg-6 text-right">
                        <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          />
                        </svg>
                      </div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb4" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-lg-6 text-right">
                        <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        >
                      </div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb3" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-lg-6 text-right"><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg></div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb2" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-lg-6 text-right"><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg></div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb1" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                  </div>
                </div>                          </span>
                        </span>
                        <span v-else-if="isLoggedIn && existe==true">
                          <span @click="rating()">
<div class="d-flex col-xl-12 col-lg-12 col-md-12 mt-4 mb-4">
                  <div class="text-center mt-3">
                    <span class="h1 font-weight-bolder mr-1">{{ average }}</span
                    ><br />
                    <span class="p">out of 5</span>
                  </div>
                  <div class="flex-grow-1">
                    <div class="row">
                      <div class="col-lg-6 text-right">
                        <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          />
                        </svg>
                      </div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb5" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-lg-6 text-right">
                        <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          />
                        </svg>
                      </div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb4" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-lg-6 text-right">
                        <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        >
                      </div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb3" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-lg-6 text-right"><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg></div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb2" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-lg-6 text-right"><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg></div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb1" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                  </div>
                </div>                           </span>
                        </span>
                        <span v-else>
                          <a href="/auth/login">
<div class="d-flex col-xl-12 col-lg-12 col-md-12 mt-4 mb-4">
                  <div class="text-center mt-3">
                    <span class="h1 font-weight-bolder mr-1">{{ average }}</span
                    ><br />
                    <span class="p">out of 5</span>
                  </div>
                  <div class="flex-grow-1">
                    <div class="row">
                      <div class="col-lg-6 text-right">
                        <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          />
                        </svg>
                      </div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb5" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-lg-6 text-right">
                        <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          />
                        </svg>
                      </div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb4" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-lg-6 text-right">
                        <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        >
                      </div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb3" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-lg-6 text-right"><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg></div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb2" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-lg-6 text-right"><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg></div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb1" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                  </div>
                </div>                           </a>
                        </span>
                      </span>
                      <span v-else>
                        <span @click="showAlert()">
<div class="d-flex col-xl-12 col-lg-12 col-md-12 mt-4 mb-4">
                  <div class="text-center mt-3">
                    <span class="h1 font-weight-bolder mr-1">{{ average }}</span
                    ><br />
                    <span class="p">out of 5</span>
                  </div>
                  <div class="flex-grow-1">
                    <div class="row">
                      <div class="col-lg-6 text-right">
                        <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          />
                        </svg>
                      </div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb5" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-lg-6 text-right">
                        <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          />
                        </svg>
                      </div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb4" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-lg-6 text-right">
                        <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        >
                      </div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb3" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-lg-6 text-right"><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg></div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb2" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-lg-6 text-right"><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg></div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb1" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                  </div>
                </div>                         </span>
                      </span>
                      <b-modal id="Rating" :title="'Rate ' + userentreprise.nameE" centered>
                        <b-form-rating id="rating" v-model="nbEval" precision="2" show-value-max show-value variant="warning" size="lg" class="mb-2 bg-transparent border-0"> </b-form-rating>
                         <label >Your feedback </label>
                    <b-form-group class="mb-3">
                      <b-input type="text" placeholder="Feedback " v-model="commentEval" ></b-input>
                    </b-form-group>
                        <template #modal-footer>
                          <b-button variant="primary" @click="Rating()">Submit your rating</b-button>
                        </template>
                      </b-modal>
                    </li>
                  </ul>
                </div>
                <div class="col-md-6">
                  <ul class="">
                    <li class="list-unstyled">
                      <div class="row">
                        <div class="col-md-12 mt-5">
                          <h4>Your feedback help us to improve our services quality</h4>
                        </div>
                      </div>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="faq container mt-5"  v-if="CurrentUserEntreprise.id == userentreprise.id">
      <div class="faq-layouting layout-spacing">
        <div class="fq-comman-question-wrapper">
          <div class="row">
            <div class="col-md-12">
              <h3>For this company</h3>
              <div class="row">
                <div class="col-md-7">
                  <ul class="">
                    <li class="list-unstyled ml-5">
                      <h1><b-button variant="info" v-if="CurrentUserEntreprise.id == userentreprise.id && promoted == true" :href="'/promoinfoentreprise/'+userentreprise.id">Promotion details <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><g fill="none" stroke="white" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"><path stroke-miterlimit="5.759" d="M3 3v16a2 2 0 0 0 2 2h16"/><path stroke-miterlimit="5.759" d="m7 14l4-4l4 4l6-6"/><path d="M18 8h3v3"/></g></svg></b-button></h1>
                      <h1><b-button v-if="CurrentUserEntreprise.id == userentreprise.id && promoted == false" variant="info" class="" v-b-modal.promotion><p>Reach more people by boosting your company </p><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><g fill="none" stroke="white" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"><path stroke-miterlimit="5.759" d="M3 3v16a2 2 0 0 0 2 2h16"/><path stroke-miterlimit="5.759" d="m7 14l4-4l4 4l6-6"/><path d="M18 8h3v3"/></g></svg></b-button></h1>
                      <b-modal id="promotion" title="Promote your company !" centered>
                        <label>Number of days</label>
                        <b-input placeholder="1,3,7..etc" type="number" v-model="nbDays" min="1" value="7"></b-input>
                        <template #modal-footer>
                          <b-button variant="primary" @click="promote()">Submit your promotion request</b-button>
                        </template>
                      </b-modal>
                    </li>
                  </ul>
                </div>
                <div class="col-md-5">
                  <ul class="">
                    <li class="list-unstyled" v-if="CurrentUser.id == userentreprise.userE">
                      <div class="row">
                        <div class="col-md-12 mt-2">
                          <router-link :to="'/updateentreprise/' + userentreprise.id"><b-button variant="info">Update your company information</b-button></router-link>
                        </div>
                      </div>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="widget widget-recent-orders mb-4">
      <div class="widget-heading">
        <h5>Other Entreprises</h5>
        <div class="row mr-1 float-right">
          <div class="col-lg-12 col-md-12 col-sm-12 filtered-list-search-live mx-auto">
            <b-form class="form-inline my-2 my-lg-0 justify-content-center" @submit.prevent="search">
              <div class="w-100">
                <b-input v-model="search" class="w-100 product-search br-25" placeholder="Search Entreprises" @keyup="search"></b-input>
              </div>
            </b-form>
          </div>
        </div>
      </div>
      <div class="widget-content">
        <b-table-simple responsive>
          <b-thead>
            <b-tr>
              <b-th><div class="th-content">Entreprise</div></b-th>
              <b-th><div class="th-content">Business type</div></b-th>
              <b-th><div class="th-content">Email</div></b-th>
              <b-th><div class="th-content">Phone</div></b-th>
              <b-th><div class="th-content th-heading">Country</div></b-th>
              <b-th><div class="th-content">Address</div></b-th>
            </b-tr>
          </b-thead>

          <b-tbody>
            <b-tr v-for="e in filteredList" :key="e.id">
              <b-td v-if="e.id != userentreprise.id"
                ><a :href="'/entreprisedetails/' + e.id"
                  ><div class="td-content">
                    <img :src=" e.imageE" alt="avatar" /><span>{{ e.nameE }} </span>
                  </div></a
                ></b-td
              >
              <b-td v-if="e.id != userentreprise.id"
                ><div class="td-content">
                  <span>{{ e.typeE }}</span>
                </div></b-td
              >
              <b-td v-if="e.id != userentreprise.id">
                <div v-for="user in Users" :key="user.id">
                  <div v-if="user.id == e.userE" class="td-content text-primary">{{ user.email }}</div>
                </div>
              </b-td>
              <b-td v-if="e.id != userentreprise.id"
                ><div class="td-content">{{ e.contactE }}</div></b-td
              >
              <b-td v-if="e.id != userentreprise.id"
                ><div class="td-content">
                  <span>{{ e.country }}</span>
                </div></b-td
              >
              <b-td v-if="e.id != userentreprise.id"
                ><div class="td-content">{{ e.addressE }}</div></b-td
              >
            </b-tr>
          </b-tbody>
        </b-table-simple>
      </div>
    </div>
  </div>
</template>
<style scoped>
.layout-px-spacing {
  min-height: calc(100vh - 170px) !important;
}
</style>
<script>
import '@/assets/sass/components/custom-counter.scss';
import Vue from 'vue';
import VueNumber from 'vue-number-animation';
Vue.use(VueNumber);
import '@/assets/sass/pages/faq/faq.scss';
import '@/assets/sass/scrollspyNav.scss';
import '@/assets/sass/widgets/widgets.scss';
import '@/assets/sass/users/user-profile.scss';
import { mapGetters, mapActions } from 'vuex';
import axios from 'axios';
export default {
  metaInfo: { title: 'Portfolio' },
  data() {
    return {
      CurrentUser: [],
      userentreprise: [],
      CurrentUserProfile:[],
      CurrentUserEntreprise: [],
      user: [],
      nbEval: 0,
      search: '',
      UserEval: '',
      commentEval:'',
      nbDays: 7,
      average: 0,
      nbStat: 0,
      promoted: false,
      existe: false,
      nb1: 0,
      nb2: 0,
      nb3: 0,
      nb4: 0,
      nb5: 0,
      nbTotal: 0,
    };
  },
  mounted() {},
  computed: {
    ...mapGetters({
      Entreprises: 'StateUserentreprises',
      Entreprisepromotions: 'StateEntreprisepromotions',
      Evaluationentreprises: 'StateEvaluationentreprises',
      Userentreprises: 'StateUserentreprises',
      User: 'StateUser',
      Users: 'StateUsers',
      Userprofiles: 'StateUserprofiles',
    }),
    filterByAccepted() {
      return this.Userentreprises.filter((entreprise) => {
        return entreprise.published == true;
      });
    },
    filteredList() {
      return this.filterByAccepted.filter((entreprise) => {
        return entreprise.nameE.toLowerCase().includes(this.search.toLowerCase());
      });
    },

    isLoggedIn: function () {
      return this.$store.getters.isAuthenticated;
    },
  },
  methods: {
    ...mapActions(['GetUsers','GetUserprofiles','CreateNotification', 'GetEntreprisepromotions', 'CreateEntreprisepromotion', 'GetCars', 'GetUserentreprises', 'GetEvaluations', 'GetEvaluationentreprises']),

    promote() {
      this.CreateEntreprisepromotion({ entreprisePE: this.userentreprise.id, nbDays: this.nbDays });
      this.promoted = true;
      this.$swal('Good Job!', 'Your Entreprise promotion has been sent, Please wait for the administrator to launch your promotion !', 'success');
    },
    async Rating() {
      let done = false;
      if (this.Evaluationentreprises.length == 0) {
        axios.post('/evaluationentreprise/evaluationentreprise-create/', {
          userentrepriseEval: this.$route.params.id,
          userEval: this.CurrentUser.id,
          nbEval: this.nbEval,
          commentEval:this.commentEval
        });
        this.GetEvaluationentreprises();
      } else {
        for (let e in this.Evaluationentreprises) {
          if (this.Evaluationentreprises[e].userentrepriseEval == this.$route.params.id && this.Evaluationentreprises[e].userEval == this.CurrentUser.id) {
            axios.post('/evaluationentreprise/evaluationentreprise-update/' + this.Evaluationentreprises[e].id + '/', {
              nbEval: this.nbEval,
            });
            done = true;
          }
        }
        if (done == false) {
          axios.post('/evaluationentreprise/evaluationentreprise-create/', {
            userentrepriseEval: this.$route.params.id,
            userEval: this.CurrentUser.id,
            nbEval: this.nbEval,
            commentEval:this.commentEval
          });
        }
        this.GetEvaluationentreprises();
      }
      this.CreateNotification({message:' Rated your Entreprise '+this.nbEval+' Stars !',byuserprofileNo:this.CurrentUserProfile.id,byuserentrepriseNo:this.CurrentUserEntreprise.id,entrepriseNo:this.$route.params.id})

      this.$router.go();
    },
    async showAlert() {
      this.$swal({
        title: 'You cannot rate your entreprise',
        padding: '2em',
      });
    },
  },
  created: function () {
    this.GetUsers();
    this.GetUserentreprises();
    this.GetEvaluationentreprises();
    this.GetEntreprisepromotions();
    this.GetUserprofiles();
    for (let u in this.Users) {
      if (this.Users[u].username == this.User) {
        this.CurrentUser = this.Users[u];
        for(let up in this.Userprofiles){
          if(this.Userprofiles[up].userU==this.CurrentUser.id){
            this.CurrentUserProfile=this.Userprofiles[up]
          }
        }
      }
    }
    for (let p in this.Userentreprises) {
      if (this.Userentreprises[p].userE == this.CurrentUser.id) {
        this.CurrentUserEntreprise = this.Userentreprises[p];
        this.existe = true;
      }
    }
    axios.get('/userentreprise/userentreprise-detail/' + this.$route.params.id + '/').then((response) => {
      this.userentreprise = response.data;
      if (this.userentreprise.published == false) {
        this.$router.push('/entreprises');
         this.$swal({
              title: 'Please Wait for the administrator to verify your informations',
              padding: '2em'
          });
      }
      this.nbEval = this.userentreprise.nbEval;
      for (let s in this.Entreprisepromotions) {
        if (this.Entreprisepromotions[s].entreprisePE == this.userentreprise.id) {
          this.promoted = true;
          const d = new Date(this.Entreprisepromotions[s].datePE);
          d.setDate(d.getDate() + parseInt(this.Entreprisepromotions[s].nbDays));
          if (new Date() > new Date(this.Entreprisepromotions[s].datePE) && this.Entreprisepromotions[s].dateP != null) {
            axios.delete(`http://127.0.0.1:8000/entreprisepromotion/entreprisepromotion-delete/${this.Entreprisepromotions[s].id}/`);
            axios.post('/userentreprise/userentreprise-update/' + this.userentreprise.id + '/', { promoted: false, published: this.userentreprise.published });
            this.promoted = false;
            this.$router.go();
          }
        }
      }
      for (let ev in this.Evaluationentreprises) {
        if (this.Evaluationentreprises[ev].userentrepriseEval == this.$route.params.id && this.Evaluationentreprises[ev].nbEval == 5) {
          this.nb5++;
        } else if (this.Evaluationentreprises[ev].userentrepriseEval == this.$route.params.id && this.Evaluationentreprises[ev].nbEval == 4) {
          this.nb4++;
        } else if (this.Evaluationentreprises[ev].userentrepriseEval == this.$route.params.id && this.Evaluationentreprises[ev].nbEval == 3) {
          this.nb3++;
        } else if (this.Evaluationentreprises[ev].userentrepriseEval == this.$route.params.id && this.Evaluationentreprises[ev].nbEval == 2) {
          this.nb2++;
        } else if (this.Evaluationentreprises[ev].userentrepriseEval == this.$route.params.id && this.Evaluationentreprises[ev].nbEval == 1) {
          this.nb1++;
        }
      }
      this.nbTotal = this.nb1 + this.nb2 + this.nb3 + this.nb4 + this.nb5;
      var sum = 0;
      var nb = 0;
      for (let e in this.Evaluationentreprises) {
        if (this.Evaluationentreprises[e].userentrepriseEval == this.userentreprise.id) {
          sum += this.Evaluationentreprises[e].nbEval;
          nb++;
        }
      }
      this.average = sum / nb;
      axios.put('/userentreprise/userentreprise-update/' + this.userentreprise.id + '/', {
        nbEval: this.average,
        nbvisits:this.entreprise.nbvisits+1
      });
      this.userentreprise.nbEval = this.average;
      axios.get('/user/users/' + this.userentreprise.userE + '/').then((response) => {
        this.user = response.data;
      });
    });
    for (let ep in this.Evaluationentreprises) {
      if (this.Evaluationentreprises[ep].userentrepriseEval == this.userentreprise.id) {
        this.nbStat = this.nbStat + 1;
      }
    }
  },
};
</script>
