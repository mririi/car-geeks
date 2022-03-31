<template>
  <div class="">
    <nav class="md:block mt-4 sizee shadow-xl dash items-center justify-between float-right">
      <div class="mt-5">
        <a href="/addquestion" class="mt-5 ml-5 mb-3"> <b-button variant="primary" class="mt-5"> Ask a question</b-button></a>
      </div>
      <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12 layout-spacing mt-5">
        <div class="widget widget-expenses">
          <div class="widget-heading">
            <h5>Questions</h5>
            <div class="task-action"></div>
          </div>

          <div class="widget-content">
            <p class="value">
              <span>this week </span>
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
                class="feather feather-trending-up"
              >
                <polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline>
                <polyline points="17 6 23 6 23 12"></polyline>
              </svg>
            </p>
            <div class="w-progress-stats">
              <b-progress variant="gradient-secondary" :value="57" :min="0" :max="100"></b-progress>
              <div class="w-icon">57%</div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12 layout-spacing">
        <div class="widget widget-visitor-by-browser">
          <div class="widget-heading">
            <h5>Members of the week</h5>
          </div>
          <span v-for="u in sortedArray.slice(0, 4)" :key="u.id">
            
              <div class="widget-content">
                <div class="browser-list">
                  <div class="w-icon icon-fill-primary">
                    <router-link :to="'/profile/' + u.id">
                  <b-avatar :src="'http://127.0.0.1:8000' + u.imageU" size="2.5rem" rounded="lg" />
                    </router-link>
                  </div>
                  <div class="w-browser-details">
                    <div class="w-browser-info">
                      <h6>{{u.firstname}}</h6>
                      <p class="browser-count">{{u.nbreplies}} <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 20 20"><path fill="currentColor" d="M7.225 5.767V3.086L0 9.542l7.225 6.691v-2.777L3 9.542l4.225-3.775zm5 1.186V3.086L5 9.542l7.225 6.691v-4.357c3.292 0 5.291.422 7.775 4.81c0-.001-.368-9.733-7.775-9.733z"/></svg></p>
                    </div>
                    <div class="w-browser-stats">
                      <b-progress variant="gradient-success" :value="u.nbreplies" :min="0" :max="nbR"></b-progress>
                    </div>
                  </div>
                </div>
              </div>
            
          </span>
        </div>
      </div>

      <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12 layout-spacing">
        <div class="widget widget-summary">
          <div class="widget-heading">
            <h5>Top categories</h5>
          </div>
          <div class="widget-content">
            <div class="summary-list">
              <div class="w-icon">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="17"
                  height="17"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  class="feather feather-shopping-bag"
                >
                  <path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path>
                  <line x1="3" y1="6" x2="21" y2="6"></line>
                  <path d="M16 10a4 4 0 0 1-8 0"></path>
                </svg>
              </div>
              <div class="w-summary-details">
                <div class="w-summary-info">
                  <h6>Income</h6>
                  <p class="summary-count">$92,600</p>
                </div>
                <div class="w-summary-stats">
                  <b-progress variant="gradient-secondary" :value="90" :min="0" :max="100"></b-progress>
                </div>
              </div>
            </div>

            <div class="summary-list">
              <div class="w-icon">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="17"
                  height="17"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  class="feather feather-tag"
                >
                  <path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"></path>
                  <line x1="7" y1="7" x2="7" y2="7"></line>
                </svg>
              </div>
              <div class="w-summary-details">
                <div class="w-summary-info">
                  <h6>Profit</h6>
                  <p class="summary-count">$37,515</p>
                </div>
                <div class="w-summary-stats">
                  <b-progress variant="gradient-success" :value="65" :min="0" :max="100"></b-progress>
                </div>
              </div>
            </div>

            <div class="summary-list">
              <div class="w-icon">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="17"
                  height="17"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  class="feather feather-credit-card"
                >
                  <rect x="1" y="4" width="22" height="16" rx="2" ry="2"></rect>
                  <line x1="1" y1="10" x2="23" y2="10"></line>
                </svg>
              </div>
              <div class="w-summary-details">
                <div class="w-summary-info">
                  <h6>Expenses</h6>
                  <p class="summary-count">$55,085</p>
                </div>
                <div class="w-summary-stats">
                  <b-progress variant="gradient-warning" :value="80" :min="0" :max="100"></b-progress>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
//import NotificationDropdown from "@/components/Dropdowns/NotificationDropdown.vue";
//import UserDropdown from "@/components/Dropdowns/UserDropdown.vue";
import '@/assets/sass/widgets/widgets.scss';
import { mapGetters, mapActions } from 'vuex';
export default {
  data() {
    return {
      collapseShow: 'hidden',
      nbR:0
    };
  },
  created: function () {
    // a function to call getposts action
    this.GetServices();
    this.GetQuestions();
    this.GetReplies();
    this.GetUserprofiles();
    this.nbR=this.Replies.length
  },
  methods: {
    toggleCollapseShow: function (classes) {
      this.collapseShow = classes;
    },
    ...mapActions(['GetServices', 'GetQuestions', 'GetReplies', 'GetUserprofiles']),
  },
  components: {},
  computed: {
    ...mapGetters({
      Services: 'StateServices',
      Questions: 'StateQuestions',
      Replies: 'StateReplies',
      Userprofiles: 'StateUserprofiles',
    }),
    isLoggedIn: function () {
      return this.$store.getters.isAuthenticated;
    },
    sortedArray: function () {
      function compare(a, b) {
        if (a.nbreplies > b.nbreplies) return -1;
        if (a.nbreplies < b.nbreplies) return 1;
        return 0;
      }

      return this.Userprofiles.slice(0).sort(compare);
    },
  },
};
</script>
<style scoped>
.dash {
  background-color: transparent;
}
.sizee {
  height: 300vh;
  width: 220px;
  display: inline-block;
  border-left: 0.1px solid #0e1726;
}

.card-width {
  width: 120px;
  height: 120px;
  justify-content: center;
  margin-left: 50px;
}
</style>