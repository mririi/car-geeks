<template>
  <div class="layout-px-spacing">
    <portal to="breadcrumb">
      <ul class="navbar-nav flex-row">
        <li>
          <div class="page-header">
            <nav class="breadcrumb-one" aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item active" aria-current="page"><span>Service Promotions informations</span></li>
              </ol>
            </nav>
          </div>
        </li>
      </ul>
    </portal>
    <div class="col-xl-12 col-lg-12 col-md-6 col-sm-12 col-12 mt-5 layout-spacing">
      <div class="widget widget-visitor-by-browser">
        <div class="widget-heading">
          <h5>Promotion Period</h5>
        </div>
        <div class="widget-content">
          <span v-for="sp in Servicepromotions" :key="sp.id">
            <span v-if="sp.Running==true">

           
            <div class="browser-list">
              <div class="w-icon icon-fill-primary">
                <span v-for="s in Services" :key="s.id">
                  <span v-if="sp.serviceP == s.id && s.userprofileS == CurrentUserProfile.id">
                    <router-link :to="'/servicedetails/' + s.id">
                      <b-avatar :src="'http://127.0.0.1:8000' + s.imageS" size="2.5rem" rounded="lg" />
                    </router-link>
                  </span>
                </span>
              </div>
              <div class="w-browser-details" v-if="getDatee < getDatee1(sp.dateP) + sp.nbDays">
                <div class="w-browser-info">
                  <h6>Left {{ getDatee1(sp.dateP) + parseInt(sp.nbDays) - getDatee }} Days</h6>
                  <p class="browser-count">{{ sp.nbDays }} Days</p>
                </div>
                <div class="w-browser-stats">
                  <b-progress variant="gradient-primary" :value="getDatee  - getDatee1(sp.dateP)" :min="1" :max="sp.nbDays"></b-progress>
                </div>
              </div>
              <div class="w-browser-details" v-else>
                <div class="w-browser-info">
                  <h6></h6>
                  <p class="browser-count">Expired</p>
                </div>
                <div class="w-browser-stats">
                  <b-progress variant="gradient-primary" :value="sp.nbDays" :min="1" :max="sp.nbDays"></b-progress>
                </div>
              </div>
            </div>
             </span>
          </span>
        </div>
      </div>
    </div>
    <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12 layout-spacing">
      <div class="widget widget-statistics">
        <div class="widget-heading">
          <h5>Statistics</h5>
          <div class="task-action"></div>
        </div>
        <div class="widget-content">
          <span v-for="sp1 in Servicepromotions" :key="sp1.id">
            <span v-if="sp1.Running==true">

            
            <span v-for="s1 in Services" :key="s1.id">
              <span v-if="sp1.serviceP == s1.id">
                <div class="row">
                  <div class="col-12">
                    <div class="w-detail">
                      <p class="w-title">Total Visits for {{s1.titleS}}</p>
                      <p class="w-stats">{{s1.nbvisits}}</p>
                    </div>
                    <apexchart v-if="total_visit_options" height="58" type="line" :options="total_visit_options" :series="total_visit_series"></apexchart>
                  </div>
                </div>
              </span>
            </span>
            </span>
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue';
import VueApexCharts from 'vue-apexcharts';
Vue.use(VueApexCharts);
Vue.component('apexchart', VueApexCharts);
import { mapGetters, mapActions } from 'vuex';
import '@/assets/sass/widgets/widgets.scss';
export default {
  metaInfo: { title: 'Promotion Info' },
  data() {
    return {
      total_visit_series: [{ data: [21, 9, 36, 12, 44, 25, 59, 41, 66, 25] }],
      paid_visit_series: [{ data: [22, 19, 30, 47, 32, 44, 34, 55, 41, 69] }],
      maxDate: '',
      valueDate: '',
      minDate: '',
      CurrentUser: [],
      CurrentUserProfile: [],
    };
  },
  created: function () {
    this.GetServices();
    this.GetServicetypes();
    this.GetServicepromotions();
    this.GetUserprofiles();
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
  },
  computed: {
    getDatee(){
      return new Date().getDate()
    },
    
    ...mapGetters({
      Services: 'StateServices',
      Servicepromotions: 'StateServicepromotions',
      Userprofiles: 'StateUserprofiles',
      Servicetypes: 'StateServicetypes',
      User: 'StateUser',
      Users: 'StateUsers',
    }),
    total_visit_options() {
      const is_dark = this.$store.state.is_dark_mode;
      return {
        chart: { sparkline: { enabled: true }, dropShadow: { enabled: true, top: 3, left: 1, blur: 3, color: '#009688', opacity: 0.7 } },
        stroke: { curve: 'smooth', width: 2 },
        markers: { size: 0 },
        colors: ['#009688'],
        grid: { padding: { top: 0, bottom: 0, left: 0 } },
        tooltip: {
          theme: is_dark ? 'dark' : 'light',
          x: { show: false },
          y: {
            title: {
              formatter: function formatter() {
                return '';
              },
            },
          },
        },
        responsive: [{ breakPoint: 576, options: { chart: { height: 95 }, grid: { padding: { top: 45, bottom: 0, left: 0 } } } }],
      };
    },
   
  },
  methods: {
    getDatee1: function(s){
      return new Date(s).getDate()
    },
    ...mapActions(['GetServices', 'GetServicepromotions', 'GetServicetypes', 'GetUsers', 'GetUserprofiles']),
  },
};
</script>
