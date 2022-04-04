<template>
  <!--  BEGIN SIDEBAR  -->
  <div class="sidebar-wrapper sidebar-theme">
    <nav ref="menu" id="sidebar">
      <div class="shadow-bottom"></div>

      <perfect-scrollbar class="list-unstyled menu-categories" tag="ul" :options="{ wheelSpeed: 0.5, swipeEasing: !0, minScrollbarLength: 40, maxScrollbarLength: 300, suppressScrollX: true }">
        <li class="menu">
          <router-link :to="'/groupdashboard/'+this.$route.params.id+'/users'" v-b-toggle class="dropdown-toggle" @click.prevent>
            <div class="">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1.25em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 640 512">
                <path
                  fill="currentColor"
                  d="M96 224c35.3 0 64-28.7 64-64s-28.7-64-64-64s-64 28.7-64 64s28.7 64 64 64zm448 0c35.3 0 64-28.7 64-64s-28.7-64-64-64s-64 28.7-64 64s28.7 64 64 64zm32 32h-64c-17.6 0-33.5 7.1-45.1 18.6c40.3 22.1 68.9 62 75.1 109.4h66c17.7 0 32-14.3 32-32v-32c0-35.3-28.7-64-64-64zm-256 0c61.9 0 112-50.1 112-112S381.9 32 320 32S208 82.1 208 144s50.1 112 112 112zm76.8 32h-8.3c-20.8 10-43.9 16-68.5 16s-47.6-6-68.5-16h-8.3C179.6 288 128 339.6 128 403.2V432c0 26.5 21.5 48 48 48h288c26.5 0 48-21.5 48-48v-28.8c0-63.6-51.6-115.2-115.2-115.2zm-223.7-13.4C161.5 263.1 145.6 256 128 256H64c-35.3 0-64 28.7-64 64v32c0 17.7 14.3 32 32 32h65.9c6.3-47.4 34.9-87.3 75.2-109.4z"
                />
              </svg>
              <span>{{ $t('Members') }}</span>
            </div>
          </router-link>
        </li>

        <li class="menu">
          <a href="#quest" v-b-toggle class="dropdown-toggle" @click.prevent>
            <div class="">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24">
                <path
                  fill="currentColor"
                  d="M22 9V8c0-.55-.45-1-1-1s-1 .45-1 1v1h-1c-.55 0-1 .45-1 1s.45 1 1 1h1v1c0 .55.45 1 1 1s1-.45 1-1v-1h1c.55 0 1-.45 1-1s-.45-1-1-1h-1zM8 12c2.21 0 4-1.79 4-4s-1.79-4-4-4s-4 1.79-4 4s1.79 4 4 4zm0 1c-2.67 0-8 1.34-8 4v3h16v-3c0-2.66-5.33-4-8-4zm4.51-8.95C13.43 5.11 14 6.49 14 8s-.57 2.89-1.49 3.95C14.47 11.7 16 10.04 16 8s-1.53-3.7-3.49-3.95zm4.02 9.78C17.42 14.66 18 15.7 18 17v3h2v-3c0-1.45-1.59-2.51-3.47-3.17z"
                />
              </svg>
              <span>{{ $t('Join') }}</span>
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
              <router-link tag="li" :to="'/groupdashboard/'+this.$route.params.id+'/join'" @click.native="toggleMobileMenu"><a>User requests</a></router-link>
              <router-link tag="li" :to="'/groupdashboard/'+this.$route.params.id+'/entreprisejoin'" @click.native="toggleMobileMenu"><a>Entreprise requests</a></router-link>
            </ul>
          </b-collapse>
        </li>
        <li class="menu">
          <a href="#questcat" v-b-toggle class="dropdown-toggle" @click.prevent>
            <div class="">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24">
                <path
                  fill="currentColor"
                  d="M16 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V8l-5-5zM8 7h3c.55 0 1 .45 1 1s-.45 1-1 1H8c-.55 0-1-.45-1-1s.45-1 1-1zm8 10H8c-.55 0-1-.45-1-1s.45-1 1-1h8c.55 0 1 .45 1 1s-.45 1-1 1zm0-4H8c-.55 0-1-.45-1-1s.45-1 1-1h8c.55 0 1 .45 1 1s-.45 1-1 1zm-1-5V5l4 4h-3c-.55 0-1-.45-1-1z"
                />
              </svg>
              <span>{{ $t('Posts') }}</span>
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
          <b-collapse id="questcat" accordion="menu">
            <ul class="collapse submenu list-unstyled show">
              <router-link tag="li" :to="'/groupdashboard/'+this.$route.params.id+'/postslist'" @click.native="toggleMobileMenu"><a>Group posts</a></router-link>
              <router-link tag="li" :to="'/groupdashboard/'+this.$route.params.id+'/postrequests'" @click.native="toggleMobileMenu"><a>Posts requests</a></router-link>
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
