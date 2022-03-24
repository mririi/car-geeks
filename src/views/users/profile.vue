<template>
  <div class="layout-px-spacing">
    <portal to="breadcrumb">
      <ul class="navbar-nav flex-row">
        <li>
          <div class="page-header">
            <nav class="breadcrumb-one" aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item active" aria-current="page"><span>Profile</span></li>
              </ol>
            </nav>
          </div>
        </li>
      </ul>
    </portal>

    <div class="row layout-spacing">
      <!-- Content -->
      <div class="col-xl-4 col-lg-6 col-md-5 col-sm-12 layout-top-spacing">
        <div class="user-profile layout-spacing">
          <div class="panel">
            <div class="panel-body">
              <div class="d-flex justify-content-between">
                <h3 class="">Profile</h3>
                <router-link :to="'/profile-edit/' + userprofile.id" v-if="CurrentUserProfile.id == userprofile.id || CurrentUser.is_superuser==true" class="mt-2 edit-profile">
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
                    class="feather feather-edit-3"
                  >
                    <path d="M12 20h9"></path>
                    <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path>
                  </svg>
                </router-link>
              </div>
              <div class="text-center user-info">
                <img :src="'http://127.0.0.1:8000' + userprofile.imageU" width="150" height="150" alt="avatar" />
                <p class="">{{ userprofile.firstname }} {{ userprofile.lastname }}</p>
              </div>
              <div class="user-info-list">
                <div class="">
                  <ul class="contacts-block list-unstyled">
                    <li class="contacts-block__item">
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
                        class="feather feather-calendar"
                      >
                        <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                        <line x1="16" y1="2" x2="16" y2="6"></line>
                        <line x1="8" y1="2" x2="8" y2="6"></line>
                        <line x1="3" y1="10" x2="21" y2="10"></line></svg
                      >{{ userprofile.dateinscrit | formatDate }}
                    </li>
                    <li class="contacts-block__item">
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
                        class="feather feather-map-pin"
                      >
                        <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                        <circle cx="12" cy="10" r="3"></circle></svg
                      >{{ userprofile.country }}
                    </li>
                    <li class="contacts-block__item">
                      <div v-for="user in Users" :key="user.id">
                        <div v-if="user.id == userprofile.userU">
                          <a :href="'mailto:' + user.email" target="_blank"
                            ><svg
                              xmlns="http://www.w3.org/2000/svg"
                              width="24"
                              height="24"
                              viewBox="0 0 24 24"
                              fill="none"
                              stroke="currentColor"
                              stroke-width="2"
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              class="feather feather-mail"
                            >
                              <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                              <polyline points="22,6 12,13 2,6"></polyline></svg
                            >{{ user.email }}</a
                          >
                        </div>
                      </div>
                    </li>
                    <li class="contacts-block__item">
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
                        class="feather feather-phone"
                      >
                        <path
                          d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"
                        ></path>
                      </svg>
                      {{ userprofile.tel }}
                    </li>
                  </ul>
                </div>
                <div class="education ml-4 col-lg-8">
                  <span class="ml-4">Rate this profile</span>
                  <span v-if="CurrentUserProfile.id != userprofile.id">
                  <span v-if="isLoggedIn && existprofile == true">
                    <span v-b-modal.Rating>
                      <b-form-rating id="rating" v-model="average" color="primary" show-value show-value-max readonly size="lg" class="mb-2 bg-transparent border-0"> </b-form-rating>
                    </span>
                  </span>
                   <span v-else-if="existentreprise==true">
                    <span @click="showAlert1()" >
                      <b-form-rating id="rating" v-model="average" variant="warning" readonly size="lg" class="mb-2 bg-transparent border-0"> </b-form-rating>
                    </span>
                  </span>
                  <span v-else>
                    <a href="/auth/login">
                      <b-form-rating id="rating" v-model="average" vcolor="primary" show-value show-value-max readonly size="lg" class="mb-2 bg-transparent border-0"> </b-form-rating>
                    </a>
                  </span>
                  </span>
                  <span v-else>
                    <span @click="showAlert()">
                      <b-form-rating id="rating" v-model="average" color="primary" show-value show-value-max readonly size="lg" class="mb-2 bg-transparent border-0"> </b-form-rating>
                    </span>
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <b-modal id="Rating" :title="'Rate ' + userprofile.firstname + ' ' + userprofile.lastname" centered>
        <b-form-rating id="rating" v-model="nbEval" precision="2" show-value-max show-value color="primary" size="lg" class="mb-2 bg-transparent border-0"> </b-form-rating>
        <template #modal-footer>
          <b-button variant="primary" @click="Rating()">Submit your rating</b-button>
        </template>
      </b-modal>
      <b-modal id="preference" title="Modify your preferences" centered>
        <h5>Question Category:</h5>
                  <b-select v-model="form.categoryPref" value="Default select">
                    <b-select-option value="0">Select Category</b-select-option>
                    <b-select-option v-for="c in Questioncategories" :key="c.id" :value="c.id">{{ c.typeC }}</b-select-option>
                  </b-select>
        <template #modal-footer>
          <b-button variant="primary" @click="preferencesUpdate()">Update</b-button>
        </template>
      </b-modal>
      <div class="col-xl-8 col-lg-6 col-md-7 col-sm-12 layout-top-spacing">
        <div class="skills layout-spacing">
          <div class="panel">
            <div class="panel-body">
              <h3 class="">Badges</h3>
              <div class="float-right"><h1><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 64 64"><path fill="#428bc1" d="M46.1 2L34.8 18.9h5.6L53 2z"/><path fill="#e8e8e8" d="M40.4 2L29.2 18.9h5.6L46.1 2z"/><path fill="#ed4c5c" d="M34.8 2L23.6 18.9h5.6L40.4 2z"/><g fill="#d3976e"><circle cx="32" cy="41.4" r="20.6"/><path d="M21.7 15.1c-.5 0-.9.4-.9.9v8.4c0 .5.4.9.9.9h20.6c.5 0 .9-.4.9-.9V16c0-.5-.4-.9-.9-.9H21.7m19.7 6.6c0 .5-.4.9-.9.9H23.6c-.5 0-.9-.4-.9-.9v-3.8c0-.5.4-.9.9-.9h16.9c.5 0 .9.4.9.9v3.8"/></g><path fill="#3e4347" d="M14.3 43.8c0-11.2 8.6-20.3 19.6-21.1c-.5 0-1.1-.1-1.6-.1c-10.5 0-19 8.5-19 19.1c0 3.1.8 6.1 2.1 8.7c-.7-2.1-1.1-4.3-1.1-6.6" opacity=".5"/><path fill="#fff" d="M39.9 57.3C49.2 51.1 52 39 46.6 29.6l.9 1.2c5.8 8.6 3.4 20.3-5.3 26.2c-2.6 1.8-5.5 2.8-8.4 3.1c2.2-.6 4.2-1.5 6.1-2.8" opacity=".33"/><path fill="#ed4c5c" d="M23.6 18.9h5.6L17.9 2H11z"/><path fill="#e8e8e8" d="M29.2 18.9h5.6L23.6 2h-5.7z"/><path fill="#3e4347" d="M32.9 4.8L30.1 9l6.6 9.9h3.7l1-1.4z" opacity=".5"/><path fill="#428bc1" d="M34.8 18.9h5.6L29.2 2h-5.6z"/><path fill="#3e4347" d="M31.5 31.5c-2.1 0-3.8 1.7-3.8 3.7H25c0 .3-.1.6-.1.9h3.8c0-2.1 1.7-3.8 3.8-3.8c.8 0 1.5.3 2.1.7c-.7-.8-1.8-1.5-3.1-1.5m5.9 10.3c1.6-1.4 2.6-3.4 2.6-5.6c0-2.3-1-4.4-2.7-5.8c1.1 1.3 1.8 3 1.8 4.8c0 2.2-1 4.3-2.6 5.6c1.6 1.4 2.6 3.4 2.6 5.6c0 4.1-3.4 7.5-7.5 7.5c-1.8 0-3.5-.7-4.8-1.8c1.4 1.6 3.4 2.7 5.8 2.7c4.1 0 7.5-3.4 7.5-7.5c-.1-2.1-1.1-4.1-2.7-5.5" opacity=".5"/><path fill="#fff" d="M32.5 28.7c1.8 0 3.5.7 4.8 1.8c-1.4-1.6-3.4-2.7-5.8-2.7c-4.1 0-7.5 3.4-7.5 7.5h1c.5-3.7 3.6-6.6 7.5-6.6m3.7 7.5c0-1.3-.6-2.4-1.6-3.1c.4.6.7 1.3.7 2.1c0 2.1-1.7 3.8-3.8 3.8v3.8c.3 0 .6.1.9.1V40c2.1 0 3.8-1.7 3.8-3.8m-3.7 15c2.1 0 3.8-1.7 3.8-3.8c0-1.3-.6-2.4-1.6-3.1c.4.6.7 1.3.7 2.1c0 2.1-1.7 3.8-3.8 3.8c-.8 0-1.5-.3-2.1-.7c.6 1.1 1.7 1.7 3 1.7m-4.6-3.7c-.1-.3-.1-.6-.1-.9H24c0 2.3 1 4.4 2.7 5.8c-1.1-1.3-1.8-3-1.8-4.8l3-.1" opacity=".33"/></svg></h1></div>
                <p v-if="userprofile.nbquestions<10" class="">{{10-userprofile.nbquestions}} questions left</p>
              <b-progress variant="primary" :min="0" :max="10" show-progress class="br-30">
                <b-progress-bar :value="userprofile.nbquestions" :label-html="`<div class='progress-title'><span>Bronze</span><span>`+this.userprofile.nbquestions*100/10+`%</span></div>`"></b-progress-bar>
              
              </b-progress>
                            <div class="float-right"><h1><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 64 64"><path fill="#428bc1" d="M46.1 2L34.8 18.9h5.6L53 2z"/><path fill="#e8e8e8" d="M40.4 2L29.2 18.9h5.6L46.1 2z"/><path fill="#ed4c5c" d="M34.8 2L23.6 18.9h5.6L40.4 2z"/><g fill="#b2c1c0"><circle cx="32" cy="41.4" r="20.6"/><path d="M21.7 15.1c-.5 0-.9.4-.9.9v8.4c0 .5.4.9.9.9h20.6c.5 0 .9-.4.9-.9V16c0-.5-.4-.9-.9-.9H21.7m19.7 6.6c0 .5-.4.9-.9.9H23.6c-.5 0-.9-.4-.9-.9v-3.8c0-.5.4-.9.9-.9h16.9c.5 0 .9.4.9.9v3.8"/></g><path fill="#3e4347" d="M14.3 43.8c0-11.2 8.6-20.3 19.6-21.1c-.5 0-1.1-.1-1.6-.1c-10.5 0-19 8.5-19 19.1c0 3.1.8 6.1 2.1 8.7c-.7-2.1-1.1-4.3-1.1-6.6" opacity=".5"/><path fill="#fff" d="M39.9 57.3C49.2 51.1 52 39 46.6 29.6c.3.4.6.8.9 1.3c5.8 8.6 3.4 20.3-5.3 26.2c-2.6 1.8-5.5 2.8-8.4 3.1c2.2-.7 4.2-1.6 6.1-2.9" opacity=".33"/><path fill="#ed4c5c" d="M23.6 18.9h5.6L17.9 2H11z"/><path fill="#e8e8e8" d="M29.2 18.9h5.6L23.6 2h-5.7z"/><path fill="#3e4347" d="M32.9 4.8L30.1 9l6.6 9.9h3.7l1-1.4z" opacity=".5"/><path fill="#428bc1" d="M34.8 18.9h5.6L29.2 2h-5.6z"/><path fill="#3e4347" d="M31.5 31.5c-2.1 0-3.8 1.7-3.8 3.7H25c0 .3-.1.6-.1.9h3.8c0-2.1 1.7-3.8 3.8-3.8c.8 0 1.5.3 2.1.7c-.7-.8-1.8-1.5-3.1-1.5M39 54H25v1h15v-3.8h-1zm-7.5-11.2c-2.1 0-3.8 1.7-3.8 3.8v3.8h.9v-2.8c0-2.1 1.7-3.8 3.8-3.8c4.1 0 7.5-3.4 7.5-7.5c0-2.3-1-4.4-2.7-5.8c1.1 1.3 1.8 3 1.8 4.8c0 4.1-3.3 7.5-7.5 7.5" opacity=".5"/><path fill="#fff" d="M28.7 50.3H39v.9H28.7zM32.5 40c2.1 0 3.8-1.7 3.8-3.8c0-1.3-.6-2.4-1.6-3.1c.4.6.7 1.3.7 2.1c0 2.1-1.7 3.8-3.8 3.8c-4.1 0-7.5 3.4-7.5 7.5V54h.9v-6.6c0-4.1 3.3-7.4 7.5-7.4m0-11.3c1.8 0 3.5.7 4.8 1.8c-1.4-1.6-3.4-2.7-5.8-2.7c-4.1 0-7.5 3.4-7.5 7.5h1c.5-3.7 3.6-6.6 7.5-6.6" opacity=".33"/></svg></h1></div>

              <p v-if="userprofile.nbquestions<10" class="">{{20-userprofile.nbquestions}} questions left</p>
              <b-progress variant="primary" :min="10" :max="20" show-progress class="br-30">
                <b-progress-bar :value="userprofile.nbquestions" :label-html="`<div class='progress-title'><span>Silver</span><span>`+this.userprofile.nbquestions*100/20+`%</span></div>`"></b-progress-bar>
              </b-progress>
              <div class="float-right"><h1><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 64 64"><path fill="#428bc1" d="M46.1 2L34.8 18.9h5.6L53 2z"/><path fill="#e8e8e8" d="M40.4 2L29.2 18.9h5.6L46.1 2z"/><path fill="#ed4c5c" d="M34.8 2L23.6 18.9h5.6L40.4 2z"/><g fill="#ffce31"><circle cx="32" cy="41.4" r="20.6"/><path d="M21.7 15.1c-.5 0-.9.4-.9.9v8.4c0 .5.4.9.9.9h20.6c.5 0 .9-.4.9-.9V16c0-.5-.4-.9-.9-.9H21.7m19.7 6.6c0 .5-.4.9-.9.9H23.6c-.5 0-.9-.4-.9-.9v-3.8c0-.5.4-.9.9-.9h16.9c.5 0 .9.4.9.9v3.8"/></g><path fill="#89664c" d="M14.3 43.8c0-11.2 8.6-20.3 19.6-21.1c-.5 0-1.1-.1-1.6-.1c-10.5 0-19 8.5-19 19.1c0 3.1.8 6.1 2.1 8.7c-.7-2.1-1.1-4.3-1.1-6.6" opacity=".5"/><path fill="#fff" d="M39.9 57.3C49.2 51.1 52 39 46.6 29.6l.9 1.2c5.8 8.6 3.4 20.3-5.3 26.2c-2.6 1.8-5.5 2.8-8.4 3.1c2.2-.6 4.2-1.5 6.1-2.8" opacity=".33"/><path fill="#ed4c5c" d="M23.6 18.9h5.6L17.9 2H11z"/><path fill="#e8e8e8" d="M29.2 18.9h5.6L23.6 2h-5.7z"/><path fill="#3e4347" d="M32.9 4.8L30.1 9l6.6 9.9h3.7l1-1.4z" opacity=".5"/><path fill="#428bc1" d="M34.8 18.9h5.6L29.2 2h-5.6z"/><path fill="#89664c" d="M26.8 35.2v1c1 0 1.9-.2 2.8-.6v-1.4c-.8.6-1.7.9-2.8 1m6.6-6.5h.9v21.6h-.9zm3.8 22.5V54H26.8v1h11.3v-3.8z" opacity=".5"/><path fill="#fff" d="M34.3 50.3h2.8v.9h-2.8zm-3.7-21.6h2.8v-.9h-3.8c0 2.1-1.7 3.8-3.8 3.8v3.7c.3 0 .6 0 .9-.1v-2.8c2.2.1 3.9-1.6 3.9-3.7m0 22.5v-16c-.3.2-.6.3-.9.5v14.6h-3.8V54h.9v-2.8h3.8" opacity=".33"/></svg></h1></div>
              <p v-if="userprofile.nbquestions<10" class="">{{30-userprofile.nbquestions}} questions left</p>
              <b-progress variant="primary" :min="20" :max="30" show-progress class="br-30">
                <b-progress-bar :value="userprofile.nbquestions" :label-html="`<div class='progress-title'><span>Gold</span><span>`+this.userprofile.nbquestions*100/30+`%</span></div>`"></b-progress-bar>
              </b-progress>
            </div>
          </div>
        </div>

        <div class="bio layout-spacing" v-if="userprofile.bio.length != 0">
          <div class="panel">
            <div class="panel-body">
              <h3 class="">Bio</h3>
              <p>
                {{ userprofile.bio }}
              </p>
            </div>
          </div>
        </div>
        <div class="education layout-spacing mt-4">
          <div class="panel">
            <div class="panel-body">
              <h3 class="">Preferences</h3>
              <div class="timeline-alter">
                <div v-for="p in Preferences" :key="p.id">
                  <div v-if="p.userprofilePref==userprofile.id">
                    <div v-for="q in Questioncategories" :key="q.id">
                      <div v-if="q.id==p.categoryPref">
                       
                          <p>Prefered Question Category : {{q.typeC}}</p>
                          <div v-if="CurrentUserProfile.id == userprofile.id"> 
                        <b-button variant="warning" v-b-modal.preference>Modify</b-button>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12 layout-spacing">
      <div class="widget widget-recent-orders">
        <div class="widget-heading">
          <h5>Related Profile</h5>
          <div class="row mr-1 float-right">
            <div class="col-lg-12 col-md-12 col-sm-12 filtered-list-search-live mx-auto">
              <b-form class="form-inline my-2 my-lg-0 justify-content-center" @submit.prevent="search">
                <div class="w-100">
                  <b-input v-model="search" class="w-100 product-search br-25" placeholder="Search Profiles" @keyup="search"></b-input>
                </div>
              </b-form>
            </div>
          </div>
        </div>
        <div class="widget-content">
          <b-table-simple responsive>
            <b-thead>
              <b-tr>
                <b-th><div class="th-content">User</div></b-th>
                <b-th><div class="th-content">Email</div></b-th>
                <b-th><div class="th-content">Phone</div></b-th>
                <b-th><div class="th-content th-heading">Country</div></b-th>
                <b-th><div class="th-content">Questions number</div></b-th>
              </b-tr>
            </b-thead>

            <b-tbody>
              <b-tr v-for="u in filteredList" :key="u.id">
                <b-td
                  ><a :href="'/profile/' + u.id"
                    ><div class="td-content">
                      <img :src="'http://127.0.0.1:8000' + u.imageU" alt="avatar" /><span>{{ u.firstname }} {{ u.lastname }} </span>
                    </div></a
                  ></b-td
                >
                <b-td>
                  <div v-for="user in Users" :key="user.id">
                    <div v-if="user.id == u.userU" class="td-content text-primary">{{ user.email }}</div>
                  </div>
                </b-td>
                <b-td
                  ><div class="td-content">{{ u.tel }}</div></b-td
                >
                <b-td
                  ><div class="td-content">
                    <span>{{ u.country }}</span>
                  </div></b-td
                >
                <b-td
                  ><div class="td-content ml-5">{{ u.nbquestions }}</div></b-td
                >
              </b-tr>
            </b-tbody>
          </b-table-simple>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import '@/assets/sass/scrollspyNav.scss';
import '@/assets/sass/widgets/widgets.scss';
import '@/assets/sass/users/user-profile.scss';
import { mapGetters, mapActions } from 'vuex';
import axios from 'axios';
export default {
  metaInfo: { title: 'User Profile' },
  data() {
    return {
      CurrentUser: [],
      userprofile: [],
      CurrentUserProfile: [],
      form:{
        categoryPref:'',
        userprofilePref:'',
      },
      nbEval: '',
      search: '',
      UserEval: '',
      average: 0,
      existprofile:false,
      existentreprise:false,
    };
  },
  mounted() {},
  methods: {
    ...mapActions(['GetPreferences','GetQuestioncategories','GetUserentreprises','CreateNotification','GetUsers', 'GetUserprofiles', 'GetEvaluations', 'GetEvaluationProfile']),
    preferencesUpdate(){
      console.log(this.form)
      axios.post('/preferences/preferences-update/'+this.userprofile.preferencesU+'/',this.form)
      this.$router.go()

    },
    async Rating() {
      let done = false;
      if (this.EvaluationProfile.length == 0) {
        axios.post('/evaluationprofile/evaluationprofile-create/', {
          userprofileEval: this.$route.params.id,
          userEval: this.CurrentUser.id,
          nbEval: this.nbEval,
        });
        this.GetEvaluationProfile()
      } else {
        for (let e in this.EvaluationProfile) {
          if (this.EvaluationProfile[e].userprofileEval == this.$route.params.id && this.EvaluationProfile[e].userEval == this.CurrentUser.id) {
            axios.post('/evaluationprofile/evaluationprofile-update/' + this.EvaluationProfile[e].id + '/', {
              nbEval: this.nbEval,
            });
            done = true;
          }
        }
        if (done == false) {
          axios.post('/evaluationprofile/evaluationprofile-create/', {
            userprofileEval: this.$route.params.id,
            userEval: this.CurrentUser.id,
            nbEval: this.nbEval,
          });
        }

        this.GetEvaluationProfile()
      }
      this.CreateNotification({message:' Rated your Profile '+this.nbEval+' Stars !',userprofileNo:this.CurrentUserProfile.id,profileNo:this.$route.params.id})
      this.$router.go();
    },
     async showAlert() {
      this.$swal({
        title: 'You cannot rating your profile',
        padding: '2em',
      });
    },
    async showAlert1() {
      this.$swal({
        title: 'You cannot rate this profile as an entreprise',
        padding: '2em',
      });
    },
  },
  computed: {
    ...mapGetters({
      Userentreprises:'StateUserentreprises',
      User: 'StateUser',
      Users: 'StateUsers',
      Userprofiles: 'StateUserprofiles',
      Evaluations: 'StateEvaluations',
      EvaluationProfile: 'StateEvaluationProfile',
      Questioncategories:'StateQuestioncategories',
      Preferences:'StatePreferences',
    }),
    isLoggedIn: function () {
      return this.$store.getters.isAuthenticated;
    },
    filteredList() {
      return this.Userprofiles.filter((profile) => {
        return (
          profile.firstname.toLowerCase().includes(this.search.toLowerCase()) ||
          profile.lastname.toLowerCase().includes(this.search.toLowerCase()) ||
          profile.country.toLowerCase().includes(this.search.toLowerCase())
        );
      });
    },
  },
  created: function () {
    this.GetUserentreprises();
    this.GetUsers();
    this.GetUserprofiles();
    this.GetEvaluations();
    this.GetEvaluationProfile();
    this.GetPreferences();
    this.GetQuestioncategories()
    for (let u in this.Users) {
      if (this.Users[u].username == this.User) {
        this.CurrentUser = this.Users[u];
      }
    }
    for (let u in this.Userprofiles) {
      if (this.Userprofiles[u].userU == this.CurrentUser.id) {
        this.CurrentUserProfile = this.Userprofiles[u];
        this.existprofile = true;
      }
    }
    for (let ue in this.Userentreprises) {
      if (this.Userentreprises[ue].userE == this.CurrentUser.id) {
        
        this.existentreprise= true;
      }
    }
    axios.get('/userprofile/userprofile-detail/' + this.$route.params.id + '/').then((response) => {
      this.userprofile = response.data;
      axios.get('/preferences/preferences-detail/' + this.userprofile.preferencesU + '/').then((response) => {
      this.form = response.data;
    }); 
      var sum = 0;
    var nb = 0;
    for (let e in this.EvaluationProfile) {
      if (this.EvaluationProfile[e].userprofileEval == this.$route.params.id) {
        sum += this.EvaluationProfile[e].nbEval;
        nb++;
      }
    }
    this.average = sum / nb;

    axios.put('/userprofile/userprofile-update/' + this.userprofile.id + '/', {
      nbEvalProfile: this.average,
    });
    this.userprofile.nbEvalProfile=this.average
    });

    
  },
};
</script>