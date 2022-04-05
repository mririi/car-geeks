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
          <b-button v-show="serviceuser==true || CurrentUser.is_superuser==true" href="https://cargeeksjs.herokuapp.com/addservice" variant="primary" class="mt-5 ml-5">
          Add a Service</b-button>
          <b-button  v-show="serviceuser==false&& CurrentUser.is_superuser==false" v-b-modal.verify variant="primary" class="mt-5 ml-5 mb-3">
          Get Verified</b-button>
    </div>
    <div >
    <router-link v-if="promo==true"
          to="https://cargeeksjs.herokuapp.com/promoinfo"
          
          class=" ml-5 mb-3"
          >
          <b-button variant="warning" class="mt-3">
          My Promotions</b-button></router-link
        >
    </div>
        
      <b-modal id="verify" title="Send Request" centered>
        <label >Insert patent <span style="color:red">*</span></label>
                    <div class="mb-4">
                      <b-file @change="onFileChanged" :class="[is_submit_form1 ? (image ? 'is-valid' : 'is-invalid') : '']"></b-file>
                    
                    </div>
      <template #modal-footer>
        <b-button variant="primary" @click="submit()">Send</b-button>
      </template>
    </b-modal>
      

    </nav>
  </div>
</template>

<script>
import axios from 'axios'
//import NotificationDropdown from "@/components/Dropdowns/NotificationDropdown.vue";
//import UserDropdown from "@/components/Dropdowns/UserDropdown.vue";
import { mapGetters, mapActions } from "vuex";
export default {
  data() {
    return {
      collapseShow: "hidden",
      serviceuser:false,
      promo:false,
      CurrentUserProfile:[],
      CurrentUserEntreprise:[],
      CurrentUser:[],
      image:null,
      is_submit_form1:false
    };
  },
  created: function () {
    // a function to call getposts action
    this.GetServices();
    this.GetUsers();
    this.GetRoles();
    this.GetServicepromotions();
    this.GetUserprofiles();
    this.GetUserentreprises();
    for (let u in this.Users){
      if(this.Users[u].username==this.User){
        this.CurrentUser=this.Users[u]
        for(let up in this.Userprofiles){
       if(this.Userprofiles[up].userU==this.CurrentUser.id){
         this.CurrentUserProfile=this.Userprofiles[up]
         for(let p in this.Servicepromotions){
      axios.get('/service/service-detail/' + this.Servicepromotions[p].serviceP + '/').then((response) => {
      if(response.data.userprofileS==this.CurrentUserProfile.id && response.data.promoted==true){
        this.promo=true
      }})
    }
       }
     }
      }
    }
    if(this.promo==false)
    {
    for (let u in this.Users){
      if(this.Users[u].username==this.User){
        this.CurrentUser=this.Users[u]
        for(let ue in this.Userentreprises){
       if(this.Userentreprises[ue].userE==this.CurrentUser.id){
         this.CurrentUserEntreprise=this.Userentreprises[ue]
         for(let p in this.Servicepromotions){
      axios.get('/service/service-detail/' + this.Servicepromotions[p].serviceP + '/').then((response) => {
      if(response.data.userentrepriseS==this.CurrentUserEntreprise.id && response.data.promoted==true){
        this.promo=true
      }})
    }
       }
     }
      }
      }
    }
    for (let r in this.Roles){
      if(this.Roles[r].userRole==this.CurrentUser.id   && this.Roles[r].service==true){
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
      "GetServicepromotions",
      "GetUserprofiles",
      'GetUserentreprises',
      'CreateNotification',
    ]),
    onFileChanged (event) {
      this.image = event.target.files[0]
      console.log(this.image)
    },
    async submit() {
      try {
        this.is_submit_form1 = true;
                if (
                  this.image
                ) {
        
      var formdata = new FormData();
      
        formdata.append("imageVerif", this.image);
      
        
        await axios.put('/userprofile/userprofile-update/'+this.CurrentUserProfile.id+'/',formdata);
        this.$bvModal.hide('verify');
        await this.CreateNotification({message:' requested a Verification !',byuserprofileNo:this.CurrentUserProfile.id,foradmin:true})
        this.$swal('Good Job!', 'Your request has been sent successfuly, Please wait for the administator to accept it !', 'success');
        this.$router.push("/services");
        }
      } catch (error) {
        throw "Il ya un error!"
      }
    },
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
      User:"StateUser",
      Servicepromotions:"StateServicepromotions",
      Userprofiles:"StateUserprofiles",
      Userentreprises: 'StateUserentreprises',
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