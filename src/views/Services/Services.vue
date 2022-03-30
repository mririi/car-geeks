<template>
  <div class="layout-px-spacing">
    <portal to="breadcrumb">
      <ul class="navbar-nav flex-row">
        <li>
          <div class="page-header">
            <nav class="breadcrumb-one" aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item active" aria-current="page"><span>Services</span></li>
              </ol>
            </nav>
          </div>
        </li>
      </ul>
    </portal>
    <div>
      <div class="row  float-right">
        <div class="col-lg-12 col-md-12 col-sm-12 filtered-list-search-live mx-auto">
          <b-form class="form-inline my-2 my-lg-0 justify-content-center" @submit.prevent="search">
            <div class="w-100">
              <b-input v-model="search" class="w-100 product-search br-25" placeholder="Search Services" @keyup="search"></b-input>
            </div>
          </b-form>
        </div>
      </div>

      <div v-b-toggle.collapse-1 class="mt-3 mb-4 col-xl-1">
        <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="22" height="20" preserveAspectRatio="xMidYMid meet" viewBox="0 0 36 36">
          <path
            fill="currentColor"
            d="M22 33V19.5L33.47 8A1.81 1.81 0 0 0 34 6.7V5a1 1 0 0 0-1-1H3a1 1 0 0 0-1 1v1.67a1.79 1.79 0 0 0 .53 1.27L14 19.58v10.2Z"
            class="clr-i-solid clr-i-solid-path-1"
          />
          <path
            fill="currentColor"
            d="M33.48 4h-31a.52.52 0 0 0-.48.52v1.72a1.33 1.33 0 0 0 .39.95l12 12v10l7.25 3.61V19.17l12-12a1.35 1.35 0 0 0 .36-.91V4.52a.52.52 0 0 0-.52-.52Z"
            class="clr-i-solid clr-i-solid-path-1"
          />
          <path fill="none" d="M0 0h36v36H0z" />
        </svg>
        <span class="h6">Filter</span>
      </div>
      <b-collapse id="collapse-1">
        <b-card class="bg-transparent border-0 border-white w-25 ml-3 default mt-2 mb-4">
          <b-form-group label="Types : " v-slot="{ ariaDescribedby }">
            <b-form-checkbox-group id="checkbox-group-2" v-model="category" :aria-describedby="ariaDescribedby" name="flavour-a1">
              <div v-for="c in Servicetypes" :key="c.id">
                <b-form-checkbox :value="c.id">
                  {{ c.descT }}
                </b-form-checkbox>
              </div>
            </b-form-checkbox-group>
          </b-form-group>
        </b-card>
      </b-collapse>
    </div>
    <hr>
    <div class="faq container">
      <div class="faq-layouting layout-spacing">
        <div class="fq-article-section">
          <h2>Services List</h2>
          <div class="row">
            <div class="col-lg-4 col-md-6 mb-lg-0 mb-4" v-for="s in filterByPromoted" :key="s.id">
              <b-badge variant="danger" class="ml-2">Sponsorised</b-badge>
              <b-card :img-src="'http://127.0.0.1:8000' + s.imageS" img-top img-alt="Service" style="height: 410px"  class="counter" img-width="100%" img-height="200px">
              
                <router-link :to="'/servicedetails/' + s.id">
                  <div class="fq-rating text-center responsive ml-4">
                    <b-form-rating id="rating" v-model="s.nbEval" readonly variant="warning" class="bg-transparent border-0 w-25"> </b-form-rating>
                  </div>
                  <h5 class="card-title text-center">{{ s.titleS }}</h5>
                  <b-badge variant="warning" class="float-right  h4 mt-3">{{ s.priceS }} DT</b-badge>
                  <p class="meta-text mt-4">
                    <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32">
                      <path
                        fill="currentColor"
                        d="M16 2A11.013 11.013 0 0 0 5 13a10.889 10.889 0 0 0 2.216 6.6s.3.395.349.452L16 30l8.439-9.953c.044-.053.345-.447.345-.447l.001-.003A10.885 10.885 0 0 0 27 13A11.013 11.013 0 0 0 16 2Zm0 15a4 4 0 1 1 4-4a4.005 4.005 0 0 1-4 4Z"
                      />
                      <circle cx="16" cy="13" r="4" fill="none" />
                    </svg>
                    {{ s.addressS }}
                  </p>
                </router-link>
              </b-card>
            </div>
            <div class="col-lg-4 col-md-6 mb-lg-0 mb-4 mt-4" v-for="s in filterByNotPromoted" :key="s.id">
              <b-card :img-src="'http://127.0.0.1:8000' + s.imageS" img-top img-alt="faq-video-tutorials" style="height:410px" img-width="100%" img-height="200px">
                <router-link :to="'/servicedetails/' + s.id">
                  <div class="fq-rating text-center ml-4">
                    <b-form-rating id="rating" v-model="s.nbEval" readonly variant="warning" class="bg-transparent border-0 w-25"> </b-form-rating>
                  </div>
                  <h5 class="card-title text-center">{{ s.titleS }}</h5>
                  <b-badge variant="warning" class="float-right h4 mt-3">{{ s.priceS }} DT</b-badge>
                  <p class="meta-text mt-4">
                    <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32">
                      <path
                        fill="currentColor"
                        d="M16 2A11.013 11.013 0 0 0 5 13a10.889 10.889 0 0 0 2.216 6.6s.3.395.349.452L16 30l8.439-9.953c.044-.053.345-.447.345-.447l.001-.003A10.885 10.885 0 0 0 27 13A11.013 11.013 0 0 0 16 2Zm0 15a4 4 0 1 1 4-4a4.005 4.005 0 0 1-4 4Z"
                      />
                      <circle cx="16" cy="13" r="4" fill="none" />
                    </svg>
                    {{ s.addressS }}
                  </p>
                </router-link>
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
import '@/assets/sass/pricing-table.scss';
import '@/assets/sass/pages/faq/faq.scss';
import { mapGetters, mapActions } from 'vuex';
export default {
  metaInfo: { title: 'Services' },
  data() {
    return {
      search: '',
      category: [],
    };
  },
  mounted() {},
  methods: {
    ...mapActions(['GetServices', 'GetServicepromotions', 'GetServicetypes', 'GetUsers', 'GetUserprofiles']),
    
  },
  computed: {
    ...mapGetters({
      Services: 'StateServices',
      Servicepromotions: 'StateServicepromotions',
      Userprofiles: 'StateUserprofiles',
      Servicetypes: 'StateServicetypes',
      User: 'StateUser',
      Users: 'StateUsers',
    }),
    filterByAccepted() {
      return this.Services.filter((service) => {
        return service.accepted == true;
      });
    },
    filteredList() {
      return this.filterByAccepted.filter((service) => {
        return service.titleS.toLowerCase().includes(this.search.toLowerCase());
      });
    },
    filterByCategory() {
      if (this.category != '') {
        return this.filteredList.filter((service) => this.category.includes(service.typeS));
      } else return this.filteredList;
    },
    filterByPromoted: function () {
      return this.filterByCategory.filter((servicep) => {
        return servicep.promoted == true;
      });
    },
    filterByNotPromoted: function () {
      return this.filterByCategory.filter((servicep) => {
        return servicep.promoted == false;
      });
    },
  },
  created: function () {
    this.GetServices();
    this.GetServicetypes();
    this.GetServicepromotions();
  },
};
</script>
