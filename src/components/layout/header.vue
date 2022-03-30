<template>
  <div>
    <!--  BEGIN NAVBAR  -->
    <div class="header-container fixed-top">
      <header class="header navbar navbar-expand-sm">
        <ul class="navbar-item theme-brand flex-row text-center">
          <li class="nav-item theme-logo">
            <router-link to="/">
              <img src="@/assets/images/Car Geeks.svg" class="navbar-logo" alt="logo" />
            </router-link>
          </li>
          <li class="nav-item theme-text">
            <router-link to="/" class="nav-link"> CARGEEKS </router-link>
          </li>
        </ul>
        <div class="d-none horizontal-menu">
          <a href="javascript:void(0);" class="sidebarCollapse" data-placement="bottom" @click="$store.commit('toggleSideBar', !$store.state.is_show_sidebar)">
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
              class="feather feather-menu"
            >
              <line x1="3" y1="12" x2="21" y2="12"></line>
              <line x1="3" y1="6" x2="21" y2="6"></line>
              <line x1="3" y1="18" x2="21" y2="18"></line>
            </svg>
          </a>
        </div>
        <ul class="navbar-item flex-row">
          <li class="nav-item align-self-center search-animated" :class="{ 'show-search': $store.state.is_show_search }">
            <svg
              @click="$store.commit('toggleSearch', !$store.state.is_show_search)"
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
              class="feather feather-search toggle-search"
            >
              <circle cx="11" cy="11" r="8"></circle>
              <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            </svg>
            <form class="form-inline search-full form-inline search" :class="{ 'input-focused': $store.state.is_show_search }">
              <div class="search-bar">
                <input
                  type="text"
                  class="form-control search-form-control ml-lg-auto"
                  placeholder='Search (Press  "/" to focus)'
                  v-model="query"
                  @blur="searchResultsVisible = false"
                  @focus="searchResultsVisible = true"
                  @keydown.esc="searchResultsVisible = false"
                  @input="softReset"
                  ref="search"
                  @keyup="performSearch"
                  @keydown.up.prevent="highlightPrevious"
                  @keydown.down.prevent="highlightNext"
                  @keydown.enter="gotoLink"
                />
              </div>
            </form>
          </li>
          <li style="margin-top: 150px; margin-right: 350px">
            <div v-if="query.length > 0" class="text-2xl cursor-pointer text-gray-600 hover:text-gray-800" @click="reset">&times;</div>

            <transition name="fade">
              <div v-if="query.length > 0 && searchResultsVisible" class="bg-white border text-left rounded-lg mt-5" style="max-height: 50rem; max-width: 15rem">
                <div class="flex flex-col" ref="results">
                  <a
                    v-for="(question, index) in searchResults"
                    :key="index"
                    :href="'/questionpage/' + question.item.id"
                    @mousedown.prevent="searchResultsVisible = true"
                    class="border-b border-gray-400 text-xl cursor-pointer p-4 hover:bg-blue-100"
                    :class="{ 'bg-blue-100': index === highlightedIndex }"
                  >
                    {{ question.item.titleQ }}

                    <span class="font-normal text-sm">{{ question.item.contentQ }}</span>
                  </a>

                  <div v-if="searchResults.length === 0" class="font-normal w-full border-b cursor-pointer p-4">
                    <p class="my-0">
                      No results for '<strong>{{ query }}</strong
                      >'
                    </p>
                  </div>
                </div>
              </div>
            </transition>
          </li>
        </ul>

        <div class="navbar-item flex-row ml-md-auto">
          <div class="dark-mode d-flex align-items-center">
            <a v-if="$store.state.dark_mode == 'light'" href="javascript:;" class="d-flex align-items-center" @click="toggleMode('dark')">
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
                class="feather feather-sun"
              >
                <circle cx="12" cy="12" r="5"></circle>
                <line x1="12" y1="1" x2="12" y2="3"></line>
                <line x1="12" y1="21" x2="12" y2="23"></line>
                <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
                <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
                <line x1="1" y1="12" x2="3" y2="12"></line>
                <line x1="21" y1="12" x2="23" y2="12"></line>
                <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
                <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
              </svg>
              <span class="ml-2">Light</span>
            </a>
            <a v-if="$store.state.dark_mode == 'dark'" href="javascript:;" class="d-flex align-items-center" @click="toggleMode('system')">
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
                class="feather feather-moon"
              >
                <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
              </svg>
              <span class="ml-2">Dark</span>
            </a>
            <a v-if="$store.state.dark_mode == 'system'" href="javascript:;" class="d-flex align-items-center" @click="toggleMode('light')">
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
                class="feather feather-airplay"
              >
                <path d="M5 17H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-1"></path>
                <polygon points="12 15 17 21 7 21 12 15"></polygon>
              </svg>
              <span class="ml-2">System</span>
            </a>
          </div>

          <b-dropdown toggle-tag="a" variant="icon-only" toggle-class="nav-link" class="nav-item language-dropdown">
            <template #button-content>
              <img v-if="selectedLang" :src="require(`@/assets/images/flags/${selectedLang.code}.png`)" class="flag-width" alt="flag" />
            </template>
            <perfect-scrollbar>
              <b-dropdown-item v-for="item in countryList" :key="item.code" link-class="d-flex align-items-center" :active="$i18n.locale === item.code" @click.prevent="changeLanguage(item)">
                <img :src="require(`@/assets/images/flags/${item.code}.png`)" class="flag-width" alt="" /> <span>{{ item.name }}</span>
              </b-dropdown-item>
            </perfect-scrollbar>
          </b-dropdown>
          <span class="mt-2" v-if="isLoggedIn">
            <b-dropdown toggle-tag="a" variant="icon-only" toggle-class="nav-link" class="nav-item message-dropdown" :right="true">
              <template #button-content>
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
                  class="feather feather-mail"
                >
                  <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                  <polyline points="22,6 12,13 2,6"></polyline>
                </svg>
              </template>

              <b-dropdown-item>
                <b-media class="media">
                  <template #aside>
                    <div class="avatar avatar-xl">
                      <span class="avatar-title rounded-circle">KY</span>
                    </div>
                  </template>
                  <h5 class="usr-name">Kara Young</h5>
                  <p class="msg-title">ACCOUNT UPDATE</p>
                </b-media>
              </b-dropdown-item>
              <b-dropdown-item>
                <b-media class="media">
                  <template #aside>
                    <img src="@/assets/images/profile-15.jpeg" alt="avatar" />
                  </template>
                  <h5 class="usr-name">Daisy Anderson</h5>
                  <p class="msg-title">ACCOUNT UPDATE</p>
                </b-media>
              </b-dropdown-item>
              <b-dropdown-item>
                <b-media class="media">
                  <template #aside>
                    <div class="avatar avatar-xl">
                      <span class="avatar-title rounded-circle">OG</span>
                    </div>
                  </template>
                  <h5 class="usr-name">Oscar Garner</h5>
                  <p class="msg-title">ACCOUNT UPDATE</p>
                </b-media>
              </b-dropdown-item>
            </b-dropdown></span
          >
          <span v-if="isLoggedIn">
            <b-dropdown toggle-tag="a" variant="icon-only" toggle-class="nav-link" menu-class="notification-scroll" class="nav-item notification-dropdown" :right="true">
                        
                        <template #button-content>
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
                                class="feather feather-bell mt-2"
                            >
                                <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
                                <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
                            </svg>
                            <span class="badge badge-success "></span>
                        </template>
                        <perfect-scrollbar>
                         <div v-for="n in Notifications" :key="n.id">
                           <b-dropdown-item  @click="updatenotif(n)" v-if="n.seen == false && n.foradmin == true && CurrentUser.is_superuser==true">
                            <b-media class="server-log">
                                <template #aside>
                                  <b-badge variant="info" class="mt-2">Dashboard</b-badge>
                                  
                                </template>
                                <div class="data-info" v-if="n.byuserprofileNo==null && n.byuserentrepriseNo!=null">
                                    <h6 class="">
                                      <div v-for="ue in Userentreprises" :key="ue.id">
                                    <div v-if="ue.id == n.byuserentrepriseNo">
                                      {{ue.nameE}} {{ n.message }}
                                    </div></div></h6>
                                    <p class="">{{ getDateago(n.dateNo) }} ago</p>
                                </div>
                                <div class="data-info" v-else-if="n.byuserentrepriseNo==null && n.byuserprofileNo!=null">
                                    <h6 class="">
                                      <div v-for="u in Userprofiles" :key="u.id">
                                    <div v-if="u.id == n.byuserprofileNo">
                                      {{u.firstname}} {{u.lastname}} {{ n.message }}
                                    </div></div></h6>
                                    <p class="">{{ getDateago(n.dateNo) }} ago</p>
                                </div>
                                <div class="data-info" v-if="n.byuserentrepriseNo==null && n.byuserprofileNo==null">
                                    <h6 class="">
                                      {{ n.message }}
                                   </h6>
                                    <p class="">{{ getDateago(n.dateNo) }} ago</p>
                                </div>
                                <div @click="deletenotif(n.id)" class="icon-status">
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
                                        class="feather feather-x"
                                    >
                                        <line x1="18" y1="6" x2="6" y2="18"></line>
                                        <line x1="6" y1="6" x2="18" y2="18"></line>
                                    </svg>
                                </div>
                            </b-media>
                        </b-dropdown-item>
                        <b-dropdown-item  @click="updatenotif(n)" v-if="n.seen == true && n.foradmin == true && CurrentUser.is_superuser==true">
                            <b-media class="server-log">
                                <template #aside>
                                  <b-badge variant="info" class="mt-2">Dashboard</b-badge>
                                </template>
                                <div class="data-info" v-if="n.byuserprofileNo==null && n.byuserentrepriseNo!=null">
                                      <div v-for="ue in Userentreprises" :key="ue.id">
                                    <div v-if="ue.id == n.byuserentrepriseNo">
                                     <p> {{ue.nameE}} {{ n.message }}</p>
                                    </div></div>
                                    <p class="">{{ getDateago(n.dateNo) }} ago</p>
                                </div>
                                <div class="data-info" v-else-if="n.byuserentrepriseNo==null && n.byuserprofileNo!=null">
                                      <div v-for="u in Userprofiles" :key="u.id">
                                    <div v-if="u.id == n.byuserprofileNo">
                                    <p>  {{u.firstname}} {{u.lastname}} {{ n.message }}</p>
                                    </div></div>
                                    <p class="">{{ getDateago(n.dateNo) }} ago</p>
                                </div>
                                <div class="data-info" v-if="n.byuserentrepriseNo==null && n.byuserprofileNo==null">
                                    <h6 class="">
                                      {{ n.message }}
                                   </h6>
                                    <p class="">{{ getDateago(n.dateNo) }} ago</p>
                                </div>
                                <div @click="deletenotif(n.id)" class="icon-status">
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
                                        class="feather feather-x"
                                    >
                                        <line x1="18" y1="6" x2="6" y2="18"></line>
                                        <line x1="6" y1="6" x2="18" y2="18"></line>
                                    </svg>
                                </div>
                            </b-media>
                        </b-dropdown-item>
                        <b-dropdown-item  @click="updatenotif(n)" v-if="Userprofile.id == n.userprofileNo && n.entrepriseNo==null && n.seen == false && n.admin == false && n.foradmin==false">
                            <b-media class="server-log">
                                <template #aside>
                                  <div v-if="n.byuserentrepriseNo==null">
                                    <div v-for="u in Userprofiles" :key="u.id">
                                    <div v-if="u.id == n.byuserprofileNo">
                                    <b-avatar :src="'http://127.0.0.1:8000'+u.imageU" class="avatar-title rounded-circle"></b-avatar>
                                    </div>
                                  </div>
                                  </div>
                                  <div v-else-if="n.byuserprofileNo==null">
                                    <div v-for="ue in Userentreprises" :key="ue.id">
                                    <div v-if="ue.id == n.byuserentrepriseNo">
                                    <b-avatar :src="'http://127.0.0.1:8000'+ue.imageE" class="avatar-title rounded-circle"></b-avatar>
                                    </div>
                                  </div>
                                  </div>
                                  
                                </template>
                                <div class="data-info" v-if="n.byuserprofileNo==null">
                                    <h6 class="">
                                      <div v-for="ue in Userentreprises" :key="ue.id">
                                    <div v-if="ue.id == n.byuserentrepriseNo">
                                      {{ue.nameE}} {{ n.message }}
                                    </div></div></h6>
                                    <p class="">{{ getDateago(n.dateNo) }} ago</p>
                                </div>
                                <div class="data-info" v-else-if="n.byuserentrepriseNo==null">
                                    <h6 class="">
                                      <div v-for="u in Userprofiles" :key="u.id">
                                    <div v-if="u.id == n.byuserprofileNo">
                                      {{u.firstname}} {{u.lastname}} {{ n.message }}
                                    </div></div></h6>
                                    <p class="">{{ getDateago(n.dateNo) }} ago</p>
                                </div>

                                <div @click="deletenotif(n.id)" class="icon-status">
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
                                        class="feather feather-x"
                                    >
                                        <line x1="18" y1="6" x2="6" y2="18"></line>
                                        <line x1="6" y1="6" x2="18" y2="18"></line>
                                    </svg>
                                </div>
                            </b-media>
                        </b-dropdown-item>
                        <b-dropdown-item  @click="updatenotif(n)" v-if="n.userprofileNo==null && Userentreprise.id == n.entrepriseNo && n.seen == false && n.admin == false && foradmin==false">
                            <b-media class="server-log">
                                <template #aside>
                                  <div v-if="n.byuserentrepriseNo==null">
                                    <div v-for="u in Userprofiles" :key="u.id">
                                    <div v-if="u.id == n.byuserprofileNo">
                                    <b-avatar :src="'http://127.0.0.1:8000'+u.imageU" class="avatar-title rounded-circle"></b-avatar>
                                    </div>
                                  </div>
                                  </div>
                                  <div v-else-if="n.byuserprofileNo==null">
                                    <div v-for="ue in Userentreprises" :key="ue.id">
                                    <div v-if="ue.id == n.byuserentrepriseNo">
                                    <b-avatar :src="'http://127.0.0.1:8000'+ue.imageE" class="avatar-title rounded-circle"></b-avatar>
                                    </div>
                                  </div>
                                  </div>
                                  
                                </template>
                                <div class="data-info" v-if="n.byuserprofileNo==null">
                                    <h6 class="">
                                      <div v-for="ue in Userentreprises" :key="ue.id">
                                    <div v-if="ue.id == n.byuserentrepriseNo">
                                      {{ue.nameE}} {{ n.message }}
                                    </div></div></h6>
                                    <p class="">{{ getDateago(n.dateNo) }} ago</p>
                                </div>
                                <div class="data-info" v-else-if="n.byuserentrepriseNo==null">
                                    <h6 class="">
                                      <div v-for="u in Userprofiles" :key="u.id">
                                    <div v-if="u.id == n.byuserprofileNo">
                                      {{u.firstname}} {{u.lastname}} {{ n.message }}
                                    </div></div></h6>
                                    <p class="">{{ getDateago(n.dateNo) }} ago</p>
                                </div>

                                <div @click="deletenotif(n.id)" class="icon-status">
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
                                        class="feather feather-x"
                                    >
                                        <line x1="18" y1="6" x2="6" y2="18"></line>
                                        <line x1="6" y1="6" x2="18" y2="18"></line>
                                    </svg>
                                </div>
                            </b-media>
                        </b-dropdown-item>
                        <b-dropdown-item @click="updatenotif(n)" v-if="Userprofile.id == n.userprofileNo && n.entrepriseNo==null && n.seen == false && n.admin == true">
                            <b-media class="server-log">
                                <template #aside>
                                  <b-badge variant="info" class="mt-3">Admin</b-badge>
                                </template>
                                <div class="data-info">
                                    <h6 class="">
                                      {{ n.message }}
                                   </h6>
                                    <p class="">{{ getDateago(n.dateNo) }} ago</p>
                                </div>

                                <div @click="deletenotif(n.id)" class="icon-status">
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
                                        class="feather feather-x"
                                    >
                                        <line x1="18" y1="6" x2="6" y2="18"></line>
                                        <line x1="6" y1="6" x2="18" y2="18"></line>
                                    </svg>
                                </div>
                            </b-media>
                        </b-dropdown-item>
                        <b-dropdown-item @click="updatenotif(n)" v-if="n.userprofileNo==null && Userentreprise.id == n.entrepriseNo && n.entrepriseNo==null && n.seen == false && n.admin == true">
                            <b-media class="server-log">
                                <template #aside>
                                  <b-badge variant="info" class="mt-3">Admin</b-badge>
                                </template>
                                <div class="data-info">
                                    <h6 class="">
                                      {{ n.message }}
                                   </h6>
                                    <p class="">{{ getDateago(n.dateNo) }} ago</p>
                                </div>

                                <div @click="deletenotif(n.id)" class="icon-status">
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
                                        class="feather feather-x"
                                    >
                                        <line x1="18" y1="6" x2="6" y2="18"></line>
                                        <line x1="6" y1="6" x2="18" y2="18"></line>
                                    </svg>
                                </div>
                            </b-media>
                        </b-dropdown-item>
                        <b-dropdown-item  @click="updatenotif(n)" v-if="Userprofile.id == n.userprofileNo && n.entrepriseNo==null && n.seen == true && n.admin == false && n.foradmin == false">
                            <b-media class="server-log">
                                <template #aside>
                                  <div v-if="n.byuserentrepriseNo==null">
                                    <div v-for="u in Userprofiles" :key="u.id">
                                    <div v-if="u.id == n.byuserprofileNo">
                                    <b-avatar :src="'http://127.0.0.1:8000'+u.imageU" class="avatar-title rounded-circle"></b-avatar>
                                    </div>
                                  </div>
                                  </div>
                                  <div v-else-if="n.byuserprofileNo==null">
                                    <div v-for="ue in Userentreprises" :key="ue.id">
                                    <div v-if="ue.id == n.byuserentrepriseNo">
                                    <b-avatar :src="'http://127.0.0.1:8000'+ue.imageE" class="avatar-title rounded-circle"></b-avatar>
                                    </div>
                                  </div>
                                  </div>
                                  
                                </template>
                                <div class="data-info" v-if="n.byuserprofileNo==null">
                                      <div v-for="ue in Userentreprises" :key="ue.id">
                                    <div v-if="ue.id == n.byuserentrepriseNo">
                                     <p> {{ue.nameE}} {{ n.message }}</p>
                                    </div></div>
                                    <p class="">{{ getDateago(n.dateNo) }} ago</p>
                                </div>
                                <div class="data-info" v-else-if="n.byuserentrepriseNo==null">
                                      <div v-for="u in Userprofiles" :key="u.id">
                                    <div v-if="u.id == n.byuserprofileNo">
                                    <p>  {{u.firstname}} {{u.lastname}} {{ n.message }}</p>
                                    </div></div>
                                    <p class="">{{ getDateago(n.dateNo) }} ago</p>
                                </div>

                                <div @click="deletenotif(n.id)" class="icon-status">
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
                                        class="feather feather-x"
                                    >
                                        <line x1="18" y1="6" x2="6" y2="18"></line>
                                        <line x1="6" y1="6" x2="18" y2="18"></line>
                                    </svg>
                                </div>
                            </b-media>
                        </b-dropdown-item>
                        <b-dropdown-item  @click="updatenotif(n)" v-if="n.userprofileNo==null && Userentreprise.id == n.entrepriseNo && n.seen == true && n.admin == false && n.foradmin == false">
                            <b-media class="server-log">
                                <template #aside>
                                  <div v-if="n.byuserentrepriseNo==null">
                                    <div v-for="u in Userprofiles" :key="u.id">
                                    <div v-if="u.id == n.byuserprofileNo">
                                    <b-avatar :src="'http://127.0.0.1:8000'+u.imageU" class="avatar-title rounded-circle"></b-avatar>
                                    </div>
                                  </div>
                                  </div>
                                  <div v-else-if="n.byuserprofileNo==null">
                                    <div v-for="ue in Userentreprises" :key="ue.id">
                                    <div v-if="ue.id == n.byuserentrepriseNo">
                                    <b-avatar :src="'http://127.0.0.1:8000'+ue.imageE" class="avatar-title rounded-circle"></b-avatar>
                                    </div>
                                  </div>
                                  </div>
                                  
                                </template>
                                <div class="data-info" v-if="n.byuserprofileNo==null">
                                      <div v-for="ue in Userentreprises" :key="ue.id">
                                    <div v-if="ue.id == n.byuserentrepriseNo">
                                     <p> {{ue.nameE}} {{ n.message }}</p>
                                    </div></div>
                                    <p class="">{{ getDateago(n.dateNo) }} ago</p>
                                </div>
                                <div class="data-info" v-else-if="n.byuserentrepriseNo==null">
                                      <div v-for="u in Userprofiles" :key="u.id">
                                    <div v-if="u.id == n.byuserprofileNo">
                                    <p>  {{u.firstname}} {{u.lastname}} {{ n.message }}</p>
                                    </div></div>
                                    <p class="">{{ getDateago(n.dateNo) }} ago</p>
                                </div>

                                <div @click="deletenotif(n.id)" class="icon-status">
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
                                        class="feather feather-x"
                                    >
                                        <line x1="18" y1="6" x2="6" y2="18"></line>
                                        <line x1="6" y1="6" x2="18" y2="18"></line>
                                    </svg>
                                </div>
                            </b-media>
                        </b-dropdown-item>
                        <b-dropdown-item @click="updatenotif(n)" v-if="Userprofile.id == n.userprofileNo && n.entrepriseNo==null && n.seen == true && n.admin == true">
                            <b-media class="server-log">
                                <template #aside>
                                  <b-badge variant="info" class="mt-3">Admin</b-badge>
                                </template>
                                <div class="data-info">
                                    <p class="">
                                      {{ n.message }}
                                   </p>
                                    <p class="">{{ getDateago(n.dateNo) }} ago</p>
                                </div>

                                <div @click="deletenotif(n.id)" class="icon-status">
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
                                        class="feather feather-x"
                                    >
                                        <line x1="18" y1="6" x2="6" y2="18"></line>
                                        <line x1="6" y1="6" x2="18" y2="18"></line>
                                    </svg>
                                </div>
                            </b-media>
                        </b-dropdown-item>
                        <b-dropdown-item @click="updatenotif(n)" v-if="n.userprofileNo==null && Userentreprise.id == n.entrepriseNo && n.seen == true && n.admin == true">
                            <b-media class="server-log">
                                <template #aside>
                                  <b-badge variant="info" class="mt-3">Admin</b-badge>
                                </template>
                                <div class="data-info">
                                    <p class="">
                                      {{ n.message }}
                                   </p>
                                    <p class="">{{ getDateago(n.dateNo) }} ago</p>
                                </div>

                                <div @click="deletenotif(n.id)" class="icon-status">
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
                                        class="feather feather-x"
                                    >
                                        <line x1="18" y1="6" x2="6" y2="18"></line>
                                        <line x1="6" y1="6" x2="18" y2="18"></line>
                                    </svg>
                                </div>
                            </b-media>
                        </b-dropdown-item>
                        </div>
                        </perfect-scrollbar>
                       
                    </b-dropdown>
            <!--<b-dropdown toggle-tag="a" variant="icon-only" toggle-class="nav-link" menu-class="notification-scroll" class="nav-item notification-dropdown" :right="true">
              <template #button-content>
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
                  class="feather feather-bell mt-2"
                >
                  <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
                  <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
                </svg>
                <span class="badge badge-success"></span>
              </template>
              <div v-for="n in Notifications" :key="n.id">
                <b-dropdown-item class="" :to="path(n)" @click="updatenotif(n)" v-if="Userprofile.id == n.userprofileNo && n.seen == false && n.admin == true">
                  <div class="data-info">
                    <h6 class="">
                      {{ n.message }}
                    </h6>
                    <b-badge>Admin</b-badge>

                    <p class="">{{ getDateago(n.dateNo) }} ago</p>
                  </div>

                  <div class="icon-status">
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
                                        class="feather feather-x"
                                    >
                                        <line x1="18" y1="6" x2="6" y2="18"></line>
                                        <line x1="6" y1="6" x2="18" y2="18"></line>
                                    </svg>
                                </div>
                </b-dropdown-item>
                <b-dropdown-divider></b-dropdown-divider>
                <b-dropdown-item class="" :to="path(n)" @click="updatenotif(n)" v-if="Userprofile.id == n.userprofileNo && n.seen == false && n.admin == false">
                  <div class="data-info">
                    <div v-for="u in Userprofiles" :key="u.id">
                      <div v-if="u.id == n.byuserprofileNo">
                        <h6 class="">{{ u.firstname }} {{ u.lastname }} {{ n.message }}</h6>
                      </div>
                    </div>

                    <p class="">{{ getDateago(n.dateNo) }} ago</p>
                  </div>

                  <div class="icon-status">
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
                                        class="feather feather-x"
                                    >
                                        <line x1="18" y1="6" x2="6" y2="18"></line>
                                        <line x1="6" y1="6" x2="18" y2="18"></line>
                                    </svg>
                                </div>
                </b-dropdown-item>
                <b-dropdown-divider></b-dropdown-divider>
              </div> </b-dropdown
          >--></span>
          <span v-if="isLoggedIn">
            <b-dropdown toggle-tag="a" variant="icon-only" toggle-class="user nav-link" class="nav-item user-profile-dropdown" :right="true">
              <template #button-content>
                <span v-if="Userprofile.length != 0">
                  <img :src="'http://127.0.0.1:8000' + Userprofile.imageU" class="navbar-logo" />
                </span>
                <span v-if="Userprofile.length == 0">
                  <img :src="'http://127.0.0.1:8000' + Userentreprise.imageE" class="navbar-logo" />
                </span>
              </template>
              <span v-if="Userprofile.length != 0">
                <b-dropdown-item :to="'/profile/' + Userprofile.id">
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
                    class="feather feather-user"
                  >
                    <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                    <circle cx="12" cy="7" r="4"></circle>
                  </svg>
                  Profile
                </b-dropdown-item>
              </span>
              <span v-else-if="Userprofile.length == 0">
                <b-dropdown-item :to="'/entreprisedetails/' + Userentreprise.id">
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
                    class="feather feather-user"
                  >
                    <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                    <circle cx="12" cy="7" r="4"></circle>
                  </svg>
                  Portfolio
                </b-dropdown-item>
              </span>
              <span v-else>
                <b-dropdown-item to="/auth/userinfo">
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
                    class="feather feather-user"
                  >
                    <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                    <circle cx="12" cy="7" r="4"></circle>
                  </svg>
                  Profile
                </b-dropdown-item>
              </span>
              <b-dropdown-divider></b-dropdown-divider>
              <b-dropdown-item to="/apps/mailbox">
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
                  class="feather feather-inbox"
                >
                  <polyline points="22 12 16 12 14 15 10 15 8 12 2 12"></polyline>
                  <path d="M5.45 5.11L2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z"></path>
                </svg>
                Inbox
              </b-dropdown-item>
              <b-dropdown-divider></b-dropdown-divider>
              <b-dropdown-item to="/auth/lockscreen">
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
                  class="feather feather-lock"
                >
                  <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                  <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                </svg>
                Lock Screen
              </b-dropdown-item>
              <b-dropdown-divider></b-dropdown-divider>

              <b-dropdown-item to="/auth/login">
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
                  class="feather feather-log-out"
                >
                  <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path>
                  <polyline points="16 17 21 12 16 7"></polyline>
                  <line x1="21" y1="12" x2="9" y2="12"></line>
                </svg>

                <span @click="logout">Sign Out</span>
              </b-dropdown-item>
            </b-dropdown></span
          >
          <span class="mt-2" v-if="isLoggedIn == false">
            <a href="auth/login" class="mt-2 ml-3">Login</a>
            <a href="auth/register" class="mt-2 ml-3 mr-3">Register</a>
          </span>
        </div>
      </header>
    </div>
    <!--  END NAVBAR  -->
    <!--  BEGIN NAVBAR  -->
    <div class="sub-header-container">
      <header class="header navbar navbar-expand-sm">
        <a href="javascript:void(0);" class="sidebarCollapse" data-placement="bottom" @click="$store.commit('toggleSideBar', !$store.state.is_show_sidebar)">
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
            class="feather feather-menu"
          >
            <line x1="3" y1="12" x2="21" y2="12"></line>
            <line x1="3" y1="6" x2="21" y2="6"></line>
            <line x1="3" y1="18" x2="21" y2="18"></line>
          </svg>
        </a>

        <!-- Portal vue for Breadcrumb -->
        <portal-target name="breadcrumb"> </portal-target>
      </header>
    </div>
    <!--  END NAVBAR  -->
    <!--  BEGIN TOPBAR  -->
    <div class="topbar-nav header navbar" role="banner">
      <nav class="topbar">
        <ul class="list-unstyled menu-categories" id="topAccordion">
          <li class="menu single-menu">
            <a href="javascript:;" data-toggle="collapse" aria-expanded="true" class="dropdown-toggle autodroprown">
              <div class="">
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
                  class="feather feather-home"
                >
                  <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                  <polyline points="9 22 9 12 15 12 15 22"></polyline>
                </svg>
                <span>{{ $t('dashboard') }}</span>
              </div>
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
                class="feather feather-chevron-down"
              >
                <polyline points="6 9 12 15 18 9"></polyline>
              </svg>
            </a>
            <ul class="collapse submenu list-unstyled" id="dashboard" data-parent="#topAccordion">
              <router-link tag="li" to="/"
                ><a>{{ $t('sales') }}</a></router-link
              >
              <router-link tag="li" to="/index2"
                ><a>{{ $t('analytics') }}</a></router-link
              >
            </ul>
          </li>

          <li class="menu single-menu">
            <a href="javascript:;" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
              <div class="">
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
                  class="feather feather-cpu"
                >
                  <rect x="4" y="4" width="16" height="16" rx="2" ry="2"></rect>
                  <rect x="9" y="9" width="6" height="6"></rect>
                  <line x1="9" y1="1" x2="9" y2="4"></line>
                  <line x1="15" y1="1" x2="15" y2="4"></line>
                  <line x1="9" y1="20" x2="9" y2="23"></line>
                  <line x1="15" y1="20" x2="15" y2="23"></line>
                  <line x1="20" y1="9" x2="23" y2="9"></line>
                  <line x1="20" y1="14" x2="23" y2="14"></line>
                  <line x1="1" y1="9" x2="4" y2="9"></line>
                  <line x1="1" y1="14" x2="4" y2="14"></line>
                </svg>
                <span>{{ $t('apps') }}</span>
              </div>
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
                class="feather feather-chevron-down"
              >
                <polyline points="6 9 12 15 18 9"></polyline>
              </svg>
            </a>
            <ul class="collapse submenu list-unstyled" id="app" data-parent="#topAccordion">
              <router-link tag="li" to="/apps/chat"><a>Chat</a></router-link>
              <router-link tag="li" to="/apps/mailbox"><a>Mailbox</a></router-link>
              <router-link tag="li" to="/apps/todo-list"><a>Todo List</a></router-link>
              <router-link tag="li" to="/apps/notes"><a>Notes</a></router-link>
              <router-link tag="li" to="/apps/scrumboard"><a>Scrumboard</a></router-link>
              <router-link tag="li" to="/apps/contacts"><a>Contacts</a></router-link>

              <li class="sub-sub-submenu-list">
                <a href="javascript:;" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
                  Invoice
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
                    class="feather feather-chevron-right"
                  >
                    <polyline points="9 18 15 12 9 6"></polyline>
                  </svg>
                </a>
                <ul class="collapse list-unstyled sub-submenu" id="appInvoice" data-parent="#app">
                  <router-link tag="li" to="/apps/invoice/list"><a>List</a></router-link>
                  <router-link tag="li" to="/apps/invoice/preview"><a>Preview</a></router-link>
                  <router-link tag="li" to="/apps/invoice/add"><a>Add</a></router-link>
                  <router-link tag="li" to="/apps/invoice/edit"><a>Edit</a></router-link>
                </ul>
              </li>
              <router-link tag="li" to="/apps/calendar"><a>Calendar</a></router-link>
            </ul>
          </li>

          <li class="menu single-menu">
            <a href="javascript:;" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
              <div class="">
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
                  class="feather feather-box"
                >
                  <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>
                  <polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline>
                  <line x1="12" y1="22.08" x2="12" y2="12"></line>
                </svg>
                <span>{{ $t('components') }}</span>
              </div>
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
                class="feather feather-chevron-down"
              >
                <polyline points="6 9 12 15 18 9"></polyline>
              </svg>
            </a>
            <ul class="collapse submenu list-unstyled" id="components" data-parent="#topAccordion">
              <router-link tag="li" to="/components/tabs"><a>Tabs</a></router-link>
              <router-link tag="li" to="/components/accordions"><a>Accordions</a></router-link>
              <router-link tag="li" to="/components/modals"><a>Modals</a></router-link>
              <router-link tag="li" to="/components/cards"><a>Cards</a></router-link>
              <router-link tag="li" to="/components/carousel"><a>Carousel</a></router-link>
              <router-link tag="li" to="/components/countdown"><a>Countdown</a></router-link>
              <router-link tag="li" to="/components/counter"><a>Counter</a></router-link>
              <router-link tag="li" to="/components/sweetalert"><a>Sweet Alerts</a></router-link>
              <router-link tag="li" to="/components/timeline"><a>Timeline</a></router-link>
              <router-link tag="li" to="/components/notifications"><a>Notifications</a></router-link>
              <router-link tag="li" to="/components/media-object"><a>Media Object</a></router-link>
              <router-link tag="li" to="/components/list-group"><a>List Group</a></router-link>
              <router-link tag="li" to="/components/pricing-table"><a>Pricing Tables</a></router-link>
              <router-link tag="li" to="/components/lightbox"><a> Lightbox </a></router-link>
            </ul>
          </li>

          <li class="menu single-menu">
            <a href="javascript:;" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
              <div class="">
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
                  class="feather feather-zap"
                >
                  <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon>
                </svg>
                <span>{{ $t('ui_kit') }}</span>
              </div>
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
                class="feather feather-chevron-down"
              >
                <polyline points="6 9 12 15 18 9"></polyline>
              </svg>
            </a>
            <ul class="collapse submenu list-unstyled" id="uiKit" data-parent="#topAccordion">
              <router-link tag="li" to="/elements/alerts"><a>Alerts</a></router-link>
              <router-link tag="li" to="/elements/avatar"><a>Avatar</a></router-link>
              <router-link tag="li" to="/elements/badges"><a>Badges</a></router-link>
              <router-link tag="li" to="/elements/breadcrumbs"><a>Breadcrumbs</a></router-link>
              <router-link tag="li" to="/elements/buttons"><a>Buttons</a></router-link>
              <router-link tag="li" to="/elements/buttons-group"><a>Button Groups</a></router-link>
              <router-link tag="li" to="/elements/color-library"><a>Color Library</a></router-link>
              <router-link tag="li" to="/elements/dropdown"><a>Dropdown</a></router-link>
              <router-link tag="li" to="/elements/infobox"><a>Infobox</a></router-link>
              <router-link tag="li" to="/elements/jumbotron"><a>Jumbotron</a></router-link>
              <router-link tag="li" to="/elements/loader"><a>Loader</a></router-link>
              <router-link tag="li" to="/elements/pagination"><a>Pagination</a></router-link>
              <router-link tag="li" to="/elements/popovers"><a>Popovers</a></router-link>
              <router-link tag="li" to="/elements/progress-bar"><a>Progress Bar</a></router-link>
              <router-link tag="li" to="/elements/search"><a>Search</a></router-link>
              <router-link tag="li" to="/elements/tooltips"><a>Tooltips</a></router-link>
              <router-link tag="li" to="/elements/treeview"><a>Treeview</a></router-link>
              <router-link tag="li" to="/elements/typography"><a>Typography</a></router-link>
            </ul>
          </li>

          <li class="menu single-menu">
            <a href="javascript:;" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
              <div class="">
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
                  class="feather feather-layout"
                >
                  <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                  <line x1="3" y1="9" x2="21" y2="9"></line>
                  <line x1="9" y1="21" x2="9" y2="9"></line>
                </svg>
                <span>{{ $t('tables') }}</span>
              </div>
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
                class="feather feather-chevron-down"
              >
                <polyline points="6 9 12 15 18 9"></polyline>
              </svg>
            </a>
            <ul class="collapse submenu list-unstyled" id="tables" data-parent="#topAccordion">
              <router-link tag="li" to="/tables/basic"><a>Basic</a></router-link>
              <li class="sub-sub-submenu-list">
                <a href="javascript:;" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
                  DataTables
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
                    class="feather feather-chevron-right"
                  >
                    <polyline points="9 18 15 12 9 6"></polyline>
                  </svg>
                </a>
                <ul class="collapse list-unstyled sub-submenu" id="datatable" data-parent="#datatable">
                  <router-link tag="li" to="/tables/basic"><a>Basic</a></router-link>
                  <router-link tag="li" to="/tables/striped"><a>Striped Table</a></router-link>
                  <router-link tag="li" to="/tables/order-sorting"><a>Order Sorting</a></router-link>
                  <router-link tag="li" to="/tables/multi-column"><a>Multi Column</a></router-link>
                  <router-link tag="li" to="/tables/multiple-tables"><a>Multiple Tables</a></router-link>
                  <router-link tag="li" to="/tables/alt-pagination"><a>Alt. Pagination</a></router-link>
                  <router-link tag="li" to="/tables/custom"><a>Custom</a></router-link>
                  <router-link tag="li" to="/tables/range-search"><a>Range Search</a></router-link>
                  <router-link tag="li" to="/tables/export"><a>Export</a></router-link>
                  <router-link tag="li" to="/tables/live-dom-ordering"><a>Live DOM ordering</a></router-link>
                  <router-link tag="li" to="/tables/miscellaneous"><a>Miscellaneous</a></router-link>
                </ul>
              </li>
            </ul>
          </li>

          <li class="menu single-menu">
            <a href="javascript:;" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
              <div class="">
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
                  class="feather feather-clipboard"
                >
                  <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
                  <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
                </svg>
                <span>{{ $t('forms') }}</span>
              </div>
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
                class="feather feather-chevron-down"
              >
                <polyline points="6 9 12 15 18 9"></polyline>
              </svg>
            </a>
            <ul class="collapse submenu list-unstyled" id="forms" data-parent="#topAccordion">
              <router-link tag="li" to="/forms/basic"><a>Basic</a></router-link>
              <router-link tag="li" to="/forms/input-group"><a>Input Group</a></router-link>
              <router-link tag="li" to="/forms/layouts"><a>Layouts</a></router-link>
              <router-link tag="li" to="/forms/validation"><a>Validation</a></router-link>
              <router-link tag="li" to="/forms/input-mask"><a>Input Mask</a></router-link>
              <router-link tag="li" to="/forms/select2"><a>Select2</a></router-link>
              <router-link tag="li" to="/forms/touchspin"><a>TouchSpin</a></router-link>
              <router-link tag="li" to="/forms/checkbox-radio"><a>Checkbox &amp; Radio</a></router-link>
              <router-link tag="li" to="/forms/switches"><a>Switches</a></router-link>
              <router-link tag="li" to="/forms/wizards"><a>Wizards</a></router-link>
              <router-link tag="li" to="/forms/file-upload"><a>File Upload</a></router-link>
              <router-link tag="li" to="/forms/quill-editor"><a>Quill Editor</a></router-link>
              <router-link tag="li" to="/forms/markdown-editor"><a>Markdown Editor</a></router-link>
              <router-link tag="li" to="/forms/date-picker"><a>Date &amp; Range Picker </a></router-link>
              <router-link tag="li" to="/forms/clipboard"><a>Clipboard</a></router-link>
            </ul>
          </li>

          <li class="menu single-menu">
            <a href="javascript:;" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
              <div class="">
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
                  class="feather feather-file"
                >
                  <path d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"></path>
                  <polyline points="13 2 13 9 20 9"></polyline>
                </svg>
                <span>{{ $t('pages') }}</span>
              </div>
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
                class="feather feather-chevron-down"
              >
                <polyline points="6 9 12 15 18 9"></polyline>
              </svg>
            </a>
            <ul class="collapse submenu list-unstyled" id="page" data-parent="#topAccordion">
              <router-link tag="li" to="/pages/helpdesk"><a>Helpdesk</a></router-link>
              <router-link tag="li" to="/pages/contact-us"><a>Contact Form</a></router-link>
              <router-link tag="li" to="/pages/faq"><a>FAQ</a></router-link>
              <router-link tag="li" to="/pages/faq2"><a>FAQ 2</a></router-link>
              <router-link tag="li" to="/pages/privacy-policy"><a>Privacy Policy</a></router-link>
              <li><a target="_blank" href="/pages/coming-soon">Coming Soon</a></li>
              <router-link tag="li" to="/pages/blank-page"><a>Blank Page</a></router-link>
              <router-link tag="li" to="/pages/sample"><a>Sample Page</a></router-link>
              <router-link tag="li" to="/profile/"><a>Profile</a></router-link>
              <router-link tag="li" to="/users/account-setting"><a>Account Settings</a></router-link>
              <li class="sub-sub-submenu-list">
                <a href="javascript:;" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
                  Error
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
                    class="feather feather-chevron-right"
                  >
                    <polyline points="9 18 15 12 9 6"></polyline>
                  </svg>
                </a>
                <ul class="collapse list-unstyled sub-submenu" id="pages-error" data-parent="#more">
                  <li><a target="_blank" href="/pages/error404">404</a></li>
                  <li><a target="_blank" href="/pages/error500">500</a></li>
                  <li><a target="_blank" href="/pages/error503">503</a></li>
                  <li><a target="_blank" href="/pages/maintenence">Maintanence</a></li>
                </ul>
              </li>
              <li class="sub-sub-submenu-list">
                <a href="javascript:;" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
                  Login
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
                    class="feather feather-chevron-right"
                  >
                    <polyline points="9 18 15 12 9 6"></polyline>
                  </svg>
                </a>
                <ul class="collapse list-unstyled sub-submenu" id="user-login" data-parent="#page">
                  <li><a target="_blank" href="/auth/login">Login Cover</a></li>
                  <li><a target="_blank" href="/auth/login-boxed">Login Boxed</a></li>
                </ul>
              </li>
              <li class="sub-sub-submenu-list">
                <a href="javascript:;" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
                  Register
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
                    class="feather feather-chevron-right"
                  >
                    <polyline points="9 18 15 12 9 6"></polyline>
                  </svg>
                </a>
                <ul class="collapse list-unstyled sub-submenu" id="user-register" data-parent="#page">
                  <li><a target="_blank" href="/auth/register">Register Cover</a></li>
                  <li><a target="_blank" href="/auth/register-boxed">Register Boxed</a></li>
                </ul>
              </li>

              <li class="sub-sub-submenu-list">
                <a href="javascript:;" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
                  Password Recovery
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
                    class="feather feather-chevron-right"
                  >
                    <polyline points="9 18 15 12 9 6"></polyline>
                  </svg>
                </a>
                <ul class="collapse list-unstyled sub-submenu" id="user-passRecovery" data-parent="#page">
                  <li><a target="_blank" href="/auth/pass-recovery">Recover ID Cover</a></li>
                  <li><a target="_blank" href="/auth/pass-recovery-boxed">Recover ID Boxed</a></li>
                </ul>
              </li>

              <li class="sub-sub-submenu-list">
                <a href="javascript:;" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
                  Lockscreen
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
                    class="feather feather-chevron-right"
                  >
                    <polyline points="9 18 15 12 9 6"></polyline>
                  </svg>
                </a>
                <ul class="collapse list-unstyled sub-submenu" id="user-lockscreen" data-parent="#page">
                  <li><a target="_blank" href="/auth/lockscreen">Unlock Cover</a></li>
                  <li><a target="_blank" href="/auth/lockscreen-boxed">Unlock Boxed</a></li>
                </ul>
              </li>
            </ul>
          </li>

          <li class="menu single-menu">
            <a href="javascript:;" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
              <div class="">
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
                  class="feather feather-plus-circle"
                >
                  <circle cx="12" cy="12" r="10"></circle>
                  <line x1="12" y1="8" x2="12" y2="16"></line>
                  <line x1="8" y1="12" x2="16" y2="12"></line>
                </svg>
                <span>{{ $t('more') }}</span>
              </div>
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
                class="feather feather-chevron-down"
              >
                <polyline points="6 9 12 15 18 9"></polyline>
              </svg>
            </a>
            <ul class="collapse submenu list-unstyled" id="more" data-parent="#topAccordion">
              <router-link tag="li" to="/dragndrop"><a>Drag and Drop</a></router-link>
              <router-link tag="li" to="/widgets"><a>Widgets</a></router-link>
              <router-link tag="li" to="/charts/apex-chart"><a>Charts</a></router-link>
              <router-link tag="li" to="/font-icons"><a>Font Icons</a></router-link>
              <li>
                <a target="_blank" href="https://cork-vue.sbthemes.com"> Documentation </a>
              </li>
            </ul>
          </li>
        </ul>
      </nav>
    </div>
    <!--  END TOPBAR  -->
  </div>
</template>
<script>
import axios from 'axios';
import { mapGetters, mapActions } from 'vuex';
//import SearchComponent from '@/components/SearchComponent'
export default {
  data() {
    return {
      selectedLang: null,
      countryList: this.$store.state.countryList,
      Userprofile: [],
      Userentreprise: [],
      CurrentUser: [],
      query: '',
      searchResultsVisible: false,
      searchResults: [],
      highlightedIndex: 0,
      options: {
        shouldSort: true,
        includeMatches: true,
        threshold: 0.5,
        location: 0,
        distance: 500,
        maxPatternLength: 32,
        minMatchCharLength: 1,
        keys: ['titleQ', 'contentQ'],
      },
      menuOpen: false,
    };
  },
  components: {
    //  SearchComponent,
  },
  mounted() {
    this.selectedLang = this.$appSetting.toggleLanguage();

    this.toggleMode();
    
  },
  computed: {
    ...mapGetters({
      Questions: 'StateQuestions',
      Userprofiles: 'StateUserprofiles',
      Userentreprises: 'StateUserentreprises',
      Users: 'StateUsers',
      User: 'StateUser',
      Notifications: 'StateNotifications',
      Replies: 'StateReplies',
    }),
    isLoggedIn: function () {
      return this.$store.getters.isAuthenticated;
    },
  },
  watch: {
    // whenever question changes, this function will run
    Notifications(newNotifications, oldNotifications) {
        if(oldNotifications!=newNotifications){
            //this.GetNotifications()
            
        }
    }
    },
  methods: {
    deletenotif(id){
      this.$swal({
        icon: 'warning',
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        showCancelButton: true,
        confirmButtonText: 'Delete',
        padding: '2em',
      }).then((result) => {
        if (result.value) {
          axios.delete(`http://127.0.0.1:8000/notifications/notification-delete/${id}/`);
          this.$swal('Deleted!', 'Your Notification has been deleted.', 'success');
          this.$router.go();
        }
      });
    },
    updatenotif(notif) {
      axios.put('/notifications/notification-update/' + notif.id + '/', { seen: true, admin: notif.admin });
      if (notif.foradmin==false &&notif.questionNo != null) {
        this.$router.push('/questionpage/' + notif.questionNo + '/')
      } else if (notif.foradmin==false &&notif.entrepriseNo == null && notif.serviceNo == null && notif.questionNo == null && notif.replyNo == null) {
        this.$router.push('/profile/' + notif.userprofileNo + '/')
      } else if (notif.foradmin==false &&notif.serviceNo != null) {
        this.$router.push('/servicedetails/' + notif.serviceNo + '/')
      } else if (notif.foradmin==false &&notif.userprofileNo == null && notif.serviceNo == null && notif.questionNo == null && notif.replyNo == null) {
        this.$router.push('/entreprisedetails/' + notif.entrepriseNo + '/')
      }else if (notif.foradmin==true && notif.questionNo!=null ) {
        this.$router.push('/dashboard/questionrequests')
      }else if (notif.foradmin==true && notif.replyNo!=null) {
        this.$router.push('/dashboard/replyrequests')
      }else if (notif.foradmin==true && notif.serviceNo!=null && notif.promotionnotif==false) {
        this.$router.push('/dashboard/servicerequests')
      }else if (notif.foradmin==true && notif.serviceNo!=null && notif.promotionnotif==true) {
        this.$router.push('/dashboard/promotionservicerequests')
      }else if (notif.foradmin==true && notif.byuserentrepriseNo!=null && notif.promotionnotif==false) {
        this.$router.push('/dashboard/entrepriserequests')
      }else if (notif.foradmin==true && notif.byuserentrepriseNo==null && notif.questionNo==false && notif.replyNo==null&& notif.serviceNo==null && notif.byuserprofileNo==null) {
        this.$router.push('/dashboard/entrepriserequests')
      }else if (notif.foradmin==true && notif.byuserentrepriseNo!=null && notif.promotionnotif==true) {
        this.$router.push('/dashboard/promotionentrepriserequests')
      }else if (notif.foradmin==true && notif.byuserprofileNo!=null && notif.verifnotif==true) {
        this.$router.push('/dashboard/userverificationrequest')
      } else if (notif.replyNo != null) {
        for (let r in this.Replies) {
          if (this.Replies[r].id == notif.replyNo) {
            this.$router.push('/questionpage/' + this.Replies[r].questionRep + '/')
          }
        }
      }
    },

    getDateago: function (s) {
      if (new Date().getHours() - new Date(s).getHours() == 0) {
        return new Date().getMinutes() - new Date(s).getMinutes() + ' mins';
      } else if (new Date().getDate() - new Date(s).getDate() == 0) {
        return new Date().getHours() - new Date(s).getHours() + ' Hours';
      } else if (new Date().getDate() - new Date(s).getDate() == 0) {
        return new Date().getHours() - new Date(s).getHours() + ' Days';
      } else if (new Date().getMonth() - new Date(s).getMonth() == 0) {
        return new Date().getDate() - new Date(s).getDate() + ' Days';
      }
    },
    reset() {
      this.query = '';
      this.highlightedIndex = 0;
    },
    softReset() {
      this.searchResultsVisible = true;
      this.highlightedIndex = 0;
    },
    focusSearch(e) {
      if (e.key === '/') {
        this.$refs.search.focus();
      }
    },
    performSearch() {
      this.$search(this.query, this.Questions, this.options).then((results) => {
        this.searchResults = results;
      });
    },
    highlightPrevious() {
      if (this.highlightedIndex > 0) {
        this.highlightedIndex = this.highlightedIndex - 1;
        this.scrollIntoView();
      }
    },
    highlightNext() {
      if (this.highlightedIndex < this.searchResults.length - 1) {
        this.highlightedIndex = this.highlightedIndex + 1;
        this.scrollIntoView();
      }
    },
    scrollIntoView() {
      this.$refs.results.children[this.highlightedIndex].scrollIntoView({ block: 'nearest' });
    },
    gotoLink() {
      if (this.searchResults[this.highlightedIndex]) {
        window.location = this.searchResults[this.highlightedIndex].item.path;
      }
    },
    ///
    toggleMenu() {
      this.menuOpen = !this.menuOpen;
    },
    toggleMode(mode) {
      this.$appSetting.toggleMode(mode);
    },

    changeLanguage(item) {
      this.selectedLang = item;
      this.$appSetting.toggleLanguage(item);
    },

    async logout() {
      await this.$store.dispatch('LogOut');
      this.$router.push('/auth/login-boxed');
    },

    ...mapActions(['GetQuestions', 'GetUserprofiles', 'GetUserentreprises', 'GetUsers', 'GetNotifications', 'GetReplies']),
  },
  created: function () {
    this.GetQuestions();
    this.GetUserprofiles();
    this.GetUserentreprises();
    this.GetUsers();
    this.GetNotifications();
    this.GetReplies();
    for (let u in this.Users) {
      if (this.Users[u].username == this.User) {
        this.CurrentUser = this.Users[u];
      }
    }
    for (let u in this.Userprofiles) {
      {
        if (this.Userprofiles[u].userU == this.CurrentUser.id) {
          this.Userprofile = this.Userprofiles[u];
        }
      }
    }

    for (let e in this.Userentreprises) {
      if (this.Userentreprises[e].userE == this.CurrentUser.id) {
        this.Userentreprise = this.Userentreprises[e];
      }
    }
  },
  
};
</script>
<style scoped>
.azjj {
    overflow: auto;
    height: 100px;
}
</style>