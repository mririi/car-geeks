<template>
  <div class="layout-px-spacing">
    <portal to="breadcrumb">
      <ul class="navbar-nav flex-row">
        <li>
          <div class="page-header">
            <nav class="breadcrumb-one" aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item active" aria-current="page"><span>Entreprise Promotions informations</span></li>
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
          <span v-for="sp in Entreprisepromotions" :key="sp.id">
            <span v-if="sp.Running==true">
          <span v-for="s in Userentreprises" :key="s.id">
                  <span v-if="sp.entreprisePE == s.id && s.id == CurrentUserEntreprise.id">
            <div class="browser-list mb-5">
              <div class="w-icon icon-fill-primary">
                    <router-link :to="'/entreprisedetails/' + s.id">
                      <b-avatar :src=" s.imageE" size="2.5rem" rounded="lg" />
                    </router-link>
                  
              </div>
              <div class="w-browser-details" v-if="getDatee < getDatee1(sp.datePE) + parseInt(sp.nbDays)">
                <div class="w-browser-info">
                  <h6>Left {{ getDatee1(sp.datePE) + parseInt(sp.nbDays) - getDatee }} Days</h6>
                  <p class="browser-count">{{ sp.nbDays }} Days</p>
                </div>
                <div class="w-browser-stats">
                  <b-progress variant="gradient-primary" :value="getDatee  - getDatee1(sp.datePE)" :min="1" :max="sp.nbDays"></b-progress>
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
          <span v-for="sp1 in Entreprisepromotions" :key="sp1.id">
            <span v-if="sp1.Running==true ">
            <span v-for="s1 in Userentreprises" :key="s1.id">
              <span v-if="sp1.entreprisePE == s1.id && CurrentUserEntreprise.id==s1.id">
                <div class="row">
                  <div class="col-12 ">
                    <div class="w-detail">
                      <p class="w-title">Total Visits for {{s1.name}}</p>
                      <p class="w-stats">{{s1.nbvisits}}</p>
                    </div>
                    <apexchart v-if="total_visit_options" height="58" type="line" class="mb-4" :options="total_visit_options" :series="total_visit_series"></apexchart>
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
      CurrentUserEntreprise: [],
    };
  },
  created: function () {
    this.GetEntreprisepromotions();
    this.GetUserentreprises();
    this.GetUsers();
    for (let u in this.Users) {
      if (this.Users[u].username == this.User) {
        this.CurrentUser = this.Users[u];
      }
    }
    for (let u in this.Userentreprises) {
      if (this.Userentreprises[u].userE == this.CurrentUser.id) {
        this.CurrentUserEntreprise = this.Userentreprises[u];
        if(this.Userentreprises[u].promoted==false){
          this.$router.push('/entreprises')
        }
      }
    }
  },
  computed: {
    getDatee(){
      return new Date().getDate()
    },
    
    ...mapGetters({
      Entreprisepromotions: 'StateEntreprisepromotions',
      Userentreprises: 'StateUserentreprises',
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
    ...mapActions(['GetEntreprisepromotions',  'GetUsers', 'GetUserentreprises']),
  },
};
</script>
