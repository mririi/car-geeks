<template>
  <div class="col-xl-12 col-lg-12 col-md-12 mb-4 mt-4 float-container">
    <b-card class="b-l-card-1">
           <div class="float-right bg-warning" style="border-radius:100px ; padding:5px" v-if="CurrentUserProfile.id==service.userprofileS">
                  <a :href="'/updateservice/'+service.id"><svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    class="feather feather-edit-3"
                  >
                    <path d="M12 20h9"></path>
                    <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path>
                  </svg> </a>
                  
             </div>   
      <div class="float-child">
        <img :src="'http://127.0.0.1:8000'+service.imageS" class="img-fluid img-thumbnail mt-5" style="height:350px ; width:100%" />
      </div>
      <div class="float-child">
        <strong class="card-category ml-4"> <b-badge variant="warning"> {{type.descT}} </b-badge></strong>
        <h4 class="card-title mt-4 ml-4">{{service.titleS}}</h4>
        <p class="card-text meta-info meta-time mb-4 ml-4"><small class="">{{service.dateS | formatDate}}</small></p>
        <p class="card-text mb-2 ml-4">{{service.details}}</p>
        <div class="w-50">
        <b-form-rating id="rating" variant="warning" size="lg" class="mb-2 bg-transparent border-0">
                </b-form-rating>
                </div>
        <h6 class="mb-4 ml-4"> <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 100 100"><path fill="currentColor" d="M88.286 67.965c-.022-.038-.052-.069-.076-.105l.002-.001L61.307 21.26l-.015.008a2.08 2.08 0 0 0-.929-.801l.038-.022l-7.986-4.612l8.871 15.365l20.178 34.949l-.002.001c.024.036.054.067.076.105a2.091 2.091 0 0 1-.765 2.855l.014.025l-29.861 17.24l1.293 2.239c.026.055.044.112.075.166a2.085 2.085 0 0 0 2.772.801l.005.008l32.465-18.743l-.014-.025a2.09 2.09 0 0 0 .764-2.854z"/><path fill="currentColor" d="M73.88 67.143a2.091 2.091 0 0 0 .765-2.855c-.022-.038-.052-.069-.076-.105l.002-.001l-26.905-46.599l-.015.008a2.08 2.08 0 0 0-.929-.801l.038-.022l-11.01-6.357v.044a2.082 2.082 0 0 0-1.846-.107l-.012-.021l-.206.119c-.004.003-.009.003-.013.006s-.007.006-.012.008L12.478 22.69a2.078 2.078 0 0 0-1.037 1.764l-.007-.004v12.714l.021-.012c-.047.427.03.872.261 1.273c.014.024.032.042.047.065l26.815 46.446c.026.055.044.112.075.166a2.085 2.085 0 0 0 2.772.801l.005.008l32.465-18.743l-.015-.025zM29.545 27.522a3.865 3.865 0 1 1 1.415-5.279a3.862 3.862 0 0 1-1.415 5.279z"/></svg> : <b-badge variant="success"> {{service.priceS}} DT </b-badge></h6>
        <h6 class="card-text mb-4 ml-4"><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path fill="currentColor" d="M16 2A11.013 11.013 0 0 0 5 13a10.889 10.889 0 0 0 2.216 6.6s.3.395.349.452L16 30l8.439-9.953c.044-.053.345-.447.345-.447l.001-.003A10.885 10.885 0 0 0 27 13A11.013 11.013 0 0 0 16 2Zm0 15a4 4 0 1 1 4-4a4.005 4.005 0 0 1-4 4Z"/><circle cx="16" cy="13" r="4" fill="none"/></svg> : {{service.addressS}}</h6>
        <h6 class="card-text mb-4 ml-4"><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 20 20"><path fill="currentColor" d="M19 14.5v-9c0-.83-.67-1.5-1.5-1.5H3.49c-.83 0-1.5.67-1.5 1.5v9c0 .83.67 1.5 1.5 1.5H17.5c.83 0 1.5-.67 1.5-1.5zm-1.31-9.11c.33.33.15.67-.03.84L13.6 9.95l3.9 4.06c.12.14.2.36.06.51c-.13.16-.43.15-.56.05l-4.37-3.73l-2.14 1.95l-2.13-1.95l-4.37 3.73c-.13.1-.43.11-.56-.05c-.14-.15-.06-.37.06-.51l3.9-4.06l-4.06-3.72c-.18-.17-.36-.51-.03-.84s.67-.17.95.07l6.24 5.04l6.25-5.04c.28-.24.62-.4.95-.07z"/></svg> : <a :href="'mailto:' + service.email" target="_blank"> {{service.email}} </a></h6>
        <h6 class="card-text mb-4 ml-4"><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path fill="currentColor" d="m20.33 21.48l2.24-2.24a2.19 2.19 0 0 1 2.34-.48l2.73 1.09a2.18 2.18 0 0 1 1.36 2v5A2.17 2.17 0 0 1 26.72 29C7.59 27.81 3.73 11.61 3 5.41A2.17 2.17 0 0 1 5.17 3H10a2.16 2.16 0 0 1 2 1.36l1.09 2.73a2.16 2.16 0 0 1-.47 2.34l-2.24 2.24s1.29 8.73 9.95 9.81Z"/></svg> : {{service.contactS}}</h6>
        <h6 class="card-text mb-4 ml-4"><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 512 512"><path fill="currentColor" d="M213.3 384c0-87 65.2-158.7 149.3-169.2v-1.5c5.5-8 21.3-21.3 21.3-42.7s-21.3-42.7-21.3-53.3C362.7 32 319.2 0 256 0c-60.5 0-106.7 32-106.7 117.3c0 10.7-21.3 32-21.3 53.3s15.2 35.4 21.3 42.7c0 0 0 21.3 10.7 53.3c0 10.7 21.3 21.3 32 32c0 10.7 0 21.3-10.7 42.7L64 362.7C21.3 373.3 0 448 0 512h271.4c-35.5-31.3-58.1-77-58.1-128zM384 256c-70.7 0-128 57.3-128 128s57.3 128 128 128s128-57.3 128-128s-57.3-128-128-128zm85.3 149.3h-64v64h-42.7v-64h-64v-42.7h64v-64h42.7v64h64v42.7z"/></svg> : <router-link :to="'/profile/'+userprofile.id"> {{userprofile.firstname}} {{userprofile.lastname}} </router-link> </h6>
      </div>
    </b-card>
  </div>
</template>

<script>
import axios from 'axios';
import { mapGetters, mapActions } from 'vuex';
export default {
  data() {
    return {
      service: [],
      userprofile: [],
      type: [],
      CurrentUser: [],
      CurrentUserProfile: [],
    };
  },

  created: function () {
    this.GetService();
    this.GetUserprofiles();
    this.GetServicetypes();
    this.GetUsers();
    for (let u in this.Users) {
      if (this.Users[u].username == this.User) {
        this.CurrentUser = this.Users[u];
      }
    }
    for (let u in this.Userprofiles) {
      if (this.Userprofiles[u].userU == this.CurrentUser.id) {
        this.CurrentUserProfile = this.Userprofiles[u];
      }
    }

    axios.get('/service/service-detail/' + this.$route.params.id + '/').then((response) => {
      this.service = response.data;

      for (let u in this.Userprofiles) {
        if (this.Userprofiles[u].id == this.service.userprofileS) {
          this.userprofile = this.Userprofiles[u];
        }
      }

      for (let t in this.Servicetypes) {
        if (this.Servicetypes[t].id == this.service.typeS) {
          this.type = this.Servicetypes[t];
        }
      }
    });
  },
  methods: {
    ...mapActions(['GetService', 'GetUserprofiles', 'GetServicetypes', 'GetUsers']),
  },
  computed: {
    ...mapGetters({
      Service: 'StateService',
      Userprofiles: 'StateUserprofiles',
      Servicetypes: 'StateServicetypes',
      User: 'StateUser',
      Users: 'StateUsers',
    }),
  },
};
</script>

<style scoped>
.float-container {
  padding: 10px;
}

.float-child {
  width: 50%;
  float: left;
  padding: 10px;
}
</style>>
