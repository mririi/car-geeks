<template>
  <div class="">
    <nav class="md:block mt-4 sizee shadow-xl dash items-center justify-between float-right">
      <div class="mt-5">
        <a href="/addquestion" class="mt-5 ml-5 mb-3"> <b-button variant="primary" class="mt-5"> {{ $t('Ask a question')}} </b-button></a>
      </div>
      <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12 layout-spacing mt-5">
        <div class="widget widget-expenses">
          <div class="widget-heading">
            <h5> {{ $t('Question of the week')}}</h5>
            <div class="task-action"></div>
          </div>

          <div class="widget-content">
            <p class="value">
              <span v-for="m in mostliked.slice(0, 1)" :key="m.id">
                <router-link :to="'/questionpage/'+m.id+'/'+m.slug">
                <span>Check here </span>
                </router-link>
              </span>
            </p>
          </div>
        </div>
      </div>
      <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12 layout-spacing">
        <div class="widget widget-visitor-by-browser">
          <div class="widget-heading">
            <h5>{{ $t('Members of the week')}}</h5>
          </div>
          <span v-for="u in sortedArray.slice(0, 4)" :key="u.id">
            <div class="widget-content">
              <div class="browser-list">
                <div class="w-icon icon-fill-primary">
                  <router-link :to="'/profile/' + u.id">
                    <b-avatar :src="u.imageU" size="2.5rem" rounded="lg" />
                  </router-link>
                </div>
                <div class="w-browser-details">
                  <div class="w-browser-info">
                    <h6>{{ u.firstname }}</h6>
                    <p class="browser-count">
                      {{ u.nbreplies }}
                      <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 20 20">
                        <path
                          fill="currentColor"
                          d="M7.225 5.767V3.086L0 9.542l7.225 6.691v-2.777L3 9.542l4.225-3.775zm5 1.186V3.086L5 9.542l7.225 6.691v-4.357c3.292 0 5.291.422 7.775 4.81c0-.001-.368-9.733-7.775-9.733z"
                        />
                      </svg>
                    </p>
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
      nbR: 0,
      mostliked: [],
    };
  },
  created: function () {
    // a function to call getposts action
    this.GetServices();
    this.GetQuestions();
    this.GetReplies();
    this.GetUserprofiles();
    this.nbR = this.Replies.length;
    this.mostliked = this.Questions.sort((a, b) => b.nblikes - a.nblikes);
    console.log(this.mostliked);
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