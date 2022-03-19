<template>
  <div class="layout-px-spacing">
    <portal to="breadcrumb">
      <ul class="navbar-nav flex-row">
        <li>
          <div class="page-header">
            <nav class="breadcrumb-one" aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item active" aria-current="page"><span>Entreprises</span></li>
              </ol>
            </nav>
          </div>
        </li>
      </ul>
    </portal>
    <div>
      <div class="mr-1 mt-2 d-flex justify-content-center w-25">
        <div class="col-lg-12 col-md-12 col-sm-12 filtered-list-search-live mx-auto">
          <b-form class="form-inline my-2 my-lg-0 justify-content-center" @submit.prevent="search">
            <div class="w-100">
              <b-input v-model="search" class="w-100 product-search br-25" placeholder="Search Entreprises" @keyup="search"></b-input>
            </div>
          </b-form>
        </div>
      </div>
    </div>
    <div class="col-lg-12 layout-spacing">
      <div class="panel-heading"></div>
      <div class="panel-body">
        <div class="container pricing-table">
          <div id="pricingWrapper" class="row" v-for="s in filterByPromoted" :key="s.id">
            
              <div class="col-md-6 col-lg-4">
                <b-card class="stacked mt-5" header-class="pt-0">
                  <template #header>
                        <b-badge variant="danger" class="float-right mt-1">Promoted</b-badge>
                    <span class="card-price"><b-avatar :src="'http://127.0.0.1:8000' + s.imageE" size="5.5rem" class="mb-2" rounded="lg" alt="..." /></span>
                    <h3 class="card-title mt-3 mb-1">{{s.nameE}}</h3>
                    <p>{{s.typeE}}</p>
                  </template>
                  <b-list-group class="list-group-minimal mb-3">
                    <b-list-group-item><b-form-rating id="rating" v-model="s.nbEval"  readonly variant="warning" size="lg" class=" bg-transparent border-0 w-25">
                                    </b-form-rating></b-list-group-item>
                    <b-list-group-item class="ml-4"><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32">
                        <path fill="currentColor" d="M24 13h-2a3.003 3.003 0 0 0-3-3V8a5.006 5.006 0 0 1 5 5Z" />
                        <path
                          fill="currentColor"
                          d="M28 13h-2a7.008 7.008 0 0 0-7-7V4a9.01 9.01 0 0 1 9 9zm-7.667 8.482l2.24-2.24a2.167 2.167 0 0 1 2.337-.48l2.728 1.092A2.167 2.167 0 0 1 29 21.866v4.961a2.167 2.167 0 0 1-2.284 2.169C7.594 27.806 3.732 11.61 3.015 5.408A2.162 2.162 0 0 1 5.169 3h4.873a2.167 2.167 0 0 1 2.012 1.362l1.091 2.728a2.167 2.167 0 0 1-.48 2.337l-2.24 2.24s1.242 8.732 9.908 9.815z"
                        />
                      </svg>
                      {{ s.contactE }}</b-list-group-item>
                    <b-list-group-item class="ml-4"><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path fill="currentColor" d="M16 2A11.013 11.013 0 0 0 5 13a10.889 10.889 0 0 0 2.216 6.6s.3.395.349.452L16 30l8.439-9.953c.044-.053.345-.447.345-.447l.001-.003A10.885 10.885 0 0 0 27 13A11.013 11.013 0 0 0 16 2Zm0 15a4 4 0 1 1 4-4a4.005 4.005 0 0 1-4 4Z"/><circle cx="16" cy="13" r="4" fill="none"/></svg> {{s.country}} </b-list-group-item>
                    
                  </b-list-group>
                  <b-button tag="a" variant="primary" :href="'/entreprisedetails/'+s.id" block>Explore more</b-button>
                </b-card>
              </div>
            
          </div>
          <div id="pricingWrapper" class="row" v-for="s in filterByNotPromoted" :key="s.id">
            
              <div class="col-md-6 col-lg-4">
                <b-card class="stacked mt-5" header-class="pt-0">
                  <template #header>
                    
                    <span class="card-price"><b-avatar :src="'http://127.0.0.1:8000' + s.imageE" size="5.5rem" class="mb-2" rounded="lg" alt="..." /></span>
                    <h3 class="card-title mt-3 mb-1">{{s.nameE}}</h3>
                    <p>{{s.typeE}}</p>
                  </template>
                  <b-list-group class="list-group-minimal mb-3">
                    <b-list-group-item><b-form-rating id="rating" v-model="s.nbEval"  readonly variant="warning" size="lg" class=" bg-transparent border-0 w-25">
                                    </b-form-rating></b-list-group-item>
                    <b-list-group-item class="ml-4"><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32">
                        <path fill="currentColor" d="M24 13h-2a3.003 3.003 0 0 0-3-3V8a5.006 5.006 0 0 1 5 5Z" />
                        <path
                          fill="currentColor"
                          d="M28 13h-2a7.008 7.008 0 0 0-7-7V4a9.01 9.01 0 0 1 9 9zm-7.667 8.482l2.24-2.24a2.167 2.167 0 0 1 2.337-.48l2.728 1.092A2.167 2.167 0 0 1 29 21.866v4.961a2.167 2.167 0 0 1-2.284 2.169C7.594 27.806 3.732 11.61 3.015 5.408A2.162 2.162 0 0 1 5.169 3h4.873a2.167 2.167 0 0 1 2.012 1.362l1.091 2.728a2.167 2.167 0 0 1-.48 2.337l-2.24 2.24s1.242 8.732 9.908 9.815z"
                        />
                      </svg>
                      {{ s.contactE }}</b-list-group-item>
                    <b-list-group-item class="ml-4"><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path fill="currentColor" d="M16 2A11.013 11.013 0 0 0 5 13a10.889 10.889 0 0 0 2.216 6.6s.3.395.349.452L16 30l8.439-9.953c.044-.053.345-.447.345-.447l.001-.003A10.885 10.885 0 0 0 27 13A11.013 11.013 0 0 0 16 2Zm0 15a4 4 0 1 1 4-4a4.005 4.005 0 0 1-4 4Z"/><circle cx="16" cy="13" r="4" fill="none"/></svg> {{s.country}} </b-list-group-item>
                    
                  </b-list-group>
                  <b-button tag="a" variant="primary" :href="'/entreprisedetails/'+s.id" block>Explore more</b-button>
                </b-card>
              </div>
            
          </div>
        </div>
      </div>
    </div>
   
  </div>
</template>
<style scoped>
.layout-px-spacing {
  min-height: calc(100vh - 170px) !important;
}
.cardzoom:hover {
  zoom: 1.05;
}
</style>
<script>
import '@/assets/sass/pages/faq/faq.scss';
import '@/assets/sass/pricing-table.scss';
import { mapGetters, mapActions } from 'vuex';
export default {
  metaInfo: { name: 'Services' },
  data() {
    return {
      search: '',
    };
  },
  mounted() {},
  methods: {
    ...mapActions(['GetUserentreprises', 'GetEntreprisepromotions', 'GetUsers', 'GetUserprofiles']),
  },
  computed: {
    ...mapGetters({
      Entreprises: 'StateUserentreprises',
      Entreprisepromotions: 'StateEntreprisepromotions',
      Userprofiles: 'StateUserprofiles',
      User: 'StateUser',
      Users: 'StateUsers',
    }),
    filterByAccepted() {
      return this.Entreprises.filter((entreprise) => {
        return entreprise.published == true;
      });
    },
    filteredList() {
      return this.filterByAccepted.filter((entreprise) => {
        return entreprise.nameE.toLowerCase().includes(this.search.toLowerCase());
      });
    },
    filterByPromoted: function () {
      return this.filteredList.filter((entreprisep) => {
        return entreprisep.promoted == true;
      });
    },
    filterByNotPromoted: function () {
      return this.filteredList.filter((entreprisep) => {
        return entreprisep.promoted == false;
      });
    },
  },
  created: function () {
    this.GetUserentreprises();
    this.GetEntreprisepromotions();
  },
};
</script>
