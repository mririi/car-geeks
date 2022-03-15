<template>
  <div class="layout-px-spacing">
    <portal to="breadcrumb">
      <ul class="navbar-nav flex-row">
        <li>
          <div class="page-header">
            <nav class="breadcrumb-one" aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item active" aria-current="page"><span>Profile</span></li>
              </ol>
            </nav>
          </div>
        </li>
      </ul>
    </portal>

    <div class="row layout-spacing">
      <!-- Content -->
      <div class="col-xl-4 col-lg-6 col-md-5 col-sm-12 layout-top-spacing">
        <div class="user-profile layout-spacing">
          <div class="panel">
            <div class="panel-body">
              <div class="d-flex justify-content-between">
                <h3 class="">Profile</h3>
                <router-link :to="'/profile-edit/' + userprofile.id" v-if="CurrentUserprofile.id == userprofile.id" class="mt-2 edit-profile">
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
                    class="feather feather-edit-3"
                  >
                    <path d="M12 20h9"></path>
                    <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path>
                  </svg>
                </router-link>
              </div>
              <div class="text-center user-info">
                <img :src="'http://127.0.0.1:8000' + userprofile.imageU" width="150" height="150" alt="avatar" />
                <p class="">{{ userprofile.firstname }} {{ userprofile.lastname }}</p>
              </div>
              <div class="user-info-list">
                <div class="">
                  <ul class="contacts-block list-unstyled">
                    <li class="contacts-block__item">
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
                        class="feather feather-calendar"
                      >
                        <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                        <line x1="16" y1="2" x2="16" y2="6"></line>
                        <line x1="8" y1="2" x2="8" y2="6"></line>
                        <line x1="3" y1="10" x2="21" y2="10"></line></svg
                      >{{ userprofile.dateinscrit | formatDate }}
                    </li>
                    <li class="contacts-block__item">
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
                        class="feather feather-map-pin"
                      >
                        <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                        <circle cx="12" cy="10" r="3"></circle></svg
                      >{{ userprofile.country }}
                    </li>
                    <li class="contacts-block__item">
                      <div v-for="user in Users" :key="user.id">
                        <div v-if="user.id == userprofile.userU">
                          <a :href="'mailto:' + user.email" target="_blank"
                            ><svg
                              xmlns="http://www.w3.org/2000/svg"
                              width="24"
                              height="24"
                              viewBox="0 0 24 24"
                              fill="none"
                              stroke="currentColor"
                              stroke-width="2"
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              class="feather feather-mail"
                            >
                              <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                              <polyline points="22,6 12,13 2,6"></polyline></svg
                            >{{ user.email }}</a
                          >
                        </div>
                      </div>
                    </li>
                    <li class="contacts-block__item">
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
                        class="feather feather-phone"
                      >
                        <path
                          d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"
                        ></path>
                      </svg>
                      {{ userprofile.tel }}
                    </li>
                  </ul>
                </div>
                <div class="education ml-4 col-lg-8">
                  <span class="ml-4">Rate this profile</span>
                  <span v-if="isLoggedIn && existe == true">
                    <span v-b-modal.Rating>
                      <b-form-rating id="rating" v-model="average" color="primary" show-value show-value-max readonly size="lg" class="mb-2 bg-transparent border-0"> </b-form-rating>
                    </span>
                  </span>
                  <span v-else>
                    <a href="/auth/login">
                      <b-form-rating id="rating" v-model="average" vcolor="primary" show-value show-value-max readonly size="lg" class="mb-2 bg-transparent border-0"> </b-form-rating>
                    </a>
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <b-modal id="Rating" :title="'Rate ' + userprofile.firstname + ' ' + userprofile.lastname" centered>
        <b-form-rating id="rating" v-model="nbEval" precision="2" show-value-max show-value color="primary" size="lg" class="mb-2 bg-transparent border-0"> </b-form-rating>
        <template #modal-footer>
          <b-button variant="primary" @click="Rating()">Submit your rating</b-button>
        </template>
      </b-modal>
      <div class="col-xl-8 col-lg-6 col-md-7 col-sm-12 layout-top-spacing">
        <div class="skills layout-spacing">
          <div class="panel">
            <div class="panel-body">
              <h3 class="">Badges</h3>

              <b-progress variant="primary" :min="0" :max="100" show-progress class="br-30">
                <b-progress-bar :value="25" :label-html="`<div class='progress-title'><span>Bronze</span><span>25%</span></div>`"></b-progress-bar>
              </b-progress>
              <b-progress variant="primary" :min="0" :max="100" show-progress class="br-30">
                <b-progress-bar :value="50" :label-html="`<div class='progress-title'><span>Silver</span><span>50%</span></div>`"></b-progress-bar>
              </b-progress>
              <b-progress variant="primary" :min="0" :max="100" show-progress class="br-30">
                <b-progress-bar :value="70" :label-html="`<div class='progress-title'><span>Gold</span><span>70%</span></div>`"></b-progress-bar>
              </b-progress>
            </div>
          </div>
        </div>

        <div class="bio layout-spacing" v-if="userprofile.bio.length != 0">
          <div class="panel">
            <div class="panel-body">
              <h3 class="">Bio</h3>
              <p>
                {{ userprofile.bio }}
              </p>
            </div>
          </div>
        </div>
        <div class="education layout-spacing mt-4">
          <div class="panel">
            <div class="panel-body">
              <h3 class="">Activity</h3>
              <div class="timeline-alter">
                <div class="item-timeline">
                  <div class="t-meta-date">
                    <p class="">04 Mar 2009</p>
                  </div>
                  <div class="t-dot"></div>
                  <div class="t-text">
                    <p>Royal Collage of Art</p>
                    <p>Designer Illustrator</p>
                  </div>
                </div>
                <div class="item-timeline">
                  <div class="t-meta-date">
                    <p class="">25 Apr 2014</p>
                  </div>
                  <div class="t-dot"></div>
                  <div class="t-text">
                    <p>Massachusetts Institute of Technology (MIT)</p>
                    <p>Designer Illustrator</p>
                  </div>
                </div>
                <div class="item-timeline">
                  <div class="t-meta-date">
                    <p class="">04 Apr 2018</p>
                  </div>
                  <div class="t-dot"></div>
                  <div class="t-text">
                    <p>School of Art Institute of Chicago (SAIC)</p>
                    <p>Designer Illustrator</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12 layout-spacing">
      <div class="widget widget-recent-orders">
        <div class="widget-heading">
          <h5>Related Profile</h5>
          <div class="row mr-1 float-right">
            <div class="col-lg-12 col-md-12 col-sm-12 filtered-list-search-live mx-auto">
              <b-form class="form-inline my-2 my-lg-0 justify-content-center" @submit.prevent="search">
                <div class="w-100">
                  <b-input v-model="search" class="w-100 product-search br-25" placeholder="Search Profiles" @keyup="search"></b-input>
                </div>
              </b-form>
            </div>
          </div>
        </div>
        <div class="widget-content">
          <b-table-simple responsive>
            <b-thead>
              <b-tr>
                <b-th><div class="th-content">User</div></b-th>
                <b-th><div class="th-content">Email</div></b-th>
                <b-th><div class="th-content">Phone</div></b-th>
                <b-th><div class="th-content th-heading">Country</div></b-th>
                <b-th><div class="th-content">Questions number</div></b-th>
              </b-tr>
            </b-thead>

            <b-tbody>
              <b-tr v-for="u in filteredList" :key="u.id">
                <b-td
                  ><a :href="'/profile/' + u.id"
                    ><div class="td-content">
                      <img :src="'http://127.0.0.1:8000' + u.imageU" alt="avatar" /><span>{{ u.firstname }} {{ u.lastname }} </span>
                    </div></a
                  ></b-td
                >
                <b-td>
                  <div v-for="user in Users" :key="user.id">
                    <div v-if="user.id == u.userU" class="td-content text-primary">{{ user.email }}</div>
                  </div>
                </b-td>
                <b-td
                  ><div class="td-content">{{ u.tel }}</div></b-td
                >
                <b-td
                  ><div class="td-content">
                    <span>{{ u.country }}</span>
                  </div></b-td
                >
                <b-td
                  ><div class="td-content ml-5">{{ u.nbquestions }}</div></b-td
                >
              </b-tr>
            </b-tbody>
          </b-table-simple>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import '@/assets/sass/scrollspyNav.scss';
import '@/assets/sass/widgets/widgets.scss';
import '@/assets/sass/users/user-profile.scss';
import { mapGetters, mapActions } from 'vuex';
import axios from 'axios';
export default {
  metaInfo: { title: 'User Profile' },
  data() {
    return {
      CurrentUser: [],
      userprofile: [],
      CurrentUserprofile: [],
      nbEval: '',
      search: '',
      UserEval: '',
      average: 0,
      existe:false
    };
  },
  mounted() {},
  methods: {
    ...mapActions(['GetUsers', 'GetCars', 'GetUserprofiles', 'GetEvaluations', 'GetEvaluationProfile']),
    async Rating() {
      let done = false;
      if (this.EvaluationProfile.length == 0) {
        axios.post('/evaluationprofile/evaluationprofile-create/', {
          userprofileEval: this.$route.params.id,
          userEval: this.CurrentUser.id,
          nbEval: this.nbEval,
        });
        this.GetEvaluationProfile()
      } else {
        for (let e in this.EvaluationProfile) {
          if (this.EvaluationProfile[e].userprofileEval == this.$route.params.id && this.EvaluationProfile[e].userEval == this.CurrentUser.id) {
            axios.post('/evaluationprofile/evaluationprofile-update/' + this.EvaluationProfile[e].id + '/', {
              nbEval: this.nbEval,
            });
            done = true;
          }
        }
        if (done == false) {
          axios.post('/evaluationprofile/evaluationprofile-create/', {
            userprofileEval: this.$route.params.id,
            userEval: this.CurrentUser.id,
            nbEval: this.nbEval,
          });
        }
        this.GetEvaluationProfile()
      }
      this.$router.go();
    },
  },
  computed: {
    ...mapGetters({
      User: 'StateUser',
      Users: 'StateUsers',
      Userprofiles: 'StateUserprofiles',
      Evaluations: 'StateEvaluations',
      EvaluationProfile: 'StateEvaluationProfile',
    }),
    isLoggedIn: function () {
      return this.$store.getters.isAuthenticated;
    },
    filteredList() {
      return this.Userprofiles.filter((profile) => {
        return (
          profile.firstname.toLowerCase().includes(this.search.toLowerCase()) ||
          profile.lastname.toLowerCase().includes(this.search.toLowerCase()) ||
          profile.country.toLowerCase().includes(this.search.toLowerCase())
        );
      });
    },
  },
  created: function () {
    this.GetUsers();
    this.GetUserprofiles();
    this.GetCars();
    this.GetEvaluations();
    this.GetEvaluationProfile();
    for (let u in this.Users) {
      if (this.Users[u].username == this.User) {
        this.CurrentUser = this.Users[u];
      }
    }
    for (let p in this.Userprofiles) {
      if (this.Userprofiles[p].userU == this.CurrentUser.id) {
        this.CurrentUserprofile = this.Userprofiles[p];
        this.existe=true
      }
    }
    axios.get('/userprofile/userprofile-detail/' + this.$route.params.id + '/').then((response) => {
      this.userprofile = response.data;
      var sum = 0;
    var nb = 0;
    for (let e in this.EvaluationProfile) {
      if (this.EvaluationProfile[e].userprofileEval == this.$route.params.id) {
        sum += this.EvaluationProfile[e].nbEval;
        nb++;
      }
    }
    this.average = sum / nb;

    axios.put('/userprofile/userprofile-update/' + this.userprofile.id + '/', {
      nbEvalProfile: this.average,
    });
    this.userprofile.nbEvalProfile=this.average
    });

    
  },
};
</script>
