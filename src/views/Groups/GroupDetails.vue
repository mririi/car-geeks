<template>
  <div class="layout-px-spacing">
    <portal to="breadcrumb">
      <ul class="navbar-nav flex-row">
        <li>
          <div class="page-header">
            <nav class="breadcrumb-one" aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="javascript:;">Groups</a></li>
                <li class="breadcrumb-item active" aria-current="page"><span>Group Details</span></li>
              </ol>
            </nav>
          </div>
        </li>
      </ul>
    </portal>
    <div id="card_8" class="col-lg-12 layout-spacing mt-3">
      <div class="panel-heading">
        <div class="row"></div>
      </div>
      <div class="panel-body">
        <b-card :img-src=" group.imageG" img-width="100%" img-height="290px" img-top class="component-card_8">
          <div class="progress-order">
            <div class="progress-order-header">
              <div class="row">
                <div class="col-md-6 col-sm-6 col-12">
                  <h2>
                    <b>{{ group.titleG }}</b>
                  </h2>
                
                  <h6>Private Group | {{ acceptedposts }} Posts</h6>
                   
                </div>
                <div class="col-md-6 pl-0 col-sm-6 col-12 text-right">
                  <span v-if="existmember == true">
                    <b-button variant="primary" :href="'/group/' + group.id + '/addpost'"
                      ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24">
                        <path fill="currentColor" d="M17 19.22H5V7h7V5H5c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2v-7h-2v7.22z" />
                        <path fill="currentColor" d="M19 2h-2v3h-3c.01.01 0 2 0 2h3v2.99c.01.01 2 0 2 0V7h3V5h-3V2zM7 9h8v2H7zm0 3v2h8v-2h-3zm0 3h8v2H7z" />
                      </svg>
                      Add Post</b-button
                    >
                  </span>

                  <span v-if="existmember == false && requested == false &&  (CurrentUserProfile.id!=null || CurrentUserEntreprise.id!=null)">
                    <b-button variant="primary" @click="Join()"
                      ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 36 36">
                        <path
                          fill="currentColor"
                          d="M12 16.14h-.87a8.67 8.67 0 0 0-6.43 2.52l-.24.28v8.28h4.08v-4.7l.55-.62l.25-.29a11 11 0 0 1 4.71-2.86A6.58 6.58 0 0 1 12 16.14Z"
                          class="clr-i-solid--badged clr-i-solid-path-1--badged"
                        />
                        <path
                          fill="currentColor"
                          d="M31.34 18.63a8.67 8.67 0 0 0-6.43-2.52a10.47 10.47 0 0 0-1.09.06a6.59 6.59 0 0 1-2 2.45a10.91 10.91 0 0 1 5 3l.25.28l.54.62v4.71h3.94v-8.32Z"
                          class="clr-i-solid--badged clr-i-solid-path-2--badged"
                        />
                        <path fill="currentColor" d="M11.1 14.19h.31a6.45 6.45 0 0 1 3.11-6.29a4.09 4.09 0 1 0-3.42 6.33Z" class="clr-i-solid--badged clr-i-solid-path-3--badged" />
                        <circle cx="17.87" cy="13.45" r="4.47" fill="currentColor" class="clr-i-solid--badged clr-i-solid-path-4--badged" />
                        <path
                          fill="currentColor"
                          d="M18.11 20.3A9.69 9.69 0 0 0 11 23l-.25.28v6.33a1.57 1.57 0 0 0 1.6 1.54h11.49a1.57 1.57 0 0 0 1.6-1.54V23.3l-.24-.3a9.58 9.58 0 0 0-7.09-2.7Z"
                          class="clr-i-solid--badged clr-i-solid-path-5--badged"
                        />
                        <path
                          fill="currentColor"
                          d="M24.43 13.44a6.54 6.54 0 0 1 0 .69a4.09 4.09 0 0 0 .58.05h.19a4.05 4.05 0 0 0 2.52-1a7.5 7.5 0 0 1-5.14-6.32A4.13 4.13 0 0 0 21.47 8a6.53 6.53 0 0 1 2.96 5.44Z"
                          class="clr-i-solid--badged clr-i-solid-path-6--badged"
                        />
                        <circle cx="30" cy="6" r="5" fill="currentColor" class="clr-i-solid--badged clr-i-solid-path-7--badged clr-i-badge" />
                        <path fill="none" d="M0 0h36v36H0z" />
                      </svg>
                      Join Group</b-button
                    >
                  </span>
                  <span v-if="CurrentUserProfile.id==null && CurrentUserEntreprise.id==null"> 
                    <b-button variant="primary" href="/auth/login"
                      ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 36 36">
                        <path
                          fill="currentColor"
                          d="M12 16.14h-.87a8.67 8.67 0 0 0-6.43 2.52l-.24.28v8.28h4.08v-4.7l.55-.62l.25-.29a11 11 0 0 1 4.71-2.86A6.58 6.58 0 0 1 12 16.14Z"
                          class="clr-i-solid--badged clr-i-solid-path-1--badged"
                        />
                        <path
                          fill="currentColor"
                          d="M31.34 18.63a8.67 8.67 0 0 0-6.43-2.52a10.47 10.47 0 0 0-1.09.06a6.59 6.59 0 0 1-2 2.45a10.91 10.91 0 0 1 5 3l.25.28l.54.62v4.71h3.94v-8.32Z"
                          class="clr-i-solid--badged clr-i-solid-path-2--badged"
                        />
                        <path fill="currentColor" d="M11.1 14.19h.31a6.45 6.45 0 0 1 3.11-6.29a4.09 4.09 0 1 0-3.42 6.33Z" class="clr-i-solid--badged clr-i-solid-path-3--badged" />
                        <circle cx="17.87" cy="13.45" r="4.47" fill="currentColor" class="clr-i-solid--badged clr-i-solid-path-4--badged" />
                        <path
                          fill="currentColor"
                          d="M18.11 20.3A9.69 9.69 0 0 0 11 23l-.25.28v6.33a1.57 1.57 0 0 0 1.6 1.54h11.49a1.57 1.57 0 0 0 1.6-1.54V23.3l-.24-.3a9.58 9.58 0 0 0-7.09-2.7Z"
                          class="clr-i-solid--badged clr-i-solid-path-5--badged"
                        />
                        <path
                          fill="currentColor"
                          d="M24.43 13.44a6.54 6.54 0 0 1 0 .69a4.09 4.09 0 0 0 .58.05h.19a4.05 4.05 0 0 0 2.52-1a7.5 7.5 0 0 1-5.14-6.32A4.13 4.13 0 0 0 21.47 8a6.53 6.53 0 0 1 2.96 5.44Z"
                          class="clr-i-solid--badged clr-i-solid-path-6--badged"
                        />
                        <circle cx="30" cy="6" r="5" fill="currentColor" class="clr-i-solid--badged clr-i-solid-path-7--badged clr-i-badge" />
                        <path fill="none" d="M0 0h36v36H0z" />
                      </svg>
                      Join Group</b-button
                    >
                  </span>
                  <span v-if="requested == true &&  (CurrentUserProfile.id!=null || CurrentUserEntreprise.id!=null)">
                    <b-button variant="primary"
                      ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24">
                        <circle cx="18" cy="12" r="0" fill="currentColor">
                          <animate attributeName="r" begin=".67" calcMode="spline" dur="1.5s" keySplines="0.2 0.2 0.4 0.8;0.2 0.2 0.4 0.8;0.2 0.2 0.4 0.8" repeatCount="indefinite" values="0;2;0;0" />
                        </circle>
                        <circle cx="12" cy="12" r="0" fill="currentColor">
                          <animate attributeName="r" begin=".33" calcMode="spline" dur="1.5s" keySplines="0.2 0.2 0.4 0.8;0.2 0.2 0.4 0.8;0.2 0.2 0.4 0.8" repeatCount="indefinite" values="0;2;0;0" />
                        </circle>
                        <circle cx="6" cy="12" r="0" fill="currentColor">
                          <animate attributeName="r" begin="0" calcMode="spline" dur="1.5s" keySplines="0.2 0.2 0.4 0.8;0.2 0.2 0.4 0.8;0.2 0.2 0.4 0.8" repeatCount="indefinite" values="0;2;0;0" />
                        </circle>
                      </svg>
                      Requested</b-button
                    >
                  </span>
                  <span v-if="group.userprofileG == CurrentUserProfile.id || group.userentrepriseG == CurrentUserEntreprise.id">
                    <b-button variant="primary" :href="'/groupdashboard/' + group.id + '/dashboard'" class="ml-3"
                      ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 36 36">
                        <path
                          fill="currentColor"
                          d="M12 16.14h-.87a8.67 8.67 0 0 0-6.43 2.52l-.24.28v8.28h4.08v-4.7l.55-.62l.25-.29a11 11 0 0 1 4.71-2.86A6.58 6.58 0 0 1 12 16.14Z"
                          class="clr-i-solid--badged clr-i-solid-path-1--badged"
                        />
                        <path
                          fill="currentColor"
                          d="M31.34 18.63a8.67 8.67 0 0 0-6.43-2.52a10.47 10.47 0 0 0-1.09.06a6.59 6.59 0 0 1-2 2.45a10.91 10.91 0 0 1 5 3l.25.28l.54.62v4.71h3.94v-8.32Z"
                          class="clr-i-solid--badged clr-i-solid-path-2--badged"
                        />
                        <path fill="currentColor" d="M11.1 14.19h.31a6.45 6.45 0 0 1 3.11-6.29a4.09 4.09 0 1 0-3.42 6.33Z" class="clr-i-solid--badged clr-i-solid-path-3--badged" />
                        <circle cx="17.87" cy="13.45" r="4.47" fill="currentColor" class="clr-i-solid--badged clr-i-solid-path-4--badged" />
                        <path
                          fill="currentColor"
                          d="M18.11 20.3A9.69 9.69 0 0 0 11 23l-.25.28v6.33a1.57 1.57 0 0 0 1.6 1.54h11.49a1.57 1.57 0 0 0 1.6-1.54V23.3l-.24-.3a9.58 9.58 0 0 0-7.09-2.7Z"
                          class="clr-i-solid--badged clr-i-solid-path-5--badged"
                        />
                        <path
                          fill="currentColor"
                          d="M24.43 13.44a6.54 6.54 0 0 1 0 .69a4.09 4.09 0 0 0 .58.05h.19a4.05 4.05 0 0 0 2.52-1a7.5 7.5 0 0 1-5.14-6.32A4.13 4.13 0 0 0 21.47 8a6.53 6.53 0 0 1 2.96 5.44Z"
                          class="clr-i-solid--badged clr-i-solid-path-6--badged"
                        />
                        <circle cx="30" cy="6" r="5" fill="currentColor" class="clr-i-solid--badged clr-i-solid-path-7--badged clr-i-badge" />
                        <path fill="none" d="M0 0h36v36H0z" />
                      </svg>
                      Manage Group</b-button
                    >
                  </span>
                </div>
              </div>
            </div>

            <div class="progress-order-body">
              <div class="row mt-4">
                <div class="col-md-12">
                  <ul class="list-inline badge-collapsed-img mb-0 mb-3">
                    <span v-for="m in Members" :key="m.id">
                      <span v-if="m.groupMem == group.id && m.userprofileMem && m.accepted == true">
                        <span v-for="uu in Userprofiles.slice(0, 4)" :key="uu.id">
                          <span v-if="uu.id == m.userprofileMem">
                            <li class="list-inline-item chat-online-usr">
                              <router-link :to="'/profile/' + uu.id">
                                <img alt="avatar" :src=" uu.imageU" class="ml-0" />
                              </router-link>
                            </li>
                          </span>
                        </span>
                      </span>
                    </span>
                    <li class="list-inline-item badge-notify">
                      <div class="notification">
                        <span class="badge badge-info badge-pill">
                          <span v-if="group.nbmembers >3">
                              +{{ group.nbmembers - 3 }} more
                          </span>
                         
                          </span>
                      </div>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </b-card>
      </div>
    </div>
    <div class="row layout-top-spacing">
      <div id="timelineProfile" class="col-xl-12 layout-spacing">
        <div class="panel-heading">
          <div class="row"></div>
        </div>
        <div class="panel-body">
          <div class="timeline-simple">
            <p v-if="existmember == true" class="timeline-title">Group Posts</p>
            <div class="timeline-list">
              <span v-for="p in GroupPost" :key="p.id">
                <span v-if="p.groupPost == group.id && p.accepted == true && existmember == true">
                  <span v-for="u in Userprofiles" :key="u.id">
                    <span v-if="u.id == p.userprofilePost">
                      <div v-if="CurrentUserProfile.id == p.userprofilePost&& p.userprofilePost !=null|| CurrentUserEntreprise.id==p.userentreprisePost &&p.userentreprisePost!=null">
                        <b-dropdown variant="icon-only" dropleft toggle-tag="a" size="1em" class="mb-4 mr-5 custom-dropdown float-right">
                          <template #button-content>
                            <svg
                              xmlns="http://www.w3.org/2000/svg"
                              style="width: 25px; height: 25px"
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
                          <b-dropdown-item :href="'/group/' + group.id + '/updatepost/' + p.id">Modify</b-dropdown-item>
                          <b-dropdown-item @click="deletePost(p.id)">Delete</b-dropdown-item>
                        </b-dropdown>
                      </div>
                      <div class="timeline-post-content">
                        <router-link :to="'/profile/' + u.id" class="text-primary">
                        <div class="user-profile">
                          <img :src=" u.imageU" img-top alt="" />
                        </div>
                        </router-link>

                        <div class="">
                          
                            <h4>{{ u.firstname }} {{ u.lastname }}<span v-if="u.id==group.userprofileG"> <b-badge variant="outline-primary" class="outline-badge-primary border-0 ml-2 mb-1">Admin</b-badge> </span></h4>
                            <p class="meta-time-date">{{ p.datecreation | formatDate }}</p>
                         
                          <div class="">
                            <h6 class="post-text">
                              {{ p.detailsP }}
                            </h6>
                          </div>
                          <div class="post-gallery-img col-md-12" v-if="p.imagePost != null">
                            <img :src=" p.imagePost" style="width: 400px; height: 200px" />
                          </div>
                          <div class="media-notation mb-5">
                            <a href="javascript:void(0);" class="mr-5"><likecomponent :userprofile="CurrentUserProfile.id" :userentreprise="CurrentUserEntreprise.id" :postid="p.id" /> </a>
                            <a href="javascript:void(0);" v-b-toggle="collapseComment(p.id)" class="mr-5"
                              ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1.28em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1792 1408">
                                <path
                                  fill="currentColor"
                                  d="M1408 512q0 139-94 257t-256.5 186.5T704 1024q-86 0-176-16q-124 88-278 128q-36 9-86 16h-3q-11 0-20.5-8t-11.5-21q-1-3-1-6.5t.5-6.5t2-6l2.5-5l3.5-5.5l4-5l4.5-5l4-4.5q5-6 23-25t26-29.5t22.5-29t25-38.5t20.5-44Q142 841 71 736T0 512q0-139 94-257T350.5 68.5T704 0t353.5 68.5T1314 255t94 257zm384 256q0 120-71 224.5T1526 1169q10 24 20.5 44t25 38.5t22.5 29t26 29.5t23 25q1 1 4 4.5t4.5 5t4 5t3.5 5.5l2.5 5l2 6l.5 6.5l-1 6.5q-3 14-13 22t-22 7q-50-7-86-16q-154-40-278-128q-90 16-176 16q-271 0-472-132q58 4 88 4q161 0 309-45t264-129q125-92 192-212t67-254q0-77-23-152q129 71 204 178t75 230z"
                                />
                              </svg>
                              {{ p.nbcomments }} Comments
                            </a>
                            <a href="javascript:void(0);" v-b-modal="modalAddComment(p.id)" class="mr-5"
                              ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 512 512">
                                <path
                                  fill="currentColor"
                                  d="M256 32C114.62 32 0 125.12 0 240c0 49.56 21.41 95 57 130.74C44.46 421.05 2.7 466 2.2 466.5A8 8 0 0 0 8 480c66.26 0 116-31.75 140.6-51.38A304.66 304.66 0 0 0 256 448c141.39 0 256-93.12 256-208S397.39 32 256 32zm96 232a8 8 0 0 1-8 8h-56v56a8 8 0 0 1-8 8h-48a8 8 0 0 1-8-8v-56h-56a8 8 0 0 1-8-8v-48a8 8 0 0 1 8-8h56v-56a8 8 0 0 1 8-8h48a8 8 0 0 1 8 8v56h56a8 8 0 0 1 8 8z"
                                />
                              </svg>
                              Add Comment
                            </a>
                          </div>
                          <b-modal :id="'modaladdcomment' + p.id" hide-footer title="Add Comment" title-tag="h4" modal-class="register-modal" footer-class="justify-content-center">
                            <form class="mt-0">
                              <div class="form-group">
                                <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24">
                                  <path
                                    fill="currentColor"
                                    d="m21.558 3.592l-1.15-1.15a1.49 1.49 0 0 0-2.12 0L13 7.731V11h3.27l5.288-5.288a1.49 1.49 0 0 0 0-2.12ZM15.579 9.45h-1.03V8.42L18 4.973l1.03 1.03Z"
                                  />
                                  <path fill="currentColor" d="M19 19H5V5h6V3H5a2.006 2.006 0 0 0-2 2v14a2.006 2.006 0 0 0 2 2h14a2.006 2.006 0 0 0 2-2v-6h-2Z" />
                                </svg>
                                <b-form-textarea
                                  type="text"
                                  class="mb-2"
                                  v-model="form.contentCom"
                                  :class="[is_submit_comment ? (form.contentCom && form.contentCom.length < 200 && form.contentCom.length > 15 ? 'is-valid' : 'is-invalid') : '']"
                                  placeholder="Enter your comment here"
                                ></b-form-textarea>
                                <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                                <b-form-invalid-feedback :class="{ 'd-block': is_submit_comment && !form.contentCom }">Please Enter content between 15 and 200 characters</b-form-invalid-feedback>
                              </div>
                              <b-button variant="primary" block class="mt-2 mb-2" @click="commentaire(p)">Submit</b-button>
                            </form>
                          </b-modal>
                          <b-collapse :id="'collapse-hd-statistics-' + p.id" accordion="helpdesk-accordion" class="mb-5 col-xl-12">
                            <span v-for="c in Comments" :key="c.id">
                              <span v-if="c.postCom == p.id">
                                <b-card-body>
                                  <span v-for="up in Userprofiles" :key="up.id">
                                    <span v-if="c.userprofileCom == up.id">
                                      <b-media>
                                        <template #aside>
                                          <router-link :to="'/profile/' + up.id" class="text-primary">
                                            <b-avatar :src=" up.imageU" class="avatar-title rounded-circl mr-4"> </b-avatar>
                                          </router-link>
                                          <p class="mt-1 mr-5">{{ c.contentCom }}</p>
                                          <div v-if="CurrentUserProfile.id == c.userprofileCom&& c.userprofileCom !=null|| CurrentUserEntreprise.id==c.userentrepriseCom &&c.userentrepriseCom!=null">
                                            <b-dropdown variant="icon-only" dropright toggle-tag="a" size="1em" class="mb-4 mr-2 ml-5 custom-dropdown float-right">
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
                                              <b-dropdown-item v-b-modal="modalModifComment(c.id)">Modify</b-dropdown-item>
                                              <b-dropdown-item @click="deleteComment(c)">Delete</b-dropdown-item>
                                            </b-dropdown>
                                            <b-modal
                                              :id="'modalModifComment' + c.id"
                                              hide-footer
                                              title="Modify Comment"
                                              title-tag="h4"
                                              modal-class="register-modal"
                                              footer-class="justify-content-center"
                                            >
                                              <form class="mt-0">
                                                <div class="form-group">
                                                  <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24">
                                                    <path
                                                      fill="currentColor"
                                                      d="m21.558 3.592l-1.15-1.15a1.49 1.49 0 0 0-2.12 0L13 7.731V11h3.27l5.288-5.288a1.49 1.49 0 0 0 0-2.12ZM15.579 9.45h-1.03V8.42L18 4.973l1.03 1.03Z"
                                                    />
                                                    <path fill="currentColor" d="M19 19H5V5h6V3H5a2.006 2.006 0 0 0-2 2v14a2.006 2.006 0 0 0 2 2h14a2.006 2.006 0 0 0 2-2v-6h-2Z" />
                                                  </svg>
                                                  <b-form-textarea
                                                    type="text"
                                                    class="mb-2"
                                                    :class="[is_submit_commentmodif ? (c.contentCom && c.contentCom.length < 200 && c.contentCom.length > 15 ? 'is-valid' : 'is-invalid') : '']"
                                                    v-model="c.contentCom"
                                                    placeholder="Modify your comment here"
                                                  ></b-form-textarea>
                                                  <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                                                  <b-form-invalid-feedback :class="{ 'd-block': is_submit_commentmodif && !c.contentCom }"
                                                    >Please Enter content between 15 and 200 characters</b-form-invalid-feedback
                                                  >
                                                </div>
                                                <b-button variant="primary" block class="mt-2 mb-2" @click="commentModif(c)">Modify</b-button>
                                              </form>
                                            </b-modal>
                                          </div>
                                        </template>
                                      </b-media>
                                    </span>
                                  </span>
                                  <span v-for="ue in Userentreprises" :key="ue.id">
                                    <span v-if="c.userentrepriseCom == ue.id">
                                      <b-media>
                                        <template #aside>
                                          <router-link :to="'/entreprisedetails/' + ue.id" class="text-primary">
                                            <b-avatar :src=" ue.imageE" class="avatar-title rounded-circl mr-4"> </b-avatar>
                                          </router-link>
                                          <p class="mt-1 mr-5">{{ c.contentCom }}</p>
                                          <div v-if="CurrentUserProfile.id == c.userprofileCom&& c.userprofileCom !=null|| CurrentUserEntreprise.id==c.userentrepriseCom &&c.userentrepriseCom!=null">
                                            <b-dropdown variant="icon-only" dropright toggle-tag="a" size="1em" class="mb-4 mr-2 ml-5 custom-dropdown float-right">
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
                                              <b-dropdown-item v-b-modal="modalModifComment(c.id)">Modify</b-dropdown-item>
                                              <b-dropdown-item @click="deleteComment(c)">Delete</b-dropdown-item>
                                            </b-dropdown>
                                            <b-modal
                                              :id="'modalModifComment' + c.id"
                                              hide-footer
                                              title="Modify Comment"
                                              title-tag="h4"
                                              modal-class="register-modal"
                                              footer-class="justify-content-center"
                                            >
                                              <form class="mt-0">
                                                <div class="form-group">
                                                  <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24">
                                                    <path
                                                      fill="currentColor"
                                                      d="m21.558 3.592l-1.15-1.15a1.49 1.49 0 0 0-2.12 0L13 7.731V11h3.27l5.288-5.288a1.49 1.49 0 0 0 0-2.12ZM15.579 9.45h-1.03V8.42L18 4.973l1.03 1.03Z"
                                                    />
                                                    <path fill="currentColor" d="M19 19H5V5h6V3H5a2.006 2.006 0 0 0-2 2v14a2.006 2.006 0 0 0 2 2h14a2.006 2.006 0 0 0 2-2v-6h-2Z" />
                                                  </svg>
                                                  <b-form-textarea
                                                    type="text"
                                                    class="mb-2"
                                                    :class="[is_submit_commentmodif ? (c.contentCom && c.contentCom.length < 200 && c.contentCom.length > 15 ? 'is-valid' : 'is-invalid') : '']"
                                                    v-model="c.contentCom"
                                                    placeholder="Modify your comment here"
                                                  ></b-form-textarea>
                                                  <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                                                  <b-form-invalid-feedback :class="{ 'd-block': is_submit_commentmodif && !c.contentCom }"
                                                    >Please Enter content between 15 and 200 characters</b-form-invalid-feedback
                                                  >
                                                </div>
                                                <b-button variant="primary" block class="mt-2 mb-2" @click="commentModif(c)">Modify</b-button>
                                              </form>
                                            </b-modal>
                                          </div>
                                        </template>
                                      </b-media>
                                    </span>
                                  </span>
                                </b-card-body>
                              </span>
                            </span>
                          </b-collapse>
                        </div>
                      </div>
                    </span>
                  </span>
                  <span v-for="ue in Userentreprises" :key="ue.id">
                    <span v-if="ue.id == p.userentreprisePost">
                      <div v-if="CurrentUserProfile.id == p.userprofilePost&& p.userprofilePost !=null|| CurrentUserEntreprise.id==p.userentreprisePost &&p.userentreprisePost!=null">
                        <b-dropdown variant="icon-only" dropleft toggle-tag="a" size="1em" class="mb-4 mr-5 custom-dropdown float-right">
                          <template #button-content>
                            <svg
                              xmlns="http://www.w3.org/2000/svg"
                              style="width: 25px; height: 25px"
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
                          <b-dropdown-item :href="'/group/' + group.id + '/updatepost/' + p.id">Modify</b-dropdown-item>
                          <b-dropdown-item @click="deletePost(p.id)">Delete</b-dropdown-item>
                        </b-dropdown>
                      </div>
                      <div class="timeline-post-content">
                        <router-link :to="'/entreprisedetails/' + ue.id" class="text-primary">
                        <div class="user-profile">
                          <img :src=" ue.imageE" img-top alt="" />
                        </div>
                        </router-link>
                        <div class="">
                          
                            <h4>{{ ue.nameE }}<span v-if="ue.id==group.userentrepriseG"> <b-badge variant="outline-primary" class="outline-badge-primary border-0 ml-2 mb-1">Admin</b-badge> </span></h4>
                            <p class="meta-time-date">{{ p.datecreation | formatDate }}</p>
                         
                          <div class="">
                            <h6 class="post-text">
                              {{ p.detailsP }}
                            </h6>
                          </div>
                          <div class="post-gallery-img col-md-12" v-if="p.imagePost != null">
                            <img :src=" p.imagePost" style="width: 400px; height: 200px" />
                          </div>
                          <div class="media-notation mb-5">
                            <a href="javascript:void(0);" class="mr-5"><likecomponent :userprofile="CurrentUserProfile.id" :userentreprise="CurrentUserEntreprise.id" :postid="p.id" /> </a>
                            <a href="javascript:void(0);" v-b-toggle="collapseComment(p.id)" class="mr-5"
                              ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1.28em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1792 1408">
                                <path
                                  fill="currentColor"
                                  d="M1408 512q0 139-94 257t-256.5 186.5T704 1024q-86 0-176-16q-124 88-278 128q-36 9-86 16h-3q-11 0-20.5-8t-11.5-21q-1-3-1-6.5t.5-6.5t2-6l2.5-5l3.5-5.5l4-5l4.5-5l4-4.5q5-6 23-25t26-29.5t22.5-29t25-38.5t20.5-44Q142 841 71 736T0 512q0-139 94-257T350.5 68.5T704 0t353.5 68.5T1314 255t94 257zm384 256q0 120-71 224.5T1526 1169q10 24 20.5 44t25 38.5t22.5 29t26 29.5t23 25q1 1 4 4.5t4.5 5t4 5t3.5 5.5l2.5 5l2 6l.5 6.5l-1 6.5q-3 14-13 22t-22 7q-50-7-86-16q-154-40-278-128q-90 16-176 16q-271 0-472-132q58 4 88 4q161 0 309-45t264-129q125-92 192-212t67-254q0-77-23-152q129 71 204 178t75 230z"
                                />
                              </svg>
                              {{ p.nbcomments }} Comments
                            </a>
                            <a href="javascript:void(0);" v-b-modal="modalAddComment(p.id)" class="mr-5"
                              ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 512 512">
                                <path
                                  fill="currentColor"
                                  d="M256 32C114.62 32 0 125.12 0 240c0 49.56 21.41 95 57 130.74C44.46 421.05 2.7 466 2.2 466.5A8 8 0 0 0 8 480c66.26 0 116-31.75 140.6-51.38A304.66 304.66 0 0 0 256 448c141.39 0 256-93.12 256-208S397.39 32 256 32zm96 232a8 8 0 0 1-8 8h-56v56a8 8 0 0 1-8 8h-48a8 8 0 0 1-8-8v-56h-56a8 8 0 0 1-8-8v-48a8 8 0 0 1 8-8h56v-56a8 8 0 0 1 8-8h48a8 8 0 0 1 8 8v56h56a8 8 0 0 1 8 8z"
                                />
                              </svg>
                              Add Comment
                            </a>
                          </div>
                          <b-modal :id="'modaladdcomment' + p.id" hide-footer title="Add Comment" title-tag="h4" modal-class="register-modal" footer-class="justify-content-center">
                            <form class="mt-0">
                              <div class="form-group">
                                <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24">
                                  <path
                                    fill="currentColor"
                                    d="m21.558 3.592l-1.15-1.15a1.49 1.49 0 0 0-2.12 0L13 7.731V11h3.27l5.288-5.288a1.49 1.49 0 0 0 0-2.12ZM15.579 9.45h-1.03V8.42L18 4.973l1.03 1.03Z"
                                  />
                                  <path fill="currentColor" d="M19 19H5V5h6V3H5a2.006 2.006 0 0 0-2 2v14a2.006 2.006 0 0 0 2 2h14a2.006 2.006 0 0 0 2-2v-6h-2Z" />
                                </svg>
                                <b-form-textarea
                                  type="text"
                                  class="mb-2"
                                  v-model="form.contentCom"
                                  :class="[is_submit_comment ? (form.contentCom && form.contentCom.length < 200 && form.contentCom.length > 15 ? 'is-valid' : 'is-invalid') : '']"
                                  placeholder="Enter your comment here"
                                ></b-form-textarea>
                                <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                                <b-form-invalid-feedback :class="{ 'd-block': is_submit_comment && !form.contentCom }">Please Enter content between 15 and 200 characters</b-form-invalid-feedback>
                              </div>
                              <b-button variant="primary" block class="mt-2 mb-2" @click="commentaire(p)">Submit</b-button>
                            </form>
                          </b-modal>
                          <b-collapse :id="'collapse-hd-statistics-' + p.id" accordion="helpdesk-accordion" class="mb-5 col-xl-12">
                            <span v-for="c in Comments" :key="c.id">
                              <span v-if="c.postCom == p.id">
                                <b-card-body>
                                  <span v-for="up in Userprofiles" :key="up.id">
                                    <span v-if="c.userprofileCom == up.id">
                                      <b-media>
                                        <template #aside>
                                          <router-link :to="'/profile/' + up.id" class="text-primary">
                                            <b-avatar :src=" up.imageU" class="avatar-title rounded-circl mr-4"> </b-avatar>
                                          </router-link>
                                          <p class="mt-1 mr-5">{{ c.contentCom }}</p>
                                          <div v-if="CurrentUserProfile.id == c.userprofileCom&& c.userprofileCom !=null|| CurrentUserEntreprise.id==c.userentrepriseCom &&c.userentrepriseCom!=null">
                                            <b-dropdown variant="icon-only" dropright toggle-tag="a" size="1em" class="mb-4 mr-2 ml-5 custom-dropdown float-right">
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
                                              <b-dropdown-item v-b-modal="modalModifComment(c.id)">Modify</b-dropdown-item>
                                              <b-dropdown-item @click="deleteComment(c)">Delete</b-dropdown-item>
                                            </b-dropdown>
                                            <b-modal
                                              :id="'modalModifComment' + c.id"
                                              hide-footer
                                              title="Modify Comment"
                                              title-tag="h4"
                                              modal-class="register-modal"
                                              footer-class="justify-content-center"
                                            >
                                              <form class="mt-0">
                                                <div class="form-group">
                                                  <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24">
                                                    <path
                                                      fill="currentColor"
                                                      d="m21.558 3.592l-1.15-1.15a1.49 1.49 0 0 0-2.12 0L13 7.731V11h3.27l5.288-5.288a1.49 1.49 0 0 0 0-2.12ZM15.579 9.45h-1.03V8.42L18 4.973l1.03 1.03Z"
                                                    />
                                                    <path fill="currentColor" d="M19 19H5V5h6V3H5a2.006 2.006 0 0 0-2 2v14a2.006 2.006 0 0 0 2 2h14a2.006 2.006 0 0 0 2-2v-6h-2Z" />
                                                  </svg>
                                                  <b-form-textarea
                                                    type="text"
                                                    class="mb-2"
                                                    :class="[is_submit_commentmodif ? (c.contentCom && c.contentCom.length < 200 && c.contentCom.length > 15 ? 'is-valid' : 'is-invalid') : '']"
                                                    v-model="c.contentCom"
                                                    placeholder="Modify your comment here"
                                                  ></b-form-textarea>
                                                  <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                                                  <b-form-invalid-feedback :class="{ 'd-block': is_submit_commentmodif && !c.contentCom }"
                                                    >Please Enter content between 15 and 200 characters</b-form-invalid-feedback
                                                  >
                                                </div>
                                                <b-button variant="primary" block class="mt-2 mb-2" @click="commentModif(c)">Modify</b-button>
                                              </form>
                                            </b-modal>
                                          </div>
                                        </template>
                                      </b-media>
                                    </span>
                                  </span>
                                  <span v-for="ue in Userentreprises" :key="ue.id">
                                    <span v-if="c.userentrepriseCom == ue.id">
                                      <b-media>
                                        <template #aside>
                                          <router-link :to="'/entreprisedetails/' + ue.id" class="text-primary">
                                            <b-avatar :src=" ue.imageE" class="avatar-title rounded-circl mr-4"> </b-avatar>
                                          </router-link>
                                          <p class="mt-1 mr-5">{{ c.contentCom }}</p>
                                          <div v-if="CurrentUserProfile.id == c.userprofileCom&& c.userprofileCom !=null|| CurrentUserEntreprise.id==c.userentrepriseCom &&c.userentrepriseCom!=null">
                                            <b-dropdown variant="icon-only" dropright toggle-tag="a" size="1em" class="mb-4 mr-2 ml-5 custom-dropdown float-right">
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
                                              <b-dropdown-item v-b-modal="modalModifComment(c.id)">Modify</b-dropdown-item>
                                              <b-dropdown-item @click="deleteComment(c)">Delete</b-dropdown-item>
                                            </b-dropdown>
                                            <b-modal
                                              :id="'modalModifComment' + c.id"
                                              hide-footer
                                              title="Modify Comment"
                                              title-tag="h4"
                                              modal-class="register-modal"
                                              footer-class="justify-content-center"
                                            >
                                              <form class="mt-0">
                                                <div class="form-group">
                                                  <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24">
                                                    <path
                                                      fill="currentColor"
                                                      d="m21.558 3.592l-1.15-1.15a1.49 1.49 0 0 0-2.12 0L13 7.731V11h3.27l5.288-5.288a1.49 1.49 0 0 0 0-2.12ZM15.579 9.45h-1.03V8.42L18 4.973l1.03 1.03Z"
                                                    />
                                                    <path fill="currentColor" d="M19 19H5V5h6V3H5a2.006 2.006 0 0 0-2 2v14a2.006 2.006 0 0 0 2 2h14a2.006 2.006 0 0 0 2-2v-6h-2Z" />
                                                  </svg>
                                                  <b-form-textarea
                                                    type="text"
                                                    class="mb-2"
                                                    :class="[is_submit_commentmodif ? (c.contentCom && c.contentCom.length < 200 && c.contentCom.length > 15 ? 'is-valid' : 'is-invalid') : '']"
                                                    v-model="c.contentCom"
                                                    placeholder="Modify your comment here"
                                                  ></b-form-textarea>
                                                  <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                                                  <b-form-invalid-feedback :class="{ 'd-block': is_submit_commentmodif && !c.contentCom }"
                                                    >Please Enter content between 15 and 200 characters</b-form-invalid-feedback
                                                  >
                                                </div>
                                                <b-button variant="primary" block class="mt-2 mb-2" @click="commentModif(c)">Modify</b-button>
                                              </form>
                                            </b-modal>
                                          </div>
                                        </template>
                                      </b-media>
                                    </span>
                                  </span>
                                </b-card-body>
                              </span>
                            </span>
                          </b-collapse>
                        </div>
                      </div>
                    </span>
                  </span>
                </span>
                
              </span>
              <span v-if="existmember == false">
                    <h4>You cannot see the posts </h4>
                </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import '@/assets/sass/scrollspyNav.scss';
import '@/assets/sass/components/timeline/custom-timeline.scss';
import { mapGetters, mapActions } from 'vuex';
import likecomponent from './like-component.vue';
import axios from 'axios';
export default {
  metaInfo: { title: 'Groups' },
  components: {
    likecomponent,
  },
  data() {
    return {
      group: [],
      CurrentUser: [],
      CurrentUserProfile: [],
      CurrentUserEntreprise: [],
      postdetails: [],
      members: [],
      existmember: false,
      requested: false,
      acceptedposts:0,
      form: {
        contentCom: '',
      },
      is_submit_comment: false,
      is_submit_commentmodif: false,
    };
  },
  created: function () {
    this.GetGroups();
    this.GetGroupposts();
    this.GetUserprofiles();
    this.GetGroupcomments();
    this.GetGroupmembers();
    this.GetUsers();
    this.GetUserentreprises();

    axios.get('/group/group-detail/' + this.$route.params.id + '/').then((response) => {
      this.group = response.data;

      for (let u in this.Users) {
        if (this.Users[u].username == this.User) {
          this.CurrentUser = this.Users[u];
        }
      }
      for (let u in this.Userprofiles) {
        if (this.Userprofiles[u].userU == this.CurrentUser.id) {
          this.CurrentUserProfile = this.Userprofiles[u];
        }
      }
      for (let ue in this.Userentreprises) {
        if (this.Userentreprises[ue].userE == this.CurrentUser.id) {
          this.CurrentUserEntreprise = this.Userentreprises[ue];
        }
      }
      for (let m in this.Members) {
        if (this.Members[m].groupMem == this.group.id && this.Members[m].accepted == true) {
          this.members.push(this.Members[m]);
        }
        if (((this.Members[m].userprofileMem == this.CurrentUserProfile.id && this.CurrentUserProfile.id!=null) || (this.Members[m].userentrepriseMem == this.CurrentUserEntreprise.id && this.CurrentUserEntreprise.id!=null))  && this.Members[m].groupMem == this.group.id && this.Members[m].accepted == true) {
          this.existmember = true;
        }
      }
      for (let m in this.Members) {
        if (this.Members[m].groupMem == this.group.id && this.Members[m].accepted == true) {
          this.members.push(this.Members[m]);
        }
        if (this.Members[m].userprofileMem == this.CurrentUserProfile.id && this.Members[m].groupMem == this.group.id && this.Members[m].accepted == false) {
          this.requested = true;
        }
      }

      for(let ac in this.GroupPost)
      {
        if(this.GroupPost[ac].accepted==true && this.GroupPost[ac].groupPost==this.group.id)
        {
          this.acceptedposts++
        }
      }
    });
  },
  mounted() {},
  computed: {
    ...mapGetters({
      Groups: 'StateGroups',
      GroupPost: 'StateGroupposts',
      Userprofiles: 'StateUserprofiles',
      Userentreprises: 'StateUserentreprises',
      Comments: 'StateGroupcomments',
      Members: 'StateGroupmembers',
      User: 'StateUser',
      Users: 'StateUsers',
    }),
  },
  methods: {
    ...mapActions(['GetGroups', 'GetUserentreprises', 'GetGroupposts', 'GetUsers', 'GetUserprofiles', 'CreateGroupcomment', 'GetGroupcomments', 'GetGroupmembers', 'CreateGroupmember']),

    collapseComment(i) {
      return 'collapse-hd-statistics-' + i;
    },
    modalAddComment(id) {
      return 'modaladdcomment' + id;
    },
    Join() {
      if(this.CurrentUser.is_superuser)
      {
      this.CreateGroupmember({ userprofileMem: this.CurrentUserProfile.id, groupMem: this.group.id , userentrepriseMem:this.CurrentUserEntreprise.id,accepted:true });
      axios.put('/group/group-update/' + this.$route.params.id + '/', { nbmembers: this.group.nbmembers+1 });
      }
      else
      {
      this.CreateGroupmember({ userprofileMem: this.CurrentUserProfile.id, groupMem: this.group.id , userentrepriseMem:this.CurrentUserEntreprise.id });
      this.$swal({
        icon: 'success',
        title: 'Requested!',
        text: 'Please wait for admin to accept your request!',
        padding: '2em',
      });
      }
      this.$router.go();
    },
    deletePost(id) {
      this.$swal({
        icon: 'warning',
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        showCancelButton: true,
        confirmButtonText: 'Delete',
        padding: '2em',
      }).then((result) => {
        if (result.value) {
          axios.delete(`/postgroup/postgroup-delete/${id}/`);
          axios.put('/group/group-update/' + this.group.id + '/', { nbposts: this.group.nbposts -=1});
          this.$swal('Deleted!', 'Your post has been deleted.', 'success');
          this.$router.go();
        }
      });
    },
    async commentModif(c) {
      try {
        this.form.contentCom = c.contentCom;
        this.is_submit_commentmodif = true;
        if (this.form.contentCom && this.form.contentCom.length < 200 && this.form.contentCom.length > 15) {
          this.$bvModal.hide('modalModifComment' + c.id);

          await axios.put('/groupcomment/groupcomment-update/' + c.id + '/', { contentCom: this.form.contentCom });
          this.is_submit_commentmodif = false;
          this.form.contentCom = '';
          this.$swal('Good Job!', 'Your comment has been updated successfuly !', 'success');
        }
      } catch (error) {
        throw 'Il ya un errora !';
      }
    },
    deleteComment(c) {
      let postdetails = [];
      this.$swal({
        icon: 'warning',
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        showCancelButton: true,
        confirmButtonText: 'Delete',
        padding: '2em',
      }).then((result) => {
        if (result.value) {
          axios.get('/postgroup/postgroup-detail/' + c.postCom + '/').then((response) => {
            postdetails = response.data;
            console.log(postdetails);
            axios.put('/postgroup/postgroup-update/' + c.postCom + '/', {
              nbcomments: (postdetails.nbcomments -= 1),
            });
          });
          axios.delete(`http://127.0.0.1:8000/groupcomment/groupcomment-delete/${c.id}/`);
          this.$swal('Deleted!', 'Your comment has been deleted.', 'success');
          this.$router.go();
        }
      });
    },
    modalModifComment(id) {
      return 'modalModifComment' + id;
    },
    async commentaire(post) {
      this.is_submit_comment = true;
      if (this.form.contentCom && this.form.contentCom.length < 200 && this.form.contentCom.length > 15) {
        this.$bvModal.hide('modaladdcomment' + post.id);
        axios.get('/postgroup/postgroup-detail/' + post.id + '/').then((response) => {
          this.postdetails = response.data;
        });
        try {
          await this.CreateGroupcomment({ contentCom: this.form.contentCom, userprofileCom: this.CurrentUserProfile.id,userentrepriseCom: this.CurrentUserEntreprise.id, postCom: post.id });
       
          await axios.put('/postgroup/postgroup-update/' + post.id + '/', {
            nbcomments: (this.postdetails.nbcomments += 1),
          });
          this.GetGroupposts();
          this.form.contentCom = '';
          this.is_submit_comment = false;
          this.$swal('Good Job!', 'Your comment has been created successfuly !', 'success');
        } catch (error) {
          throw 'Il ya un errora !';
        }
      }
    },
  },
};
</script>
<style scoped>
</style>