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
                                    <b-avatar :src="u.imageU" class="avatar-title rounded-circle"></b-avatar>
                                    </div>
                                  </div>
                                  </div>
                                  <div v-else-if="n.byuserprofileNo==null">
                                    <div v-for="ue in Userentreprises" :key="ue.id">
                                    <div v-if="ue.id == n.byuserentrepriseNo">
                                    <b-avatar :src="ue.imageE" class="avatar-title rounded-circle"></b-avatar>
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
                        <b-dropdown-item  @click="updatenotif(n)" v-if="n.userprofileNo==null && Userentreprise.id == n.entrepriseNo && n.seen == false && n.admin == false && n.foradmin==false">
                            <b-media class="server-log">
                                <template #aside>
                                  <div v-if="n.byuserentrepriseNo==null">
                                    <div v-for="u in Userprofiles" :key="u.id">
                                    <div v-if="u.id == n.byuserprofileNo">
                                    <b-avatar :src="u.imageU" class="avatar-title rounded-circle"></b-avatar>
                                    </div>
                                  </div>
                                  </div>
                                  <div v-else-if="n.byuserprofileNo==null">
                                    <div v-for="ue in Userentreprises" :key="ue.id">
                                    <div v-if="ue.id == n.byuserentrepriseNo">
                                    <b-avatar :src="ue.imageE" class="avatar-title rounded-circle"></b-avatar>
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
                                    <b-avatar :src="u.imageU" class="avatar-title rounded-circle"></b-avatar>
                                    </div>
                                  </div>
                                  </div>
                                  <div v-else-if="n.byuserprofileNo==null">
                                    <div v-for="ue in Userentreprises" :key="ue.id">
                                    <div v-if="ue.id == n.byuserentrepriseNo">
                                    <b-avatar :src="ue.imageE" class="avatar-title rounded-circle"></b-avatar>
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
                                    <b-avatar :src="u.imageU" class="avatar-title rounded-circle"></b-avatar>
                                    </div>
                                  </div>
                                  </div>
                                  <div v-else-if="n.byuserprofileNo==null">
                                    <div v-for="ue in Userentreprises" :key="ue.id">
                                    <div v-if="ue.id == n.byuserentrepriseNo">
                                    <b-avatar :src="ue.imageE" class="avatar-title rounded-circle"></b-avatar>
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
                  <img :src=" Userprofile.imageU" class="navbar-logo" />
                </span>
                <span v-if="Userprofile.length == 0">
                  <img :src=" Userentreprise.imageE" class="navbar-logo" />
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
              <b-dropdown-item to="/apps/chat" v-if="isLoggedIn && Userprofile.id!=null">
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
            <a href="/auth/login" class="mt-2 ml-3">Login</a>
            <a href="/auth/register" class="mt-2 ml-3 mr-3">Register</a>
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
             <router-link to="/questions" v-b-toggle class="dropdown-toggle" @click.prevent>
            <div class="">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 512 512">
                <path
                  fill="currentColor"
                  d="M504 256c0 136.997-111.043 248-248 248S8 392.997 8 256C8 119.083 119.043 8 256 8s248 111.083 248 248zM262.655 90c-54.497 0-89.255 22.957-116.549 63.758c-3.536 5.286-2.353 12.415 2.715 16.258l34.699 26.31c5.205 3.947 12.621 3.008 16.665-2.122c17.864-22.658 30.113-35.797 57.303-35.797c20.429 0 45.698 13.148 45.698 32.958c0 14.976-12.363 22.667-32.534 33.976C247.128 238.528 216 254.941 216 296v4c0 6.627 5.373 12 12 12h56c6.627 0 12-5.373 12-12v-1.333c0-28.462 83.186-29.647 83.186-106.667c0-58.002-60.165-102-116.531-102zM256 338c-25.365 0-46 20.635-46 46c0 25.364 20.635 46 46 46s46-20.636 46-46c0-25.365-20.635-46-46-46z"
                />
              </svg>
              <span>{{ $t('Questions')}} </span>
            </div>
          </router-link>
          </li>

          <li class="menu single-menu">
             <router-link to="/services" v-b-toggle class="dropdown-toggle" @click.prevent>
            <div class="">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 512 512">
                <path
                  fill="currentColor"
                  d="M501.1 395.7L384 278.6c-23.1-23.1-57.6-27.6-85.4-13.9L192 158.1V96L64 0L0 64l96 128h62.1l106.6 106.6c-13.6 27.8-9.2 62.3 13.9 85.4l117.1 117.1c14.6 14.6 38.2 14.6 52.7 0l52.7-52.7c14.5-14.6 14.5-38.2 0-52.7zM331.7 225c28.3 0 54.9 11 74.9 31l19.4 19.4c15.8-6.9 30.8-16.5 43.8-29.5c37.1-37.1 49.7-89.3 37.9-136.7c-2.2-9-13.5-12.1-20.1-5.5l-74.4 74.4l-67.9-11.3L334 98.9l74.4-74.4c6.6-6.6 3.4-17.9-5.7-20.2c-47.4-11.7-99.6.9-136.6 37.9c-28.5 28.5-41.9 66.1-41.2 103.6l82.1 82.1c8.1-1.9 16.5-2.9 24.7-2.9zm-103.9 82l-56.7-56.7L18.7 402.8c-25 25-25 65.5 0 90.5s65.5 25 90.5 0l123.6-123.6c-7.6-19.9-9.9-41.6-5-62.7zM64 472c-13.2 0-24-10.8-24-24c0-13.3 10.7-24 24-24s24 10.7 24 24c0 13.2-10.7 24-24 24z"
                />
              </svg>
              <span>{{ $t('Services') }} </span>
            </div>
          </router-link>
          </li>

          <li class="menu single-menu">
           <router-link to="/entreprises" v-b-toggle class="dropdown-toggle" @click.prevent>
            <div class="">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.88em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 448 512">
                <path
                  fill="currentColor"
                  d="M436 480h-20V24c0-13.255-10.745-24-24-24H56C42.745 0 32 10.745 32 24v456H12c-6.627 0-12 5.373-12 12v20h448v-20c0-6.627-5.373-12-12-12zM128 76c0-6.627 5.373-12 12-12h40c6.627 0 12 5.373 12 12v40c0 6.627-5.373 12-12 12h-40c-6.627 0-12-5.373-12-12V76zm0 96c0-6.627 5.373-12 12-12h40c6.627 0 12 5.373 12 12v40c0 6.627-5.373 12-12 12h-40c-6.627 0-12-5.373-12-12v-40zm52 148h-40c-6.627 0-12-5.373-12-12v-40c0-6.627 5.373-12 12-12h40c6.627 0 12 5.373 12 12v40c0 6.627-5.373 12-12 12zm76 160h-64v-84c0-6.627 5.373-12 12-12h40c6.627 0 12 5.373 12 12v84zm64-172c0 6.627-5.373 12-12 12h-40c-6.627 0-12-5.373-12-12v-40c0-6.627 5.373-12 12-12h40c6.627 0 12 5.373 12 12v40zm0-96c0 6.627-5.373 12-12 12h-40c-6.627 0-12-5.373-12-12v-40c0-6.627 5.373-12 12-12h40c6.627 0 12 5.373 12 12v40zm0-96c0 6.627-5.373 12-12 12h-40c-6.627 0-12-5.373-12-12V76c0-6.627 5.373-12 12-12h40c6.627 0 12 5.373 12 12v40z"
                />
              </svg>
              <span>{{ $t('Entreprises') }} </span>
            </div>
          </router-link>
          </li>

          <li class="menu single-menu">
            <router-link to="/groups" v-b-toggle class="dropdown-toggle" @click.prevent>
            <div class="">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 36 36">
                <path
                  fill="currentColor"
                  d="M12 16.14h-.87a8.67 8.67 0 0 0-6.43 2.52l-.24.28v8.28h4.08v-4.7l.55-.62l.25-.29a11 11 0 0 1 4.71-2.86A6.59 6.59 0 0 1 12 16.14Z"
                  class="clr-i-solid clr-i-solid-path-1"
                />
                <path
                  fill="currentColor"
                  d="M31.34 18.63a8.67 8.67 0 0 0-6.43-2.52a10.47 10.47 0 0 0-1.09.06a6.59 6.59 0 0 1-2 2.45a10.91 10.91 0 0 1 5 3l.25.28l.54.62v4.71h3.94v-8.32Z"
                  class="clr-i-solid clr-i-solid-path-2"
                />
                <path fill="currentColor" d="M11.1 14.19h.31a6.45 6.45 0 0 1 3.11-6.29a4.09 4.09 0 1 0-3.42 6.33Z" class="clr-i-solid clr-i-solid-path-3" />
                <path fill="currentColor" d="M24.43 13.44a6.54 6.54 0 0 1 0 .69a4.09 4.09 0 0 0 .58.05h.19A4.09 4.09 0 1 0 21.47 8a6.53 6.53 0 0 1 2.96 5.44Z" class="clr-i-solid clr-i-solid-path-4" />
                <circle cx="17.87" cy="13.45" r="4.47" fill="currentColor" class="clr-i-solid clr-i-solid-path-5" />
                <path
                  fill="currentColor"
                  d="M18.11 20.3A9.69 9.69 0 0 0 11 23l-.25.28v6.33a1.57 1.57 0 0 0 1.6 1.54h11.49a1.57 1.57 0 0 0 1.6-1.54V23.3l-.24-.3a9.58 9.58 0 0 0-7.09-2.7Z"
                  class="clr-i-solid clr-i-solid-path-6"
                />
                <path fill="none" d="M0 0h36v36H0z" />
              </svg>
              <span>{{ $t('Groups') }}</span>
            </div>
          </router-link>
          </li>

          <li class="menu single-menu">
           <router-link to="/news" v-b-toggle class="dropdown-toggle" @click.prevent>
            <div class="">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1.13em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 576 512">
                <path
                  fill="currentColor"
                  d="M552 64H88c-13.255 0-24 10.745-24 24v8H24c-13.255 0-24 10.745-24 24v272c0 30.928 25.072 56 56 56h472c26.51 0 48-21.49 48-48V88c0-13.255-10.745-24-24-24zM56 400a8 8 0 0 1-8-8V144h16v248a8 8 0 0 1-8 8zm236-16H140c-6.627 0-12-5.373-12-12v-8c0-6.627 5.373-12 12-12h152c6.627 0 12 5.373 12 12v8c0 6.627-5.373 12-12 12zm208 0H348c-6.627 0-12-5.373-12-12v-8c0-6.627 5.373-12 12-12h152c6.627 0 12 5.373 12 12v8c0 6.627-5.373 12-12 12zm-208-96H140c-6.627 0-12-5.373-12-12v-8c0-6.627 5.373-12 12-12h152c6.627 0 12 5.373 12 12v8c0 6.627-5.373 12-12 12zm208 0H348c-6.627 0-12-5.373-12-12v-8c0-6.627 5.373-12 12-12h152c6.627 0 12 5.373 12 12v8c0 6.627-5.373 12-12 12zm0-96H140c-6.627 0-12-5.373-12-12v-40c0-6.627 5.373-12 12-12h360c6.627 0 12 5.373 12 12v40c0 6.627-5.373 12-12 12z"
                />
              </svg>
              <span>{{ $t('News') }}</span>
            </div>
          </router-link>
          </li>

          <li class="menu single-menu">
            <router-link to="/faq" v-b-toggle class="dropdown-toggle" @click.prevent>
            <div class="">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 26 26"><path fill="currentColor" d="M13 0c-1.7 0-3 1.3-3 3v6c0 1.7 1.3 3 3 3h6l4 4v-4c1.7 0 3-1.3 3-3V3c0-1.7-1.3-3-3-3H13zm4.188 3h1.718l1.688 6h-1.5l-.407-1.5h-1.5L16.813 9H15.5l1.688-6zM18 4c-.1.4-.212.888-.313 1.188l-.28 1.312h1.187l-.282-1.313C18.113 4.888 18 4.4 18 4zM3 10c-1.7 0-3 1.3-3 3v6c0 1.7 1.3 3 3 3v4l4-4h6c1.7 0 3-1.3 3-3v-6h-3c-1.9 0-3.406-1.3-3.906-3H3zm4.594 2.906c1.7 0 2.5 1.4 2.5 3c0 1.4-.481 2.288-1.281 2.688c.4.2.874.306 1.374.406l-.374 1c-.7-.2-1.426-.512-2.126-.813c-.1-.1-.275-.093-.375-.093C6.112 18.994 5 18 5 16c0-1.7.994-3.094 2.594-3.094zm0 1.094c-.8 0-1.188.9-1.188 2c0 1.2.388 2 1.188 2c.8 0 1.218-.9 1.218-2s-.418-2-1.218-2z"/></svg>
              <span>{{ $t('FAQ') }}</span>
            </div>
          </router-link>
          </li>

          <li class="menu single-menu">
            <router-link to="/contact-us" v-b-toggle class="dropdown-toggle" @click.prevent>
            <div class="">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1536 1536">
                <path
                  fill="currentColor"
                  d="M515 783v128H263V783h252zm0-255v127H263V528h252zm758 511v128H932v-128h341zm0-256v128H601V783h672zm0-255v127H601V528h672zm135 860V148q0-8-6-14t-14-6h-32L978 384L768 213L558 384L180 128h-32q-8 0-14 6t-6 14v1240q0 8 6 14t14 6h1240q8 0 14-6t6-14zM553 278l185-150H332zm430 0l221-150H798zm553-130v1240q0 62-43 105t-105 43H148q-62 0-105-43T0 1388V148Q0 86 43 43T148 0h1240q62 0 105 43t43 105z"
                />
              </svg>
              <span>{{ $t('Contact Us') }}</span>
            </div>
          </router-link>
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
          axios.delete(`https://cargeeks.herokuapp.com/notifications/notification-delete/${id}/`);
          this.$swal('Deleted!', 'Your Notification has been deleted.', 'success');
          this.$router.go();
        }
      });
    },
    updatenotif(notif) {
      axios.put('/notifications/notification-update/' + notif.id + '/', { seen: true, admin: notif.admin });
      if (notif.foradmin==false &&notif.questionNo != null) {
        this.$router.push('/questionpage/' + notif.questionNo + '/' + this.Questions.find((d)=>d.id==notif.questionNo).slug)
      } else if (notif.foradmin==false &&notif.entrepriseNo == null && notif.serviceNo == null && notif.questionNo == null && notif.replyNo == null) {
        this.$router.push('/profile/' + notif.userprofileNo + '/')
      } else if (notif.foradmin==false &&notif.serviceNo != null) {
        this.$router.push('/servicedetails/' + notif.serviceNo + '/')
      } else if (notif.foradmin==false &&notif.userprofileNo == null && notif.serviceNo == null && notif.questionNo == null && notif.replyNo == null) {
        this.$router.push('/entreprisedetails/' + notif.entrepriseNo + '/')
      }else if (notif.foradmin==true && notif.questionNo!=null ) {
        this.$router.push('/dashboard/questionrequests')
      }else if (notif.foradmin==true && notif.replyNo!=null) {
        this.$router.push('/dashboard/repliesrequests')
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
            this.$router.push('/questionpage/' + this.Replies.find((d)=>d.id==notif.replyNo).questionRep + '/' + this.Questions.find((d)=>d.id==this.Replies.find((d)=>d.id==notif.replyNo).questionRep).slug)
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