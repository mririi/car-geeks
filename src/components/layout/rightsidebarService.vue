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
    <a
          href="http://localhost:8080/addservice"
          
          class="mt-5 ml-5 mb-3"
          >
          <b-button variant="primary" class="mt-5">
          Add a Service</b-button></a
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
      serviceuser:false,
    };
  },
  created: function () {
    // a function to call getposts action
    this.GetServices();
    this.GetUsers();
    this.GetRoles();
    for (let u in this.Users){
      if(this.Users[u].id==this.User){
        this.CurrentUser=this.Users[u].id
      }
    }
    for (let r in this.Roles){
      if(this.Roles[r].userRole==this.CurrentUser && this.Roles[r].service==true){
        this.serviceuser=true
      }
    }
  },
  methods: {
    toggleCollapseShow: function (classes) {
      this.collapseShow = classes;
    },
    ...mapActions([
      "GetServices",
      "GetUsers",
      "GetRoles",
    ]),
  },
  components: {
    //NotificationDropdown,
    // UserDropdown,
  
  },
  computed: {
    ...mapGetters({
      Services: "StateServices",
      Roles: "StateRoles",
      Users: "StateUsers",
    }),
    isLoggedIn: function () {
      return this.$store.getters.isAuthenticated;
    },
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