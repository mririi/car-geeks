<template>
  <div >
    <nav
    
      class="
        md:block
        mt-4
        sizee
        shadow-xl
        dash
        
        items-center
        justify-between
        float-right
      "
    >
      <div class="mt-5">
        <router-link
          to="/addquestion"
          
          class="mt-5 ml-5 mb-3"
          >
          <b-button variant="primary" class="mt-5">
          Ask a question</b-button></router-link
        >
      </div>

    </nav>
  </div>
</template>

<script>
//import NotificationDropdown from "@/components/Dropdowns/NotificationDropdown.vue";
//import UserDropdown from "@/components/Dropdowns/UserDropdown.vue";
import { mapGetters, mapActions } from "vuex";
export default {
  data() {
    return {
      collapseShow: "hidden",
      nbQ: "",
      nbR: "",
      nbU: "",
    };
  },
  created: function () {
    // a function to call getposts action
    this.GetServices();
    this.GetQuestions();
    this.GetReplies();
    this.GetUserprofiles();
    this.nbQ = this.Questions.length;
    this.nbR = this.Replies.length;
    this.nbU = this.Userprofiles.length;
  },
  methods: {
    toggleCollapseShow: function (classes) {
      this.collapseShow = classes;
    },
    ...mapActions([
      "GetServices",
      "GetQuestions",
      "GetReplies",
      "GetUserprofiles",
    ]),
  },
  components: {
    //NotificationDropdown,
    // UserDropdown,
  
  },
  computed: {
    ...mapGetters({
      Services: "StateServices",
      Questions: "StateQuestions",
      Replies: "StateReplies",
      Userprofiles: "StateUserprofiles",
    }),
  },
};
</script>
<style scoped>
.dash {
  background-color: transparent;
}
.sizee {
  
  height: 900px;
  width: 220px;
  display: inline-block;
  border-left: 0.3px solid #0e1726;
}


.card-width {
  width: 120px;
  height: 120px;
  justify-content: center;
  margin-left: 50px;
}

</style>