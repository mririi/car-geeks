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
    <div class="col-xl-10 mt-3 col-lg-6 col-md-6 col-sm-12 col-12 layout-spacing">
      <div class="widget widget-card-one">
        <div class="widget-heading">
          <b-media>
            <template #aside>
              <div class="w-img">
                <img :src="'http://127.0.0.1:8000' + userprofile.imageU" alt="avatar" />
              </div>
            </template>
            <h6>{{ userprofile.firstname }} {{ userprofile.lastname }}</h6>
            <p class="meta-date-time">{{ question.dateQ | formatDate }}</p>
            <h4 class="mt-5">{{ question.titleQ }}</h4>
          </b-media>
        </div>
        <div class="widget-content">
          <h6 class="ml-5 mb-5">{{ question.contentQ }}</h6>
          <div class="widget-content mb-5" v-if="question.imageQ != null">
            <img :src="'http://127.0.0.1:8000' + question.imageQ" class="rounded mx-auto d-block" style="max-width: 100%; height: auto" />
          </div>
          <div class="w-action">
            <div class="card-like ml-4">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                class="feather feather-thumbs-up"
              >
                <path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path>
              </svg>
              <span @click="like">{{ question.nblikes }} Likes</span>
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
              <span v-b-modal.exampleModalCenter>Reply</span>
            </div>

            <!-- Reply Modal -->
            <b-modal id="exampleModalCenter" hide-footer title="Add Answer" title-tag="h4" modal-class="register-modal" footer-class="justify-content-center">
              <form class="mt-0">
                <div class="form-group">
                  <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24">
                    <path fill="currentColor" d="m21.558 3.592l-1.15-1.15a1.49 1.49 0 0 0-2.12 0L13 7.731V11h3.27l5.288-5.288a1.49 1.49 0 0 0 0-2.12ZM15.579 9.45h-1.03V8.42L18 4.973l1.03 1.03Z" />
                    <path fill="currentColor" d="M19 19H5V5h6V3H5a2.006 2.006 0 0 0-2 2v14a2.006 2.006 0 0 0 2 2h14a2.006 2.006 0 0 0 2-2v-6h-2Z" />
                  </svg>
                  <b-form-textarea type="text" v-model="replies.contentR" class="mb-2" placeholder="Enter your reply content here"></b-form-textarea>
                  <div class="mt-4 mb-5">
                    <svg xmlns="http://www.w3.org/2000/svg" class="mb-1" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24">
                      <g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2">
                        <path d="M2 6a4 4 0 0 1 4-4h12a4 4 0 0 1 4 4v12a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V6Z" />
                        <circle cx="8.5" cy="8.5" r="2.5" />
                        <path d="M14.526 12.621L6 22h12.133A3.867 3.867 0 0 0 22 18.133V18c0-.466-.175-.645-.49-.99l-4.03-4.395a2 2 0 0 0-2.954.006Z" />
                      </g>
                    </svg>
                    <b-file @change="onFileChanged"></b-file>
                  </div>
                </div>
                <b-button variant="primary" block class="mt-2 mb-2" @click="reply">Submit</b-button>
              </form>
            </b-modal>
          </div>
          <div id="mediaObjectNotationIcon" class="col-lg-12 layout-spacing mt-5">
            <div class="panel-heading">
              <div v-if="question.nbrep != 0" class="row">
                <h5 class="mt-4 ml-4">{{ question.nbrep }} Answers</h5>
                <div class="panel-body mb-3 pill-justify-right">
                  <b-tabs pills nav-class=" justify-content-end mb-5">
                    <b-tab title="Default" active>
                      <div v-for="rep in Replies" :key="rep.id">
                        <div v-if="rep.questionRep == question.id" class="panel-body notation-text-icon">
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
                            <h5 class="media-text ml-5 mb-1">
                              {{ rep.contentR }}
                            </h5>
                            <div v-if="rep.imageR != null" class="widget-content mb-4">
                              <img :src="'http://127.0.0.1:8000' + rep.imageR" class="rounded mx-auto d-block" style="max-width: 100%; height: auto" />
                            </div>
                            <div class="media-notation mb-4 float-right">
                              <a href="javascript:void(0);" class="mr-2"
                                ><svg
                                  xmlns="http://www.w3.org/2000/svg"
                                  width="22"
                                  height="22"
                                  viewBox="0 0 24 30"
                                  fill="none"
                                  stroke="currentColor"
                                  stroke-width="2"
                                  stroke-linecap="round"
                                  stroke-linejoin="round"
                                  class="feather feather-thumbs-up"
                                >
                                  <path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path>
                                </svg>
                                {{ rep.nblikesR }} likes
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
                                <span v-b-modal.registerModal1>Add a comment</span>
                              </a>
                              
                              <!-- Comment Modal -->
                              <b-modal id="registerModal1" hide-footer title="Add Comment" title-tag="h4" modal-class="register-modal" footer-class="justify-content-center">
                                <form class="mt-0">
                                  <div class="form-group">
                                    <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24">
                                      <path
                                        fill="currentColor"
                                        d="m21.558 3.592l-1.15-1.15a1.49 1.49 0 0 0-2.12 0L13 7.731V11h3.27l5.288-5.288a1.49 1.49 0 0 0 0-2.12ZM15.579 9.45h-1.03V8.42L18 4.973l1.03 1.03Z"
                                      />
                                      <path fill="currentColor" d="M19 19H5V5h6V3H5a2.006 2.006 0 0 0-2 2v14a2.006 2.006 0 0 0 2 2h14a2.006 2.006 0 0 0 2-2v-6h-2Z" />
                                    </svg>
                                    <b-form-textarea type="text" class="mb-2" placeholder="Enter your comment here"></b-form-textarea>
                                  </div>
                                  <b-button variant="primary" block class="mt-2 mb-2" @click="$bvModal.hide('registerModal1')">Submit</b-button>
                                </form>
                              </b-modal>
                            </div>
                          </b-media>
                          <hr width="90%">
                        </div>
                      </div>
                    </b-tab>
                    <b-tab title="Newest">
                      <div class="panel-body notation-text-icon">
                        <b-media>
                          <template #aside>
                            <img class="rounded mr-2" src="@/assets/images/profile-4.jpeg" width="40px" alt="pic1" />
                          </template>
                          <h6 class="">Samira</h6>
                          <p class="meta-date-time media-text mb-4">Monday, Nov 18</p>
                          <p class="media-text">
                            Sed dapibus nulla elementum, rutrum neque eu, gravida neque. Fusce condimentum cursus mauris et ornare. Mauris fermentum mi id sollicitudin viverra. Aenean dignissim sed
                            ante eget dapibus.
                          </p>
                          <div class="widget-content mb-4">
                            <img src="https://i.gaw.to/content/photos/40/87/408765_2020_Ford_Ranger.jpg" class="rounded mx-auto d-block" style="max-width: 100%; height: auto" />
                          </div>
                          <div class="media-notation float-right">
                            <a href="javascript:void(0);" class="mr-2"
                              ><svg
                                xmlns="http://www.w3.org/2000/svg"
                                width="22"
                                height="22"
                                viewBox="0 0 24 30"
                                fill="none"
                                stroke="currentColor"
                                stroke-width="2"
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                class="feather feather-thumbs-up"
                              >
                                <path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path>
                              </svg>
                              50 likes
                            </a>
                            <a href="javascript:void(0);" class="mr-2"
                              ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="20" height="20" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1792 1536">
                                <path
                                  fill="currentColor"
                                  d="M896 128q-204 0-381.5 69.5T232.5 385T128 640q0 112 71.5 213.5T401 1029l87 50l-27 96q-24 91-70 172q152-63 275-171l43-38l57 6q69 8 130 8q204 0 381.5-69.5t282-187.5T1664 640t-104.5-255t-282-187.5T896 128zm896 512q0 174-120 321.5t-326 233t-450 85.5q-70 0-145-8q-198 175-460 242q-49 14-114 22h-5q-15 0-27-10.5t-16-27.5v-1q-3-4-.5-12t2-10t4.5-9.5l6-9l7-8.5l8-9q7-8 31-34.5t34.5-38t31-39.5t32.5-51t27-59t26-76q-157-89-247.5-220T0 640q0-174 120-321.5t326-233T896 0t450 85.5t326 233T1792 640z"
                                />
                              </svg>
                              25 comments
                            </a>
                            <a href="javascript:void(0);" class="mr-2">
                              <svg
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
                              <span v-b-modal.registerModal2>Add a comment</span>
                            </a>
                            <!-- Comment Modal -->
                            <b-modal id="registerModal2" hide-footer title="Add Comment" title-tag="h4" modal-class="register-modal" footer-class="justify-content-center">
                              <form class="mt-0">
                                <div class="form-group">
                                  <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24">
                                    <path
                                      fill="currentColor"
                                      d="m21.558 3.592l-1.15-1.15a1.49 1.49 0 0 0-2.12 0L13 7.731V11h3.27l5.288-5.288a1.49 1.49 0 0 0 0-2.12ZM15.579 9.45h-1.03V8.42L18 4.973l1.03 1.03Z"
                                    />
                                    <path fill="currentColor" d="M19 19H5V5h6V3H5a2.006 2.006 0 0 0-2 2v14a2.006 2.006 0 0 0 2 2h14a2.006 2.006 0 0 0 2-2v-6h-2Z" />
                                  </svg>
                                  <b-form-textarea type="text" class="mb-2" placeholder="Enter your comment here"></b-form-textarea>
                                </div>
                                <b-button variant="primary" block class="mt-2 mb-2" @click="$bvModal.hide('registerModal2')">Submit</b-button>
                              </form>
                            </b-modal>
                          </div>
                        </b-media>
                      </div>
                    </b-tab>
                    <b-tab title="Oldest">
                      <div class="panel-body notation-text-icon">
                        <b-media>
                          <template #aside>
                            <img class="rounded mr-2" src="@/assets/images/profile-4.jpeg" width="40px" alt="pic1" />
                          </template>
                          <h6 class="">Samira</h6>
                          <p class="meta-date-time media-text mb-4">Monday, Nov 18</p>
                          <p class="media-text">
                            Sed dapibus nulla elementum, rutrum neque eu, gravida neque. Fusce condimentum cursus mauris et ornare. Mauris fermentum mi id sollicitudin viverra. Aenean dignissim sed
                            ante eget dapibus.
                          </p>
                          <div class="widget-content mb-4">
                            <img src="https://i.gaw.to/content/photos/40/87/408765_2020_Ford_Ranger.jpg" class="rounded mx-auto d-block" style="max-width: 100%; height: auto" />
                          </div>
                          <div class="media-notation float-right">
                            <a href="javascript:void(0);" class="mr-2"
                              ><svg
                                xmlns="http://www.w3.org/2000/svg"
                                width="22"
                                height="22"
                                viewBox="0 0 24 30"
                                fill="none"
                                stroke="currentColor"
                                stroke-width="2"
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                class="feather feather-thumbs-up"
                              >
                                <path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path>
                              </svg>
                              50 likes
                            </a>
                            <a href="javascript:void(0);" class="mr-2"
                              ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="20" height="20" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1792 1536">
                                <path
                                  fill="currentColor"
                                  d="M896 128q-204 0-381.5 69.5T232.5 385T128 640q0 112 71.5 213.5T401 1029l87 50l-27 96q-24 91-70 172q152-63 275-171l43-38l57 6q69 8 130 8q204 0 381.5-69.5t282-187.5T1664 640t-104.5-255t-282-187.5T896 128zm896 512q0 174-120 321.5t-326 233t-450 85.5q-70 0-145-8q-198 175-460 242q-49 14-114 22h-5q-15 0-27-10.5t-16-27.5v-1q-3-4-.5-12t2-10t4.5-9.5l6-9l7-8.5l8-9q7-8 31-34.5t34.5-38t31-39.5t32.5-51t27-59t26-76q-157-89-247.5-220T0 640q0-174 120-321.5t326-233T896 0t450 85.5t326 233T1792 640z"
                                />
                              </svg>
                              25 comments
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
                              <span v-b-modal.registerModal3>Add a comment</span>
                            </a>
                            <!-- Comment Modal -->
                            <b-modal id="registerModal3" hide-footer title="Add Comment" title-tag="h4" modal-class="register-modal" footer-class="justify-content-center">
                              <form class="mt-0">
                                <div class="form-group">
                                  <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24">
                                    <path
                                      fill="currentColor"
                                      d="m21.558 3.592l-1.15-1.15a1.49 1.49 0 0 0-2.12 0L13 7.731V11h3.27l5.288-5.288a1.49 1.49 0 0 0 0-2.12ZM15.579 9.45h-1.03V8.42L18 4.973l1.03 1.03Z"
                                    />
                                    <path fill="currentColor" d="M19 19H5V5h6V3H5a2.006 2.006 0 0 0-2 2v14a2.006 2.006 0 0 0 2 2h14a2.006 2.006 0 0 0 2-2v-6h-2Z" />
                                  </svg>
                                  <b-form-textarea type="text" class="mb-2" placeholder="Enter your comment here"></b-form-textarea>
                                </div>
                                <b-button variant="primary" block class="mt-2 mb-2" @click="$bvModal.hide('registerModal3')">Submit</b-button>
                              </form>
                            </b-modal>
                          </div>
                        </b-media>
                      </div></b-tab
                    >
                    <b-tab title="Most liked">
                      <div class="panel-body notation-text-icon">
                        <b-media>
                          <template #aside>
                            <img class="rounded mr-2" src="@/assets/images/profile-4.jpeg" width="40px" alt="pic1" />
                          </template>
                          <h6 class="">Samira</h6>
                          <p class="meta-date-time media-text mb-4">Monday, Nov 18</p>
                          <p class="media-text">
                            Sed dapibus nulla elementum, rutrum neque eu, gravida neque. Fusce condimentum cursus mauris et ornare. Mauris fermentum mi id sollicitudin viverra. Aenean dignissim sed
                            ante eget dapibus.
                          </p>
                          <div class="widget-content mb-4">
                            <img src="https://i.gaw.to/content/photos/40/87/408765_2020_Ford_Ranger.jpg" class="rounded mx-auto d-block" style="max-width: 100%; height: auto" />
                          </div>
                          <div class="media-notation float-right">
                            <a href="javascript:void(0);" class="mr-2"
                              ><svg
                                xmlns="http://www.w3.org/2000/svg"
                                width="22"
                                height="22"
                                viewBox="0 0 24 30"
                                fill="none"
                                stroke="currentColor"
                                stroke-width="2"
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                class="feather feather-thumbs-up"
                              >
                                <path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path>
                              </svg>
                              50 likes
                            </a>
                            <a href="javascript:void(0);" class="mr-2"
                              ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="20" height="20" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1792 1536">
                                <path
                                  fill="currentColor"
                                  d="M896 128q-204 0-381.5 69.5T232.5 385T128 640q0 112 71.5 213.5T401 1029l87 50l-27 96q-24 91-70 172q152-63 275-171l43-38l57 6q69 8 130 8q204 0 381.5-69.5t282-187.5T1664 640t-104.5-255t-282-187.5T896 128zm896 512q0 174-120 321.5t-326 233t-450 85.5q-70 0-145-8q-198 175-460 242q-49 14-114 22h-5q-15 0-27-10.5t-16-27.5v-1q-3-4-.5-12t2-10t4.5-9.5l6-9l7-8.5l8-9q7-8 31-34.5t34.5-38t31-39.5t32.5-51t27-59t26-76q-157-89-247.5-220T0 640q0-174 120-321.5t326-233T896 0t450 85.5t326 233T1792 640z"
                                />
                              </svg>
                              25 comments
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
                              <span v-b-modal.registerModal4>Add a comment</span>
                            </a>
                            <!-- Comment Modal -->
                            <b-modal id="registerModal4" hide-footer title="Add Comment" title-tag="h4" modal-class="register-modal" footer-class="justify-content-center">
                              <form class="mt-0">
                                <div class="form-group">
                                  <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24">
                                    <path
                                      fill="currentColor"
                                      d="m21.558 3.592l-1.15-1.15a1.49 1.49 0 0 0-2.12 0L13 7.731V11h3.27l5.288-5.288a1.49 1.49 0 0 0 0-2.12ZM15.579 9.45h-1.03V8.42L18 4.973l1.03 1.03Z"
                                    />
                                    <path fill="currentColor" d="M19 19H5V5h6V3H5a2.006 2.006 0 0 0-2 2v14a2.006 2.006 0 0 0 2 2h14a2.006 2.006 0 0 0 2-2v-6h-2Z" />
                                  </svg>
                                  <b-form-textarea type="text" class="mb-2" placeholder="Enter your comment here"></b-form-textarea>
                                </div>
                                <b-button variant="primary" block class="mt-2 mb-2" @click="$bvModal.hide('registerModal4')">Submit</b-button>
                              </form>
                            </b-modal>
                          </div>
                        </b-media>
                      </div>
                    </b-tab>
                  </b-tabs>
                </div>
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
export default {
  data() {
    return {
      question: [],
      userprofile: [],
      userprofileRep: [],
      CurrentUserProfile:[],
      CurrentUser:[],
      replies: {
        contentR: '',
        questionRep:'',
      },
      image: null,
       vote: {
        questionVo: "",
        userprofileVo: "",
        replyVo: "",
        like:false,
      },
    };
  },
  computed: {
    ...mapGetters({
      Questions: 'StateQuestions',
      Replies: 'StateReplies',
      Userprofiles: 'StateUserprofiles',
      User: "StateUser",
      Users: "StateUsers",
      Votes: "StateVotes",
    }),
  },
  methods: {
    ...mapActions(['GetQuestions','GetUsers',"GetVotes","CreateVote", 'GetReplies', 'GetUserprofiles', 'CreateReply', 'CreateComment']),
    onFileChanged(event) {
      this.image = event.target.files[0];
    },
    like() {
      this.GetVotes();
      this.vote.questionVo = this.$route.params.id;
      this.vote.userprofileVo = this.CurrentUserProfile.id;
      console.log("question"+this.vote.questionVo+" user is "+ this.vote.userprofileVo)
      let nb = 0;
      for (let v in this.Votes) {
        if (this.Votes[v].userprofileVo == this.CurrentUserProfile.id && this.Votes[v].questionVo==this.$route.params.id) {
          nb = nb + 1;
        }
      }
      
      if (nb == 0) {
            axios.put("/question/question-update/" + this.$route.params.id + "/", {
              nblikes: (this.question.nblikes += 1),
            });
            this.vote.like=true
            this.CreateVote(this.vote);
            console.log("nb==0 is done "+this.vote)
          }
      
      if (this.Votes.length != 0) {
        this.GetVotes();
        for (let v in this.Votes) {
			if (
            this.Votes[v].questionVo == this.$route.params.id &&
            this.Votes[v].userprofileVo == this.CurrentUserProfile.id &&
            this.Votes[v].like == true
          ) {
            axios.put("/question/question-update/" + this.$route.params.id + "/", {
              nblikes: (this.question.nblikes -=1),
            });
            axios.post("/vote/vote-update/" + this.Votes[v].id + "/", {
              like:false
            });
            console.log(this.Votes[v])
          console.log("if in for up")
          }
        }
      } else {
        axios.put("/question/question-update/" + this.$route.params.id + "/", {
          nblikes: (this.question.nblikes += 1),
        });
		this.vote.voteup = true;
		this.vote.votedown = false;
        this.CreateVote(this.vote);
        console.log("last else in up")
      }
      this.GetVotes();
    },
      
     
    async reply() {
      console.log(this.replies.contentR)
      try {
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
        await axios.put('/question/question-update/' + this.$route.params.id + '/', {
          nbrep: (this.question.nbrep += 1),
        });
        /*for(let r in this.Replies)
        {
          if(this.Replies[r].userprofileRep == this.form.userprofileRep && this.Replies[r].questionRep == this.form.questionRep )
          {
             this.replyNo = this.Replies[r]
          }
        }
        if(this.question.userprofileQ != this.CurrentUserProfile.id)
        await axios.post("/notification/notification-create/" , {
          userprofileNo: this.question.userprofileQ, questionNo:this.$route.params.id, replyNo: this.repNo.id,contentNo: this.CurrentUserProfile.lastname+" "+this.CurrentUserProfile.firstname+" has responded to your question"
        });*/
        this.replies.contentR = '';
        await axios.put(
          "/userprofile/userprofile-update/" + this.userprofileRep + "/",
          { nbreplies: (this.CurrentUserProfile.nbreplies += 1) }
        );
      } catch (error) {
        throw 'Il ya un error!';
      }
    },
  },
  created() {
    //this.GetComments();
    this.GetQuestions();
    this.GetReplies();
    this.GetUsers();
    this.GetUserprofiles();
    this.CreateReply();
    this.GetVotes();
    this.CreateVote();

    for (let u in this.Users) {
      if (this.Users[u].username == this.User) {
        this.CurrentUser = this.Users[u];
      }
    }
    /*for (let u in this.Userprofiles) {
      if (this.Userprofiles[u].userU == this.CurrentUser.id) {
        this.CurrentUserProfile = this.Userprofiles[u];
        //this.comment.userprofileCo = this.Userprofiles[u].id;
      }
    }*/
    axios
      .get('/question/question-detail/' + this.$route.params.id + '/')
      .then((response) => {
        this.question = response.data;
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