<template>
  <div class="layout-px-spacing app-contacts">
    <portal to="breadcrumb">
      <ul class="navbar-nav flex-row">
        <li>
          <div class="page-header">
            <nav class="breadcrumb-one" aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="javascript:;">Dashboard</a></li>
                <li class="breadcrumb-item active" aria-current="page"><span>Users</span></li>
              </ol>
            </nav>
          </div>
        </li>
      </ul>
    </portal>

    <div class="row layout-spacing layout-top-spacing" id="cancel-row">
      <div class="col-lg-12">
        <div class="panel-body searchable-container" :class="[grid_type]">
          <div class="row">
            <div class="col-xl-4 col-lg-5 col-md-5 col-sm-7 filtered-list-search layout-spacing align-self-center">
              <form class="form-inline my-2 my-lg-0">
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
                    class="feather feather-search"
                  >
                    <circle cx="11" cy="11" r="8"></circle>
                    <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                  </svg>
                  <b-input v-model.trim="search" class="product-search" placeholder="Search Profiles..." />
                </div>
              </form>
            </div>

            <div class="col-xl-8 col-lg-7 col-md-7 col-sm-5 text-sm-right text-center layout-spacing align-self-center">
              <div class="d-flex justify-content-sm-end justify-content-center">
                

                <div class="switch align-self-center">
                  <a href="javascript:;" @click="grid_type = 'list'">
                    <svg
                      :class="{ 'active-view': grid_type == 'list' }"
                      xmlns="http://www.w3.org/2000/svg"
                      width="24"
                      height="24"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      stroke-width="2"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      class="feather feather-list view-list mr-1"
                    >
                      <line x1="8" y1="6" x2="21" y2="6"></line>
                      <line x1="8" y1="12" x2="21" y2="12"></line>
                      <line x1="8" y1="18" x2="21" y2="18"></line>
                      <line x1="3" y1="6" x2="3" y2="6"></line>
                      <line x1="3" y1="12" x2="3" y2="12"></line>
                      <line x1="3" y1="18" x2="3" y2="18"></line>
                    </svg>
                  </a>
                  
                </div>

               
              </div>
            </div>
          </div>

          <div class="searchable-items" :class="[grid_type]">
            <div class="items items-header-section">
              <div class="item-content">
                <div class="">
                  
                  <h4>Name</h4>
                </div>
                <div class="user-location">
                  <h4 style="margin-left: 270px">Country</h4>
                </div>
                <div class="user-phone">
                  <h4 style="margin-left: 190px">Phone</h4>
                </div>
                <div class="user-email">
                  <h4 style="margin-left: 100px">Questions number</h4>
                </div>
               
              </div>
            </div>

            <div v-for="user in filteredList" class="items" :key="user.id">
              <div class="item-content">
                <div class="user-profile">
                  <router-link :to="'/profile/'+user.id">
                  <img :src="'https://cargeeks.herokuapp.com' + user.imageU" alt="avatar" />
                   </router-link>
                  <div class="user-meta-info">
                    <p class="user-name">{{ user.firstname }} {{user.lastname}}</p>
                  
                  </div>
                </div>
                
                <div class="user-location">
                  <p class="info-title">Location:</p>
                  <p class="usr-location">{{ user.country }}</p>
                </div>
                <div class="user-phone">
                  <p class="info-title">Phone:</p>
                  <p class="usr-ph-no">{{ user.tel }}</p>
                </div>
                <div class="user-email">
                  <p class="info-title">Questions number:</p>
                  <p class="usr-email-addr mr-4">{{ user.nbquestions }}</p>
                </div>
               
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>
.searchable-container .switch {
  width: auto;
  height: auto;
}
.searchable-container .searchable-items.grid .items .user-profile .custom-checkbox {
  display: none !important;
}
</style>

<script>
import '@/assets/sass/apps/contacts.scss';
import axios from 'axios'
import { mapGetters, mapActions } from 'vuex';
export default {
  metaInfo: { title: 'Contact Profile' },
  components: {},
  computed: {
    check_all_checkbox() {
      if (this.contacts_list.length && this.ids.length == this.contacts_list.length) {
        return true;
      } else {
        return false;
      }
   
    },
    filteredList() {
      return this.Userprofiles.filter((profile) => {
        return (
          profile.firstname.toLowerCase().includes(this.search.toLowerCase()) ||
          profile.lastname.toLowerCase().includes(this.search.toLowerCase()) 
        );
      });
    },
        ...mapGetters({
      User: 'StateUser',
      Users: 'StateUsers',
      Userprofiles: 'StateUserprofiles'}),
  },
  data() {
    return {
      params: { id: null, name: '', email: '', role: '', phone: '', location: '' },
      contacts_list: [],
      filterd_contacts_list: [],
      search: '',
      ids: [],
      grid_type: 'list',
      CurrentUser: [],
      userprofile: [],
      CurrentUserprofile: [],
    };
  },
  mounted() {
    this.bind_contacts();
  },
  methods: { ...mapActions(['GetUsers', 'GetCars', 'GetUserprofiles']),

    
  },
  created: function () {
    this.GetUsers();
    this.GetUserprofiles();
    for (let u in this.Users) {
      if (this.Users[u].username == this.User) {
        this.CurrentUser = this.Users[u];
      }
    }
    for (let p in this.Userprofiles) {
      if (this.Userprofiles[p].userU == this.CurrentUser.id) {
        this.CurrentUserprofile = this.Userprofiles[p];
      }
    }
    axios.get('/userprofile/userprofile-detail/' + this.$route.params.id + '/').then((response) => {
      this.userprofile = response.data;
    });
  },
};
</script>
