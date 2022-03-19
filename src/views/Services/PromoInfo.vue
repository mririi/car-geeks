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
                        <span v-for="s in Services" :key="s.id">
                        <div class="browser-list">
                            <div class="w-icon icon-fill-primary">
                                <router-link :to="'/servicedetails/'+s.id">
                                <b-avatar :src="'http://127.0.0.1:8000'+s.imageS" size="2.5rem" rounded="lg"/>
                                </router-link>
                            </div>
                            <div class="w-browser-details">
                                <div class="w-browser-info">
                                    <h6>Left</h6>
                                    <p class="browser-count">7 Days</p>
                                </div>
                                <div class="w-browser-stats">
                                    <b-progress variant="gradient-primary" :value="4" :min="1" :max="7"></b-progress>
                                </div>
                            </div>
                        </div>
                      
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
        metaInfo: { title: 'Comming Soon' },
        data() {
            return {
                
            };
        },
        created: function () {
        this.GetServices();
        this.GetServicetypes();
        this.GetServicepromotions();

        },
        computed:{
 ...mapGetters({
      Services: 'StateServices',
      Servicepromotions: 'StateServicepromotions',
      Userprofiles: 'StateUserprofiles',
      Servicetypes: 'StateServicetypes',
      User: 'StateUser',
      Users: 'StateUsers',
    }),
        },
        methods: {
          ...mapActions(['GetServices','GetServicepromotions','GetServicetypes', 'GetUsers', 'GetUserprofiles']),
        }
    };
</script>
