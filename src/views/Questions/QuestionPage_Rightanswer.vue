<template>
  <div class="layout-px-spacing">
    <portal to="breadcrumb">
      <ul class="navbar-nav flex-row">
        <li>
          <div class="page-header">
            <nav class="breadcrumb-one" aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item active" aria-current="page"><span>Question Page</span></li>
              </ol>
            </nav>
          </div>
        </li>
      </ul>
    </portal>
    <div class="col-xl-12 mt-3 col-lg-6 col-md-12 col-sm-12 col-12 layout-spacing">
      
      <div class="widget widget-card-one">
        <div v-if="CurrentUserProfile.id == question.userprofileQ">
              <b-dropdown variant="icon-only"  toggle-tag="a" size="1em" class="mb-4 mr-2 custom-dropdown mt-3 float-right">
                <template #button-content>
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    style="width: 18px; height: 18px"
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    class="feather feather-more-vertical"
                  >
                    <circle cx="12" cy="12" r="1"></circle>
                    <circle cx="12" cy="5" r="1"></circle>
                    <circle cx="12" cy="19" r="1"></circle>
                  </svg>
                </template>
                <b-dropdown-item :href="'/updatequestion/'+question.id">Modify</b-dropdown-item>
                <b-dropdown-item @click="deleteQuestion(question.id)">Delete</b-dropdown-item>
              </b-dropdown>
              </div>
        <div class="widget-heading">
          
          <b-media>
            
            <template #aside>
              <div class="w-img">
                <img :src="'http://127.0.0.1:8000' + userprofile.imageU" alt="avatar" />
              </div>
              
            </template>
            
            <router-link :to="'/profile/'+userprofile.id">
            <h6>{{ userprofile.firstname }} {{ userprofile.lastname }}</h6>
            </router-link>
            
            <p class="meta-date-time">{{ question.dateQ | formatDate }}</p>
            
            <b-card class="bg-transparent border-0 col-12">
          <b-card-text>  <h4 class="font-weight-bold">{{ question.titleQ }}</h4></b-card-text></b-card>
            
          </b-media>
        </div>
        
        <div class="widget-content">
          <b-card class="bg-transparent border-0 col-12">
            <b-card-text>
          <h6 class="ml-5 mb-5">{{ question.contentQ }}</h6></b-card-text></b-card>
          <div class="widget-content mb-5" v-if="question.imageQ != null">
            <img :src="'http://127.0.0.1:8000' + question.imageQ" class="rounded mx-auto d-block" style="max-width: 100%; height: auto" />
          </div>
          <div class="w-action">
            <div class="card-like ml-4">
              <span v-if="isLoggedIn && CurrentUserProfile.id!=null">
                <svg
                  v-show="likedQuestion == false"
                  @click="liked()"
                  xmlns="http://www.w3.org/2000/svg"
                  aria-hidden="true"
                  role="img"
                  width="24"
                  height="24"
                  preserveAspectRatio="xMidYMid meet"
                  viewBox="0 0 512 512"
                >
                  <path
                    fill="currentColor"
                    d="M96 191.1H32c-17.67 0-32 14.33-32 31.1v223.1c0 17.67 14.33 31.1 32 31.1h64c17.67 0 32-14.33 32-31.1V223.1c0-16.8-14.3-32-32-32zM512 227c0-36.89-30.05-66.92-66.97-66.92h-99.86C354.7 135.1 360 113.5 360 100.8c0-33.8-26.2-68.78-70.06-68.78c-46.61 0-59.36 32.44-69.61 58.5c-31.66 80.5-60.33 66.39-60.33 93.47c0 12.84 10.36 23.99 24.02 23.99a23.88 23.88 0 0 0 14.97-5.26c76.76-61.37 57.97-122.7 90.95-122.7c16.08 0 22.06 12.75 22.06 20.79c0 7.404-7.594 39.55-25.55 71.59a23.934 23.934 0 0 0-3.066 11.72c0 13.92 11.43 23.1 24 23.1h137.6C455.5 208.1 464 216.6 464 227c0 9.809-7.766 18.03-17.67 18.71c-12.66.86-22.36 11.4-22.36 23.94c0 15.47 11.39 15.95 11.39 28.91c0 25.37-35.03 12.34-35.03 42.15c0 11.22 6.392 13.03 6.392 22.25c0 22.66-29.77 13.76-29.77 40.64c0 4.515 1.11 5.961 1.11 9.456c0 10.45-8.516 18.95-18.97 18.95h-52.53c-25.62 0-51.02-8.466-71.5-23.81l-36.66-27.51a23.851 23.851 0 0 0-14.38-4.811c-13.85 0-24.03 11.38-24.03 24.04c0 7.287 3.312 14.42 9.596 19.13l36.67 27.52C235 468.1 270.6 480 306.6 480h52.53c35.33 0 64.36-27.49 66.8-62.2c17.77-12.23 28.83-32.51 28.83-54.83a65.97 65.97 0 0 0-.64-9.122c17.84-12.15 29.28-32.58 29.28-55.28a66.33 66.33 0 0 0-1.876-15.64C499.9 270.1 512 250.2 512 227z"
                  />
                </svg>
              </span>
              <span v-else>
                <a href="/auth/userinfo">
                  <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 512 512">
                    <path
                      fill="currentColor"
                      d="M96 191.1H32c-17.67 0-32 14.33-32 31.1v223.1c0 17.67 14.33 31.1 32 31.1h64c17.67 0 32-14.33 32-31.1V223.1c0-16.8-14.3-32-32-32zM512 227c0-36.89-30.05-66.92-66.97-66.92h-99.86C354.7 135.1 360 113.5 360 100.8c0-33.8-26.2-68.78-70.06-68.78c-46.61 0-59.36 32.44-69.61 58.5c-31.66 80.5-60.33 66.39-60.33 93.47c0 12.84 10.36 23.99 24.02 23.99a23.88 23.88 0 0 0 14.97-5.26c76.76-61.37 57.97-122.7 90.95-122.7c16.08 0 22.06 12.75 22.06 20.79c0 7.404-7.594 39.55-25.55 71.59a23.934 23.934 0 0 0-3.066 11.72c0 13.92 11.43 23.1 24 23.1h137.6C455.5 208.1 464 216.6 464 227c0 9.809-7.766 18.03-17.67 18.71c-12.66.86-22.36 11.4-22.36 23.94c0 15.47 11.39 15.95 11.39 28.91c0 25.37-35.03 12.34-35.03 42.15c0 11.22 6.392 13.03 6.392 22.25c0 22.66-29.77 13.76-29.77 40.64c0 4.515 1.11 5.961 1.11 9.456c0 10.45-8.516 18.95-18.97 18.95h-52.53c-25.62 0-51.02-8.466-71.5-23.81l-36.66-27.51a23.851 23.851 0 0 0-14.38-4.811c-13.85 0-24.03 11.38-24.03 24.04c0 7.287 3.312 14.42 9.596 19.13l36.67 27.52C235 468.1 270.6 480 306.6 480h52.53c35.33 0 64.36-27.49 66.8-62.2c17.77-12.23 28.83-32.51 28.83-54.83a65.97 65.97 0 0 0-.64-9.122c17.84-12.15 29.28-32.58 29.28-55.28a66.33 66.33 0 0 0-1.876-15.64C499.9 270.1 512 250.2 512 227z"
                    />
                  </svg>
                </a>
              </span>
              <span v-if="isLoggedIn">
                <svg
                  v-show="likedQuestion == true"
                  @click="deleteliked()"
                  xmlns="http://www.w3.org/2000/svg"
                  aria-hidden="true"
                  role="img"
                  width="24"
                  height="24"
                  preserveAspectRatio="xMidYMid meet"
                  viewBox="0 0 512 512"
                >
                  <path
                    fill="currentColor"
                    d="M128 447.1v-224c0-17.67-14.33-31.1-32-31.1H32c-17.67 0-32 14.33-32 31.1v223.1c0 17.67 14.33 31.1 32 31.1h64c17.7 1.8 32-11.7 32-30.2zm384-223c0-26.5-21.48-47.98-48-47.98H317.5c22.77-37.91 34.52-80.88 34.52-96.02C352 56.52 333.5 32 302.5 32c-63.13 0-26.36 76.15-108.2 141.6l-16.3 13c-11.8 9.5-17.8 23.4-17.9 37.4c-.023.023 0 0 0 0l-.1 160c0 15.1 7.113 29.33 19.2 38.39l34.14 25.59C241 468.8 274.7 480 309.3 480H368c26.52 0 48-21.47 48-47.98c0-3.635-.48-7.143-1.246-10.55C434 415.2 448 397.4 448 376c0-9.148-2.697-17.61-7.139-24.88C463.1 347 480 327.5 480 304.1c0-12.5-4.893-23.78-12.72-32.32C492.2 270.1 512 249.5 512 224.1z"
                  />
                </svg>
              </span>
              <span>{{ likes }} Likes</span>
            </div>
            <div class="card-like mr-4">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16">
                <g fill="currentColor">
                  <path
                    d="M8.098 5.013a.144.144 0 0 1 .202.134V6.3a.5.5 0 0 0 .5.5c.667 0 2.013.005 3.3.822c.984.624 1.99 1.76 2.595 3.876c-1.02-.983-2.185-1.516-3.205-1.799a8.74 8.74 0 0 0-1.921-.306a7.404 7.404 0 0 0-.798.008h-.013l-.005.001h-.001L8.8 9.9l-.05-.498a.5.5 0 0 0-.45.498v1.153c0 .108-.11.176-.202.134L4.114 8.254a.502.502 0 0 0-.042-.028a.147.147 0 0 1 0-.252a.497.497 0 0 0 .042-.028l3.984-2.933zM9.3 10.386c.068 0 .143.003.223.006c.434.02 1.034.086 1.7.271c1.326.368 2.896 1.202 3.94 3.08a.5.5 0 0 0 .933-.305c-.464-3.71-1.886-5.662-3.46-6.66c-1.245-.79-2.527-.942-3.336-.971v-.66a1.144 1.144 0 0 0-1.767-.96l-3.994 2.94a1.147 1.147 0 0 0 0 1.946l3.994 2.94a1.144 1.144 0 0 0 1.767-.96v-.667z"
                  />
                  <path
                    d="M5.232 4.293a.5.5 0 0 0-.7-.106L.54 7.127a1.147 1.147 0 0 0 0 1.946l3.994 2.94a.5.5 0 1 0 .593-.805L1.114 8.254a.503.503 0 0 0-.042-.028a.147.147 0 0 1 0-.252a.5.5 0 0 0 .042-.028l4.012-2.954a.5.5 0 0 0 .106-.699z"
                  />
                </g>
              </svg>
              <span v-if="isLoggedIn && CurrentUserProfile.id!=null">
                <span v-b-modal.exampleModalCenter>Reply</span>
              </span>
              <span v-else>
                <a href="/auth/userinfo"> <span>Reply</span> </a>
              </span>
            </div>

            <!-- Reply Modal -->
            <b-modal id="exampleModalCenter" hide-footer title="Add Answer" title-tag="h4" modal-class="register-modal" footer-class="justify-content-center">
              <form class="mt-0">
                <div class="form-group">
                  <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24">
                    <path fill="currentColor" d="m21.558 3.592l-1.15-1.15a1.49 1.49 0 0 0-2.12 0L13 7.731V11h3.27l5.288-5.288a1.49 1.49 0 0 0 0-2.12ZM15.579 9.45h-1.03V8.42L18 4.973l1.03 1.03Z" />
                    <path fill="currentColor" d="M19 19H5V5h6V3H5a2.006 2.006 0 0 0-2 2v14a2.006 2.006 0 0 0 2 2h14a2.006 2.006 0 0 0 2-2v-6h-2Z" />
                  </svg>
                  <b-form-textarea type="text" v-model="replies.contentR" class="mb-2" :class="[is_submit_reply ? (replies.contentR && replies.contentR.length<500 && replies.contentR.length>25 ? 'is-valid' : 'is-invalid') : '']" placeholder="Enter your reply content here"></b-form-textarea>
                  <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                      <b-form-invalid-feedback :class="{ 'd-block': is_submit_reply && !replies.contentR }">Please Enter content between 25 and 500 characters</b-form-invalid-feedback>
                    
                  <div class="mt-4 mb-5">
                    <svg xmlns="http://www.w3.org/2000/svg" class="mb-1" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24">
                      <g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2">
                        <path d="M2 6a4 4 0 0 1 4-4h12a4 4 0 0 1 4 4v12a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V6Z" />
                        <circle cx="8.5" cy="8.5" r="2.5" />
                        <path d="M14.526 12.621L6 22h12.133A3.867 3.867 0 0 0 22 18.133V18c0-.466-.175-.645-.49-.99l-4.03-4.395a2 2 0 0 0-2.954.006Z" />
                      </g>
                    </svg>
                    <b-file @change="onFileChanged" ></b-file>                    
                  </div>
                </div>
                <b-button
                  variant="primary"
                  block
                  class="mt-2 mb-2"
                  @click="
                    reply();
                  "
                  >Submit</b-button
                >
              </form>
            </b-modal>
          </div>
          <div class="float-right mt-4">
            <b-button-group>
                    <a class="btn btn-outline-primary" href="#" >Right Answer</a>
                    <a class="btn btn-primary" :href="'/questionpage/'+question.id+'/'" >Newest</a>
                    <a class="btn btn-primary" :href="'/questionpageoldest/'+question.id+'/'">Oldest</a>
                    <a class="btn btn-primary" :href="'/questionpagemostliked/'+question.id+'/'">Most Liked</a>
                    </b-button-group>
                    </div>
          <h5 class="mt-4 ml-4"> Answers</h5>
                <div id="mediaObjectNotationIcon" class="col-lg-12 layout-spacing mt-5 row">
            <div class="panel-heading col-12">
                <div class="panel-body mb-3 pill-justify-right col-xl-12">
                    <b-tab title="Newest" active>
                      <div v-for="rep in Replies" :key="rep.id">
                        <div v-if="rep.questionRep == question.id && rep.accepted==true && rep.checked==true" class="panel-body notation-text-icon">
                          
                          <b-media>
                            <div v-for="u in Userprofiles" :key="u.id">
                              <div v-if="u.id == rep.userprofileRep">
                                <div class="float-left">
                                  <b-avatar class="mr-3" :square="true" size="3rem" :src="'http://127.0.0.1:8000' + u.imageU" width="40px" />
                                </div>
                                <h6 class="">{{ u.firstname }} {{ u.lastname }}</h6>
                              </div>
                            </div>
                            <p class="meta-date-time media-text mb-4">{{ rep.dateR | formatDate }}</p>
                            <b-card class="bg-transparent border-0 col-12">
                              <b-media>
                                <template #aside>
                              <b-card-text>
<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="3em" height="3em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><path fill="#62b47d" fill-rule="evenodd" d="M2 15.5V2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.74.439L8 13.069l-5.26 2.87A.5.5 0 0 1 2 15.5zm8.854-9.646a.5.5 0 0 0-.708-.708L7.5 7.793L6.354 6.646a.5.5 0 1 0-.708.708l1.5 1.5a.5.5 0 0 0 .708 0l3-3z"/></svg>
                              
                              </b-card-text>
                              <b-card-text>
                            <h5 class="media-text ml-3 mb-1">
                              {{ rep.contentR }}
                            </h5>
                             </b-card-text>
                                </template>
                              </b-media>
                             </b-card>
                            <div v-if="rep.imageR != null" class="widget-content mb-4 ml-4">
                              <img :src="'http://127.0.0.1:8000' + rep.imageR" class="rounded mx-auto d-block" style="max-width: 100%; height: auto" />
                            </div>
                            <div class="media-notation mb-4 float-right">
                              <a href="javascript:void(0);" class="">
                                  <likecomponent :replyid="rep.id" :userprofile="CurrentUserProfile.id" />
                              </a>
                              <a href="javascript:void(0);" class="mr-2"
                                ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="20" height="20" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1792 1536">
                                  <path
                                    fill="currentColor"
                                    d="M896 128q-204 0-381.5 69.5T232.5 385T128 640q0 112 71.5 213.5T401 1029l87 50l-27 96q-24 91-70 172q152-63 275-171l43-38l57 6q69 8 130 8q204 0 381.5-69.5t282-187.5T1664 640t-104.5-255t-282-187.5T896 128zm896 512q0 174-120 321.5t-326 233t-450 85.5q-70 0-145-8q-198 175-460 242q-49 14-114 22h-5q-15 0-27-10.5t-16-27.5v-1q-3-4-.5-12t2-10t4.5-9.5l6-9l7-8.5l8-9q7-8 31-34.5t34.5-38t31-39.5t32.5-51t27-59t26-76q-157-89-247.5-220T0 640q0-174 120-321.5t326-233T896 0t450 85.5t326 233T1792 640z"
                                  />
                                </svg>
                                {{ rep.nbCommentR }} comments
                              </a>
                              <a href="javascript:void(0);" class=""
                                ><svg
                                  xmlns="http://www.w3.org/2000/svg"
                                  width="20"
                                  height="20"
                                  viewBox="0 0 24 24"
                                  fill="none"
                                  stroke="currentColor"
                                  stroke-width="2"
                                  stroke-linecap="round"
                                  stroke-linejoin="round"
                                  class="feather feather-message-square"
                                >
                                  <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
                                </svg>
                                <span v-if="isLoggedIn && CurrentUserProfile.id!=null">
                                  <span v-b-modal="modalCreateCommentRight(rep.id)">Add a comment</span>
                                </span>
                                <span v-else>
                                  <a href="/auth/userinfo"> <span>Add a comment</span></a>
                                </span>
                              </a>

                              <!-- Comment Modal -->

                              <b-modal :id="'modalCreateCommentRight' + rep.id" hide-footer title="Add Comment" title-tag="h4" modal-class="register-modal" footer-class="justify-content-center">
                                <form class="mt-0">
                                  <div class="form-group">
                                    <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24">
                                      <path
                                        fill="currentColor"
                                        d="m21.558 3.592l-1.15-1.15a1.49 1.49 0 0 0-2.12 0L13 7.731V11h3.27l5.288-5.288a1.49 1.49 0 0 0 0-2.12ZM15.579 9.45h-1.03V8.42L18 4.973l1.03 1.03Z"
                                      />
                                      <path fill="currentColor" d="M19 19H5V5h6V3H5a2.006 2.006 0 0 0-2 2v14a2.006 2.006 0 0 0 2 2h14a2.006 2.006 0 0 0 2-2v-6h-2Z" />
                                    </svg>
                                    <b-form-textarea type="text" class="mb-2" v-model="comment.contentCo" :class="[is_submit_comment ? (comment.contentCo && comment.contentCo.length<200 && comment.contentCo.length>15 ? 'is-valid' : 'is-invalid') : '']" placeholder="Enter your comment here"></b-form-textarea>
                                  <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                      <b-form-invalid-feedback :class="{ 'd-block': is_submit_comment && !comment.contentCo }">Please Enter content between 15 and 200 characters</b-form-invalid-feedback>
                                  </div>
                                  <b-button
                                    variant="primary"
                                    block
                                    class="mt-2 mb-2"
                                    @click="
                                      commentaire(rep);
                                    "
                                    >Submit</b-button
                                  >
                                </form>
                              </b-modal>
                            </div>
                          </b-media>
                          <hr width="90%" />
                          <div v-for="c in Comments" :key="c.id">
                            <div v-if="c.replyCo == rep.id">
                              <div v-if="CurrentUserProfile.id == c.userprofileCo">
                                <b-dropdown v-if="CurrentUserProfile.id == c.userprofileCo" variant="icon-only" dropleft toggle-tag="a" class="mr-2 custom-dropdown float-right">
                                  <template #button-content>
                                    <svg
                                      xmlns="http://www.w3.org/2000/svg"
                                      style="width: 15px; height: 15px"
                                      width="24"
                                      height="24"
                                      viewBox="0 0 24 24"
                                      fill="none"
                                      stroke="currentColor"
                                      stroke-width="2"
                                      stroke-linecap="round"
                                      stroke-linejoin="round"
                                      class="feather feather-more-vertical"
                                    >
                                      <circle cx="12" cy="12" r="1"></circle>
                                      <circle cx="12" cy="5" r="1"></circle>
                                      <circle cx="12" cy="19" r="1"></circle>
                                    </svg>
                                  </template>
                                  <b-modal :id="'modalModifCommentRight' + c.id" hide-footer title="Modify Comment" title-tag="h4" modal-class="register-modal" footer-class="justify-content-center">
                                    <form class="mt-0">
                                      <div class="form-group">
                                        <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24">
                                          <path
                                            fill="currentColor"
                                            d="m21.558 3.592l-1.15-1.15a1.49 1.49 0 0 0-2.12 0L13 7.731V11h3.27l5.288-5.288a1.49 1.49 0 0 0 0-2.12ZM15.579 9.45h-1.03V8.42L18 4.973l1.03 1.03Z"
                                          />
                                          <path fill="currentColor" d="M19 19H5V5h6V3H5a2.006 2.006 0 0 0-2 2v14a2.006 2.006 0 0 0 2 2h14a2.006 2.006 0 0 0 2-2v-6h-2Z" />
                                        </svg>
                                        <b-form-textarea type="text" class="mb-2" :class="[is_submit_commentmodif ? (c.contentCo && c.contentCo.length<200 && c.contentCo.length>15 ? 'is-valid' : 'is-invalid') : '']" v-model="c.contentCo" placeholder="Modify your comment here"></b-form-textarea>
                                      <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                      <b-form-invalid-feedback :class="{ 'd-block': is_submit_commentmodif && !c.contentCo }">Please Enter content between 15 and 200 characters</b-form-invalid-feedback>
                    
                                      </div>
                                      <b-button
                                        variant="primary"
                                        block
                                        class="mt-2 mb-2"
                                        @click="
                                          commentModif(c);
                                        "
                                        >Modify</b-button
                                      >
                                    </form>
                                  </b-modal>
                                  <b-dropdown-item v-b-modal="modalModifCommentRight(c.id)">Modify</b-dropdown-item>
                                  <b-dropdown-item @click="deleteComment(c)">Delete</b-dropdown-item>
                                </b-dropdown>
                              </div>
                              <p class="float-right mr-4" style="font-size: 10px">{{ c.dateCo | formatDate }}</p>
                              <b-card class="ml-5 bg-transparent border-0"><b-card-text>{{ c.contentCo }} - 
                                <span v-for="u in Userprofiles" :key="u.id">
                                  <span v-if="u.id==c.userprofileCo">
                                   <a class="text-primary" :href="'/profile/'+u.id+'/'"> {{u.firstname}} {{u.lastname}}</a>
                                  </span>
                                </span>
                                </b-card-text></b-card>
                              <hr width="90%" />
                            </div>
                          </div>
                        </div>
                      </div>
                    </b-tab>
                    
                </div>
              </div>
            </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

import '@/assets/sass/widgets/widgets.scss';
import { mapGetters, mapActions } from 'vuex';
import likecomponent from './like-component.vue'
export default {
  metaInfo: { title: 'Question Page' },
  components:{
    likecomponent,
  },
  data() {
    return {
      showMore:false,
      question: [],
      userprofile: [],
      userprofileRep: [],
      CurrentUserProfile: [],
      replydetails: [],
      comment: {
        contentCo: '',
        replyCo: '',
        userprofileCo: '',
      },
      CurrentUser: [],
      likedQuestion: false,
      likedReply: false,
      likes: 0,
      replies: {
        contentR: '',
        questionRep: '',
      },
      image: null,
      vote: {
        questionVo: '',
        userprofileVo: '',
        replyVo: '',
      },
      is_submit_reply:false,
      is_submit_replymodif:false,
      is_submit_comment:false,
      is_submit_commentmodif:false,
    };
  },
  computed: {
    ...mapGetters({
      Questions: 'StateQuestions',
      Replies: 'StateReplies',
      Userprofiles: 'StateUserprofiles',
      User: 'StateUser',
      Users: 'StateUsers',
      Votes: 'StateVotes',
      Comments: 'StateComments',
    }),
    isLoggedIn: function () {
      return this.$store.getters.isAuthenticated;
    },
  },
  methods: {
    ...mapActions(['GetComments', 'GetQuestions', 'GetUsers', 'GetVotes', 'CreateVote', 'GetReplies', 'GetUserprofiles', 'CreateReply', 'CreateComment']),
    onFileChanged(event) {
      this.image = event.target.files[0];
    },
    deleteliked() {
      for (let v in this.Votes) {
        if (this.Votes[v].questionVo === this.vote.questionVo && this.Votes[v].userprofileVo === this.vote.userprofileVo) {
          axios.delete('/vote/vote-delete/' + this.Votes[v].id + '/');
        }
      }

      axios.put('/question/question-update/' + this.$route.params.id + '/', {
        nblikes: this.likes - 1,
      });
      this.likedQuestion = false;
      this.likes -= 1;
    },
    liked() {
      this.CreateVote(this.vote);

      axios.put('/question/question-update/' + this.$route.params.id + '/', {
        nblikes: this.likes + 1,
      });
      this.likedQuestion = true;
      this.likes += 1;
    },
    deleteReply(id) {
      this.$swal({
        icon: 'warning',
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        showCancelButton: true,
        confirmButtonText: 'Delete',
        padding: '2em',
      }).then((result) => {
        if (result.value) {
          axios.delete(`http://127.0.0.1:8000/reply/reply-delete/${id}/`);
          axios.put('/userprofile/userprofile-update/' + this.CurrentUserProfile.id + '/', { nbreplies: (this.CurrentUserProfile.nbreplies -= 1) });
          axios.put('/question/question-update/' + this.$route.params.id + '/', {
            nbrep: (this.question.nbrep -= 1),
          });
          this.$swal('Deleted!', 'Your reply has been deleted.', 'success');
          this.$router.go();
        }
      });
    },
    deleteComment(c) {
      let replydetails = [];
      this.$swal({
        icon: 'warning',
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        showCancelButton: true,
        confirmButtonText: 'Delete',
        padding: '2em',
      }).then((result) => {
        if (result.value) {
          axios.get('/reply/reply-detail/' + c.replyCo + '/').then((response) => {
            replydetails = response.data;

            axios.post('/reply/reply-update/' + c.replyCo + '/', {
              nbCommentR: (replydetails.nbCommentR -= 1),
            });
          });
          axios.delete(`http://127.0.0.1:8000/comment/comment-delete/${c.id}/`);
          this.$swal('Deleted!', 'Your comment has been deleted.', 'success');
          this.$router.go();
        }
      });
    },
    async reply() {
      try {
        this.is_submit_reply=true
        if(this.replies.contentR && this.replies.contentR.length<500 && this.replies.contentR.length>25){
          this.$bvModal.hide("exampleModalCenter")
        for (let u in this.Userprofiles) {
          if (this.Userprofiles[u].userU == this.CurrentUser.id) {
            this.userprofileRep = this.Userprofiles[u].id;
            this.CurrentUserProfile = this.Userprofiles[u];
          }
        }
        var formdata = new FormData();
        if (this.image != null) {
          formdata.append('imageR', this.image);
        }
        formdata.append('contentR', this.replies.contentR);
        formdata.append('questionRep', this.questionRep);
        formdata.append('userprofileRep', this.userprofileRep);
        await this.CreateReply(formdata);
        
        this.replies.contentR = '';
        this.GetReplies();
        this.is_submit_reply=false
      }} catch (error) {
        throw 'Il ya un error!';
      }
    },
    async replyModif(r) {
      try {
        
        this.replies.contentR = r.contentR;
        this.is_submit_replymodif=true
        if(this.replies.contentR && this.replies.contentR.length<500 && this.replies.contentR.length>25){
          this.$bvModal.hide('modalModifReplyRight'+r.id)
        var formdata = new FormData();
        if (this.image != null) {
          formdata.append('imageR', this.image);
        }
        formdata.append('contentR', this.replies.contentR);
        formdata.append('checked', r.checked);
        await axios.post('/reply/reply-update/' + r.id + '/', formdata);
        this.GetReplies();
        this.is_submit_replymodif=false
      }} catch (error) {
        throw 'Il ya un errora !';
      }
    },
    async commentaire(rep) {
      this.is_submit_comment=true
        if(this.comment.contentCo && this.comment.contentCo.length<200 && this.comment.contentCo.length>15){
          this.$bvModal.hide('modalCreateCommentRight'+rep.id)
      axios.get('/reply/reply-detail/' + rep.id + '/').then((response) => {
        this.replydetails = response.data;
      });
      this.comment.replyCo = rep.id;
      try {
        await this.CreateComment(this.comment);
        await axios.post('/reply/reply-update/' + rep.id + '/', {
          nbCommentR: (this.replydetails.nbCommentR += 1),
        });
        this.GetReplies();
        this.comment.contentCo = '';
        this.is_submit_comment=false
      
      } catch (error) {
        throw 'Il ya un errora !';
      }}
    },
    async commentModif(c) {
      try {
        this.comment.contentCo = c.contentCo;
        this.is_submit_commentmodif=true
        if(this.comment.contentCo && this.comment.contentCo.length<200 && this.comment.contentCo.length>15){
          this.$bvModal.hide('modalModifCommentRight'+c.id)
        
        await axios.post('/comment/comment-update/' + c.id + '/', { contentCo: this.comment.contentCo });
        this.GetReplies();
        this.GetComments();
        this.is_submit_commentmodif=false
      }} catch (error) {
        throw 'Il ya un errora !';
      }
    },
    //right answer
    modalCreateCommentRight(i) {
      return 'modalCreateCommentRight' + i;
    },
    modalModifCommentRight(i) {
      return 'modalModifCommentRight' + i;
    },
  },
  created() {
    //this.GetComments();
    this.GetQuestions();
    this.GetReplies();
    this.GetUsers();
    this.GetUserprofiles();
    this.GetVotes();
    this.GetComments();
    //liked replies
    
    //sort by newest
    this.oldestreplies = this.Replies.reverse();
    this.mostlikedreplies = this.Replies.sort((a, b) => b.nblikesR - a.nblikesR);
    axios
      .get('/question/question-detail/' + this.$route.params.id + '/')
      .then((response) => {
        this.question = response.data;
        this.likes = this.question.nblikes;
        for (let u in this.Users) {
          if (this.Users[u].username == this.User) {
            this.CurrentUser = this.Users[u];
            for (let p in this.Userprofiles) {
              if (this.Userprofiles[p].userU == this.CurrentUser.id) {
                this.CurrentUserProfile = this.Userprofiles[p];
                this.vote.questionVo = this.question.id;
                this.vote.userprofileVo = this.CurrentUserProfile.id;
                this.comment.userprofileCo = this.CurrentUserProfile.id;
                for (let v in this.Votes) {
                  if (this.Votes[v].userprofileVo == this.CurrentUserProfile.id && this.Votes[v].questionVo == this.question.id) {
                    this.likedQuestion = true;
                  }
                }
              }
            }
          }
        }

        axios.get('/userprofile/userprofile-detail/' + this.question.userprofileQ + '/').then((response) => {
          this.userprofile = response.data;
          this.questionRep = this.question.id;
        });
      })
      .catch((err) => {
        console.log(err);
      });
      
  },
};
</script>

<style>
</style>