<template>
  <div class="">
    <nav class="md:block mt-4 sizee shadow-xl dash items-center justify-between float-right">
      <div class="mt-5">
        <a href="/creategroup" class="mt-5 ml-5 mb-3"> <b-button variant="primary" class="mt-5"> Create Group</b-button></a>
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