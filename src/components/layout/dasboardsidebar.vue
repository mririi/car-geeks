<template>
  <!--  BEGIN SIDEBAR  -->
  <div class="sidebar-wrapper sidebar-theme">
    <nav ref="menu" id="sidebar">
      <div class="shadow-bottom"></div>

      <perfect-scrollbar class="list-unstyled menu-categories" tag="ul" :options="{ wheelSpeed: 0.5, swipeEasing: !0, minScrollbarLength: 40, maxScrollbarLength: 300, suppressScrollX: true }">
        <li class="menu">
          <router-link to="/dashboard/users"  v-b-toggle class="dropdown-toggle" @click.prevent>
            <div class="">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1.25em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 640 512">
                <path
                  fill="currentColor"
                  d="M96 224c35.3 0 64-28.7 64-64s-28.7-64-64-64s-64 28.7-64 64s28.7 64 64 64zm448 0c35.3 0 64-28.7 64-64s-28.7-64-64-64s-64 28.7-64 64s28.7 64 64 64zm32 32h-64c-17.6 0-33.5 7.1-45.1 18.6c40.3 22.1 68.9 62 75.1 109.4h66c17.7 0 32-14.3 32-32v-32c0-35.3-28.7-64-64-64zm-256 0c61.9 0 112-50.1 112-112S381.9 32 320 32S208 82.1 208 144s50.1 112 112 112zm76.8 32h-8.3c-20.8 10-43.9 16-68.5 16s-47.6-6-68.5-16h-8.3C179.6 288 128 339.6 128 403.2V432c0 26.5 21.5 48 48 48h288c26.5 0 48-21.5 48-48v-28.8c0-63.6-51.6-115.2-115.2-115.2zm-223.7-13.4C161.5 263.1 145.6 256 128 256H64c-35.3 0-64 28.7-64 64v32c0 17.7 14.3 32 32 32h65.9c6.3-47.4 34.9-87.3 75.2-109.4z"
                />
              </svg>
              <span>{{ $t('Users') }}</span>
            </div>
          </router-link>
        </li>

        <li class="menu">
          <a href="#quest" v-b-toggle class="dropdown-toggle" @click.prevent>
            <div class="">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 512 512">
                <path
                  fill="currentColor"
                  d="M504 256c0 136.997-111.043 248-248 248S8 392.997 8 256C8 119.083 119.043 8 256 8s248 111.083 248 248zM262.655 90c-54.497 0-89.255 22.957-116.549 63.758c-3.536 5.286-2.353 12.415 2.715 16.258l34.699 26.31c5.205 3.947 12.621 3.008 16.665-2.122c17.864-22.658 30.113-35.797 57.303-35.797c20.429 0 45.698 13.148 45.698 32.958c0 14.976-12.363 22.667-32.534 33.976C247.128 238.528 216 254.941 216 296v4c0 6.627 5.373 12 12 12h56c6.627 0 12-5.373 12-12v-1.333c0-28.462 83.186-29.647 83.186-106.667c0-58.002-60.165-102-116.531-102zM256 338c-25.365 0-46 20.635-46 46c0 25.364 20.635 46 46 46s46-20.636 46-46c0-25.365-20.635-46-46-46z"
                />
              </svg>
              <span>{{ $t('Questions') }}</span>
            </div>
            <div>
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
            </div>
          </a>
          <b-collapse id="quest" accordion="menu">
            <ul class="collapse submenu list-unstyled show">
              <router-link tag="li" to="/dashboard/questionlist" @click.native="toggleMobileMenu"><a>Questions List</a></router-link>
              <router-link tag="li" to="/dashboard/questionrequests" @click.native="toggleMobileMenu"><a>Add Question requests</a></router-link>
            </ul>
          </b-collapse>
        </li>
        <li class="menu">
          <a href="#rep" v-b-toggle class="dropdown-toggle" @click.prevent>
            <div class="">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1.13em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1792 1600">
                <path
                  fill="currentColor"
                  d="M640 1018v70q0 42-39 59q-13 5-25 5q-27 0-45-19L19 621Q0 602 0 576t19-45L531 19q29-31 70-14q39 17 39 59v69L243 531q-19 19-19 45t19 45zm1152 38q0 58-17 133.5t-38.5 138t-48 125t-40.5 90.5l-20 40q-8 17-28 17q-6 0-9-1q-25-8-23-34q43-400-106-565q-64-71-170.5-110.5T1024 837v251q0 42-39 59q-13 5-25 5q-27 0-45-19L403 621q-19-19-19-45t19-45L915 19q29-31 70-14q39 17 39 59v262q411 28 599 221q169 173 169 509z"
                />
              </svg>
              <span>{{ $t('Replies') }}</span>
            </div>
            <div>
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
            </div>
          </a>
          <b-collapse id="rep" accordion="menu">
            <ul class="collapse submenu list-unstyled show">
              <router-link tag="li" to="/dashboard/replieslist" @click.native="toggleMobileMenu"><a>Replies List</a></router-link>
              <router-link tag="li" to="/dashboard/repliesrequests" @click.native="toggleMobileMenu"><a>Add Reply requests</a></router-link>
            </ul>
          </b-collapse>
        </li>
        <li class="menu">
          <a href="#comment" v-b-toggle class="dropdown-toggle" @click.prevent>
            <div class="">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1.13em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 576 512">
                <path
                  fill="currentColor"
                  d="M416 192c0-88.4-93.1-160-208-160S0 103.6 0 192c0 34.3 14.1 65.9 38 92c-13.4 30.2-35.5 54.2-35.8 54.5c-2.2 2.3-2.8 5.7-1.5 8.7S4.8 352 8 352c36.6 0 66.9-12.3 88.7-25c32.2 15.7 70.3 25 111.3 25c114.9 0 208-71.6 208-160zm122 220c23.9-26 38-57.7 38-92c0-66.9-53.5-124.2-129.3-148.1c.9 6.6 1.3 13.3 1.3 20.1c0 105.9-107.7 192-240 192c-10.8 0-21.3-.8-31.7-1.9C207.8 439.6 281.8 480 368 480c41 0 79.1-9.2 111.3-25c21.8 12.7 52.1 25 88.7 25c3.2 0 6.1-1.9 7.3-4.8c1.3-2.9.7-6.3-1.5-8.7c-.3-.3-22.4-24.2-35.8-54.5z"
                />
              </svg>
              <span>{{ $t('Comments') }}</span>
            </div>
            <div>
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
            </div>
          </a>
          <b-collapse id="comment" accordion="menu">
            <ul class="collapse submenu list-unstyled show">
              <router-link tag="li" to="/dashboard/commentslist" @click.native="toggleMobileMenu"><a>Comments List</a></router-link>
             
            </ul>
          </b-collapse>
        </li>
        <li class="menu">
          <a href="#services" v-b-toggle class="dropdown-toggle" @click.prevent>
            <div class="">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 512 512">
                <path
                  fill="currentColor"
                  d="M501.1 395.7L384 278.6c-23.1-23.1-57.6-27.6-85.4-13.9L192 158.1V96L64 0L0 64l96 128h62.1l106.6 106.6c-13.6 27.8-9.2 62.3 13.9 85.4l117.1 117.1c14.6 14.6 38.2 14.6 52.7 0l52.7-52.7c14.5-14.6 14.5-38.2 0-52.7zM331.7 225c28.3 0 54.9 11 74.9 31l19.4 19.4c15.8-6.9 30.8-16.5 43.8-29.5c37.1-37.1 49.7-89.3 37.9-136.7c-2.2-9-13.5-12.1-20.1-5.5l-74.4 74.4l-67.9-11.3L334 98.9l74.4-74.4c6.6-6.6 3.4-17.9-5.7-20.2c-47.4-11.7-99.6.9-136.6 37.9c-28.5 28.5-41.9 66.1-41.2 103.6l82.1 82.1c8.1-1.9 16.5-2.9 24.7-2.9zm-103.9 82l-56.7-56.7L18.7 402.8c-25 25-25 65.5 0 90.5s65.5 25 90.5 0l123.6-123.6c-7.6-19.9-9.9-41.6-5-62.7zM64 472c-13.2 0-24-10.8-24-24c0-13.3 10.7-24 24-24s24 10.7 24 24c0 13.2-10.7 24-24 24z"
                />
              </svg>
              <span>{{ $t('Services') }}</span>
            </div>
            <div>
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
            </div>
          </a>
          <b-collapse id="services" accordion="menu">
            <ul class="collapse submenu list-unstyled show">
              <router-link tag="li" to="/dashboard/servicelist" @click.native="toggleMobileMenu"><a>Services List</a></router-link>
              <router-link tag="li" to="/apps/mailbox" @click.native="toggleMobileMenu"><a>Create Requests</a></router-link>
            </ul>
          </b-collapse>
        </li>
        <li class="menu">
          <a href="#entreprises" v-b-toggle class="dropdown-toggle" @click.prevent>
            <div class="">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 36 36">
                <path
                  fill="currentColor"
                  d="M31 8h-9v25h11V10a2 2 0 0 0-2-2Zm-5 17h-2v-2h2Zm0-5h-2v-2h2Zm0-5h-2v-2h2Zm4 10h-2v-2h2Zm0-5h-2v-2h2Zm0-5h-2v-2h2Z"
                  class="clr-i-solid clr-i-solid-path-1"
                />
                <path
                  fill="currentColor"
                  d="M17.88 3H6.12A2.12 2.12 0 0 0 4 5.12V33h5v-3h6v3h5V5.12A2.12 2.12 0 0 0 17.88 3ZM9 25H7v-2h2Zm0-5H7v-2h2Zm0-5H7v-2h2Zm0-5H7V8h2Zm4 15h-2v-2h2Zm0-5h-2v-2h2Zm0-5h-2v-2h2Zm0-5h-2V8h2Zm4 15h-2v-2h2Zm0-5h-2v-2h2Zm0-5h-2v-2h2Zm0-5h-2V8h2Z"
                  class="clr-i-solid clr-i-solid-path-2"
                />
                <path fill="none" d="M0 0h36v36H0z" />
              </svg>
              <span>{{ $t('Entreprises') }}</span>
            </div>
            <div>
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
            </div>
          </a>
          <b-collapse id="entreprises" accordion="menu">
            <ul class="collapse submenu list-unstyled show">
              <router-link tag="li" to="/apps/chat" @click.native="toggleMobileMenu"><a>Enreprises List</a></router-link>
            </ul>
          </b-collapse>
        </li>
        <li class="menu">
          <a href="#promotion" v-b-toggle class="dropdown-toggle" @click.prevent>
            <div class="">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24">
                <path
                  fill="currentColor"
                  d="M12 2C6.486 2 2 6.486 2 12s4.486 10 10 10s10-4.486 10-10S17.514 2 12 2zm1 14.915V18h-2v-1.08c-2.339-.367-3-2.002-3-2.92h2c.011.143.159 1 2 1c1.38 0 2-.585 2-1c0-.324 0-1-2-1c-3.48 0-4-1.88-4-3c0-1.288 1.029-2.584 3-2.915V6.012h2v1.109c1.734.41 2.4 1.853 2.4 2.879h-1l-1 .018C13.386 9.638 13.185 9 12 9c-1.299 0-2 .516-2 1c0 .374 0 1 2 1c3.48 0 4 1.88 4 3c0 1.288-1.029 2.584-3 2.915z"
                />
              </svg>
              <span>{{ $t('Promotions') }}</span>
            </div>
            <div>
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
            </div>
          </a>
          <b-collapse id="promotion" accordion="menu">
            <ul class="collapse submenu list-unstyled show">
              <router-link tag="li" to="/apps/chat" @click.native="toggleMobileMenu"><a>Promoted Services</a></router-link>
              <router-link tag="li" to="/apps/mailbox" @click.native="toggleMobileMenu"><a>Promoted Entreprises</a></router-link>
              <router-link tag="li" to="/apps/todo-list" @click.native="toggleMobileMenu"><a>Services Requests</a></router-link>
              <router-link tag="li" to="/apps/todo-list" @click.native="toggleMobileMenu"><a>Entreprises Requests</a></router-link>
            </ul>
          </b-collapse>
        </li>
        <li class="menu">
          <a href="#groups" v-b-toggle class="dropdown-toggle" @click.prevent>
            <div class="">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24">
                <path
                  fill="currentColor"
                  d="M8.07 16c.09-.23.13-.39.91-.69c.97-.38 1.99-.56 3.02-.56s2.05.18 3.02.56c.77.3.81.46.91.69H8.07zM12 8c.55 0 1 .45 1 1s-.45 1-1 1s-1-.45-1-1s.45-1 1-1"
                  opacity=".3"
                />
                <path
                  fill="currentColor"
                  d="M4 13c1.1 0 2-.9 2-2s-.9-2-2-2s-2 .9-2 2s.9 2 2 2zm1.13 1.1c-.37-.06-.74-.1-1.13-.1c-.99 0-1.93.21-2.78.58A2.01 2.01 0 0 0 0 16.43V18h4.5v-1.61c0-.83.23-1.61.63-2.29zM20 13c1.1 0 2-.9 2-2s-.9-2-2-2s-2 .9-2 2s.9 2 2 2zm4 3.43c0-.81-.48-1.53-1.22-1.85A6.95 6.95 0 0 0 20 14c-.39 0-.76.04-1.13.1c.4.68.63 1.46.63 2.29V18H24v-1.57zm-7.76-2.78c-1.17-.52-2.61-.9-4.24-.9c-1.63 0-3.07.39-4.24.9A2.988 2.988 0 0 0 6 16.39V18h12v-1.61c0-1.18-.68-2.26-1.76-2.74zM8.07 16c.09-.23.13-.39.91-.69c.97-.38 1.99-.56 3.02-.56s2.05.18 3.02.56c.77.3.81.46.91.69H8.07zM12 8c.55 0 1 .45 1 1s-.45 1-1 1s-1-.45-1-1s.45-1 1-1m0-2c-1.66 0-3 1.34-3 3s1.34 3 3 3s3-1.34 3-3s-1.34-3-3-3z"
                />
              </svg>
              <span>{{ $t('Groups') }}</span>
            </div>
            <div>
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
            </div>
          </a>
          <b-collapse id="groups" accordion="menu">
            <ul class="collapse submenu list-unstyled show">
              <router-link tag="li" to="/apps/chat" @click.native="toggleMobileMenu"><a>Groups List</a></router-link>
              <router-link tag="li" to="/apps/mailbox" @click.native="toggleMobileMenu"><a>Create Group Requests</a></router-link>
              
            </ul>
          </b-collapse>
        </li>
        <li class="menu">
          <a href="#cars" v-b-toggle class="dropdown-toggle" @click.prevent>
            <div class="">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 512 512">
                <path
                  fill="currentColor"
                  d="M499.99 176h-59.87l-16.64-41.6C406.38 91.63 365.57 64 319.5 64h-127c-46.06 0-86.88 27.63-103.99 70.4L71.87 176H12.01C4.2 176-1.53 183.34.37 190.91l6 24C7.7 220.25 12.5 224 18.01 224h20.07C24.65 235.73 16 252.78 16 272v48c0 16.12 6.16 30.67 16 41.93V416c0 17.67 14.33 32 32 32h32c17.67 0 32-14.33 32-32v-32h256v32c0 17.67 14.33 32 32 32h32c17.67 0 32-14.33 32-32v-54.07c9.84-11.25 16-25.8 16-41.93v-48c0-19.22-8.65-36.27-22.07-48H494c5.51 0 10.31-3.75 11.64-9.09l6-24c1.89-7.57-3.84-14.91-11.65-14.91zm-352.06-17.83c7.29-18.22 24.94-30.17 44.57-30.17h127c19.63 0 37.28 11.95 44.57 30.17L384 208H128l19.93-49.83zM96 319.8c-19.2 0-32-12.76-32-31.9S76.8 256 96 256s48 28.71 48 47.85s-28.8 15.95-48 15.95zm320 0c-19.2 0-48 3.19-48-15.95S396.8 256 416 256s32 12.76 32 31.9s-12.8 31.9-32 31.9z"
                />
              </svg>
              <span>{{ $t('Cars') }}</span>
            </div>
            <div>
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
            </div>
          </a>
          <b-collapse id="cars" accordion="menu">
            <ul class="collapse submenu list-unstyled show">
              <router-link tag="li" to="/apps/chat" @click.native="toggleMobileMenu"><a>Cars List</a></router-link>
            </ul>
          </b-collapse>
        </li>
        <li class="menu">
          <a href="#rec" v-b-toggle class="dropdown-toggle" @click.prevent>
            <div class="">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 36 36">
                <path fill="currentColor" d="M21 12H7a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h14a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1ZM8 10h12V7.94H8Z" class="clr-i-outline clr-i-outline-path-1" />
                <path fill="currentColor" d="M21 14.08H7a1 1 0 0 0-1 1V19a1 1 0 0 0 1 1h11.36L22 16.3v-1.22a1 1 0 0 0-1-1ZM20 18H8v-2h12Z" class="clr-i-outline clr-i-outline-path-2" />
                <path
                  fill="currentColor"
                  d="M11.06 31.51v-.06l.32-1.39H4V4h20v10.25l2-1.89V3a1 1 0 0 0-1-1H3a1 1 0 0 0-1 1v28a1 1 0 0 0 1 1h8a3.44 3.44 0 0 1 .06-.49Z"
                  class="clr-i-outline clr-i-outline-path-3"
                />
                <path fill="currentColor" d="m22 19.17l-.78.79a1 1 0 0 0 .78-.79Z" class="clr-i-outline clr-i-outline-path-4" />
                <path fill="currentColor" d="M6 26.94a1 1 0 0 0 1 1h4.84l.3-1.3l.13-.55v-.05H8V24h6.34l2-2H7a1 1 0 0 0-1 1Z" class="clr-i-outline clr-i-outline-path-5" />
                <path
                  fill="currentColor"
                  d="m33.49 16.67l-3.37-3.37a1.61 1.61 0 0 0-2.28 0L14.13 27.09L13 31.9a1.61 1.61 0 0 0 1.26 1.9a1.55 1.55 0 0 0 .31 0a1.15 1.15 0 0 0 .37 0l4.85-1.07L33.49 19a1.6 1.6 0 0 0 0-2.27ZM18.77 30.91l-3.66.81l.89-3.63L26.28 17.7l2.82 2.82Zm11.46-11.52l-2.82-2.82L29 15l2.84 2.84Z"
                  class="clr-i-outline clr-i-outline-path-6"
                />
                <path fill="none" d="M0 0h36v36H0z" />
              </svg>
              <span>{{ $t('Reclamations') }}</span>
            </div>
            <div>
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
            </div>
          </a>
          <b-collapse id="rec" accordion="menu">
            <ul class="collapse submenu list-unstyled show">
              <router-link tag="li" to="/apps/chat" @click.native="toggleMobileMenu"><a>Reclamations List</a></router-link>
              
            </ul>
          </b-collapse>
        </li>

        <!--</ul>-->
      </perfect-scrollbar>
    </nav>
  </div>
  <!--  END SIDEBAR  -->
</template>
<script>
export default {
  data() {
    return { menu_collapse: 'dashboard' };
  },

  watch: {
    $route(to) {
      const selector = document.querySelector('#sidebar a[href="' + to.path + '"]');
      const ul = selector.closest('ul.collapse');
      if (!ul) {
        const ele = document.querySelector('.dropdown-toggle.not-collapsed');
        if (ele) {
          ele.click();
        }
      }
    },
  },

  mounted() {
    // default menu selection on refresh
    const selector = document.querySelector('#sidebar a[href="' + window.location.pathname + '"]');
    if (selector) {
      const ul = selector.closest('ul.collapse');
      if (ul) {
        let ele = ul.closest('li.menu').querySelectorAll('.dropdown-toggle');
        if (ele) {
          ele = ele[0];
          setTimeout(() => {
            ele.click();
          });
        }
      } else {
        selector.click();
      }
    }
  },

  methods: {
    toggleMobileMenu() {
      if (window.innerWidth < 991) {
        this.$store.commit('toggleSideBar', !this.$store.state.is_show_sidebar);
      }
    },
  },
};
</script>
